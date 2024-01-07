#!/bin/bash
# Script that takes in URL, send a request to that URL and display size of the body of the response
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
