#!/bin/bash
search_dir=examples

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
