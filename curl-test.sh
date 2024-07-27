#!/bin/bash

# Generate user for the new timeline post
NAME="user$(date +%s)"
EMAIL="$NAME@gmail.com"
CONTENT="adi is cool"

# Create a new post using the POST endpoint
POST_RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT")

# Check if the POST request was successful
if echo "$POST_RESPONSE" | grep -q '"id"'; then
    echo "POST request successful: $POST_RESPONSE"
else
    echo "POST request failed: $POST_RESPONSE"
    exit 1
fi

# Retrieve the list of timeline posts using the GET endpoint
GET_RESPONSE=$(curl -s http://localhost:5000/api/timeline_post)

# Check if the new post is in the list of timeline posts
if echo "$GET_RESPONSE" | grep -q "$NAME"; then
    echo "GET request successful: New post found in timeline posts."
elsemymys
    echo "GET request failed: New post not found in timeline posts."
    exit 1
fi
