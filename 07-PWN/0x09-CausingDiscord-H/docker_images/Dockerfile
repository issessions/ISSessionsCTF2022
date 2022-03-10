FROM ghcr.io/google/nsjail/nsjail:latest

## Update & Install
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y cowsay

## Copy essential files
RUN mkdir /app/
COPY bot.py /app/
COPY requirements.txt /app/
COPY monkey.cow /usr/share/cowsay/cows/
COPY token.env /tmp/
COPY flag.txt /home/monkey/
#ENV PATH="${PATH}:/usr/games"

## Install requirements
RUN pip3 install -r /app/requirements.txt

RUN groupadd -g 6666 monkey && \
    useradd -m -d /home/monkey -s /bin/bash -g 6666 -G monkey -u 6666 monkey
RUN chmod 500 /app/bot.py

## Run challenge
CMD ["nsjail",                                \
    "-Mo",                                \
    "--hostname", "monkey",               \
    "--chroot", "/",                      \
    "--cwd", "/app",                      \
    "-u", "monkey", \
    "--disable_clone_newnet",\
    "--bindmount","/tmp",\
    "--",                                 \
    "/usr/bin/python3",                   \
    "bot.py"                        \
    ]