#!/bin/bash
ps aux --sort=-pcpu | head -n 10
ps aux --sort=-pcpu | head -n 10 > processes.txt

for line in {1..10}
do
	mkdir "dir$line"
	adjustedLine=$((line + 1))
	awk "NR==$adjustedLine" processes.txt > dir$line/file$line
done
	