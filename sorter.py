import os
import argparse
import sys

sort_folders=["Audio", "Videos", "Program Files", "Images", "Documents","Compressed", "Webpage","Others"]
extensions={"Audio":['.wav','.pcm','.aiff','mp3','.aac','.flac','.alac'],
            "Videos":['.amv','.mp4','.mkv','avi','.mov','.webm','.m4v'],
            "Program Files":['.c','.java','.cpp','.py','.js','.ts','.cs','.swift','.pl','.bat','.com','.exe','.go','.msi','.sh',
            '.class','.r'],
            "Images":['.gif','.png','.jpg','.jpeg','.webp','.heif','.bmp','.raw','.tiff'],
            "Documents":[".doc", ".docx", ".odt", ".pdf", ".rtf", ".txt", 
            ".wpd", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", 
            ".odp", ".epub", ".md", ".csv"],"Compressed":[
            ".zip", ".rar", ".7z", ".gz", ".bz2", ".xz", 
            ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".tar.xz", 
            ".lzma", ".tar", ".iso", ".cab", ".arj", 
            ".lzh", ".z", ".cpio"],
            "Webpage":[".html", ".htm", ".php", ".asp", ".aspx", ".jsp", 
            ".css", ".js", ".xml", ".xhtml"],"Others":[]}

def main():
    source, path =path_args()
    is_valid_path(source, path)
    folders=os.listdir(source)
    check_dir(path)
    sort_files(source, path, folders)




def is_valid_path(source,dest):
    if not os.path.exists(source):
        sys.exit(f"Error: The source path '{source}' does not exist.")
    if not os.path.isdir(source):
        sys.exit(f"Error: The source path '{source}' is not a directory.")
    if not os.path.exists(dest):
        sys.exit(f"Error: The destination path '{dest}' does not exist.")
    if not os.path.isdir(dest):
        sys.exit(f"Error: The destination path '{dest}' is not a directory.")

def path_args():
    parser=argparse.ArgumentParser(description="Sort for the files")
    parser.add_argument("-p", "--path", help="path of the folder to be sorted", default=os.getcwd(), type=str)
    parser.add_argument("-d", "--destination", help="destination folder", default=os.getcwd(), type=str)
    args=parser.parse_args()
    return args.path, args.destination

def check_dir(dest):
    for folder in sort_folders:
        folder_path = os.path.join(dest, folder)
        if not os.path.exists(folder_path):
            print(f"Creating folder: {folder_path}")
            os.mkdir(folder_path)

def move_file(src, dest_folder, file_name):
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    target_path = os.path.join(dest_folder, file_name)
    print(f"Moving {src} to {dest_folder}")
    os.rename(src, target_path)

def sort_files(source, dest, files):
    try:
        for file_name in files:
            current_path = os.path.join(source, file_name)

            if os.path.isfile(current_path):
                moved = False
                file_name_lower = file_name.lower()

                for folder in sort_folders:
                    if len(extensions[folder]) > 0:
                        for ext in extensions[folder]:
                            if file_name_lower.endswith(ext):
                                target_folder = os.path.join(dest, folder)
                                move_file(current_path, target_folder, file_name)
                                moved = True
                                break
                    if moved:
                        break

                if not moved:
                    move_file(current_path, os.path.join(dest, "Others"), file_name)
        print("TASK COMPLETED")            

    except PermissionError:
        sys.exit("Permission Error! Please run the program as administrator!")


if __name__=="__main__":
    main()
    
