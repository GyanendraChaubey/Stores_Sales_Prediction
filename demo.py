from storesales import pipeline
from storesales.pipeline.pipeline import Pipeline
from storesales.exception import StoresalesException
from storesales.logger import logging

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()
