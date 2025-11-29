import logging
from pathlib import Path

# Create logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Advanced configuration with file output
logging.basicConfig(
    level=logging.DEBUG,  # Show all levels
    format='%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("logs/app.log"),    # Save to file
        logging.StreamHandler()                 # Also print to console
    ]
)

# Create logger
logger = logging.getLogger(__name__)

# Now all logs go to both console AND file!
logger.debug("This is a debug message")
logger.info("Application started")
logger.warning("This will be saved to logs/app.log")
logger.error("Error messages are logged")
logger.critical("Critical issues tracked")

def calculate_employee_bonus(name, salary, performance_score):
    logger.info("Calculating bonus for {name}")
    if performance_score >= 8:
        bonus = salary * 0.15
        logger.info(f"Excellent performance! Bonus: ${bonus}")
    elif performance_score >= 6:
        bonus = salary * 0.10
        logger.info(f"Good performance! Bonus: ${bonus}")
    else:
        bonus = salary * 0.05
        print(f"Standard bonus: ${bonus}")
        logger.info(f"Standard bonus: ${bonus}")

    print(f"Total bonus for {name}: ${bonus}")
    logger.info(f"Total bonus for {name}: ${bonus}")
    return bonus

calculate_employee_bonus("Alice", 70000, 9)
calculate_employee_bonus("Bob", 60000, 5)