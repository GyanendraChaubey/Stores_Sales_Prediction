from storesales.pipeline.pipeline import Pipeline
from storesales.exception import StoresalesException
from storesales.logger import logging
from storesales.config.configuration import Configuration
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuartion().get_data_validation_config()
        # print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()