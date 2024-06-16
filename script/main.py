import os
import json
import plyvel
import binascii

def list_db_files(db_path):
    print("Listing files in the LevelDB directory:")
    for root, dirs, files in os.walk(db_path):
        for file in files:
            print(file)
    print("\n")

def fetch_values(db_path):
    values = {}
    try:
        db = plyvel.DB(db_path, create_if_missing=False)
        print(db)
        for key, value in db:
            try:
                decoded_key = key.decode('utf-8')
                if ("blockMeshKey" not in decoded_key):
                    continue
            except UnicodeDecodeError:
                decoded_key = binascii.hexlify(key).decode('utf-8')
            try:
                decoded_value = value.decode('utf-8')
            except UnicodeDecodeError:
                decoded_value = binascii.hexlify(value).decode('utf-8')
            
            values[decoded_key] = decoded_value
        db.close()
    except plyvel._plyvel.Error as e:
        print(f"Error: {e}")
    return values

def save_to_json(data, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    db_path = r'/mnt/c/Users/Ayush Agrawal/AppData/Local/Google/Chrome/User Data/Default/Local Extension Settings/'
    json_path = 'leveldb_data.json'
    try:
        final_values = {}
        for i in os.listdir(db_path):
            values = fetch_values(db_path + "/" + i)
            print(values)
            final_values.update(values)
        save_to_json(final_values, json_path)
        print(f"Data has been successfully saved to {json_path}")
    except plyvel._plyvel.CorruptionError as e:
        print(f"CorruptionError: {e}")
