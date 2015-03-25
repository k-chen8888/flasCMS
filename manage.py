# Set path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Flask Manager
from flask.ext.script import Manager, Server

# Packages
# Add more packages below index
from index import index

# Bind managers to packages
# Add more managers below mgr_index
mgr_index = Manager(index)

# Activate mgr for index package with debug and reload on by default
# For other managers, call .add_command on them, name the command, and start the server
mgr_index.add_command('runserver', Server(
	use_debugger = True,
	use_reloader = True,
	host = '0.0.0.0')
)

'''
Start the manager
Remeber to start with a command!
'''
if __name__ == '__main__':
	# Change mgr_index to the name of the default manager 
	mgr_index.run()
