#!/bin/bash

# author: Adi

# Kill all existing tmux sessions
tmux kill-server

# Start a new detached Tmux session named portfolio_website
# cd, fetch, venv, install, run
tmux new-session -d -s  portfolio_website \
    "cd ~/fellowship_website && \
    git fetch && \
    git reset origin/main --hard && \
    source python3-virtualenv/bin/activate && \
    pip install -r requirements.txt && \
    flask run --host=0.0.0.0"

echo "Redeployment process initiated in tmux session. Your site should be up and running soon."
