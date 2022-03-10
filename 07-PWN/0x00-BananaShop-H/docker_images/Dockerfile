FROM ghcr.io/google/nsjail/nsjail:latest

RUN apt-get update

COPY BananaShop /home/shop/BananaShop
COPY flag.txt /home/shop/flag.txt

CMD ["nsjail",                             \
        "-Ml",                            \
        "--hostname", "monkey",           \
        "--port", "6666",               \
        "--chroot", "/",            \
        "--cwd", "/home/shop",        \
        "--",                     \
        "./BananaShop"  \
        ]