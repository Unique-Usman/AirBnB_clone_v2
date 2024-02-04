#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime
from os.path import exists
import os

# env.hosts = ['localhost']
# env.user = "uniqueusman"
env.hosts = ['54.87.224.239']  # <IP web-01>, <IP web-02>


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

# ^ All remote commands must be executed on your both web servers
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)


def do_deploy(archive_path):
    """ distributes an archive to my web servers
    """
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesnt exist
    filename = archive_path.split('/')[-1]
    # so now filename is <web_static_2021041409349.tgz>
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    # curr = '/data/web_static/current'
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        # ^ Upload the archive to the /tmp/ directory of the web server
        run("mkdir -p {}/".format(no_tgz))
        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        # ^ Delete the archive from the web server
        run("rm -rf /data/web_static/current")
        # Delete the symbolic link /data/web_static/current from the web server
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        return True
    except Exception as e:
        return False


def deploy():
    """Deploy on full scale"""
    path_created = do_pack()
    if not path_created:
        return False
    return do_deploy(path_created)

# The script follows these steps:
# Call the do_pack() function & store the path of the created archive
# Return False if no archive has been created
# Call the do_deploy(archive_path) func, using the path of the new archive
# Return the return value of do_deploy
