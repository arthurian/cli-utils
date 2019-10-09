#!/usr/bin/env python
# vim: set ft=python noai et ts=4 sw=4:

import os
import os.path
import sys
import ConfigParser

credentials_file = os.path.join(os.path.expanduser('~'), '.aws', 'credentials')
items = {'key': 'aws_access_key_id', 'secret': 'aws_secret_access_key'}

if len(sys.argv) < 2:
    print "Usage: %s profileName [key|secret]" % sys.argv[0]
    sys.exit(0)

config = ConfigParser.RawConfigParser()
config.read(credentials_file)
section = sys.argv[1]
if len(sys.argv) == 2:
    print "\n".join([config.get(section, items[item]) for item in ('key', 'secret')])
else:
    if sys.argv[2] in items:
        print config.get(section, items[sys.argv[2]])
    else:
        sys.stderr.write("Invalid credential item specified: %s\n" % sys.argv[2])
        sys.exit(1)
