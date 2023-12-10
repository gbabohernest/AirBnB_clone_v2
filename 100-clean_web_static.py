#!/usr/bin/python3
"""This module defines a Fabfile to delete out-of-date archives"""
from fabric.api import env, local, put, run, cd, lcd

env.hosts = ['54.146.86.193', '54.209.169.142']


def do_clean(number=0):
    """
      Delete out-of-date archives.

      Args:
          number (int): The number of archives to keep.

      If number is 0 or 1, keeps only the most recent archive. If
      number is 2, keeps the most and second-most recent archives,
      etc.
    """
    number = max(1, int(number))

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd("/data/web_static/releases"):
        run("ls -t | grep 'web_static_' | tail -n +{} |"
            "xargs rm -rf".format(number + 1))
