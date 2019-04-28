#!/usr/bin/env python
import os
import sys
from starlette.applications import Starlette
import uvicorn
import ssl

app = Starlette()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sigrh_cpl.settings')
    """uvicorn.run(
        app,
        host="0.0.0.0",
        port=8433,
        ssl_version=ssl.PROTOCOL_SSLv23,
        cert_reqs=ssl.CERT_OPTIONAL,
        ssl_certfile="./salakiaku.pem",
        ssl_keyfile="./key.pem",       
            
    )"""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
