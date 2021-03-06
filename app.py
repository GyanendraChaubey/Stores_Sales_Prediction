from flask import Flask
import sys
from storesales.logger import logging
from storesales.exception import StoresalesException


app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
       raise Exception("We are testing custom exception")
    except Exception as e:
        storesales = StoresalesException(e,sys)
        logging.info(storesales.error_message)
        logging.info("We are testing logging")
    return "CI CD Pipeline has been established"

if __name__=="__main__":
    app.run(debug=True)