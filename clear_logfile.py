import sys
import os
import shutil

# clear_logfile file.log 1 5

if len(sys.argv) != 4:
    print('Use 4 args for script: "clear_logfile.py file.log 1 5"')
    exit(1)

file_name = sys.argv[1]
max_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if os.path.isfile(file_name):
    logfile_size = os.stat(file_name).st_size / 1024

    if logfile_size >= max_size:

        if logs_number > 0:

            for i in range(logs_number, 1, -1):
                src = file_name + '_' + str(i-1)
                dst = file_name + '_' + str(i)

                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print('Copying:' + src + ' -> ' + dst)

            shutil.copyfile(file_name, file_name + '_1')
            print('Copying:' + file_name + '   -> ' + file_name + '_1')
        with open(file_name, 'w'):
            print('Cleaning:' + file_name)
        print('Done')
