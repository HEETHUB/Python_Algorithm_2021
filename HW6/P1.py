class Company:
    def __init__(self, name, employees, year, stock_price,revenue):
        # write your code below
        self.name = name
        self.employees = employees
        self.year = year
        self.stock_price = stock_price
        self.revenue = revenue
    
    def is_older(self, other):
        # write your code below
        if int(self.year) < int(other.year):
            return True
        else:
            return False
    
    def revenue_per_employee(self):
        #write your code below
        return self.revenue / self.employees