#!/usr/bin/env bash

LOG_FILE=myprogram.log
echo "Log file: $LOG_FILE"

trap 'echo "$(date)": Error on line $LINENO: "$BASH_COMMAND" >> $LOG_FILE' ERR

mycommand
