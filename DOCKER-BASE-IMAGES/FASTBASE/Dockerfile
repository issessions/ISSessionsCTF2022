FROM debian:stable-slim

## Update system and install man pages, wget, vim, caps, git, zip, and sudo
RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y man-db manpages manpages-dev && \
    apt-get install -y vim libcap2-bin zip sudo

## Install Daemons and Services
RUN apt-get install -y openssh-server rsyslog supervisor \ 
    && apt-get install -y nano less build-essential bsdmainutils sysstat cowsay fortune \
    && apt-get install -y ltrace strace xxd gdb binutils \
    && apt-get install -y python3-pip libssl-dev libffi-dev python3-dev

## Instasll pip
RUN apt-get install -y python3-pip && pip3 install keyring && pip3 install keyrings.cryptfile

## Remove executable from pip
RUN rm -rf /usr/bin/pip3 /usr/bin/crontab /usr/bin/apt /usr/bin/apt-get /usr/lib/apt 

## Remove Unneeded Software 
RUN dpkg --remove --force-depends \
    openssh-client openssh-sftp-server; \
    apt-get autoremove; \
    exit 0

## Disable software installation
RUN rm -r /etc/apt/sources.list

## Rsyslog Settings: Make Syslog Files World-Readable
RUN sed -i 's/\$FileCreateMode 0640/$FileCreateMode 0644/' /etc/rsyslog.conf

## SSH Setting
RUN mkdir /var/run/sshd \ 
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/#MaxSessions 10/MaxSessions 100/' /etc/ssh/sshd_config \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

## Cleaning Loose Ends
RUN rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

## Create user
RUN groupadd -g 6666 monkey && \
    useradd -m -d /home/monkey -s /bin/bash -g 6666 -G monkey -u 6666 monkey -p \
    $(python3 -c 'import crypt; print(crypt.crypt("monkey", crypt.mksalt(crypt.METHOD_SHA512)))') && \
    echo "AllowUsers monkey" >> /etc/ssh/sshd_config

#delete history
USER monkey
RUN echo 'set +o history' >> ~/.bashrc
USER root

## Custom banner
COPY BANNER /etc/
RUN cat /etc/BANNER > /etc/motd && rm /etc/BANNER

## Launch Supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

