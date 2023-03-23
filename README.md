# sftp

This Repository contains sftp configuration with python script that build custom image from atmoz Dockerfile.

# usage:  

```$ ./setup.py ``` : build and start container from Dockerfile.

```to upload file to sftpserver move files or copy in to upload (docker-compose.yml location path).```

Default FileZilla sftp login:

- Host : ```server ip address```
- default_port : ```40```
- username : ```admin```
- password : ```admin```

For linux (connect-stp uses localhost as ip)  

```$ ./connect-sftp ``` : connect to sftp with bash script 
