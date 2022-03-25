import random
import time

items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
random.shuffle(items)  # list is shuffled every new game
screen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pl1score = 0
pl2score = 0

while True:

    print(screen)
    print("player 1\n ")
    print("score=", pl1score)
    print("insert two numbers from 1 to 20:")  # first player chooses two numbers that he thinks they hold the same item
    i = int(input())
    j = int(input())
    while i < 1 or i > 20 or j < 1 or j > 20:
        print("insert two numbers from 1 to 20:")  # player must insert ony from 1 to 20
        i = int(input())
        j = int(input())
    i -= 1
    j -= 1
    a = screen[i]
    b = screen[j]
    screen[i] = items[i]
    screen[j] = items[j]
    print(screen)
    time.sleep(5)    # giving the player a moment to see what he have selected
    screen[i] = a
    screen[j] = b
    print("\n"*50)   # to clear the screen

    if items[i] == items[j]:
        screen[i] = "*"
        screen[j] = "*"
        pl1score += 1
    if screen == ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']:
        if pl2score > pl1score:
            print("player 2 wins")
        elif pl1score > pl2score:
            print("player 1 wins ")
        else:
            print("draw")
        break
    print(screen)
    print("player 2\n")
    print("score=", pl2score)
    print("insert two numbers from 1 to 20:")  # 2nd player chooses two numbers that he thinks they hold the same item
    k = int(input())
    m = int(input())
    while k < 1 or k > 20 or m < 1 or m > 20:  # player must insert ony from 1 to 20
        print("insert two numbers from 1 to 20:")
        k = int(input())
        m = int(input())
    k -= 1
    m -= 1
    z = screen[k]
    y = screen[m]
    screen[k] = items[k]
    screen[m] = items[m]
    print(screen)
    time.sleep(5)   # giving the player a moment to see what he have selected
    screen[k] = z
    screen[m] = y
    print("\n" * 50)   # to clear the screen
    if items[k] == items[m]:
        screen[k] = "*"
        screen[m] = "*"
        pl2score += 1
    if screen == ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']:
        if pl2score > pl1score:
            print("player 2 wins")
        elif pl1score > pl2score:
            print("player 1 wins ")
        else:
            print("draw")
        break
