import prepare_data_image

PATH_TO_DATA = 'titan03_oct' # the path to the folder with images
PATH_TO_EXIT = 'Transform_data' # the path to the folder with transform data

#prepare_data_image.extract_images_and_overwrite_image_name(PATH_TO_DATA, PATH_TO_EXIT)
prepare_data_image.extract_images_and_overwrite_image_name(PATH_TO_DATA, PATH_TO_EXIT, flag=1)