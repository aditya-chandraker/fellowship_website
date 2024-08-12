#!/bin/bash
# author: Adi

cd ~/fellowship_website
git fetch
git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

echo "Redeployment process w/ Docker initiated. Your site should be up and running soon."
