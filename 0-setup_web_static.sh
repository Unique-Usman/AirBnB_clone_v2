#!/usr/bin/env bash
# install nginx on a server and set it up with html

sudo apt-get update

if command -v nginx > /dev/null 2>&1; then
  echo "Nginx is already installed."
else
  # Install Nginx
  sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Web Static" | sudo tee /data/web_static/releases/test/index.html

target_folder="/data/web_static/releases/test/"
symbolic_link="/data/web_static/current"

# Remove existing symbolic link if it exists
if [[ -L "$symbolic_link" ]]; then
  rm "$symbolic_link"
  echo "Existing symbolic link removed."
fi

# Create a new symbolic link
ln -s "$target_folder" "$symbolic_link"
echo "Symbolic link created to $target_folder."

sudo chown -R ubuntu:ubuntu /data/ 

# Update Nginx configuration
hbnb_static="\\\n\\tlocation /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}"
sudo sed -i "33i $hbnb_static" /etc/nginx/sites-available/default
sudo service nginx restart
