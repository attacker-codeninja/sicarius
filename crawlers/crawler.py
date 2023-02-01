from requests_html import AsyncHTMLSession
import urllib3
import lxml
import requests
import pyppeteer
import websockets
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings()
import asyncio


class Crawler:
    def __init__(self) -> None:
        self.urls_list = []
        self.url_links_dict = {}

    async def work(self, url):
        asession = AsyncHTMLSession()
        try:
            response = await asession.get(url, verify=False, timeout=10)
            if response.status_code == 200:
                await response.html.arender(sleep = 5, timeout=10)
                if len(response.html.absolute_links) > 0:
                    return response.html.absolute_links
                return 0
        except (KeyboardInterrupt,websockets.exceptions.ConnectionClosedError, pyppeteer.errors.PageError,urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError, asyncio.exceptions.IncompleteReadError, lxml.etree.ParserError, asyncio.exceptions.InvalidStateError, requests.exceptions.ReadTimeout, pyppeteer.errors.TimeoutError, pyppeteer.errors.TimeoutError):
            pass