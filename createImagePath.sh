#!/bin/bash
search_dir=image_to_compute

command_str="python3 run.py "

for image in "$search_dir"/*
do
        image_dir=""
		image_dir+=$image
        image_dir+=" "
        command_str+=$image_dir
done

command_str+="--output-dir output/"

$command_str
