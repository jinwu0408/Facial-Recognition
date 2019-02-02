import shutil
import os

source = "../images/00"
dest1 = '../Project_2/Training'
dest2 = '../Project_2/Validation'
dest3 = '../Project_2/Testing'

files = os.listdir(source)

for f in files:
    if (f.startswith("yaleB11_P00A") or f.startswith("yaleB11_P01A")):
        shutil.move(f, dest1)
   # elif (f.startswith("Intel") or f.startswith("intel")):
  #      shutil.move(f, dest2)

