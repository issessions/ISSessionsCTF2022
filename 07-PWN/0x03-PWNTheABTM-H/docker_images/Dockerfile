FROM ghcr.io/google/nsjail/nsjail:latest

## Update & Install
RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip

## Copy essential files
RUN mkdir /app
COPY PWNTheABTM.py /app/PWNTheABTM.py
COPY requirements.txt /app/requirements.txt
COPY flag.txt /app/flag.txt

## Install requirements
RUN pip3 install -r /app/requirements.txt

## Run challenge
CMD ["nsjail",                                \
        "-Ml",                                \
        "--hostname", "monkey",               \
        "--port", "6666",                     \
        "--chroot", "/",                      \
        "--cwd", "/app",                      \
        "--env", "PYTHONIOENCODING=UTF-8",    \
        "--",                                 \
        "/usr/bin/python3",                   \
        "PWNTheABTM.py"                       \
]