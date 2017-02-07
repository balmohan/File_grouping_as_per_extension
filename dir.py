import os
import shutil
import glob
cpath=os.getcwd()+"\\"	#+"\\"+"Downloads\\"
listext=[]
src=[]
dst=[]
def get_extention(cpath):
	listoffiles=os.listdir(os.getcwd())
	for i in listoffiles:
		extention=i.split(".")[-1]
		extention=extention.upper()
		listext.append(extention)
	return set(listext)
	
def create_folders(cpath):
	for i in get_extention(cpath):
		createfolders=cpath +"//"+i
		if os.path.exists(createfolders)==False: #Checks for folder already present or not
			os.mkdir(createfolders)			#Creats New Folder
			#print i
			print ("Folder Name " +i+" Successfully Created")
		else:
			print("Folder " +i+" already exist ignoring it")
			
def srcfilename():
	srcpath=[]
	for i in os.listdir(cpath):
		if os.path.isfile(cpath+i):
			srcpath.append(cpath+i)
	return srcpath
def dstlocation():
	dstpath=[]
	for i in os.listdir(cpath):
		if os.path.isfile(cpath+i)==False:
			dstpath.append(cpath+i)
	return dstpath
def move():
	src=srcfilename()
	dst=dstlocation()
	for i in range(0,len(src)) :
		for j in range(0,len(dst)):
			exttopath=src[i].split(".")[-1]
			uexttopath=exttopath.upper()
			filepath=cpath+uexttopath
			#return filepath
			if cmp(filepath,dst[j])==0:
				print ("Files moved successfully")
				shutil.move(src[i],dst[j])
if os.path.exists(cpath)==True:
	#print (cpath)
	#print (get_extention(cpath))
	create_folders(cpath)
	#print (srcfilename())
	#print (dstlocation())
	move()
else:
	#os.mkdir("Downloads")
	print (os.getcwd())
	exit
