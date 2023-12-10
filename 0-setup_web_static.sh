#!/usr/bin/env bash
#  Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
if command -v nginx > /dev/null 2>&1 
then
    true
else
    sudo apt-get -y install nginx
fi
test -e /data/
if (($? == 1))
then
    sudo mkdir /data/
fi
test -e /data/web_static/
if (($? == 1))
then
    sudo mkdir /data/web_static/
fi
test -e /data/web_static/releases/
if (($? == 1))
then
    sudo mkdir /data/web_static/releases/
fi
test -e /data/web_static/shared/
if (($? == 1))
then
    sudo mkdir /data/web_static/shared/
fi
test -e /data/web_static/releases/test/
if (($? == 1))
then
    sudo mkdir /data/web_static/releases/test/
fi
echo "Web Static" | sudo tee /data/web_static/releases/test/index.html
test -L /data/web_static/current
if (($? == 1))
then
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
    sudo rm /data/web_static/current
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
hbnb_static="\\\n\\tserver{\\n\\t\\tlocation /hbnb_static/{\\n\\t\\t\\talias /data/web_static/current/;\\n\\t\\t}\\n\\t}"
sudo sed -i "64i $hbnb_static" /etc/nginx/nginx.conf
sudo service nginx restart
