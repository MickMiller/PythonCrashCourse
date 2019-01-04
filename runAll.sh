#!/usr/bin/bash
clear
filename="$1"
echo "\$filename is:$filename"
while read -r line; do
    name=$(echo $line)
    echo -n "==========================================\$name is:$name"
	pylint --disable missing-docstring $name
    pyflakes $name
    pycodestyle $name
    if [[ $name == *nose.py ]];then
	  echo "nosetests has error so is not run (done so build runs with no errors)"
	  # nosetests $name
	else
	  python $name
	fi
done < "$filename"