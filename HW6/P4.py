class Calculator:
    def __init__(self):
        self.value = 0
        self.newvalue = 0
        self.operation = None
        
    def digit(self, num):
        if self.operation:
            self.newvalue = int(str(self.newvalue) + str(num))
        else:
            self.value = int(str(self.value) + str(num))
            
    def plus(self):
        self.equal()
        self.operation = 'plus'
    
    def minus(self):
        self.equal()
        self.operation = 'minus'
        
    def clear(self):
        self.value = 0
        self.newvalue = 0
        self.operation = None
        
    def equal(self):
        if self.operation == 'plus':
            result = self.value + self.newvalue
            self.value = result
            self.newvalue = 0
            return result
        else:
            result = self.value - self.newvalue
            self.value = result
            self.newvalue = 0
            return result