#!/usr/bin/env bash

SCRIPT_NAME="$(basename "${0}")"
SESSION_NAME="Flasher"

colorNONE="\033[0m"       # resets color to terminal's FG color.
colorK="\033[0;30m"       # regular black
colorR="\033[0;31m"       # regular red
colorG="\033[0;32m"       # regular green
colorY="\033[0;33m"       # regular yellow
colorB="\033[0;34m"       # regular blue
colorM="\033[0;35m"       # regular magenta
colorC="\033[0;36m"       # regular cyan
colorW="\033[0;37m"       # regular white
colorKEM="\033[1;30m"     # bold black
colorREM="\033[1;31m"     # bold red
colorGEM="\033[1;32m"     # bold green
colorYEM="\033[1;33m"     # bold yellow
colorBEM="\033[1;34m"     # bold blue
colorMEM="\033[1;35m"     # bold magenta
colorCEM="\033[1;36m"     # bold cyan
colorWEM="\033[1;37m"     # bold white

function fail_self_test
{
  printf "%s ${colorR}%s${colorNONE}%s\n" "Self-check" "failed" "."
  printf "%s\n" "Aborting."
  exit 1
}

printf "%s\n" "Self-checking..."

printf " --> %s " "Checking whether tmux server exists..."
if [ tmux info &>/dev/null ]; then
  printf "${colorR}%s${colorNONE}%s\n" "NO" "."
  fail_self_test
else
  printf "${colorG}%s${colorNONE}%s\n" "yes" "."
fi

printf " --> %s \"${colorC}%s${colorNONE}\" %s " \
    "Checking whether session" "Flasher" "exists..."
if [ tmux has-session -t "${SESSION_NAME}" 2>/dev/null ]; then
  printf "${colorR}%s${colorNONE}%s\n" "YES" "."
  fail_self_test
else
  printf "${colorG}%s${colorNONE}%s\n" "no" "."
fi

printf "%s ${colorG}%s${colorNONE}%s\n" "Self-check" "passed" "."
