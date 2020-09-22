pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt

python config.py
venv/bin/supervisord -c /etc/supervisord.conf
venv/bin/supervisorctl update all