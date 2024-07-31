#!/bin/bash
# author: Adi

cd ~/fellowship_website
git fetch
git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
sudo systemctl restart myportfolio

echo "Redeployment process initiated in using systemd. Your site should be up and running soon."
