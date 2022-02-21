import os
from aiohttp import web

from plataurus.settings import Config
from plataurus.api.app import create_app

# Server information
SERVER_HOST = os.getenv('SERVER_HOST', Config.Application.host)
SERVER_PORT = os.getenv('SERVER_PORT', Config.Application.port)


def main():
    app = create_app()
    web.run_app(app, host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
