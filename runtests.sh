echo "##### PY23 #######"
/opt/python23/bin/python source/_tests/tests23.py

echo "##### PY24 #######"
/opt/python24/bin/python source/_tests/tests24.py

echo "##### PY25 #######"
/opt/python25/bin/python source/_tests/tests24.py

echo "##### PY26 #######"
./python26/bin/python source/_tests/tests26.py

echo "##### PY27 #######"
# Run both the Python 2.6 tests and the 2.7 specific tests:
./python27/bin/python source/_tests/tests26.py
./python27/bin/python source/_tests/tests27.py


echo "##### PY31 #######"
./python31/bin/python3 source/_tests/tests31.py

echo "##### PY32 #######"
./python32/bin/python3 source/_tests/tests32.py

echo "##### PY33 #######"
./python33/bin/python3 source/_tests/tests32.py

echo "##### PY34 #######"
./python34/bin/python3 source/_tests/tests32.py
