#!/bin/bash

#botRunner.sh, runs all bots a directory

#run server
python server.py&

cd ./bots

for filename in $( ls bot* );
do
	echo "Executing:" $filename
	python $filename&
done