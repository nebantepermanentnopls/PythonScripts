from sys import argv
import os
import time

# delete_old_files.py age [ derectories ]

start_time = time.asctime()

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS = 0
AGE = int(argv[1])
DIRECTORIES = argv[2:]


def delete_old_files(folder):
    global TOTAL_DELETED_SIZE
    global TOTAL_DELETED_FILES
    global AGE
    age_time = time.time() - 60 * 60 * 24 * AGE
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)
            if os.path.getmtime(file_name) < age_time:
                TOTAL_DELETED_FILES += 1
                TOTAL_DELETED_SIZE += os.path.getsize(file_name)
                print('DELETING FILE: ' + file_name)
                os.remove(file_name)


def delete_empty_directories(folder):
    global TOTAL_DELETED_DIRS
    deleted_dirs_in_run = 0
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            deleted_dirs_in_run += 1
            print('DELETED EMPTY DIR: ' + path)
            os.rmdir(path)
    if deleted_dirs_in_run > 0:
        delete_empty_directories(folder)
    TOTAL_DELETED_DIRS += deleted_dirs_in_run


for directory in DIRECTORIES:
    delete_old_files(directory)
    delete_empty_directories(directory)

finish_time = time.asctime()

print('-------------------------------------------------')
print('START TIME: ' + start_time)
print('FINISH TIME: ' + finish_time)
print('TOTAL DELETED SIZE: ' + str(TOTAL_DELETED_SIZE / 1024 / 1024) + 'MB')
print('TOTAL DELETED FILES: ' + str(TOTAL_DELETED_FILES))
print('TOTAL DELETED DIRECTORIES: ' + str(TOTAL_DELETED_DIRS))
print('-------------------------------------------------')
