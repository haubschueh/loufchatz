#!flask/bin/python
from app import app
HOST='172.20.10.6'

# Starting on my server, your ip address may be different.
app.run(host=HOST, debug=True)
