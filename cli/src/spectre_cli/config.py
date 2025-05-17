"""Configure environment variables."""

import os

SPECTRE_SERVER_HOST = os.environ.get("SPECTRE_SERVER_HOST", None)
SPECTRE_SERVER_PORT = os.environ.get("SPECTRE_SERVER_PORT", None)

if SPECTRE_SERVER_HOST is not None and SPECTRE_SERVER_PORT is not None:
    SPECTRE_SERVER = f"http://{SPECTRE_SERVER_HOST}:{SPECTRE_SERVER_PORT}"
else:
    SPECTRE_SERVER = os.environ.get("SPECTRE_SERVER", "http://localhost:5000")


