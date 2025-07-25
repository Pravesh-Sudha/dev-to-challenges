#!/bin/bash

# Update system

sudo apt update -y
sudo apt upgrade -y

# Install Python, pip, venv, nginx, git

sudo apt install -y python3 python3-pip python3-venv nginx git

# Clone your GitHub project (REPLACE with your repo)

cd /home/ubuntu
git clone https://github.com/Pravesh-Sudha/dev-to-challenges.git
cd dev-to-challenges/philo-agent

# Set up Python virtual environment

python3 -m venv venv
source venv/bin/activate

# Install requirements

pip install -r requirements.txt
pip install gunicorn

# Test gunicorn (run once, ctrl+c after checking)

gunicorn -w 4 app:app --bind 0.0.0.0:8000

# Set up systemd service for gunicorn

sudo tee /etc/systemd/system/voiceapp.service > /dev/null <<EOF
[Unit]
Description=Gunicorn instance to serve Philosophy Voice App
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/dev-to-challenges/philo-agent
Environment="PATH=/home/ubuntu/dev-to-challenges/philo-agent/venv/bin"
ExecStart=/home/ubuntu/dev-to-challenges/philo-agent/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
EOF

# Enable and start the Gunicorn service

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl start voiceapp
sudo systemctl enable voiceapp

# Configure Nginx

sudo tee /etc/nginx/sites-available/voiceapp > /dev/null <<EOF
server {
    server_name philosophy.praveshsudha.com;

    location / {
   	proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_cache_bypass $http_upgrade;
    }

    location /static/ {
        alias /home/ubuntu/dev-to-challenges/philo-agent/static/;
    }

    client_max_body_size 20M;

    access_log /var/log/nginx/voiceapp_access.log;
    error_log /var/log/nginx/voiceapp_error.log;


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/philosophy.praveshsudha.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/philosophy.praveshsudha.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = philosophy.praveshsudha.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name philosophy.praveshsudha.com;
    return 404; # managed by Certbot


}
EOF

# Set correct permissions for all files
sudo chmod -R 755 /home/ubuntu/dev-to-challenges/philo-agent/static

# Make sure all files are owned by the same user running the app (usually ubuntu)
sudo chown -R ubuntu:ubuntu /home/ubuntu/dev-to-challenges/philo-agent/static
sudo chmod +x /home/ubuntu
sudo chmod +x /home/ubuntu/dev-to-challenges
sudo chmod +x /home/ubuntu/dev-to-challenges/philo-agent


# Enable Nginx config

sudo ln -s /etc/nginx/sites-available/voiceapp /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t && sudo systemctl restart nginx

echo "✅ Deployment complete. Access your app via EC2 public IP!"