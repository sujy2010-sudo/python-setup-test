print("\n" + "="*70)
print("PROGRAM 9: EMPLOYEE DATABASE (Combining All Skills) - EXTENDED")
print("="*70)

class EmployeeDatabase:
    def __init__(self):
        self.employees = {}       # {id: {"name":..., "department":..., "salary":...}}
        self.by_department = {}   # {department: [ids]}
        self.by_name = {}         # {name: id}

    def add_employee(self, employee_id, name, department, salary):
        self.employees[employee_id] = {
            "name": name,
            "department": department,
            "salary": salary
        }
        if department not in self.by_department:
            self.by_department[department] = []
        self.by_department[department].append(employee_id)
        self.by_name[name] = employee_id
        print(f"Added employee: {name} (ID: {employee_id})")

    def get_employee(self, employee_id):
        return self.employees.get(employee_id)

    def find_by_name(self, name):
        employee_id = self.by_name.get(name)
        if employee_id:
            emp = self.employees[employee_id].copy()
            emp["id"] = employee_id
            return emp
        return None

    def get_department_employees(self, department):
        """Get all employees in a department"""
        emp_ids = self.by_department.get(department, [])
        return [dict(id=emp_id, **self.employees[emp_id]) for emp_id in emp_ids]

    def get_salary_stats(self):
        """Calculate salary statistics"""
        salaries = [emp["salary"] for emp in self.employees.values()]
        return {
            "min": min(salaries) if salaries else 0,
            "max": max(salaries) if salaries else 0,
            "average": sum(salaries) / len(salaries) if salaries else 0,
            "total": sum(salaries)
        }

    def give_raises(self, department, percentage):
        """Give raises to all employees in a department"""
        emp_ids = self.by_department.get(department, [])
        for emp_id in emp_ids:
            old_salary = self.employees[emp_id]["salary"]
            new_salary = old_salary * (1 + percentage / 100)
            self.employees[emp_id]["salary"] = new_salary
            print(f"{self.employees[emp_id]['name']}: "
                  f"${old_salary:,.0f} -> ${new_salary:,.0f}")

    # ---------------- New methods requested ----------------

    def remove_employee(self, employee_id):
        """Remove employee from employees, by_department and by_name indexes."""
        emp = self.employees.pop(employee_id, None)
        if not emp:
            print(f"No employee with ID {employee_id} found.")
            return False

        # remove from department list
        dept = emp["department"]
        if dept in self.by_department:
            try:
                self.by_department[dept].remove(employee_id)
                if not self.by_department[dept]:
                    del self.by_department[dept]  # cleanup empty department
            except ValueError:
                pass

        # remove from name map
        name = emp["name"]
        self.by_name.pop(name, None)

        print(f"Removed employee: {name} (ID: {employee_id})")
        return True

    def transfer_employee(self, employee_id, new_department):
        """Move employee to a different department, updating indexes."""
        emp = self.employees.get(employee_id)
        if not emp:
            print(f"No employee with ID {employee_id} found.")
            return False

        old_department = emp["department"]
        if old_department == new_department:
            print(f"{emp['name']} is already in {new_department}.")
            return True

        # remove from old department list
        if old_department in self.by_department:
            try:
                self.by_department[old_department].remove(employee_id)
                if not self.by_department[old_department]:
                    del self.by_department[old_department]
            except ValueError:
                pass

        # add to new department list
        if new_department not in self.by_department:
            self.by_department[new_department] = []
        self.by_department[new_department].append(employee_id)

        # update employee record
        emp["department"] = new_department
        print(f"Transferred {emp['name']} (ID: {employee_id}) "
              f"{old_department} -> {new_department}")
        return True

    def get_high_earners(self, threshold):
        """Return list of employees with salary > threshold."""
        return [
            dict(id=eid, **edata)
            for eid, edata in self.employees.items()
            if edata["salary"] > threshold
        ]

    def get_department_stats(self, department):
        """Return count, average salary, total salary for a department."""
        emp_ids = self.by_department.get(department, [])
        salaries = [self.employees[eid]["salary"] for eid in emp_ids]
        total = sum(salaries)
        count = len(salaries)
        avg = total / count if count else 0
        return {"department": department, "count": count, "average": avg, "total": total}

    def search_employees(self, query):
        """Case-insensitive partial match search on employee names."""
        q = query.lower()
        results = []
        for eid, edata in self.employees.items():
            if q in edata["name"].lower():
                results.append(dict(id=eid, **edata))
        return results

# ---------------- Example usage ----------------
if __name__ == "__main__":
    db = EmployeeDatabase()
    db.add_employee(1001, "Alice Johnson", "Engineering", 75000)
    db.add_employee(1002, "Bob Smith", "Sales", 60000)
    db.add_employee(1003, "Charlie Davis", "Engineering", 80000)
    db.add_employee(1004, "Diana Prince", "HR", 65000)

    print("\n-- Transfer Charlie to Sales --")
    db.transfer_employee(1003, "Sales")

    print("\n-- Remove Bob --")
    db.remove_employee(1002)

    print("\n-- High earners (threshold 70,000) --")
    for emp in db.get_high_earners(70000):
        print(emp)

    print("\n-- Department stats: Sales --")
    print(db.get_department_stats("Sales"))

    print("\n-- Search for 'ali' --")
    print(db.search_employees("ali"))
