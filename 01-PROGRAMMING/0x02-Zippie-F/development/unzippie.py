#!/usr/bin/python3

import subprocess
import os

name = ''

for i in range(500):
    
    ## Grab directory contents
    name = os.listdir("FLAG")
    print(name)

    ztype = subprocess.check_output(f"file FLAG/{name[0]}", shell=True).decode("utf-8")

    if "Zip archive data" in ztype:
        ## zip
        ## Unzip file
        subprocess.call(f"unzip FLAG/{name[0]}", shell=True)
        
        ## Remove old archive
        subprocess.call(f"rm FLAG/{name[0]}", shell=True)

    elif "POSIX tar archive" in ztype:
        ## tar
        ## Unzip tar
        subprocess.call(f"tar -xf FLAG/{name[0]}", shell=True)

        ## Remove old archivee
        subprocess.call(f"rm FLAG/{name[0]}", shell=True)

    elif "7-zip archive data" in ztype:
        ## 7z
        ## Unzip 7z
        subprocess.call(f"7z x FLAG/{name[0]}", shell=True)

        ## Remove old archive
        subprocess.call(f"rm FLAG/{name[0]}", shell=True)
        
    else:
        ## gz
        ## Rename to gz
        nname = name[0].rstrip(".gz")
        subprocess.call(f"mv --force FLAG/{name[0]} FLAG/{nname}.gz", shell=True)

        ## Unzip gz
        subprocess.call(f"gunzip FLAG/{nname}", shell=True)
        