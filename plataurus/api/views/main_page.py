import aiohttp_jinja2
from aiohttp import web

from plataurus.api.views.base import BaseHandler
from plataurus.settings import Config
from plataurus.utils.matching import get_matches


class MainPage(BaseHandler):
    async def get(self) -> web.Response:
        return aiohttp_jinja2.render_template("index.html", self.request,
                                              {"first_text": Config.Application.default_first_text,
                                               "second_text": Config.Application.default_second_text})

    async def post(self) -> web.Response:
        params = await self.request.json()
        first_matches, second_matches = get_matches(first_text=params['firstText'], second_text=params['secondText'],
                                                    threshold=params['rangeValue'])

        return web.json_response({"firstCommon": first_matches,
                                  "secondCommon": second_matches})
