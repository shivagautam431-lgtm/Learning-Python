# Smart Bill Calculator
price1 = float(input("Write the price of the first item: "))
price2 = float(input("Write the price of the second item: "))

total = price1 + price2

print("Your Total bill is: " + str(total))

# Decision Making Process
if total > 500:
    print("Congratulations! The bill is more than 500, you will get a 10%  discount.")
else:
    print("Your bill is less than 500, no discount recevied.")
