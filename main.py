#BUILDING FILE ORGANIZER
import os 
from pathlib import Path
path = "C:\\Users\\Shiva\\Downloads\\newfiles"
if os.path.exists(path):
	files = os.listdir(path)
	for file in files:	
		full_path = os.path.join(path,file)
		if os.path.isfile(full_path):
			print(full_path)

else:
	print("Sorry Invalid Path")