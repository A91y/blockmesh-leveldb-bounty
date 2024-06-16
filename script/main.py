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
    db = plyvel.DB(db_path, create_if_missing=False)
    values = {}
    print(db)
    for key, value in db:
        print(f"Key: {key}, Value: {value}")
        try:
            decoded_key = key.decode('utf-8')
        except UnicodeDecodeError:
            decoded_key = binascii.hexlify(key).decode('utf-8')
        try:
            decoded_value = value.decode('utf-8')
        except UnicodeDecodeError:
            decoded_value = binascii.hexlify(value).decode('utf-8')
        
        values[decoded_key] = decoded_value
    db.close()
    return values

def save_to_json(data, json_path):
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    db_path = r'/mnt/c/Users/Ayush Agrawal/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb'
    # db_path = r'/mnt/c/Users/Ayush Agrawal/AppData/Local/Google/Chrome/User Data/Default/Local Extension Settings/cnnfbafpcajlendgbnkkamohphfeplog'
    json_path = 'leveldb_data.json'

    if os.path.exists(db_path):
        list_db_files(db_path)
    else:
        print("Path does not exist")

    try:
        values = fetch_values(db_path)
        print(values)
        save_to_json(values, json_path)
        print(f"Data has been successfully saved to {json_path}")
    except plyvel._plyvel.CorruptionError as e:
        print(f"CorruptionError: {e}")
