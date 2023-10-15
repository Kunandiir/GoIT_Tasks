import shutil
import os
import sys
import re
from unidecode import unidecode


def main():
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        sort_folders(folder_path)
    else:
        print("No folder path provided.")



def sort_folders (path):
    img_list = []
    vid_list = []
    docs_list = []
    mus_list = []
    arc_list = []
    els_list = []
    folds = ["images", "videos", "docs", "music", "archives", "else"]
    ext = {
        "images" : ['JPEG', 'PNG', 'JPG', 'SVG'],
        "videos" : ['AVI', 'MP4', 'MOV', 'MKV'],
        "docs" : ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
        "music" : ['MP3', 'OGG', 'WAV', 'AMR'],
        "archives" : ['ZIP', 'GZ', 'TAR'],
        "else" : [] 
    }
    ext_lst = []
    unknown_ext_lst = []
    for folder in ext.keys():
        try:
            os.makedirs(os.path.join(path, folder))
        except FileExistsError:
            print(f"{folder.capitalize()} folder already exists")
            
    for root, dirs, files in os.walk(path):
        for filename in files:
            _, fold_name = os.path.split(root)
            name, exten = os.path.splitext(filename)
            if exten.replace(".", "").upper() in ext["images"]:
                if not name in img_list:
                    img_list.append(name)
                if not exten in ext_lst:
                    ext_lst.append(exten)
                try:
                    shutil.move(root + "/" + filename, path + "/images")
                    rename_file(path + "/images/" + filename)
                except:
                    pass
            elif exten.replace(".", "").upper() in ext["videos"]:
                if not name in vid_list:
                    vid_list.append(name)
                if not exten in ext_lst:
                    ext_lst.append(exten)
                try:
                    shutil.move(root + "/" + filename, path + "/videos")
                    rename_file(path + "/videos/" + filename)
                except:
                    pass
            elif exten.replace(".", "").upper() in ext["docs"]:
                if not name in docs_list:
                    docs_list.append(name)
                if not exten in ext_lst:
                    ext_lst.append(exten)
                try:
                    shutil.move(root + "/" + filename, path + "/docs")
                    rename_file(path + "/docs/" + filename)
                except:
                    pass
            elif exten.replace(".", "").upper() in ext["music"]:
                if not name in mus_list:
                    mus_list.append(name)
                if not exten in ext_lst:
                    ext_lst.append(exten)
                try:
                    shutil.move(root + "/" + filename, path + "/music")
                    rename_file(path + "/music/" + filename)
                except:
                    pass
            elif exten.replace(".", "").upper() in ext["archives"]:
                if not name in arc_list:
                    arc_list.append(name)
                if not exten in ext_lst:
                    ext_lst.append(exten)
                try:
                    _, flname = os.path.split(root + "/" + filename)
                    named, _ = os.path.splitext(flname)
                    shutil.unpack_archive(root + "/" + filename, path + "/archives/"+ named)
                    os.remove(root + "/" + filename)
                except:
                    pass
            else:
                if not name in els_list:
                    els_list.append(name)
                if not exten in unknown_ext_lst:
                    unknown_ext_lst.append(exten)
                try:
                    shutil.move(root + "/" + filename, path + "/else")
                    rename_file(path + "/else/" + filename)
                except:
                    pass
    delete_empty_folders(path)
    print("Here is all files in this path\n" + "1)images:\n " + "\n ".join(img_list))
    print("1)image:\n " + "\n ".join(img_list))
    print("2)video:\n " + "\n ".join(vid_list))
    print("3)docs:\n " + "\n ".join(docs_list))
    print("4)music:\n " + "\n ".join(mus_list))
    print("5)archives:\n " + "\n ".join(arc_list))
    print("6)else:\n " + "\n ".join(els_list))

    print("Here is all extentions\n")
    print("1)Exist extentions:\n " + "\n ".join(ext_lst))
    print("2)Unknown extentions:\n " + "\n ".join(unknown_ext_lst))
def delete_empty_folders(path):
    for root, dirs, _ in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)



def normalize(filename):
    filename = unidecode(filename)

    filename = re.sub(r'[^a-zA-Z0-9]', '_', filename)

    return filename

def rename_file(old_filename):
    directory, old_name = os.path.split(old_filename)
    old_name, extension = os.path.splitext(old_name)

    new_name = normalize(old_name)

    new_filename = os.path.join(directory, new_name + extension)

    os.rename(old_filename, new_filename)

if __name__ == "__main__":
    main()