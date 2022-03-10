FROM ghcr.io/google/nsjail/nsjail:latest

## Update & Install
RUN apt-get update

## Copy essential files
RUN mkdir /app
COPY BananaOverflow2 /app/BananaOverflow2
COPY flag.txt /app/flag.txt

## Run challenge
CMD ["nsjail",                                \
        "-Ml",                                \
        "--hostname", "monkey",               \
        "--port", "6666",                     \
        "--chroot", "/",                      \
        "--cwd", "/app",                      \
        "--",                                 \
        "/usr/bin/stdbuf", "-o0","./BananaOverflow2"                     \
]

