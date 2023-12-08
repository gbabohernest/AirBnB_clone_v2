#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['54.146.86.193', '54.209.169.142']


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path to the generated archive if successful, None otherwise.
    """

    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -czf {} web_static/".format(archive_path))

    if result.failed:
        return None

    return archive_path


def do_deploy(archive_path):
    """Distributes archived web_static from do_pack() to web servers

       Args:
          archive_path (str): Path to the archive file.

       Returns:
          bool: True if deployment succeeds, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = filename.split(".")[0]

    if put(archive_path, "/tmp/").failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            filename, name)).failed:
        return False
    if run("rm /tmp/{}".format(filename)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ "
           "/data/web_static/current".format(name)).failed:
        return False

    return True


def deploy():
    """
    Create and distribute an archive to web servers.

    Returns:
        bool: True if deployment succeeds, False otherwise.
    """
    # Call do_pack and store the path of the created archive
    archive_path = do_pack()

    if archive_path is None or not os.path.exists(archive_path):
        return False

    return do_deploy(archive_path)
