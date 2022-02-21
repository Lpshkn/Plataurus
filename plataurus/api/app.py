import jinja2
import aiohttp_jinja2
from aiohttp import web
from os.path import dirname, join

from plataurus.api.views.main_page import MainPage


def create_app() -> web.Application:
    app_main = web.Application()

    aiohttp_jinja2.setup(app_main, loader=jinja2.FileSystemLoader(join(dirname(__file__), "templates")))

    app_main.router.add_view("/", MainPage)

    return app_main
