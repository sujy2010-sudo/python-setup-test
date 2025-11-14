import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
     handlers=[
        logging.FileHandler("logs/app.log"),    # Save to file
        logging.StreamHandler()                 # Also print to console
    ]   
)


employees = [
    {
        "id": 101,
        "name": "Alice Johnson",
        "department": "Engineering",
        "salary": 75000,
        "performance_score": 8.5,
        "years_of_service": 3
    },
    {
        "id": 102,
        "name": "Bob Smith",
        "department": "Sales",
        "salary": 60000,
        "performance_score": 7.2,
        "years_of_service": 2
    },
    {
        "id": 103,
        "name": "Charlie Davis",
        "department": "Engineering",
        "salary": 85000,
        "performance_score": 9.1,
        "years_of_service": 5
    },
    {
        "id": 104,
        "name": "Diana Prince",
        "department": "HR",
        "salary": 65000,
        "performance_score": 8.0,
        "years_of_service": 4
    },
    {
        "id": 105,
        "name": "Eve Wilson",
        "department": "Engineering",
        "salary": 80000,
        "performance_score": 8.8,
        "years_of_service": 3
    },
    {
        "id": 106,
        "name": "Frank Miller",
        "department": "Sales",
        "salary": 55000,
        "performance_score": 6.5,
        "years_of_service": 1
    },
    {
        "id": 107,
        "name": "Grace Lee",
        "department": "Marketing",
        "salary": 62000,
        "performance_score": 7.8,
        "years_of_service": 2
    },
    {
        "id": 108,
        "name": "Henry Brown",
        "department": "Engineering",
        "salary": 90000,
        "performance_score": 9.5,
        "years_of_service": 6
    }
]


logger = logging.getLogger(__name__)
#logger.debug("This is a debug message")
#logger.info("Application started")
#logger.warning("This will be saved to logs/app.log")
#logger.error("Error messages are logged")
#logger.critical("Critical issues tracked")

auth_logger = logging.getLogger("auth")
db_logger = logging.getLogger("database")

#auth_logger.info("User authentication successful")
#db_logger.warning("Database connection slow")

#calculate_total_employees()
 


def calculate_total_employees():
    try:
        print(f"\nTotal employees: {len(employees)} ")
    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace

calculate_total_employees()


def get_department_breakdown():
    try:
        print(f"\ndepartment breakdown")
        #from collections import defaultdict
        #dept_to_names = defaultdict(list)
        #for emp in employees:
            #dept_to_names[emp["department"]].append(emp["name"])
       #     print(f"\nDepartment to Names: {dict(dept_to_names)}")
       #     print(f"\n{emp["department"]}: employees ")
        
        eng_employees = [emp for emp in employees if emp["department"] == "Engineering"] # output is a list
        print(f"\nEngineering team: {len(eng_employees)} employees")
        Sales_employees = [emp for emp in employees if emp["department"] == "Sales"] # output is a list
        print(f"\nSales team: {len(Sales_employees)} employees")
        HR_employees = [emp for emp in employees if emp["department"] == "HR"] # output is a list
        print(f"\nHR team: {len(HR_employees)} employees")
        Marketing_employees = [emp for emp in employees if emp["department"] == "Marketing"] # output is a list
        print(f"\nMarketing team: {len(Marketing_employees)} employees")
    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace
        
get_department_breakdown()

def calculate_average_salary():
    try:
        
        eng_employees = [emp for emp in employees ] # output is a list
              
        total_sal = sum(emp["salary"] for emp in eng_employees)
        print(f"Average Salary: ${total_sal/len(eng_employees):,.2f}")

    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace

calculate_average_salary()
def find_top_performers():
    try:
        
        eng_employees = [emp for emp in employees ] # output is a list
        high_ids = [id for id in eng_employees if id["performance_score"]  > 8.0]
        print(f"\nTop Performers (score ≥ 8.0): {len(high_ids)} employees")    
        for emp in high_ids:
            print(f"\n{emp['name']}: {emp['performance_score']} - {emp['department']}")
        
        

    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace
find_top_performers()
def find_high_earners():
    try:
        
        eng_employees = [emp for emp in employees ] # output is a list
        total_sal = sum(emp["salary"] for emp in eng_employees)
        avg_sal=total_sal/len(eng_employees)
        print(f"\n{avg_sal}")
        rounded_value = (avg_sal // 10000) * 10000
        print(int(rounded_value))
      
        high_ids = [id for id in eng_employees if id["salary"]  > 70000]
        print(f"\nHigh Earners (salary > $70,000):: {len(high_ids)} employees")    
        for emp in high_ids:
            print(f"\n{emp['name']}: ${emp['salary']:,}")
        
        

    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace
find_high_earners()
from collections import defaultdict
def get_department_salary_stats():
    
    try:
       dept_data = defaultdict(list)
       for emp in employees:
            dept_data[emp["department"]].append(emp["salary"])
            for dept, salaries in dept_data.items():
                total = sum(salaries)
                count = len(salaries)
                average = total / count

                print(f"\nDepartment: {dept}")
                print(f"  Total Salary: {total}")
                print(f"  Average Salary: {average}")
                print(f"  Employee Count: {count}")
    except Exception as e:
        logger.error("An error occurred", exc_info=True)  # Includes stack trace
get_department_salary_stats()








