FROM gcr.io/issessions/privescbaseimg:latest

## VULNERABILITY:
## --------------
## Remove user privilege from vi
RUN chmod 700 /usr/bin/vim
## Create sudo privilege for monkey user
RUN echo "monkey ALL = NOPASSWD: /usr/bin/vim" >> /etc/sudoers
## --------------

## Remove user privilege from git
RUN chmod 700 /usr/bin/git

## Copy files to system
WORKDIR /home/monkey
COPY flag.txt ./.flag.txt
COPY todo.txt .
COPY AuthSec.zip .

## Unzip archive
RUN unzip AuthSec.zip && rm AuthSec.zip

## Change ownership
RUN chown monkey:monkey .flag.txt
RUN chown monkey:monkey todo.txt
RUN chown -R monkey:monkey AuthSec

## Change permissions to read and execute
RUN chmod 444 .flag.txt
RUN chmod 444 todo.txt
RUN chmod 555 AuthSec
RUN chmod a-w AuthSec/*
RUN chmod -R a-w AuthSec/.git
RUN chmod 555 /home/monkey

## Start ssh on port 22
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
