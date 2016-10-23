#!/bin/bash

git fetch
if [ $(git rev-parse HEAD) == $(git rev-parse @{u}) ]; then
   echo "NOT UPDATED"
   exit 0
fi

echo "UPDATED: REBUILD!"
git pull
make html
make pdf-all
cp -r build/html/* /var/www/python3porting.com
cp build/*.pdf /var/www/python3porting.com/pdfs
