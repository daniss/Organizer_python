# File Organizer

This Python script serves as a file organizer, sorting files based on their extensions into designated folders. It utilizes the `shutil` and `os` modules for file manipulation and directory operations.

## Features

- **Automatic Organization**: Quickly sorts files from a source directory into destination folders based on their file extensions.
- **Customizable Extensions**: Easily extend the script to handle additional file types by updating the extension-to-folder mapping.
- **Efficient**: Utilizes efficient Python libraries to ensure fast and reliable file organization.

## How to Use

1. Clone or download the repository to your local machine.
2. Update the `extension_to_folder` dictionary in the script to map file extensions to desired destination folders.
3. Run the script and provide the source directory containing the files to organize.

## Example

Suppose you have a directory containing various files such as `document.pdf`, `image.jpg`, and `script.py`. Running the organizer script will move these files to appropriate folders like `Documents`, `Images`, and `Scripts`, respectively.

## Requirements

- Python 3.x
- `shutil` and `os` modules (included in Python's standard library)

## Acknowledgments

Special thanks to the Python community for their valuable contributions and the developers behind the `shutil` and `os` modules for providing powerful tools for file management.
