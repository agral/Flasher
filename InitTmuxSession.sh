#!/usr/bin/env bash

SCRIPT_NAME="$(basename "${0}")"


printf "%s\n" "Self-checking..."

# Checks whether tmux server exists:
printf " --> %s " "Checking whether tmux server exists..."
if [ ! tmux info &>/dev/null ] ; then
  printf "%s\n" "NO."
  exit 1
else
  printf "%s\n" "yes."
fi
