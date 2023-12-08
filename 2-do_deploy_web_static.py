#!/usr/bin/python3
"""This module defines a Fabric script to distribute
   archived web_static to web servers
"""

from os.path import exists
from fabric.api import local, run, env, put

env.hosts = ['54.146.86.193', '54.209.169.142']
env.user = 'ubuntu'
env.key_filename = ['/home/vagrant/.ssh/id_rsa']


def do_deploy(archive_path):
    """
      Distributes archived web_static from do_pack() to web servers

      Args:
          archive_path (str): Path to the archive file.

      Returns:
          bool: True if deployment succeeds, False otherwise.
      """

    if not exists(archive_path):
        return False

    try:
        # upload the archive to /tmp/ directory on the remote servers
        put(archive_path, "/tmp/")
        # Extract the contents to /data/web_static/releases/
        filename = archive_path.split('/')[-1]
        directory_name = "/data/web_static/releases/{}".format(filename
                                                               .split('.')[0])
        run("sudo mkdir -p {}".format(directory_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, directory_name))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(filename))
        # Delete symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(directory_name))
        print("New version deployed!")

        return True

    except Exception as e:
        print("Deployment failed", str(e))
        return False
