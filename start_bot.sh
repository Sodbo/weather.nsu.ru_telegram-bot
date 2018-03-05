#!/bin/bash

source activate weather

try() {
    python3 bot.py
}

catch() {
    echo Shit happened!
    sleep 5    
}

while true; do
    try || catch
done