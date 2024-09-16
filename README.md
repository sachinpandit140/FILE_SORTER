# File Sorter 

## Overview

The File Sorter Script is a Python utility designed to organize files in a specified directory by moving them into categorized subdirectories based on their file extensions. The script supports several predefined categories such as "Audio," "Videos," "Program Files," "Images," "Documents," "Compressed," "Webpage," and "Others." 

## Requirements

- Python 3.x installed on your system.
- Basic knowledge of running Python scripts from the command line.
- Appropriate permissions to read, write, and create directories in the target folder.

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
python file_sorter.py -p <path> or python sorter.py --path <path>
```
`<path>`: The directory path where the files need to be sorted. If not provided, the script will default to the current working directory.
## Arguments
`-p`, `--path`: Specify the path of the folder to be sorted. Example: -p "C:\MyFiles"

### Example
## Sorting files in a directory
To sort files located in `C:\Downloads`, run:
```bash
python file_sorter.py "C:\Downloads"
```
The script will move files into appropriate subdirectories such as "Audio," "Videos," etc., based on their extensions.

### Batch File Integration
You can automate the script execution using a batch file. Create a file named `run_file_sorter.bat` with the following content:
```batch
@echo off
REM SET PATH TO PYTHON
REM (THIS IS USUALLY DONE DURING PYTHON INSTALLATION)

REM Set the path to your Python script (THIS IS USUALLY DONE DURING PYTHON INSTALLATION)
SET SCRIPT_PATH=C:\SP\Python\Script\sorter.py

SET CURRENT_PATH=%CD%

REM CHANGE "%cd" to your path for desired path


python "%SCRIPT_PATH%" -p "%CURRENT_PATH%"

REM example "python "%SCRIPT_PATH" -p "%CURRENT_PATH"" which is the default value
REM example "%PYTHON_PATH%" "%SCRIPT_PATH%" -p "%CURRENT_PATH%" can also be done
echo DONE!
pause


```

Replace `C:\Path\To\Your\Script\file_sorter.py` with the actual path.

## Error Handling
- **PermissionError**: If you encounter a PermissionError, ensure that you have the necessary read/write permissions for the directories and files.
- **OSError**: Ensure that the target directories do not contain files with the same names or paths that might conflict.

## Author
Sachin Pandit

### License
This script is provided under the [MIT License](https://github.com/sachinpandit140/FILE_SORTER/blob/main/LICENSE). You are free to use, modify, and distribute it as you see fit.





