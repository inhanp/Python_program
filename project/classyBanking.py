"""
Functions about classyBanking

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: INHAN PARK
"""

class Account:
    def __init__(self, sOwner, iID, fBalance):
        self.__owner = sOwner
        self.__id = iID
        self.__balance = fBalance
        
    def getOwner(self):
        return self.__owner
    
    def getID(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def setOwner(self, sOwner):
        self.__owner = sOwner
        
    def setID(self, iID):
        self.__id = iID
        
    def setBalance(self, fBalance):
        self.__balance = fBalance
                
    def deposit(self, amount):
        self.setBalance(self.getBalance() + amount)
    
    def withdraw(self, amount):
        self.setBalance(round(self.getBalance() - amount, 3))
        if self.getBalance() < 0:
            print('warning : Balance falls below 0')
            self.setBalance(round(self.getBalance() - 5, 3))
            
            
    def printAccountInfo(self):
        print('Owner of account is %s' %self.getOwner())
        print('ID of account is %6d' %self.getID())
        print('Balance of account is %.3f' %self.getBalance())

                
    
class CheckingAccount(Account):
    def __init__(self, sOwner, iID, fBalance, iTF):
        super().__init__(sOwner, iID, fBalance)
        self.__transactionCount = 0
        self.__transactionFee = iTF
        
    def getTransactionCount(self):
        return self.__transactionCount
    
    def getTransactionFee(self):
        return self.__transactionFee
    
    def setTransactionCount(self, iTC):
        self.__transactionCount = iTC
        
    def setTransactionFee(self, iTF):
        self.__transactionFee = iTF
    
    def deposit(self, amount):
        super().deposit(amount)
        self.setTransactionCount(self.getTransactionCount() + 1)
        self.deductFees()
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.setTransactionCount(self.getTransactionCount() + 1)
        self.deductFees()
    
    def deductFees(self):
        if self.getTransactionCount() == 5:
            self.withdraw(self.getTransactionFee())
            self.setTransactionCount(0)
    
    
    
class SavingsAccount(Account):
    
    def __init__(self, sOwner, iID, fBalance, fIR):
        super().__init__(sOwner, iID, fBalance)
        self.__interestRate = fIR

    def getInterestRate(self):
        return self.__interestRate
    
    def setInterestRate(self, fIR):
        self.__interestRate = fIR
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.setInterestRate(0)

    def applyInterest(self):
        super().deposit(self.getBalance()*self.getInterestRate())
            
            
def main():
    testAccount()
    testCheckingAccount()
    testSavingsAccount()



############################################################    
    
# Below are the tests for getOwner()
def testAccount():
    #Initialize Account
    park = Account('peter',123456,98.765)
    
    #Test get functions
    assert park.getOwner() == 'peter', 'owner of account is peter'
    assert park.getID() == 123456, 'ID is 123456'
    assert park.getBalance() == 98.765, 'balance of account is 98.765'
    
    #Test set functions
    park.setOwner('doctor')
    park.setID(545454)
    park.setBalance(12.567)
    assert park.getOwner() == 'doctor', 'owner of account is doctor'
    assert park.getID() == 545454, 'ID is 545454'
    assert park.getBalance() == 12.567, 'balance of account is 12.567'
    
    #Test deposit()
    park.deposit(11.111)
    assert park.getBalance() == 23.678, 'balance of account should be 23.678'
    
    #Test withdraw()
    park.withdraw(10.000)
    assert park.getBalance() == 13.678, 'balance of account should be 13.677'
    
    #Test withdraw() when balance becomes less than 0
    park.setBalance(30.000)
    park.withdraw(50.000)
    assert park.getBalance() == -25.000, 'extra penalty $5 is deducted also, so balance becomes -25.000'
    
    park.printAccountInfo()
    
def testCheckingAccount():
    #Initialize CheckingAccount
    park = CheckingAccount('peter', 123456, 98.765, 50)
    
    #Test get functions
    assert park.getTransactionCount() == 0, 'initial transaction count is 0'
    assert park.getTransactionFee() == 50, 'transaction fee is 50'
    
    #Test set functions
    park.setTransactionCount(2)
    assert park.getTransactionCount() == 2, 'current transaction count is 2'
    park.setTransactionFee(70)
    assert park.getTransactionFee() == 70, 'current transaction fee is 50'
    
    #Test deposit()
    park.deposit(100.000)
    assert park.getBalance() == 198.765, 'current balance of account should be 198.765'
    assert park.getTransactionCount() == 3, 'current transaction count is 3'
    
    #Test withdraw()
    park.withdraw(30.000)
    assert park.getTransactionCount() == 4, 'current transaction count is 4'
    assert park.getBalance() == 168.765, 'current balance of account should be 168.765'
    
    #Test withdraw() when balance becomes less than 0
    park.setTransactionCount(0)
    park.setBalance(30.000)
    park.withdraw(50.000)
    assert park.getTransactionCount() == 1, 'Since balance is withdrawn, transaction count added'
    
    #Test deductFees()
    park.setBalance(168.765)
    park.setTransactionCount(5)
    park.deductFees()
    #current transaction fee is 70, so 70 is deducted
    assert park.getBalance() == 98.765, 'current balance of account should be 98.765'
    assert park.getTransactionCount() == 0, 'transaction count becomes 0 after deduct fee'
    

# Below are the tests for setOwner()
def testSavingsAccount():
    #Initialize SavingAccount
    park = SavingsAccount('peter', 123456, 98.765, 0.5)
    
    #Test get function
    assert park.getInterestRate() == 0.5, 'initial interest rate is 10'
    
    #Test set function
    park.setInterestRate(0.07)
    assert park.getInterestRate() == 0.07, 'current interest rate is 5'
    
    #Test withdraw()
    park.setBalance(500.000)
    park.withdraw(200.000)
    assert park.getBalance() == 300.000
    
    #Test withdraw() when balance becomes less than 0
    park.setBalance(500.000)
    park.withdraw(600.000)
    assert park.getInterestRate() == 0, 'since balance falls below 0, interest rate becomes 0'
    
    #Test applyInterest()
    park.setBalance(1000)
    park.setInterestRate(0.07)
    park.applyInterest()
    assert park.getBalance() == 1070.000, 'With interest rate 10, 10% of current balance is added'

############################################################    
    
if __name__ == "__main__":    
    main()