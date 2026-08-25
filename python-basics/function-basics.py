
def calculate_final_bill(amount):
    if amount >= 10000:
        discount_rate = 0.50
    elif amount >= 3000:
        discount_rate = 0.20
    elif amount >= 1000:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    #Calculate discount amount
    discount_amount = amount * discount_rate

    #Calcuate and return final checkout amount

    final_amount = amount - discount_amount
    return final_amount

# Calling function


bills = [200, 1020, 2000, 5000, 25000, 35000, 20, 10000, 3500, 4500,1020, 2000, 5000, 25000, 35000, 20, 10000, 3500, 4]

for i in range(len(bills)):
    final_bill = calculate_final_bill(bills[i])
    print (f" Checkout Amount of bill No. {i+1} is {final_bill} ")


for bill in bills:
    print (bill)
