def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            # print(numCoins)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins
#%%
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
    knownResults[change] = minCoins
    return minCoins

def dpMakeChange(coinValueList, change):
    minCoins=[0]*(change+1)
    coinsUsed=[0]*(change+1)
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents -j]+1
                newCoin = j
            print (f'j={j}')                
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change], coinsUsed

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
#%%
if __name__ == '__main__':
    num = recMC([1,5,10,25],26)
    print (num)
    num2 = recDC([1,5,10,25],26,[0]*27)
    print (num2)

    cl = [1, 5, 10, 21, 25]
 
    [minCoins, coinsUsed] = dpMakeChange(cl, 63)
    printCoins(coinsUsed, 63)
# %%
