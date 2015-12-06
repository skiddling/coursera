import os
import re

files = os.listdir(".")
for f in files:
    fname = os.path.splitext(f)
    suffix = fname[1]
    if(suffix == ".vtt"):
        handle = open(f, 'r')
        newfile = open(fname[0] + '.srt', 'w')
        wholefile = handle.read()
        temp = re.subn('\.', ',', wholefile)
        t = re.subn('WEBVTT', '', temp[0])
        newfile.write(t[0])
        handle.close()
        newfile.close()
