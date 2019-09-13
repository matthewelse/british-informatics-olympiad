import math

amount = 10000
total_repaid = 0

interest, repay = 43, 46
count = 0

while amount > 0:
    interest_month = math.ceil((interest / 100) * amount)
    amount += interest_month
    repaid = math.ceil((repay / 100) * amount)
    repaid = min(max(5000, repaid), amount)
    total_repaid += repaid
    count += 1
    amount -= repaid

print("%d" % count)
