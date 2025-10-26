import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            dest_folder = os.path.join(folder_path, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))

if __name__ == "__main__":
    path = input("Inserisci il percorso della cartella da organizzare: ")
    organize_files(path)
    print("File organizzati per estensione!")
