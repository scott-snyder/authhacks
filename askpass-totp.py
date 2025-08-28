#!/usr/bin/python

import sys
import getpass
import subprocess

prompt = ' '.join (sys.argv[1:])

if prompt.find ('2nd factor') >= 0:
    cp = subprocess.run ('totp cern', capture_output = True, text = True, shell=True)
    totp = cp.stdout.strip()
    print (totp)
else:
    password = getpass.getpass (prompt)
    print (password)

