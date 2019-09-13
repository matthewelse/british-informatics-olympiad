import math

best = 0
best_interest = 0
best_repay = 0

for interest in range(100):
    for repay in range(100):

        amount = 10000
        total_repaid = 0

        while amount > 0:
            interest_month = math.ceil((interest / 100) * amount)
            amount += interest_month
            repaid = math.ceil((repay / 100) * amount)
            repaid = min(max(5000, repaid), amount)
            total_repaid += repaid
            amount -= repaid

            if amount >= 10000:
                break

        if amount == 0:
            if total_repaid > best:
                best = total_repaid
                best_interest = interest
                best_repay = repay

print("interest: %d%%" % best_interest)
print("repay: %d%%" % best_repay)
