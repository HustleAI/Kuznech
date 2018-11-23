import os
import shutil
import logging

logging.basicConfig(filename="prepare_data.log", level=logging.INFO,
                    format='%(asctime)s : %(levelname)s - %(message)s')

logging.info("Start script")

def extract_images_and_overwrite_image_name(path_to_data, path_to_exit, flag=0):
    if os.path.isdir(path_to_data or path_to_exit) is False:            # check(object is a directory?)
        return logging.critical("*** Critical error! One of the path or both wrong. Please read documentation")
    if flag not in [0,1]:                                               # check(flag is set correctly?)
        return logging.critical("*** Critical error! Flag wrong. Please read documentation")
    logging.debug("### Used mode: flag={}".format(flag))
    logging.debug("## Used session: {}".format(path_to_data))
    for folder in os.listdir(path_to_data):                             # for any folder from session
        logging.debug("# Used folder: {}".format(folder))
        if os.path.isdir(os.path.join(path_to_data, folder)) is False:  # check(object is a directory?)
            logging.debug("*** Attention! This object: " + folder + " is not a folder")
            continue
        for filename in os.listdir(os.path.join(path_to_data, folder)): # for any file from folder
            logging.debug("Used file: {}".format(filename))
            if os.path.isfile(os.path.join(path_to_data, folder, filename)) is False:  # check(file or dir?)
                logging.debug("*** Attention! This object: " + filename + " is not a file")
                continue
            if filename.endswith("jpg") is False:               # check(file is a image?)
                logging.debug("*** Attention! This file: " + filename + " is not a image")
                continue
            if flag == 0:
                if filename.startswith("full_image") is False:
                    new_filename = "{}_".format(folder) + filename
                    logging.debug("New name file: {}".format(new_filename))
                    shutil.copy(os.path.join(path_to_data, folder, filename), os.path.join(path_to_exit, new_filename))
            elif flag == 1:
                if filename.startswith("full_image"):
                    new_filename = "{}_".format(folder) + filename
                    logging.debug("New name file: {}".format(new_filename))
                    shutil.copy(os.path.join(path_to_data, folder, filename), os.path.join(path_to_exit, new_filename))
    logging.info("# Transformed files in folder: {}".format(path_to_exit))
    for file in os.listdir(path_to_exit):                             # for any folder from session
        logging.info(file)
    logging.info("Script done. All renamed images in folder: {}".format(path_to_exit))