import os
import shutil

def extract_images_and_overwrite_image_name(path_to_data, path_to_exit, flag=0):

    for folder in os.listdir(path_to_data): # for any folder from session
        for filename in os.listdir(os.path.join(path_to_data, folder)): # for any file from folder
            if flag == 0:
                if filename.startswith("full_image") is False:
                    new_filename = "{}_".format(folder) + filename
                    if os.path.isfile(os.path.join(path_to_data, folder, filename)): # check file
                        shutil.copy(os.path.join(path_to_data, folder, filename), os.path.join(path_to_exit, new_filename))
            elif flag == 1:
                if filename.startswith("full_image"):
                    new_filename = "{}_".format(folder) + filename
                    if os.path.isfile(os.path.join(path_to_data, folder, filename)):
                        shutil.copy(os.path.join(path_to_data, folder, filename), os.path.join(path_to_exit, new_filename))