# File Sorter 

## Overview

The File Sorter Script is a Python utility designed to organize files in a specified directory by moving them into categorized subdirectories based on their file extensions. The script supports several predefined categories such as "Audio," "Videos," "Program Files," "Images," "Documents," "Compressed," "Webpage," and "Others." It is further customizable with basic knowledge of python to add extensions for filter or further filters to sort.


## Requirements

- Python 3.x installed on your system.

## File Categories and Extensions

The script sorts files into the following categories based on their extensions:

- **Audio**: `.wav`, `.pcm`, `.aiff`, `.mp3`, `.aac`, `.flac`, `.alac`
- **Videos**: `.amv`, `.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, `.m4v`
- **Program Files**: `.c`, `.java`, `.cpp`, `.py`, `.js`, `.ts`, `.cs`, `.swift`, `.pl`, `.bat`, `.com`, `.exe`, `.go`, `.msi`, `.sh`, `.class`, `.r`
- **Images**: `.gif`, `.png`, `.jpg`, `.jpeg`, `.webp`, `.heif`, `.bmp`, `.raw`, `.tiff`
- **Documents**: `.doc`, `.docx`, `.odt`, `.pdf`, `.rtf`, `.txt`, `.wpd`, `.xls`, `.xlsx`, `.ods`, `.ppt`, `.pptx`, `.odp`, `.epub`, `.md`, `.csv`
- **Compressed**: `.zip`, `.rar`, `.7z`, `.gz`, `.bz2`, `.xz`, `.tar.gz`, `.tgz`, `.tar.bz2`, `.tbz2`, `.tar.xz`, `.lzma`, `.tar`, `.iso`, `.cab`, `.arj`, `.lzh`, `.z`, `.cpio`
- **Webpage**: `.html`, `.htm`, `.php`, `.asp`, `.aspx`, `.jsp`, `.css`, `.js`, `.xml`, `.xhtml`
- **Others**: Files with extensions that do not match any of the above categories.

## Usage

### Command Line

To run the script, use the following command:

```bash
python sorter.py -p <path> or python sorter.py --path <path>
```
`<path>`: The directory path where the files need to be sorted. If not provided, the script will default to the current working directory.
## Arguments
`-p`, `--path`: Specify the path of the folder to be sorted. Example: -p "C:\MyFiles"

### Example
## Sorting files in a directory
To sort files located in `C:\Downloads`, run:
```bash
python sorter.py "C:\Downloads"
```
The script will move files into appropriate subdirectories such as "Audio," "Videos," etc., based on their extensions.

### Batch File Integration
You can automate the script execution using a batch file. Create a file named `sorter.bat` with the following content:
```batch
@echo off
REM SET PATH TO PYTHON
SET PYTHON_PATH=<YOUR PYTHON PATH HERE>
REM (THIS IS USUALLY DONE DURING PYTHON INSTALLATION)

REM Set the path to your Python script
SET SCRIPT_PATH= <placeholder path here>

SET CURRENT_PATH=%CD%

SET DEST_PATH=%CD%

REM CHANGE "%cd" to your path for desired path


"%PYTHON_PATH% "%SCRIPT_PATH%" -p "%CURRENT_PATH%" -d "%DEST_PATH%"

REM example "%PYTHON_PATH%" "%SCRIPT_PATH%" -p "%CURRENT_PATH%" can also be done
echo DONE!
pause



```

Replace `<placeholder path here>` with the actual path.

## Running the Script in Bash

To run the script using Bash, follow these steps:

1. **Open a Terminal**: Access your terminal or command line interface.

2. **Navigate to the Script Directory**: Use the `cd` command to change to the directory where your `sorter.py` script is located. For example:

    ```bash
    cd /path/to/your/script
    ```

3. **Run the Script**: Use the following command to execute the script:

    ```bash
    python3 file_sorter.py -p /path/to/your/directory -d /path/to/your/directory
    ```

    - `/path/to/your/directory`: Replace this with the path to the directory you want to sort. If the path contains spaces, enclose it in quotes.

### Example

To sort files located in `/home/user/Downloads`, run:

```bash
python3 file_sorter.py -p "/home/user/Downloads"
```

## Error Handling
- **PermissionError**: If you encounter a PermissionError, ensure that you have the necessary read/write permissions for the directories and files.
- **OSError**: Ensure that the target directories do not contain files with the same names or paths that might conflict.

## Author
Sachin Pandit

### License
This script is provided under the [MIT License](https://github.com/sachinpandit140/FILE_SORTER/blob/main/LICENSE). You are free to use, modify, and distribute it as you see fit.





