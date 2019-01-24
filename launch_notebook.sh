#!/bin/sh
# USAGE: bash launch_notebook.sh (in a docker container)

jupyter-notebook --allow-root --ip=`ip route | awk 'NR==2 {print $9}'`
