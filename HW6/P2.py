from P1 import Company # Do Not Modify

class Industry(Company):
    def __init__(self, type, companies):
        self.type = type
        self.companies = companies

    def average_stock_price(self):
        total = 0 
        for company in self.companies:
            total += company.stock_price
        return total / len(self.companies)