#BUILDING FILE ORGANIZER
import os 
from pathlib import Path
import shutil
managing = {
	"Images" : [".jpg", ".jpeg", ".png", ".gif"],
	"Videos" : [".mp4", ".mkv", ".avi"],
	"PDFs"   : [".pdf"],
	"Music"  : [".mp3", ".wav"],
	"Docx" 	 : [".docx"],
	"Excel"  : [".xlsx",".csv"],
	"Others Files" : [".exe",".zip"],
	"Python Files" : [".py"],
	"Java Files"   : [".java"],
	"C++ Files"   : [".cpp"],

 } 
while True:
	path = input("Enter Your FIle URL > ").strip()
	# path = "C:\\Users\\Shiva\\Downloads\\newfiles" # TEMPORARY URL FILE AS EXPERIMENT.
	if path != "1":
		if os.path.exists(path):
			files = os.listdir(path)
			for file in files:	
				full_path = os.path.join(path,file) #new path resource 
				if os.path.isfile(full_path):
					print(full_path)
					full_path = Path(full_path)
					extension = full_path.suffix
					for category,extensions in managing.items():
						if extension in extensions:
							new_files = os.path.join(path,category)
							os.makedirs(new_files,exist_ok=True)
							try:
								shutil.move(full_path,new_files)
							except Exception as e:
								print("Sorry",e)	

		else:
			print("Sorry Invalid Path")
	else:
		break
