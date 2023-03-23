FROM debian:bullseye
RUN apt-get update && \
    apt-get -y install openssh-server && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/run/sshd && \
    rm -f /etc/ssh/ssh_host_*key*

COPY sshd_config /etc/ssh/sshd_config
COPY create-sftp-user /usr/local/bin/
COPY entrypoint /

EXPOSE 22

ENTRYPOINT ["/entrypoint"]