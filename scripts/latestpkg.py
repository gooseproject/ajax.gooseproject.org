#!/usr/bin/python
from __future__ import print_function
import koji
from operator import itemgetter
kojiclient = koji.ClientSession('http://koji.gooselinux.org/kojihub', {})

tag = "gl6-alpha"

lastbuild = sorted(kojiclient.getLatestBuilds(tag), key=itemgetter('completion_time'))[-1]

print(lastbuild)
