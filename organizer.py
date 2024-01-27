import os
import shutil

extension_to_folder = {
    '.txt': 'TextFiles',
    '.jpg': 'ImageFiles',
    '.png': 'ImageFiles',
    '.docx': 'DocumentFiles',
    '.xlsx': 'DocumentFiles',
    '.pdf': 'DocumentFiles',
    '.mp3': 'AudioFiles',
    '.mp4': 'VideoFiles',
    #'.py': 'PythonScripts',
    # Ajoutez d'autres extensions et dossiers au besoin
}

current_directory = os.getcwd()
lst_dir = os.listdir(current_directory)
y = 0
for i in range(len(lst_dir)):
    y = lst_dir[i].find('.')
    for extension, folder in extension_to_folder.items():
        if extension == lst_dir[i][y:len(lst_dir[i])]:
            directory_to_create = folder
            path_fichier = os.path.join(current_directory, lst_dir[i])
            path = os.path.join(current_directory, directory_to_create)
            try:
                os.mkdir(path)
            except:
                pass
            shutil.move(path_fichier, path)
            break