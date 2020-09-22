#coding=utf-8

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from tornado.options import define, options

define("port", default=8001, help="run on the given port ", type=int)

__APP_NAME__ = 'super_demo'
remote_project_dir = '/test/super_demo'

## TODO logging 无效，有效日志文件在sp_log_dir中 
def init_log(name):    
    logger = logging.getLogger(name)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("{}/{}.log".format(remote_project_dir, name))
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")    
    
if __name__=="__main__":
    # 启动tornado实例
    init_log(__APP_NAME__)
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()