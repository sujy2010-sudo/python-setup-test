import logging 
from pathlib import Path 

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
  )

def process_order_good(order_id):
    logging.info(f"Processing order{order_id}")
    logging.info(f"Order{order_id} completed")
    
process_order_good(12345)

logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error")
logging.critical("this is critical")

def divide_numbers(a,b):
    logging.info(f"dividing {a} by {b}")
    try:
        result=a/b
        logging.info(f"Result:{result}")
        return result
    except  ZeroDivisionError:
        logging.error(f"Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        logging.error(f"invalid types:{e}")
        return None
            
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "abc")
user_id=1122334
action="login"
logging.info(f"user {user_id} performed action:{action}")
logging.info("user %s logged in at %s","alice","09:15:23")
    
    
    
    
