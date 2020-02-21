if [ ! -d venv ]
then
    echo 'Setting up virtualenv...'
    virtualenv -p python3.6 venv
fi
source venv/bin/activate
echo 'Installing python dependencies...'
pip install -r ./src/requirements.txt