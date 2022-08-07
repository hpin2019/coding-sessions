import logging
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from logging.handlers import RotatingFileHandler
from common import settings
from apiserver.userapi import UserAPI
#from apiserver.contactapi import ContactAPI
#from apiserver.ordersapi import OrdersAPI
from pathlib import Path
import argparse
import time
import sys
import traceback


logger = logging.getLogger()

def start_logger():
    logformatter =  logging.Formatter(settings.LOG_FORMAT)


    #print "Log format ",logformatter
    #print "Log level ",LOG_LEVEL
    filepath = Path(settings.LOG_FILE)
    filepath.parent.mkdir(exist_ok=True, parents=True)
    logger.setLevel(settings.DEFAULT_LEVELS[settings.FILE_LOG_LEVEL])
    fh = RotatingFileHandler(settings.LOG_FILE, maxBytes=(1048576*5), backupCount=7)
    fh.setFormatter(logformatter)
    logger.addHandler(fh)


    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logging.Formatter(settings.CONSOLE_LOG_FORMAT))
    consoleHandler.setLevel(settings.DEFAULT_LEVELS[settings.CONSOLE_LOG_LEVEL])
    logger.addHandler(consoleHandler)

    #logging.basicConfig(filename=self.log_file_path,format=logformatter,level=settings.DEFAULT_LEVELS[LOG_LEVEL])

    logger.info("FlaskServer started")



def start_app():
    try:
        start_logger()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        print("MyApp : unable to enable logger")

    try:
        app = Flask(__name__)
        CORS(app)
        api = Api(app)
        resource_class_kwargs = { "key": "value"}
        api.add_resource(UserAPI, '/user/profile/',resource_class_kwargs=resource_class_kwargs)
        '''
        api.add_resource(ContactAPI, '/contact/',resource_class_kwargs=resource_class_kwargs)
        api.add_resource(OrdersAPI, '/orders/',resource_class_kwargs=resource_class_kwargs)
        api.add_resource(FeedbackAPI, '/feedback/<string:action>',resource_class_kwargs=resource_class_kwargs)
        '''
        logger.info("Running FlaskServer")
        return app
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        logger.error("Unable to start FlaskServer")
        return None


if __name__ == '__main__':
    my_app = start_app()
    if my_app:
        logger.info("Running MyApp")
        my_app.run(use_reloader=True,host='0.0.0.0',port=int(settings.SERVER_PORT),debug=True)
    else:
        logger.error("Error starting MyApp")
    exit(1)
else:
    gunicorn_app = start_app()
