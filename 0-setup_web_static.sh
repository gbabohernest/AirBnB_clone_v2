#!/usr/bin/env bash
# A Bash script that sets up web server with nginx for the deployment of web_static

# update & install nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create neccessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create a fake html file with content for testing nginx configuration
echo -e "some fake content for testing\n" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create/recreate a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# update Nginx configuration
# nginx_config="/etc/nginx/sites-available/default"
# sudo sed -i '/^\tlocation \/ {/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://frontendmentor.io/profile/gbabohernest/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart

exit 0
