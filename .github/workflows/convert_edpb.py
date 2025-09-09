import pandas as pd
import json
import argparse
import sys
from datetime import datetime

def convert_csv_to_edpb_json(csv_filepath, json_filepath):
    try:
        df = pd.read_csv(csv_filepath, sep=',', skipinitialspace=True, dtype=str)
        df = df.fillna('')

    except FileNotFoundError:
        print(f"::error file={csv_filepath}::CSV file not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"::warning file={csv_filepath}::CSV file is empty.")
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print(f"Created empty JSON file: {json_filepath}")
        return
    except Exception as e:
        print(f"::error file={csv_filepath}::Failed to read CSV file. Error: {e}")
        sys.exit(1)

    required_columns = ['ID', 'Platform', 'Category', 'Cookie / Data Key name', 'Domain', 
                        'Description', 'Retention period', 'Data Controller', 
                        'User Privacy & GDPR Rights Portals', 'Wildcard match']
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"::error file={csv_filepath}::Missing required columns: {', '.join(missing_columns)}")
        sys.exit(1)

    output_data = []
    current_time = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'

    base_entry = {
        "name": "Open Cookie Database",
        "author": "Jack Kwakman",
        "category": "cookie",
        "knowledges": [],
        "created_at": current_time
    }

    for _, record in df.iterrows():

        try:
            wildcard_match_int = int(record.get('Wildcard match', 0))
        except ValueError:
            wildcard_match_int = 0 

        knowledge_entry = {
            "updated_at": current_time,
            "created_at": current_time,
            "kind": "cookie", # Hardcoded zoals in het voorbeeld
            "domain": record.get('Domain', ''),
            "name": record.get('Cookie / Data Key name', ''),
            "category": record.get('Category', '').lower(), 
            "source": record.get('Platform', ''),
            "controller": record.get('Data Controller', ''),
            "date": "",
            "policy": record.get('User Privacy & GDPR Rights Portals', ''),
            "reference": record.get('ID', ''), 
            "comment": record.get('Description', '')
        }
        base_entry["knowledges"].append(knowledge_entry)
    
    output_data.append(base_entry)

    try:
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully converted '{csv_filepath}' to '{json_filepath}'")
    except Exception as e:
        print(f"::error file={json_filepath}::Failed to write JSON file. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert CSV to EU EDPB grouped JSON format.')
    parser.add_argument('csv_input', help='Path to the input CSV file.')
    parser.add_argument('json_output', help='Path to the output JSON file.')

    args = parser.parse_args()

    convert_csv_to_edpb_json(args.csv_input, args.json_output)
