#!/usr/bin/env bash
# sets up the web static
if ! [ -x "$(command -v nginx)" ]; then
    apt-get -y install nginx
fi

if [[ ! (-d /data/) ]]; then
    mkdir /data/
fi

if [[ ! (-d /data/web_static/) ]]; then
    mkdir /data/web_static/
fi

if [[ ! (-d /data/web_static/releases/) ]]; then
    mkdir /data/web_static/releases/
fi

if [[ ! (-d /data/web_static/shared/) ]]; then
    mkdir /data/web_static/shared/
fi

if [[ ! (-d /data/web_static/releases/test/) ]]; then
    mkdir /data/web_static/releases/test/
fi

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

location="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
if [ "$(grep -c 'location /hbnb_static' /etc/nginx/sites-available/default)" -eq 0 ]; then
    sed -i "/listen 80 default_server;/a $location" /etc/nginx/sites-available/default
fi

service nginx start
