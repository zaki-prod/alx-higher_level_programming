#!/bin/bash
# A script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
