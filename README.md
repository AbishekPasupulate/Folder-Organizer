# Folder Organizer Script

This Python script automatically organizes files in a specified directory into subdirectories based on file types. It uses the `watchdog` library to monitor changes in the source directory and move files to the appropriate folders for organization.

## Features

- **Automatic File Organization**: Organizes files into directories such as Music, Videos, Images, Documents, Executables, and more based on their extensions.
- **Real-Time Monitoring**: Uses `watchdog` to monitor the source folder and move files as soon as they are added or modified.
- **Customizable**: You can customize the source and destination directories, as well as file extensions.
- **Supports Multiple File Types**: Includes support for a variety of file types like audio, video, images, documents, executables, and code files.

## Requirements

- Python 3.x
- `watchdog` library

To install the necessary dependencies, run:

```bash
pip install watchdog
```
## File Types Supported

- **Audio**: `.mp3`, `.wav`, `.flac`, `.aac`, etc.
- **Video**: `.mp4`, `.avi`, `.mov`, `.wmv`, etc.
- **Images**: `.jpg`, `.png`, `.gif`, `.bmp`, `.svg`, etc.
- **Documents**:
  - **Word**: `.doc`, `.docx`
  - **PDF**: `.pdf`
  - **Excel**: `.xls`, `.xlsx`, `.csv`
  - **PowerPoint**: `.ppt`, `.pptx`
- **Executable**: `.exe`
- **Source Code**:
  - **C**: `.c`, `.h`
  - **Python**: `.py`
- **Compressed Files**: `.zip`, `.tar.gz`, `.rar`

## Setup Instructions

- Clone this repository:
```bash
git clone https://github.com/your-username/folder-organizer.git
cd folder-organizer
```
- Open the `main.py` file and set the `source_dir` (the directory to monitor) and destination directories for different file types.
```bash
# Example directories
source_dir = "C:/Users/YourUserName/Downloads"
```
- Run the script
```bash
python organizer.py
```
- This will start monitoring the source_dir and automatically organize files as they are added or modified.

## How It Works

- The script watches the specified source_dir for new or modified files using the watchdog library.
- When a file is detected, it checks the file's extension and moves it to the appropriate destination folder.
- If a folder for a particular file type does not exist, it will be created automatically.

## Customization

- You can easily modify the file extensions, destination directories, or add additional types by editing the `extensions.py` file.

### Example: Adding New File Type
- If you want to add a new file type (e.g., .txt files), add the following to `extensions.py`:

```bash
text_file = ['.txt']
```

- Then, add a new check function for `.txt` files in the MoverHandler class:
```bash
def check_text_files(self, entry, name):
    from extensions import text_file
    for ext in text_file:
        if name.endswith(ext) or name.endswith(ext.upper()):
            self.move_to_dir("Text_Files", entry, name)
```

## Contributing
- Contributions are welcome! If you find any bugs or would like to suggest improvements, feel free to create an issue or submit a pull request.

## Notes:
- Replace `"C:/Users/YourUserName/Downloads"` with your actual directory paths.
- Add more instructions as necessary based on your project's complexity.
- If you're using GitHub Pages, you can even add images to show how the script works!