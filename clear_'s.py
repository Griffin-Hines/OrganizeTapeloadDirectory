import os

directory = "./"

file_list = os.listdir(directory)

for filename in file_list:
        if(filename.startswith('_')):
            count = 0
            for char in filename:
                if char == '_':
                    count += 1
                else:
                    break
             new_name = filename[count:]
        full_path = os.path.join(directory, filename)
        os.rename(full_path, os.path.join(directory, new_name))
