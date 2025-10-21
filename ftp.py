import os
import configparser
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Read values from the config file
ftp_user = config.get("FTP", "USER", fallback="admin")
ftp_pass = config.get("FTP", "PASS", fallback="admin@123")
ftp_port = config.getint("FTP", "PORT", fallback=2121)
shared_folder = config.get("FTP", "SHARED_FOLDER", fallback=os.getcwd())
allow_anonymous = config.getboolean("FTP", "ALLOW_ANONYMOUS", fallback=True)

# Setup authorizer
authorizer = DummyAuthorizer()
authorizer.add_user(ftp_user, ftp_pass, shared_folder, perm="elradfmw")

if allow_anonymous:
    authorizer.add_anonymous(shared_folder, perm="elr")

# Configure FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Start FTP server
server = FTPServer(("0.0.0.0", ftp_port), handler)

print(f"FTP Server running on port {ftp_port}...")
print(f"Serving directory: {shared_folder}")
print(f"Anonymous access: {'Enabled' if allow_anonymous else 'Disabled'}")

server.serve_forever()
