plants = []
zombie = []
n = input()
while n != 'stop':

    plants.append(n)
    n = input()
k = input()
while k != 'stop':

    zombie.append(k)
    k = input()

def func(plants, zombie, counter = len(plants) - len(zombie)):
    for i in range(min(len(plants), len(zombie))):

        if int(plants[i]) - int(zombie[i]) > 0:
            counter += 1
        if int(plants[i]) - int(zombie[i]) < 0:
            counter -= 1

    if counter > 0:
        return True
    if counter == 0:
        if sum(plants) >= sum(zombie):
            return True
        else:
            return False
    if counter < 0:
        return False
print(func(plants,zombie))



