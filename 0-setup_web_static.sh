#!/usr/bin/env bash
if ! [ -x "$(command -v nginx)" ]; then
    apt-get -y install nginx
fi

if [[ ! (-d "/data/") ]]; then
    mkdir "/data/"
fi

if [[ ! (-d "/data/web_static/") ]]; then
    mkdir "/data/web_static/"
fi

if [[ ! (-d "/data/web_static/releases/") ]]; then
    mkdir "/data/web_static/releases/"
fi

if [[ ! (-d "/data/web_static/shared/") ]]; then
    mkdir "/data/web_static/shared/"
fi

if [[ ! (-d "/data/web_static/releases/test/") ]]; then
    mkdir "/data/web_static/releases/test/"
fi

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/current /data/web_static/releases/test/

chown -R -H ubuntu:ubuntu /data/

#location=""
