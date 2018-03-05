#!/bin/bash

LOCK="$TMP/sodbosha.lock"

case "$1" in
    "start")
        bash "`dirname $0`/start_bot.sh" &
        BOT_PID=$!
        echo $BOT_PID > $LOCK
    ;;
    
    "stop")
        if [ -f "$LOCK" ]; then
            BOT_PID=$(cat $LOCK)
            echo "Kill service $BOT_PID"
            kill $BOT_PID
            rm -f $LOCK
        else
            echo "Service dosen't look alive..."
        fi
    ;;
    
    *)
        echo "Usage: service (start|stop)"
        ;;
esac