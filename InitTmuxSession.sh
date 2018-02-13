#!/usr/bin/env bash

SCRIPT_NAME="$(basename "${0}")"
SESSION_NAME="Flasher"


printf "%s\n" "Self-checking..."

printf " --> %s " "Checking whether tmux server exists..."
if [ ! tmux info &>/dev/null ]; then
  printf "%s\n" "NO."
  exit 1
else
  printf "%s\n" "yes."
fi

printf " --> %s \"%s\" %s " "Checking whether session" "Flasher" "exists..."
if [ tmux has-session -t "${SESSION_NAME}" 2>/dev/null ]; then
  printf "%s\n" "YES."
  exit 1
else
  printf "%s\n" "no."
fi

printf "Self-check passed.\n"
