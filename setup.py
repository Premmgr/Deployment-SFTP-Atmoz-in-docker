#!/usr/bin/env python3
import subprocess
from subprocess import PIPE, run
import time
import os

from subprocess import run, PIPE
atmoz_path = "atmoz_conf"

# execution_time decoration
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_called = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time:.5f} seconds")
        return function_called
    return wrapper

# linux subprocess call
def linx_sub_call(string):
    cmd = string.split()
    try:
        result = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print(result.stdout)
        print(result.stderr)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error running command '{' '.join(cmd)}': {e}")
def os_call(string):
    try:
        os.system(f'{string}')
    except (FileNotFoundError, PermissionError) as e:
        print(f'Error running command {string}')        


@execution_time
def build_docker(build_name, build_version):
    os.chdir(atmoz_path)
    try:
        os_call(f'docker build -t {build_name}:{build_version} .')
    except FileNotFoundError as e:
        print(f'Error on during {__name__} process')


docker_build_name = "custom_sftp"
version = "latest"

build_docker(build_name=docker_build_name, build_version=version)

os_call(string="docker-compose up -d")






