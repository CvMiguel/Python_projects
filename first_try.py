def copy_with_different_name( file_path, target_directoty, new_name):
    # This function should copy the file in 'file_path' to 'target_directory' with the name 'new_name'
    # The file should be copied to the target_directory with the new name
    # The function should return the new path of the copied file

    shutil.copy(file_path, target_directoty)
    return os.path.join(target_directoty, new_name)
