import shutil
import os

source = os.listdir("../images/00")
dest1 = '../Project_2/Training'
dest2 = '../Project_2/Validation'
dest3 = '../Project_2/Testing'

for files in source:
	shutil.move(files,dest1)






#shutil.copyfileobj(00,Testing[p,5])


#files = os.listdir(source)

#for f in files:
 #   if (f.startswith("yaleB11")):
 #       shutil.move(f, dest1)
   # elif (f.startswith("Intel") or f.startswith("intel")):
  #      shutil.move(f, dest2)

