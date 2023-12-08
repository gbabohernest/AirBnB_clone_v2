#!/usr/bin/python3
"""This module defines a Fabric script to distribute
   archived web_static to web servers
"""
import os.path
from fabric.api import env, put, run

env.hosts = ['54.146.86.193', '54.209.169.142']


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
