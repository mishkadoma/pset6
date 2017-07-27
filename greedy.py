coins = 0
money_amount = -1

def set_money():
    print("Hi! How much change is owed?")
    global money_amount
    money_amount = float(input("> ")) * 100

    
while money_amount < 0:
    set_money()

for i in [25, 10, 5, 1]:
    while money_amount / i >= 1.0:
        coins += 1
        money_amount -= i
        
print(coins)



