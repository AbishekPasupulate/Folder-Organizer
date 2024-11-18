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

## File Types Supported

- Audio: '.mp3', '.wav', '.flac', '.aac', etc
- Video: '.mp4', '.avi', '.mov', '.wmv', etc.
- Images: '.jpg', '.png', '.gif', '.bmp', '.svg', etc.
- Documents:
