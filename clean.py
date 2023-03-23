#!/usr/bin/env python3
import os

from subprocess import run, PIPE


# os_call
def os_call(string):
    try:
        os.system(f'{string}')
    except (FileNotFoundError, PermissionError) as e:
        print(f'Error running command {string}')        

docker_build_name = "custom_sftp"
version = "latest"

os_call(string=f"docker stop {docker_build_name}")
os_call(string=f'docker rm {docker_build_name}')
os_call(string=f"docker images {docker_build_name} -q | xargs docker rmi -f")