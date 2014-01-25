#!/bin/bash

#botRunner.sh, runs all bots a directory

cd ./bots/

for filename in $( ls bot* );
do
	echo "Executing:" $filename
	python $filename&
done