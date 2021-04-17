#!/usr/bin/python3
"""module deply web static"""
from fabric.api import *
from datetime import datetime
from os.path import *


def do_deploy(archive_path):
    """packs everything into versions"""
    if not exists(archive_path):
        return False
    
    env.hosts = [
        '54.157.200.176',
        '35.237.198.52',
    ]
    try:
        filename = str(archive_path).split("/")[-1]
        filename = filename.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}".format(filename, filename))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format())
        print("New version deployed!")
        return True
    except:
        return False
