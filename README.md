# LevelDB Chrome Extension Data Extractor

This project provides a Chrome extension that sets a value in Chrome's local storage using the `chrome.storage` API, along with a Python script that fetches and displays this value from Chrome's LevelDB database.

## Overview

The project contains two main components:

1. **Chrome Extension**: A simple "Hello World" extension that stores a value in Chrome's local storage.
2. **Python Script**: A script that reads the stored value from Chrome's LevelDB database and saves it to a JSON file.

## Chrome Extension

### How Value is Set

The Chrome extension uses the `chrome.storage.local.set` API to store a value. The value is set when the "Set Value" button is clicked in the extension popup.

### Variables Used

- `key`: The key used to store the value in local storage, it is set to "blockMeshKey".
- `value`: The value stored in local storage. In this case, it is set to "hello world".

### Extension Files

- `manifest.json`: The manifest file for the Chrome extension.
- `popup.html`: The HTML file for the extension popup.
- `popup.js`: The JavaScript file that handles setting and getting the value in local storage.

## Python Script

### How to Install

1. **Install Python**: Ensure you have Python 3 installed on your system.
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```
3. **Install Dependencies**:
   ```bash
   pip install plyvel
   ```

### How to Run

1. **Close Chrome**: Ensure Chrome is closed to avoid file locking issues.
2. **Run the Script**:
   ```bash
   python fetch_leveldb.py
   ```

### How to Generate Output

The script will generate a `leveldb_data.json` file containing the stored values from Chrome's LevelDB database.

## How It Works

### Chrome Extension

1. **Setting the Value**:

   - When the "Set Value" button is clicked, the `setValue` function is called.
   - The `chrome.storage.local.set` API is used to store the value `{blockMeshKey: "hello world"}`.

2. **Getting the Value**:
   - When the "Get Value" button is clicked, the `getValue` function is called.
   - The `chrome.storage.local.get` API is used to retrieve the value associated with the key.

### Python Script

1. **Fetch Values**:

   - The script opens Chrome's LevelDB database located at `/mnt/c/Users/Ayush Agrawal/AppData/Local/Google/Chrome/User Data/Default/Local Extension Settings/`. (I am using WSL)
   - It iterates over each subdirectory in the specified path and opens the LevelDB database files.
   - It reads all key-value pairs and filters keys containing `"blockMeshKey"`.
   - Decoded values are stored in a dictionary.

2. **Save to JSON**:
   - The script saves the fetched values to a `leveldb_data.json` file in the current directory.

### Error Handling

The script includes error handling to manage cases where the database is corrupted or files are missing, printing appropriate error messages.

### Note
This is the most unoptimized version of the code just for quick research purposes and demostration and can be optimized further.

---
