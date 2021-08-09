#!/bin/bash



if [[ $1 == "set" ]]
then
   export $(grep -v '^#' .env | xargs)
elif [[ $1 == "unset" ]]
then
   unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)
else
   echo "Please use set or unset only."
fi
