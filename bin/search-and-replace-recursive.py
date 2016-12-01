#!/usr/bin/env python
# vim: set ft=python noai et ts=4 sw=4:

import os, os.path, sys, fnmatch

def searchReplace(directory, search, replace, filePattern):
    absdir  = os.path.abspath(directory)
    processed = 0
    print "Starting in %s searching for pattern %s" % (absdir, filePattern)
    for path, dirs, files in os.walk(absdir):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            print "Processing %s" % filepath
            with open(filepath) as f:
                s = f.read()
            s = s.replace(search, replace)
            with open(filepath, "w") as f:
                f.write(s)
            processed += 1
    print "Processed %s files." % processed

if len(sys.argv) != 5:
    print "Usage: %s [dir] [search] [replace] [filePattern]" % os.path.split(sys.argv[0])[1]
    sys.exit(0)

searchReplace(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
