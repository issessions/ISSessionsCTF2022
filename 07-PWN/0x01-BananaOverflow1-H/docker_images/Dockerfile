FROM ghcr.io/google/nsjail/nsjail:latest

## Update & Install
RUN apt-get update

## Copy essential files
RUN mkdir /app
COPY BananaOverflow1 /app/BananaOverflow1
COPY flag.txt /app/flag.txt

## Run challenge
CMD ["nsjail",                                \
        "-Ml",                                \
        "--hostname", "monkey",               \
        "--port", "6666",                     \
        "--chroot", "/",                      \
        "--cwd", "/app",                      \
        "--",                                 \
        "BananaOverflow1"                     \
]

