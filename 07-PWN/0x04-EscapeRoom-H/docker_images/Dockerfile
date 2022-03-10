FROM ghcr.io/google/nsjail/nsjail:latest

## Update & Install
RUN apt-get update && apt-get install -y python3

## Copy essential files
COPY app.py /home/monkey/app.py
COPY flag0.txt /home/monkey/flag0.txt
COPY flag1.txt /home/monkey/flag1.txt
COPY flag2.txt /home/monkey/flag2.txt
COPY flag3.txt /home/monkey/flag3.txt
COPY flag4.txt /home/monkey/flag4.txt
COPY flag5.txt /home/monkey/flag5.txt
COPY flag6.txt /home/monkey/flag6.txt
COPY flag7.txt /home/monkey/flag7.txt
COPY flag8.txt /home/monkey/flag8.txt
COPY flag9.txt /home/monkey/flag9.txt

## Create user
RUN groupadd -g 6666 monkey && \
    useradd -m -d /home/monkey -s /bin/bash -g 6666 -G monkey -u 6666 monkey -p \
    $(python3 -c 'import crypt; print(crypt.crypt("monkey", crypt.mksalt(crypt.METHOD_SHA512)))')

CMD ["nsjail",			                \
        "-Ml",			                \
        "--hostname", "monkey",       	\
        "--user", "monkey",             \
        "--group", "monkey",            \
        "--port", "6666",   	        \
        "--skip_setsid",                \
        "--chroot", "/",        	    \
        "--cwd", "/home/monkey",    	\
        "--",		         	        \
        "/usr/bin/python3",             \
        "app.py"	                    \
]