#!/bin/bash

tempKey=""
key=""
key2=""
dirCounter=1

echo "Input youre starting directory:"
read dirCounter


while [ dirCounter > 0 ]; do
	cd "/root/Downloads/PyNight/Hard6/$dirCounter"

	for file in `find /root/Downloads/PyNight/Hard6/$dirCounter -exec file {} + | grep ASCII | awk 'BEGIN { FS = ":" } ; { print $1 }'`; do tempKey=`grep KEY $file | awk 'BEGIN { FS = ":" } ; { print $2 }'`; done
	dirCounter=$((dirCounter-1))
	echo $dirCounter
	read pause2
	echo "Bout to unzip $dirCounter with $key boss"
	unzip -d "/root/Downloads/PyNight/Hard6/$dirCounter" -P "$key" "$dirCounter.zip";
done
