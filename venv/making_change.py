def changePossibilitiesBottomUp(amount, denominations):
    wayOfDoingNCents = [0] * (amount + 1)
    wayOfDoingNCents[0] = 1

    for coin in denominations:

        for higherAmount in range(coin, amount + 1):
            higherAmountRemainder = higherAmount - coin
            waysOfDoingNCents[higherAmount] += (waysOfDoingNCents[higherAmountRemainder])

    return waysOfDoingNCents[amount]
