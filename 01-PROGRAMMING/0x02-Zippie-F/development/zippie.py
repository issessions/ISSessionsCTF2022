#!/usr/bin/python3

import subprocess
import os
import time
from random import randrange

## Compression type
zip_type = ["zip", "tar", "7z", "gz"]

for i in range(1, 501):
    ## Grab random number
    rand = randrange(5)

    ## Grabbing filenames in current directory
    name = os.listdir("flag?")

    if rand == 0:
        ## zip
        ## zip -9 -m flag?/<i>.zip flag?/<filename>
        subprocess.call(f"zip -9 -m flag?/{i}.zip flag?/{name[0]}", shell=True)
    
    elif rand == 1:
        ## tar
        ## tar -cf <i>.tar <filename>
        subprocess.call(f"tar -cf flag?/{i}.tar flag?/{name[0]}", shell=True)

        ## Removing extra file
        subprocess.call(f"rm flag?/{name[0]}", shell=True)
    
    elif rand == 2:
        ## 7z
        ## 7z a <i>.7z <filename>
        subprocess.call(f"7z a flag?/{i}.7z flag?/{name[0]}", shell=True)

        ## Removing extra file
        subprocess.call(f"rm flag?/{name[0]}", shell=True)

    else:
        ## gz
        ## gzip <filename>
        subprocess.call(f"gzip flag?/{name[0]}", shell=True)

        ## Renaming archive file
        subprocess.call(f"mv flag?/{name[0]}.gz flag?/{str(i)}", shell=True)