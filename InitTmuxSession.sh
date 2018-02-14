#!/usr/bin/env bash

SCRIPT_NAME="$(basename "${0}")"
SESSION_NAME="Flasher"

# Should the bash color-codes be used in the output? (true/false)
USE_BASH_COLORS=true

if [ "${USE_BASH_COLORS}" = true ]; then
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
fi

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
if (tmux has-session -t "${SESSION_NAME}" 2>/dev/null); then
  printf "${colorR}%s${colorNONE}%s\n" "YES" "."
  #fail_self_test
  tmux kill-session -t "${SESSION_NAME}" 2>/dev/null
else
  printf "${colorG}%s${colorNONE}%s\n" "no" "."
fi

printf "%s ${colorG}%s${colorNONE}%s\n" "Self-check" "passed" "."

printf "%s\n" "Creating session contents..."
tmux new-session -d -s "${SESSION_NAME}"

# First window: git. Left pane: status, right pane: log of commits.
tmux rename-window -t "${SESSION_NAME}:1" "git"
tmux send-keys -t "${SESSION_NAME}:1" "git st" Enter
tmux split-window -t "${SESSION_NAME}:1" -h
tmux send-keys -t "${SESSION_NAME}:1.right" "git lc" Enter
tmux select-pane -t "${SESSION_NAME}:1.left"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "1"
printf ": ${colorM}%s${colorNONE}\n" "git"

# Second window: main code. Left pane: flake, right pane: vim.
tmux new-window -t "${SESSION_NAME}:2" -n "main"
tmux send-keys -t "${SESSION_NAME}:2" "flake8 main.py" Enter
tmux split-window -t "${SESSION_NAME}:2" -h
tmux send-keys -t "${SESSION_NAME}:2.right" "vim main.py" Enter
tmux select-pane -t "${SESSION_NAME}:2.right"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "2"
printf ": ${colorM}%s${colorNONE}\n" "main"

# Third window: Application code. Left pane: flake, right pane: vim.
tmux new-window -t "${SESSION_NAME}:3" -n "Application"
tmux send-keys -t "${SESSION_NAME}:3" "flake8 Application.py" Enter
tmux split-window -t "${SESSION_NAME}:3" -h
tmux send-keys -t "${SESSION_NAME}:3.right" "vim Application.py" Enter
tmux select-pane -t "${SESSION_NAME}:3.right"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "3"
printf ": ${colorM}%s${colorNONE}\n" "Application"

# Fourth window: LatexBuilder code. Left pane: flake, right pane: vim.
tmux new-window -t "${SESSION_NAME}:4" -n "LatexBuilder"
tmux send-keys -t "${SESSION_NAME}:4" "flake8 LatexBuilder.py" Enter
tmux split-window -t "${SESSION_NAME}:4" -h
tmux send-keys -t "${SESSION_NAME}:4.right" "vim LatexBuilder.py" Enter
tmux select-pane -t "${SESSION_NAME}:4.right"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "4"
printf ": ${colorM}%s${colorNONE}\n" "LatexBuilder"

# Fifth window: Config code. Left pane: flake, right pane: vim.
tmux new-window -t "${SESSION_NAME}:5" -n "Config"
tmux send-keys -t "${SESSION_NAME}:5" "flake8 Config.py" Enter
tmux split-window -t "${SESSION_NAME}:5" -h
tmux send-keys -t "${SESSION_NAME}:5.right" "vim Config.py" Enter
tmux select-pane -t "${SESSION_NAME}:5.right"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "5"
printf ": ${colorM}%s${colorNONE}\n" "Config"

# Sixth window: Utils code. Left pane: flake, right pane: vim.
tmux new-window -t "${SESSION_NAME}:6" -n "Utils"
tmux send-keys -t "${SESSION_NAME}:6" "flake8 Utils.py" Enter
tmux split-window -t "${SESSION_NAME}:6" -h
tmux send-keys -t "${SESSION_NAME}:6.right" "vim Utils.py" Enter
tmux select-pane -t "${SESSION_NAME}:6.right"
printf " --> [${colorG}OK${colorNONE}] ${colorY}%s${colorNONE}" "6"
printf ": ${colorM}%s${colorNONE}\n" "Utils"

# Brings first window (git) to front:
tmux select-window -t "${SESSION_NAME}:1"

printf "${colorG}%s${colorNONE}%s\n" "Successfully completed" "."
