coins = 0

while True:
    print("Hi! How much change is owed?")
    money_amount = float(input("> ")) * 100
    if money_amount >= 0:
        break

for i in [25, 10, 5, 1]:
    while money_amount / i >= 1.0:
        coins += 1
        money_amount -= i
        
print(coins)



