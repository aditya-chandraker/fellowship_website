#!/bin/bash
# author: Adi

cd ~/fellowship_website
git fetch
git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
sudo systemctl restart myportfolio

echo "Redeployment process w/ Docker initiated. Your site should be up and running soon."
