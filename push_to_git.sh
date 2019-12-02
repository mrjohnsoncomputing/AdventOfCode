#!/bin/bash
git add .
echo "Please enter a commit message"
read msg
git commit -m "${msg}" 
git push
