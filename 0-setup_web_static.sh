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

apt-get update
apt-get install -y nginx


mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo $html > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current


sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/

printf %s "server {
	listen 80 default_server;
	listen [::]:80 defualt_server;
	add_header X-Served-By $hostname;
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

sudo systemctl restart nginx

echo -e "\nCompleted. ✅\n"
