FROM gcr.io/issessions/privescbaseimg:latest

## VULNERABILITY:
## --------------
## Remove user privilege from wget
RUN chmod 700 /usr/bin/wget
## Create sudo privilege for monkey user
RUN echo "monkey ALL = NOPASSWD: /usr/bin/wget" >> /etc/sudoers
## --------------

## Copy over file and chnage permissions
WORKDIR /home/monkey
COPY flag.txt .
RUN chmod 400 flag.txt

## Start ssh on port 22
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
