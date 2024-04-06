#!/usr/bin/env bash

#This script is to setup the web servers for the deployment
# of the web_static

html='<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'

echo -e "Installing Nginx if not already installed"

apt-get update
apt-get install -y nginx

echo -e "Setting up the directories\n"

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo $html > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current


chown -R ubuntu /data/
chgrp -R ubuntu /data/


echo -e "Updating the Server configuration\n"

printf %s "server {
	listen 80 default_server;
	listen [::]:80 defualt_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /index/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 http://cuberule.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}

}" > /etc/nginx/sites-available/default


echo -e "Restarting the Nginx service"

service nginx restart

echo -e "\nCompleted. ✅\n"
