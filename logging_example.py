import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(filename)s | %(message)s',
    #datefmt='%Y%M%D H%M%S'
    datefmt='%Y-%m-%d %H:%M:%S',
     handlers=[
        logging.FileHandler("logs/app.log"),    # Save to file
        logging.StreamHandler()                 # Also print to console
    ]   
)
logger = logging.getLogger(__name__)
auth_logger = logging.getLogger("auth")
db_logger = logging.getLogger("database")


def calculate_employee_bonus(name, salary, performance_score):
    print(f"Calculating bonus for {name}")

    if performance_score >= 8:
        bonus = salary * 0.15
        #print(f"Excellent performance! Bonus: ${bonus}")
        logging.info(f"Excellent performance! Bonus: ${bonus}")
    elif performance_score >= 6:
        bonus = salary * 0.10
        #print(f"Good performance! Bonus: ${bonus}")
        logging.info(f"Good performance! Bonus: ${bonus}")
    else:
        bonus = salary * 0.05
        #print(f"Standard bonus: ${bonus}")
        logging.info(f"Standard bonus: ${bonus}")

   # print(f"Total bonus for {name}: ${bonus}")
    logging.info(f"Total bonus for {name}: ${bonus}")
    return bonus

# Use logging.info, logging.warning, etc.
# Your improved version here:



# Test your function
calculate_employee_bonus("Alice", 70000, 9)
calculate_employee_bonus("Bob", 60000, 5)