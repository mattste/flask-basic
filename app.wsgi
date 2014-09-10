import sys

activate_this = '/home/ec2-user/Envs/flask-basic-venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/www/flask-basic')

from hello import app as application