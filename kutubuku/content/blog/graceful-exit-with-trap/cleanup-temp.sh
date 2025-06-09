#!/usr/bin/env bash

echo "Temp file should be cleaned up when exit"

temp_file=$(mktemp)
echo "Temp file: $temp_file"

# Trap the EXIT signal and remove the temporary file
trap 'rm -f "$temp_file"; exit 1' EXIT
