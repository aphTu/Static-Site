import os
import shutil


# recursive function
# copies all content from source directory to destination directory -- static to public
def static_to_public(destination, source):
    source_path = os.path.join(".", source)
    dest_path = os.path.join(".", destination)
    # print(f"source path: {source_path}")
    # print(os.listdir("./static"))
    # print(os.listdir(source_path))

    # delete all contents of the destination directory
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        os.makedirs(dest_path)
    else:
        os.makedirs(dest_path)
    # copy item from source directory
    if not os.path.exists(source_path):
        raise Exception(
            f"{source} directory does not exist, please ensure {source} directory exist"
        )
    dir_of_static = os.listdir(source_path)
    log = []
    # print(f"dir_of_static: {dir_of_static}")
    for item in dir_of_static:
        item_path = os.path.join(source_path, item)
        if os.path.isfile(item_path):
            # print(f"item_path: {item_path}")
            shutil.copy(item_path, dest_path)
            log.append(f"Added item: {item}")
        else:
            log.append(f"Added item: {item}")
            dest_path_temp = os.path.join(dest_path, item)
            src_path_temp = os.path.join(source_path, item)
            temp_log = static_to_public(destination=dest_path_temp, source=src_path_temp)
            log.extend(temp_log)
    #     #     items.extend()
    return log
