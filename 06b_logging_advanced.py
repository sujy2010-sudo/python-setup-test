import logging
from pathlib import Path

Path("logs").mkdir(exist_ok =True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
    
)

logger =logging.getLogger(__name__)

logger.debug("This is debug message")
logger.info("this is info message")
logger.warning("this is warning message")
logger.critical("this is critical message")
logger.error("this is error message")

auth_logger =logging.getLogger("auth")
db_logger=logging.getLogger("database")

auth_logger.info("user logging successfull")
db_logger.warning("database connection slow")

def buggy_function():
    try:
        result=10/0
    except Exception as e:
        logger.error("An error occured",exc_info=True)
        
        
buggy_function()        
    
    

