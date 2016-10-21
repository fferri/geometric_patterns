#!/bin/sh
ffmpeg -framerate 30 -i $1-%08d.png -c:v libx264 -r 30 -pix_fmt yuv420p $1.mp4
