class Account:

    def __init__(self, acc_no, acc_pass):     
        self.acc_no=acc_no   
        self.__acc_pass=acc_pass       #add __ to make the attribute or method private
        
    def reset_pass(self):       #internal functions can access private attributes and methods
        print(self.__acc_pass)

acc1= Account("nikki","dora")  
print(acc1.acc_no)
print(acc1.reset_pass())