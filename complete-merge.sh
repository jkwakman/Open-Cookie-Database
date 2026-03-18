#!/bin/bash
# Auto-merge and rewrite for cookiedatabase.org scrape when it completes

set -e

cd "$(dirname "$0")"

echo "=== Waiting for cookiedatabase scraper to complete ==="
while [ ! -f "scripts/cookiedatabase-missing.csv" ]; do
    if ! pgrep -f "scrape_cookiedatabase.py scrape" > /dev/null 2>&1; then
        echo "ERROR: Scraper process stopped but file not created"
        exit 1
    fi
    sleep 30
    echo "Still waiting for scraper... $(date)"
done

cookies_found=$(( $(wc -l < scripts/cookiedatabase-missing.csv) - 1 ))
echo "✓ Scraper completed! Found $cookies_found new cookies"
echo ""

echo "=== Merging into database ==="
python3 scripts/scrape_cookiedatabase.py merge
echo ""

echo "=== Rewriting descriptions ==="
python3 scripts/rewrite_descriptions.py
echo ""

echo "=== Current database state ==="
csv_rows=$(wc -l < open-cookie-database.csv)
json_platforms=$(python3 -c "import json; db=json.load(open('open-cookie-database.json')); print(len(db))")
json_cookies=$(python3 -c "import json; db=json.load(open('open-cookie-database.json')); print(sum(len(v) for v in db.values()))")
echo "CSV: $csv_rows rows"
echo "JSON: $json_platforms platforms, $json_cookies total cookies"
echo ""

echo "=== Committing changes ==="
git add -A
git commit -m "merge: cookiedatabase.org data ($cookies_found cookies) + rewrite descriptions

- Merged $cookies_found cookies from cookiedatabase.org scraping
- Applied pattern-based description rewrites
- Database now contains $((csv_rows - 1)) cookies"

echo ""
echo "✓ All done! Ready to push:"
echo "  git push origin master"
