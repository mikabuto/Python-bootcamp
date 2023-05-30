gold_ingots = 'gold_ingots'

def split_booty(*purses: dict[str, int]):
    sum_ingots = 0
    for purse in purses:
        sum_ingots += purse.get(gold_ingots, 0)
    return tuple({gold_ingots: (sum_ingots + i) // 3} for i in range(3))

print('==================================\n booty: {"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}')
print(split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}))

print('\n==================================\n booty: {"gold_ingots":1}, {"gold_ingots":0}')
print(split_booty({"gold_ingots":1}, {"gold_ingots":0}))

print('\n==================================\n booty: {"gold_ingots":6}, {"gold_ingots":6}')
print(split_booty({"gold_ingots":6}, {"gold_ingots":6}))

print('\n==================================\n booty: {"gold_ingots":5}, {"gold_ingots":5}')
print(split_booty({"gold_ingots":5}, {"gold_ingots":5}))