import pandas as pd
import json
import argparse
from collections import defaultdict
import sys

def convert_csv_to_grouped_json(csv_filepath, json_filepath):
    try:
        df = pd.read_csv(csv_filepath, sep=',', skipinitialspace=True, dtype=str)
        df = df.fillna('')

    except FileNotFoundError:
        print(f"::error file={csv_filepath}::CSV file not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"::warning file={csv_filepath}::CSV file is empty.")
        # Maak een lege JSON structuur aan of stop, afhankelijk van gewenst gedrag
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=4)
        print(f"Created empty JSON file: {json_filepath}")
        return # Stop verdere uitvoering
    except Exception as e:
        print(f"::error file={csv_filepath}::Failed to read CSV file. Error: {e}")
        sys.exit(1)

    if 'Platform' not in df.columns:
        print(f"::error file={csv_filepath}::Required column 'Platform' not found in CSV.")
        sys.exit(1)

    grouped_data = defaultdict(list)

    records = df.to_dict('records')

    for record in records:
        platform = record.get('Platform', 'Unknown Platform')

        cookie_details = {
            'id': record.get('ID', ''),
            'category': record.get('Category', ''),
            'cookie': record.get('Cookie / Data Key name', ''),
            'domain': record.get('Domain', ''),
            'description': record.get('Description', ''),
            'retentionPeriod': record.get('Retention period', ''),
            'dataController': record.get('Data Controller', ''),
            'privacyLink': record.get('User Privacy & GDPR Rights Portals', ''),
            'wildcardMatch': record.get('Wildcard match', '')
        }
        grouped_data[platform].append(cookie_details)

    try:
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(grouped_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully converted '{csv_filepath}' to '{json_filepath}'")
    except Exception as e:
        print(f"::error file={json_filepath}::Failed to write JSON file. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert CSV to grouped JSON.')
    parser.add_argument('csv_input', help='Path to the input CSV file.')
    parser.add_argument('json_output', help='Path to the output JSON file.')

    args = parser.parse_args()

    convert_csv_to_grouped_json(args.csv_input, args.json_output)
