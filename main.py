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
			full_path = Path(full_path)
			extension = full_path.suffix
			print(extension)
	

else:
	print("Sorry Invalid Path")