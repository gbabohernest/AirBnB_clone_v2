#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from the contents
of the web_static folder.

This script defines a function, do_pack(), which creates a
compressed archive(.tgz) containing all the files within the
web_static folder.

The generated archive is stored in the 'versions' folder, and
its name follows the
format: web_static_<year><month><day><hour><minute><second>.tgz.

Returns:
    str: The path to the generated archive if successful, None otherwise.
"""

from datetime import datetime
from fabric.api import local


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
