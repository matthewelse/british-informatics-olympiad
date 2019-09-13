import math

amount = 10000
total_repaid = 0

interest, repay = (int(x) for x in input().split(' '))

while amount > 0:
    interest_month = math.ceil((interest / 100) * amount)
    amount += interest_month
    repaid = math.ceil((repay / 100) * amount)
    repaid = min(max(5000, repaid), amount)
    total_repaid += repaid
    amount -= repaid

print("%.2f" % (total_repaid / 100))
