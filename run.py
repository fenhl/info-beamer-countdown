#!/usr/bin/env python3

import sys

sys.path.append('/opt/py')

import datetime
import pathlib
import shutil
import socket
import subprocess
import time
import timespec

if __name__ == '__main__':
    # copy dependencies into the node directory because some info-beamer versions don't support symlinks
    shutil.copy2('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', pathlib.Path(__file__).parent / 'dejavu_sans.ttf')
    shutil.copy2('/opt/git/github.com/fenhl/info-beamer-text/master/text.lua', pathlib.Path(__file__).parent / 'text.lua')
    # run node
    target_date = timespec.parse(sys.argv[1:])
    popen = subprocess.Popen(['info-beamer', '/home/fenhl/info-beamer-countdown'])
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto('countdown/delta/set:{}'.format((target_date - datetime.datetime.now(datetime.timezone.utc)).total_seconds()).encode('utf-8'), ('127.0.0.1', 4444))
    sys.exit(popen.wait())
