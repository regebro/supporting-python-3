
virtualenv -p `which python2.6` python26
virtualenv -p `which python2.7` python27
virtualenv -p `which python3.1` python31
virtualenv -p `which python3.2` python32
virtualenv -p `which python3.3` python33
virtualenv -p `which python3.4` python34

for i in 26 27 31 32 33 34
do
    python$i/bin/pip install zope.interface setuptools==11.2
done

# initialize files
make test > /dev/null || echo "Ignore failures"
make test > /dev/null || echo "Ignore failures"
make test > /dev/null || echo "Ignore failures"
make test > /dev/null || echo "Ignore failures"
make test > /dev/null || echo "Ignore failures"
make test > /dev/null || echo "Ignore failures"
