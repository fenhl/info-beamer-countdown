#!/usr/bin/env python3

import sys

sys.path.append('/opt/py')

import datetime
import gitdir.host.github
import pathlib
import shutil
import socket
import subprocess
import time
import timespec

NODE_DIR = pathlib.Path(__file__).parent

if __name__ == '__main__':
    # copy dependencies into the node directory because some info-beamer versions don't support symlinks
    shutil.copy2('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', NODE_DIR / 'dejavu_sans.ttf')
    shutil.copy2(gitdir.host.github.GitHub().repo('fenhl/info-beamer-text').branch_path() / 'text.lua', NODE_DIR / 'text.lua')
    # run node
    target_date = timespec.parse(sys.argv[1:])
    popen = subprocess.Popen(['info-beamer', str(NODE_DIR))
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto('countdown/delta/set:{}'.format((target_date - datetime.datetime.now(datetime.timezone.utc)).total_seconds()).encode('utf-8'), ('127.0.0.1', 4444))
    sys.exit(popen.wait())
