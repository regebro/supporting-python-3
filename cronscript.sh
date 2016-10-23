#!/bin/bash

cd /mnt/sites/supporting-python-3

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
TODAY=`date +%Y%m%d`
cp build/*${TODAY}.pdf /var/www/python3porting.com/pdfs
rm /var/www/python3porting.com/pdfs/SupportingPython3*latest.pdf
ln -s /var/www/python3porting.com/pdfs/SupportingPython3-phone-1.0-${TODAY}.pdf /var/www/python3porting.com/pdfs/SupportingPython3-phone-1.0-latest.pdf
ln -s /var/www/python3porting.com/pdfs/SupportingPython3-screen-1.0-${TODAY}.pdf /var/www/python3porting.com/pdfs/SupportingPython3-screen-1.0-latest.pdf
ln -s /var/www/python3porting.com/pdfs/SupportingPython3-tablet-1.0-${TODAY}.pdf /var/www/python3porting.com/pdfs/SupportingPython3-tablet-1.0-latest.pdf
