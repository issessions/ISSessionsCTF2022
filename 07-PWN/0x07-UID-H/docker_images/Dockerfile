FROM gcr.io/issessions/privescbaseimg:latest

## VULNERABILITY:
## --------------
## Add capability to python
RUN setcap cap_setuid+ep /usr/bin/python3.9
## --------------

## Copy over file and chnage permissions
COPY hashes.txt /root
RUN chmod 400 /root/hashes.txt

## Start ssh on port 22
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
