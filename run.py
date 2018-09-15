#!/usr/bin/env python3

import sys

sys.path.append('/opt/py')

import datetime
import shutil
import socket
import subprocess
import time
import timespec

if __name__ == '__main__':
    shutil.copy2('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/home/fenhl/info-beamer-countdown/dejavu_sans.ttf')
    shutil.copy2('/opt/git/github.com/fenhl/info-beamer-text/master/text.lua', '/home/fenhl/info-beamer-countdown/text.lua')
    target_date = timespec.parse(sys.argv[1:])
    popen = subprocess.Popen(['info-beamer', '/home/fenhl/info-beamer-countdown'])
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto('countdown/delta/set:{}'.format((target_date - datetime.datetime.now(datetime.timezone.utc)).total_seconds()).encode('utf-8'), ('127.0.0.1', 4444))
    sys.exit(popen.wait())
