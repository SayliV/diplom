import glob
import shutil
import os

dir1 = input("Enter path where to pick up from: ")
dir2 = input("Enter path where to move it: ")
extension = input("Enter extention: ")

files_to_copy = glob.glob(os.path.join(dir1,"*."+extension))
destination_path = dir2
for file in files_to_copy:
    shutil.copy2(file, destination_path)