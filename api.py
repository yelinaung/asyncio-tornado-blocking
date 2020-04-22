import logging
import time
import asyncio

import tornado.ioloop
import tornado.web

from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.log import enable_pretty_logging


class BlockHandler(tornado.web.RequestHandler):

    async def get(self):
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.long_running_task)
        logging.info("Request received for the BlockHandler")
        self.write("request accepted")

    def long_running_task(self):
        for i in range(5):
            logging.info(f"building trie {i}")
            time.sleep(1)
        logging.info("done.")


class MainHandler(tornado.web.RequestHandler):

    async def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/block", BlockHandler),
    ])


def main():
    enable_pretty_logging()
    AsyncIOMainLoop().install()
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(1234, '127.0.0.1')
    server.start()
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
