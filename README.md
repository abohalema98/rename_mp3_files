### Updated README File Content

---

### File Renaming Script

This Python script allows users to rename files in a specified folder sequentially with a chosen file extension. It is a simple utility for organizing files with consistent naming patterns.

---

### Features
- **Dynamic File Extension**: Users can specify the desired file extension (e.g., `.mp3`, `.png`).
- **Sequential Renaming**: Files are renamed in a `001.extension`, `002.extension` format.
- **Error Handling**: Validates folder paths, file extensions, and handles unexpected errors gracefully.
- **Universal Compatibility**: Works with any file type, not limited to `.mp3`.

---

### How to Use
1. **Prerequisites**:
   - Python installed on your system. Download Python from the official website: [Download Python](https://www.python.org/downloads/).
   - A folder with files you want to rename.

2. **Run the Script**:
   - Save the script as `rename_files.py`.
   - Run the script using a terminal or command prompt:
     ```bash
     python rename_files.py
     ```

3. **Follow Prompts**:
   - Enter the full path to the folder containing the files.
   - Specify the desired file extension (e.g., `mp3`, `png`).

4. **Results**:
   - Files in the folder will be renamed sequentially, starting from `001`.

---

### Example
#### Before:
```
song1.mp3
track.mp3
audiofile.mp3
```

#### After:
```
001.mp3
002.mp3
003.mp3
```

---

### Limitations
- Files without extensions or those already matching the desired extension will be skipped.
- Ensure that the folder contains only files you wish to rename.

---

### Contributing
Feel free to contribute to improve the script! Submit a pull request or report issues.

---

### License
This project is open-source and available under the [MIT License](LICENSE).
