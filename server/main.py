import glob
import os
import shutil

source_path = '../source/*'
destination_path = '../destination'

postfixes = [1, 2, 3]

while True:
    source_objects = glob.glob(source_path)

    if len(source_objects) <= 0:
        continue

    object_path = source_objects[0]
    object_name = object_path.split('\\')[-1].split('.')

    prefix = object_name[0]
    file_extention = object_name[1]

    main_file_name = object_name[0] + '.' + object_name[1]
    shutil.copy(object_path, '.')

    file = open(main_file_name, 'r')
    lines = file.readlines()
    file.close()
    os.remove(f'./{main_file_name}')

    for item in range(1, len(postfixes)+1):
        file_name = f'{prefix}_{item}.{file_extention}'
        file = open(file_name, 'w')
        for j in range((item)*10):
            file.write(lines[j])
        file_path = f'./{file_name}'
        file.close()
        shutil.copy(file_path, f'{destination_path}/{file_name}')
        os.remove(file_path)

    os.remove(object_path)
