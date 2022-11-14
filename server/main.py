import glob
import os
import shutil
import pathlib

source_path = '../source/*'
destination_path = '../destination'

postfixes = [1, 2, 3]

while True:
    # get files inside source directory
    source_objects = glob.glob(source_path)

    # check if there are any source object available
    if len(source_objects) <= 0:
        continue

    # get object path and object name
    object_path = source_objects[0]
    object_name = object_path.split('\\')[-1].split('.')

    # get file prefix and extention
    prefix = object_name[0]
    file_extention = object_name[1]

    if file_extention == 'py':
        os.system(f'python {object_path}')
    else:
        # copy file from source directory to server directory
        main_file_name = object_name[0] + '.' + object_name[1]
        shutil.copy(object_path, '.')

        # open main file and get lines, finally remove main file
        file = open(main_file_name, 'r')
        lines = file.readlines()
        file.close()
        os.remove(f'./{main_file_name}')

        # open a directory
        directory = 'files'
        parent_dir = pathlib.Path(__file__).parent.resolve()
        dir_path = os.path.join(parent_dir, directory)
        os.mkdir(dir_path)

        # open files inside the directory
        for item in range(1, len(postfixes)+1):
            file_name = f'{prefix}_{item}.{file_extention}'
            file_path = f'{dir_path}/{file_name}'
            file = open(file_path, 'w')
            for j in range((item)*10):
                file.write(lines[j])

            file.close()

        # make archive the directory, move to destination, unpack, then remove
        shutil.make_archive(dir_path, 'zip', parent_dir, directory)
        shutil.move(f'{dir_path}.zip', destination_path)
        shutil.unpack_archive(
            f'{destination_path}/{directory}.zip', destination_path, 'zip')
        os.remove(f'{destination_path}/{directory}.zip')

        # move files from destination/files to destination
        files_objects = glob.glob(f'{destination_path}/{directory}/*')
        for object in files_objects:
            shutil.move(object, destination_path)
        os.rmdir(f'{destination_path}/{directory}')

        # remove the files directory
        shutil.rmtree(dir_path)

    # remove object from source
    os.remove(object_path)
