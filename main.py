#BUILDING FILE ORGANIZER
import os 
path = input("ENTER YOUR PATH > ").strip()
if os.path.exists(path):
	folders = os.listdir(path)
	for file in folders:
		print(file)
else:
	print("Sorry Invalid Path")