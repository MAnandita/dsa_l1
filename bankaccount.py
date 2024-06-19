class bankaccount:
    def __init__(self, holder, accnumber):
        self.holder = holder
        self.accnumber = accnumber

    __balance = 10000

    def add_balance(self, amount):
        if amount <= 0:
            print("INVALID AMOUNT")
        else:
            self.__balance += amount
            print(self.__balance)
    
    def subtract_balance(self, amount):
        if amount > self.__balance:
            print("INVALID AMOUNT")
        else:
            self.__balance -= amount
            print(self.__balance)

elle = bankaccount("Elle Woods",1123581321)
elle.add_balance(600)
elle.subtract_balance(11000)

