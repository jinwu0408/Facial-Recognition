import shutil
import os

source = "/home/ubuntu/Team2A-AJJW/images/00"
dest1 = '/home/ubuntu/Team2A-AJJW/Project_2/Training'
dest2 = '/home/ubuntu/Team2A-AJJW/Project_2/Validation'
dest3 = '/home/ubuntu/Team2A-AJJW/Project_2/Testing'

files = os.listdir(source)

for f in files:
    if (f.startswith("yaleB11")):
        shutil.move(f, dest1)
   # elif (f.startswith("Intel") or f.startswith("intel")):
  #      shutil.move(f, dest2)

