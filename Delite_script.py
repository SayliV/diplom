import glob
import os

dir = input("Enter path: ")
extension = input("Enter extention: ")

filelist = glob.glob(os.path.join(dir,"*."+extension))
for f in filelist:
    os.remove(f)
