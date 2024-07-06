#!/bin/bash

# Find all files less than 50 MB and add them to the staging area
find . -type f -size -50M -exec git add {} +

# Commit the changes
git commit -m "Add all files less than 50 MB"

# Push the changes to the remote repository
git push origin main
