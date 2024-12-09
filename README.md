# Rename MP3 Tool

A Python-based tool to rename `.mp3` files in a folder to sequentially numbered names (`001.mp3`, `002.mp3`, etc.).

---

## Features
- Renames all `.mp3` files in a specified folder.
- Assigns sequential numbers to filenames (e.g., `001.mp3`, `002.mp3`).
- Handles large numbers of files efficiently.
- Interactive: prompts the user to enter the folder path at runtime.

---

## Requirements

### Software Requirements
- Python 3.6 or later

### Supported Platforms
- Windows
- macOS
- Linux

---

## Installation

1. **Download or Clone the Tool**:
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the folder as a ZIP file and extract it.

2. **Navigate to the Tool Folder**:
   ```bash
   cd rename_mp3_tool
   ```

3. **Install Required Dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```
   > Note: This tool only uses Python’s standard libraries, so `requirements.txt` may be empty.

---

## Usage

1. Run the tool:
   ```bash
   python rename_mp3_tool.py
   ```

2. Enter the folder path containing `.mp3` files when prompted.

3. The tool will rename all `.mp3` files in the folder to sequentially numbered filenames (e.g., `001.mp3`, `002.mp3`).

---

## Example

### Input:
A folder contains the following files:
```
MySong.mp3
AnotherTrack.mp3
CoolAudio.mp3
```

### Output:
The renamed files will be:
```
001.mp3
002.mp3
003.mp3
```

---

## Notes
- The original names of the `.mp3` files will be removed.
- The tool will not rename files without the `.mp3` extension.
- If the specified folder does not exist, the tool will prompt an error message.

---

## Troubleshooting
- **No files renamed:** Ensure the folder contains `.mp3` files.
- **Path not found error:** Verify the folder path entered is correct.
- **Permission denied:** Ensure you have write permissions for the folder.

---

## Optional: Create Executable (Advanced)

To package this script into a standalone executable (e.g., for users without Python):

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:
   ```bash
   pyinstaller --onefile rename_mp3_tool.py
   ```

3. The executable will be located in the `dist` folder.

---

## License
This tool is free to use and modify. Share and enjoy!

