#!/bin/bash

folder_name="data"

# Check if the folder exists
if [ ! -d "data" ]; then
    # If it doesn't exist, create it
    mkdir "data"
    echo "Folder 'data' created."
else
    echo "Folder 'data' already exists."
fi
