#!/bin/bash -x
sudo apt-get update -y
sudo apt-get install python3 -y
sudo apt install python3-pip -y
pip install flask
pip install gunicorn 
sudo apt-get update -y
sudo apt-get install nginx -y
git clone https://github.com/ravi1312/webapp.git
cd webapp
python3 app.py
