class Budget:

    def __init__(self, category):
        self.category = category
        self.file = []

    def get_balance(self):
        total = 0
        for item in self.file:
            total += item[0]
        return total

    def deposit(self, amt_to_deposit, desc):
        self.file.append([amt_to_deposit, desc])

    def withdrawal(self, amt_to_withdraw):

        balance = self.get_balance()
        if amt_to_withdraw > balance:
            print(f'{self.category} budget is low')
            
        elif amt_to_withdraw <= balance:
            balance -= amt_to_withdraw
            print(f'Withdrawal successful, balance remaining {balance}')
            self.file.append([int(-(amt_to_withdraw))])
            return balance


    def transfer(self, category, tran_category, amt):
        transfer_amt = self.get_balance()
        self.category = category

        if tran_category != self.category:
            transfer_amt -= amt
            self.file.append(transfer_amt)
            return transfer_amt


#use these to test the file     

# bud_1 = Budget('food')
# bud_2 = Budget('clothing')

# bud_1.deposit(5000, 'to buy meat')
# bud_2.deposit(3200, 'to new clothing')

# print(bud_1.withdrawal(1500))
# print(bud_2.withdrawal(2200))

# print('*'*10)

# print(bud_1.get_balance())
# print(bud_2.get_balance())

# print('*'*10)

# print(bud_1.transfer('food', 'clothing', 400))
# print(bud_2.transfer('clothing', 'food', 800))