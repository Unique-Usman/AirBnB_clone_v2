#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.25.15.14', '34.232.78.53']
env.user = "ubuntu"


def do_pack():
    """generates a .tgz archive from the contents of a file"""
    date = datetime.now()
    date = date.strftime("%Y%m%d%H%M%S")
    archive_path = "./versions/web_static_{}.tgz".format(date)
    if not os.path.exists("./versions/"):
        os.mkdir("./versions/")
    cmd = local("tar -cvzf {} web_static/".format(archive_path))

    if cmd.succeeded:
        return archive_path
    if cmd.failed:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        archive_filename = archive_path.split('/')[-1]
        uncompressed_filename = archive_filename[:-4]
        run("mkdir -p /data/web_static/releases/{}"
            .format(uncompressed_filename))
        run("tar -xvzf  /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, uncompressed_filename))
        run("sudo rm /tmp/{}".format(archive_filename))
        run("sudo rm -r /data/web_static/current")
        run("ln -s\
             /data/web_static/releases/{}/web_static /data/web_static/current"
            .format(uncompressed_filename))
        return True
    except Exception:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success