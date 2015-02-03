#!/bin/bash
PYTHON23=`which python23`
PYTHON23=${PYTHON23:-`which python2.3`}
PYTHON23=${PYTHON23:-/opt/python23/bin/python}
PYTHON24=`which python24`
PYTHON24=${PYTHON24:-`which python2.4`}
PYTHON24=${PYTHON24:-/opt/python24/bin/python}
PYTHON25=`which python25`
PYTHON25=${PYTHON25:-`which python2.5`}
PYTHON25=${PYTHON25:-/opt/python25/bin/python}
PYTHON26=`which python26`
PYTHON26=${PYTHON26:-`which python2.6`}
PYTHON26=${PYTHON26:-/opt/python26/bin/python}
PYTHON27=`which python27`
PYTHON27=${PYTHON27:-`which python2.7`}
PYTHON27=${PYTHON27:-/opt/python27/bin/python}
PYTHON31=`which python31`
PYTHON31=${PYTHON31:-`which python3.1`}
PYTHON31=${PYTHON31:-/opt/python31/bin/python}
PYTHON32=`which python32`
PYTHON32=${PYTHON32:-`which python3.2`}
PYTHON32=${PYTHON32:-/opt/python32/bin/python}
PYTHON33=`which python33`
PYTHON33=${PYTHON33:-`which python3.3`}
PYTHON33=${PYTHON33:-/opt/python33/bin/python}
PYTHON34=`which python34`
PYTHON34=${PYTHON34:-`which python3.4`}
PYTHON34=${PYTHON34:-/opt/python34/bin/python}


echo "##### PY23 #######"
$PYTHON23 source/_tests/tests23.py

echo "##### PY24 #######"
$PYTHON24 source/_tests/tests24.py

echo "##### PY25 #######"
$PYTHON25 source/_tests/tests24.py

echo "##### PY26 #######"
$PYTHON26 source/_tests/tests26.py

echo "##### PY27 #######"
# Run both the Python 2.6 tests and the 2.7 specific tests:
$PYTHON27 source/_tests/tests26.py
$PYTHON27 source/_tests/tests27.py


echo "##### PY31 #######"
$PYTHON31 source/_tests/tests31.py

echo "##### PY32 #######"
$PYTHON32 source/_tests/tests32.py

echo "##### PY33 #######"
$PYTHON33 source/_tests/tests32.py

echo "##### PY34 #######"
$PYTHON34 source/_tests/tests32.py
