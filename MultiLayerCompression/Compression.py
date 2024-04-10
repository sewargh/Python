import os
from zipfile import ZipFile
import pyminizip
import hashlib


#Get the current directory the script is running from.
directory = os.getcwd()
print("NOTE: there should be in this path " + directory + " the following files: \n1)ListOfNames.txt file \n2)secret.txt")

#the file name to be compressed.
tocompressfile="secret.txt"

#open the file with name used as compress file name and their hash as the password.
f = open(directory+"/ListOfNames.txt","r")

#loop for every name in the file and compress with password
for name in f:
    name = name.strip()#eliminate the end line that came from the file so the hash is not wrong.
    hashedName = hashlib.md5(name.encode('utf-8')).hexdigest() #hash the name to set it as the password.

    print(name + ": ",end="") 
    print(hashedName)

    #pyminizip allows for password protection for zipping files 
    pyminizip.compress(directory + "/" + tocompressfile , "" , directory +"/" + name + ".zip"  , hashedName, 9)
    tocompressfile=name+".zip" #change the name of the file to be compresseed to the created zip file.

#the arguemtns of the pyminizip function are as follows: 
#(srcfile, prefix, zipfile name, password, compress_level) --> #pyminizip.compress("/srcfile/path.txt", "file_path_prefix", "/distfile/path.zip", "password", int(compress_level))

print("the final compressed file is finally created with the name: " + name + ".zip")

f.close()
