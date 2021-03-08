import os 
import sys
import fileinput 


os.system("tput setaf 3" )
print("\t\t\t WELCOME TO THE AUTOMATION SCRIPT ")
os.system("tput setaf 5")
print("\t\t\t-------------------------------------------------------")
os.system("tput setaf 7")
print("""
\n
Howdy User !
Press 1:To Setup and Mount LVM
Press 2:To Increase the size of LVM
Press 3:To Decrease the size of LVM
Press 4:To Configure the LVM as your Datanode drive

 """) 

os.system("tput setaf 4")
option=input("Enter your choice: ")
print(option)

if int(option) == 1:
	
	os.system("tput setaf 1")
	print("List How Many Disks You Have")
	os.system("fdisk -l")
	os.system("tput setaf 4")
	print("----------------------------------")

	ch=input("You want to create LVM  parition in which disk ?: ")
	print(ch)
	b="pvcreate"+" "+ch
	print(b)
	os.system(b)
	os.system("pvdisplay")
	
	os.system("tput setaf 7")
	vgname=input("Enter the name of the VOLUME GROUP: ")
	print(vgname)
	c="vgcreate"+" "+vgname+" "+ch
	os.system(c)
	d="vgdisplay"+" "+"/dev/"+vgname+" "+ch
	os.system(d)
	
	os.system("tput setaf 7")
	lvname=input("Enter the name of the LOGICAL VOLUME:")	
	print(lvname)
	lvsize=input("Enter the size of LOGICAL VOLUME IN G-GiB ,M-MiB,K-KiB :")
	print(lvsize)
	lvcreate="lvcreate"+" "+"--size"+" "+lvsize+"--name"+lvname+" "+vgname
	os.system(lvcreate)
	os.system("lvdisplay")
	
	os.system("tput setaf 7")
	print("Lets mount the LVM into a dir")
	dir_name=input("So what should be the name of the directory:")
	print(dir_name)
	mkdir="mkdir"+" "+dir_name
	os.system(mkdir)
	format="mkfs.ext4"+" "+"/dev/"+vgname+"/lvol0"
	os.system(format)
	print("Please wait mounting the LVM to the directory given")
	mount="mount"+" "+"/dev/"+vgname+"/"+"lvol0"+" "+dir_name
	os.system(mount)
	print("Sucessfully mounted")
	
	os.system("tput setaf 1")
	os.system("tput setaf 7")
	
         

elif int(option) == 2:
	

	os.system("tput setaf 6")	
	os.system("vgdisplay")
	vgname=input("Enter the Volume Group: ")
	print(vgname)
	os.system("lvdisplay")
	print("Thanks for the input wait while we find the location")
	ext_size=input("OK Buddy,how much you want the extend in K-KiB,M-MiB,G-GiB DONT EXCEED THE SIZE OF VOLUME GROUP :) :")
	print(ext_size)
	lvextd="lvextend"+" "+"--size"+" "+"+"+ext_size+" "+"/dev/"+vgname+"/"+"lvol0"
	os.system(lvextd)
	resize2fs="resize2fs"+" "+"/dev/"+vgname+"/"+"lvol0"
	os.system(resize2fs)
	os.system("tput setaf 3")
	os.system("lvdisplay")
	os.system("tput setaf 6")
	print("LVM EXTENDED ENJOY !!!")
	os.system("tput setaf 3")
	print("OK,Thanks for using the script")
	os.system("tput setaf 7")
	

elif int(option) == 3:
    vgname=input("Enter the Volume Group which is already created: ")
    print(vgname)
    dir_name=input("Enter the name of the directory which is mounted:")
    print(dir_name)
    umount="umount"+" "+"/dev/"+vgname+"/"+"lvol0"+" "+dir_name
    os.system(umount)
    print("Sucessfully unmounted")
    Scan="e2fsck"+" "+"-f"+" "+"/dev/mapper/"+vgname+"-lvol0"
    os.system(Scan)
    print("Sucessfully Scanned/Cleaned")
    clean_size=input("OK, how much you want the clean in K-KiB,M-MiB,G-GiB :) :")
    print(clean_size)
    resize2fs="resize2fs"+" "+"/dev/mapper/"+vgname+"-"+"lvol0"+" "+clean_size
    os.system(resize2fs)
    os.system("tput setaf 6")	
    os.system("lvdisplay")
    print("Thanks for the input wait while we find the location")
    print("If data is present in the drive, the data of which we are reducing will be lost")
    red_size=input("OK, how much you want the reduce in K-KiB,M-MiB,G-GiB :) :")
    print(red_size)
    lvred="lvreduce"+" "+"--size"+" "+"-"+red_size+" "+"/dev/"+vgname+"/"+"lvol0"
    os.system(lvred)
    os.system("tput setaf 3")
    os.system("lvdisplay")
    os.system("tput setaf 6")
    print("LVM REDUCED ENJOY !!!")
    os.system("tput setaf 3")
    print("OK,Thanks for using the script")
    os.system("tput setaf 7")
    print("Please wait mounting the LVM to the directory given")
    mount="mount"+" "+"/dev/"+vgname+"/"+"lvol0"+" "+dir_name
    os.system(mount)
    print("Sucessfully mounted")

	


elif int(option) == 5:
	
	print("Hope so you have setup the Hadoop Datanode i will just add this dynamic partition in a bit")
	textToReplace =input("Enter the directory of the folder you want configure as Datanode drive in the form of /root/folder_name: ")
	print(textToReplace)
	textToSearch =input("Please enter the existing folder used for Datanode storage: ")
	print(textToSearch)

	fileToSearch = '/etc/hadoop/hdfs-site.xml'
	tempFile = open( fileToSearch, 'r+' )
	for line in fileinput.input( fileToSearch ):
   		tempFile.write( line.replace( textToSearch, textToReplace))
	tempFile.close()
	
	print("Done please start your Datanode now..")

else:
	os.system("tput setaf 1")
	print("Please enter a valid option")
	os.system("tput setaf 7")
	



	









