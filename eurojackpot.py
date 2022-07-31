from random import randint

minRad = [38, 32, 40, 46, 49, 10, 4]

howManyWeeksItTakes = 0
match = False

while match == False:
    howManyWeeksItTakes = howManyWeeksItTakes + 1
    thisWeekDraw = [randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 12), randint(1, 12)]
    if thisWeekDraw == minRad:
        match = True
    else:
        print(f'\rSå här många veckor har gått: {howManyWeeksItTakes}', end='', flush=True)

print("DU HAR VUNNIT EUROJACKPOT, DET TOG BARA %s VECKOR!", howManyWeeksItTakes)
