import glob                                                                                                                                          
import os
 
files = []
 
## Append all images to list
for filename in glob.glob('*.jpg'):
    files.append(filename)
 
## Upload all images
for image in sorted(files):
    print "uploading %s" % image
    command = "gdput.py -t ocr %s > result.log" % image
    print "running %s" % command
    os.system(command)
    resultfile = open("result.log","r").readlines()
 
    for line in resultfile:
        if "id:" in line:
            fileid = line.split(":")[1].strip()
            filename = image.split(".")[0] + ".txt"
            get_command = "gdget.py -f txt -s %s %s" % (filename, fileid)
            print "running %s" % get_command
            os.system(get_command)
 
## Merge all results to single txt file
print "Merging all text files into ocr-result.txt"
os.system("cat *.txt > ocr-result.txt")
print "Done"
