from datetime import datetime
from time import sleep
import random
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

# count = 1
# while count < 10:
#     count = count + 1
#     print("inside loop...")
#     sleep(1)

# i = 0
# for i in range(0,9):
#     i = i + 1
#     print("inside the for loop....")
#     sleep(1)
for i in range(5):
    right_this_time = datetime.today().minute
    if right_this_time in odds:
        print("This minute seems a littile odd")
    else:
        print("Not an odd minute")
    rand_int = random.randint(1,60)
    print("sleeping for", rand_int, " sec")
    sleep(random.randint(1,60))
