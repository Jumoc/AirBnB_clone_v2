#!/usr/bin/python3
"""module deply web static"""
from fabric.api import *
from datetime import datetime
from os.path import *


env.hosts = [
        '54.157.200.176',
        '35.237.198.52',
    ]


def do_pack():
    """packs everything into versions"""
    local("mkdir -p versions")
    tarname = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    try:
        print("Packing web_static to versions/{}".format(
            tarname
        ))
        local("tar -czvf versions/{} web_static".format(tarname))
        print("web_static packed: versions/{} -> {}Bytes".format(
            tarname, getsize("versions/{}".format(tarname))
        ))
        return "versions/{}".format(tarname)
    except:
        return None


def do_deploy(archive_path):
    """packs everything into versions"""
    if not exists(archive_path):
        return False
    try:
        filename = str(archive_path).split("/")[-1]
        filename = filename.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -zxf /tmp/{}.tgz -C /data/web_static/releases/{}".format(
            filename, filename
            ))
        run("rm /tmp/{}.tgz".format(filename))

        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                filename, filename
            ))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} "
            "/data/web_static/current".format(filename))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Full deploy of server"""
    path = do_pack()
    if (path is None):
        return False

    return(do_deploy(path))


def do_clean(number=0):
    """Clean all files"""
    pathsLocal = local("ls versions", capture=True)
    pathsServer = run("ls /data/web_static/releases")
    s_paths = pathsServer.split("  ")
    l_paths = pathsLocal.split("\n")

    l_dates = []
    for f in l_paths:
        f = f.split("_")[-1].split(".")[0]
        l_dates.append(datetime.strptime(f, "%Y%m%d%H%M%S"))
    l_dates.sort(reverse=True)

    s_dates = []
    for f in s_paths:
        if "_" in f and "." in f:
            f = f.split("_")[-1].split(".")[0]
            s_dates.append(datetime.strptime(f, "%Y%m%d%H%M%S"))
    s_dates.sort(reverse=True)

    for i in range(len(l_dates)):
        if (i >= int(number)):
            datestring = l_dates[i].strftime("%Y%m%d%H%M%S")
            local("rm versions/web_static_{}.tgz".format(datestring))

    for i in range(len(s_dates)):
        if (i >= int(number)):
            datestring = s_dates[i].strftime("%Y%m%d%H%M%S")
            run("rm versions/web_static_{}.tgz".format(datestring))

