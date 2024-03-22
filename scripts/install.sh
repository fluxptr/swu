#!/bin/bash

curl https://get.modular.com | sh - && \
modular auth mut_e5285eee571c4b07b3c9e6c9cfda59ee

modular install mojo

BASHRC=$( [ -f "$HOME/.bash_profile" ] && echo "$HOME/.bash_profile" || echo "$HOME/.bashrc" )
echo 'export MODULAR_HOME="/home/codespace/.modular"' >> "$BASHRC"
echo 'export PATH="/home/codespace/.modular/pkg/packages.modular.com_mojo/bin:$PATH"' >> "$BASHRC"
source "$BASHRC"
