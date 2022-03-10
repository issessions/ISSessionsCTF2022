FROM gcr.io/issessions/fastbase:latest

COPY gottagofast /usr/bin/gottagofast
COPY flag.txt /root/flag.txt

RUN chown root.root /root/flag.txt
RUN chmod 400 /root/flag.txt
RUN chown root.root /usr/bin/gottagofast
RUN chmod 4755 /usr/bin/gottagofast

RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
