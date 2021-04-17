#!/usr/bin/python3
"""module pack web static"""
from fabric.api import *
from datetime import datetime
from os.path import getsize


def do_pack():
    """packs everything into versions"""
    local("mkdir -p /versions")
    tarname = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    try:
        print("Packing web_static to versions/{}.tgz".format(
            tarname
        ))
        local("tar -czvf /versions/{} /data/web_static/".format(tarname))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
            tarname, getsize("/versions/{}.tgz".format(tarname))
        ))
        return "/versions/{}.tgz".format(tarname)
    except:
        return None
