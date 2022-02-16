def reading(filepath):
    with open(filepath, "r") as file_obj:
        return file_obj.readlines()