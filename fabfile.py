#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = [localhost]

env.user = "zibxto"

def do_pack():
    """generates a .tgz archive from the contents of a file"""
    date = datetime.now()
    date = date.strftime("%Y%B%d%H%M%S")
    if not os.path.exists("./versions/"):
        os.mkdir("./versions/")
    cmd = local("tar -cvf ./versions/web_static_{}.tgz ./web_static/".format(date))

    if cmd.succeeded:
        return "./versions/web_static_{}.tgz".format(date)
    if cmd.failed:
        return None
