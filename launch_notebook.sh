#!/bin/sh
# used from docker image

jupyter-notebook --ip=`ip route | awk 'NR==2 {print $9}'`
