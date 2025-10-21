# Python FTP Server (Configurable)

A lightweight and configurable **FTP Server** built using [`pyftpdlib`](https://github.com/giampaolo/pyftpdlib).  
This project allows you to share files over a local or remote network with configurable settings using a `config.ini` file.

---

## Features

- Customizable **username**, **password**, **port**, and **shared folder**
- Optional **anonymous read-only access**
- Simple configuration via `config.ini`
- Lightweight and easy to deploy

---

## Project Structure

```
ftp-server/
│
├── server.py
├── config.ini
└── README.md
```

---

## Requirements

- Python 3.8+
- `pyftpdlib` package

Install dependencies:

```bash
pip install pyftpdlib
```

---

## Configuration

Edit the `config.ini` file to set your preferences:

```ini
[FTP]
USER = user
PASS = 123452
PORT = 2121
SHARED_FOLDER = /Users/nithishkumarkr/
ALLOW_ANONYMOUS = true
```

| Field | Description |
|--------|-------------|
| **USER** | FTP username |
| **PASS** | FTP password |
| **PORT** | Port to run the server on (use `2121` if `21` requires admin privileges) |
| **SHARED_FOLDER** | Directory to share via FTP |
| **ALLOW_ANONYMOUS** | Allow anonymous read-only access (`true` or `false`) |

---

## Running the Server

Run the FTP server with:

```bash
python server.py
```

You should see an output like:

```
FTP Server running on port 2121...
Serving directory: /Users/nithishkumarkr/
Anonymous access: Enabled
```

---

## Connecting to the FTP Server

You can connect using:

### Command Line (macOS/Linux/Windows)
```bash
ftp localhost 2121
```

### FTP Client (e.g., FileZilla)
- **Host:** localhost  
- **Port:** 2121  
- **Username:** admin  
- **Password:** admin@123  

---

## Stopping the Server

Press **Ctrl + C** in the terminal to stop the FTP server.

---

## Notes

- Running on port `21` requires **root/admin privileges** — prefer `2121`.
- Make sure your **firewall allows the chosen port**.
- Avoid using weak passwords when exposing the server to external networks.

## License

This project is open-source and available for personal or educational use.
