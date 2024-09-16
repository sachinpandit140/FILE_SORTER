import os
import re
import argparse
import sys

sort_folders=["Audio", "Videos", "Program Files", "Images", "Documents","Compressed", "Webpage","Others"]
extensions={"Audio":['.wav','.pcm','.aiff','mp3','.aac','.flac','.alac'],
            "Videos":['.amv','.mp4','.mkv','avi','.mov','.webm','.m4v'],
            "Program Files":['.c','.java','.cpp','.py','.js','.ts','.cs','.swift','.pl','.bat','.com','.exe','.go','.msi','.sh'
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
    path=path_args()
    folders=os.listdir(path)
    folders=check_dir(folders, path)
    sort(path, folders)



def check_path(path: str):
    if re.match(r"([A-Z]:/){1}([a-zA-Z0-9!@#$%*^&:\"]+/)*"):
        return True
    return False

def path_args():
    parser=argparse.ArgumentParser(description="Sort for the files")
    parser.add_argument("-p", "--path", help="path of the folder to be sorted", default=os.getcwd(), type=str)
    args=parser.parse_args()
    return args.path

def check_dir(l, p):
    for char in sort_folders:
        if char in l:
            pass
        else:
            if char not in os.listdir(p):
                    new_path=os.path.join(p, char )
                    print(f"New Path: {new_path} made.")
                    mode=0o666
                    os.mkdir(new_path)
                
    return os.listdir(p)

def sort(pat, fold):
    try:
        for char in fold:
            current_path = os.path.join(pat, char)
            
            if os.path.isfile(current_path):
                moved = False 

                for obj in sort_folders:
                    if len(extensions[obj]) != 0:
                        for ext in extensions[obj]:
                            char=char.lower()
                            if char.endswith(ext):
                                initial_path = current_path
                                target_path = os.path.join(pat, obj)

                                if not os.path.exists(target_path):
                                    os.mkdir(target_path)

                                target_file_path = os.path.join(target_path, char)
                                os.rename(initial_path, target_file_path)
                                moved = True
                                break

                    if moved:
                        break 


                if not moved:
                    target_path = os.path.join(pat, "Others")

                    if not os.path.exists(target_path):
                        os.mkdir(target_path)

                    target_file_path = os.path.join(target_path, char)
                    os.rename(current_path, target_file_path)
    except PermissionError:
        sys.exit("Permission Error! Please run the program as administrator!")


if __name__=="__main__":
    main()
    