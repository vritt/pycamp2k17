#!/usr/bin/python3.4


# 1. Open Image  - https://goo.gl/UKWg3G
# 2. Listen To Song - https://youtu.be/x4AaYr1t3TA
# 3. Read news. - http://timesofindia.indiatimes.com/home/headlines

import time

print("Starting Break taker on ", time.ctime())

total_breaks = range(3)

info = "We will be taking total {total} breaks at ".format(total=len(total_breaks))

print(info, list(total_breaks))

for break_time in total_breaks:

    # Wait for specific time.
    time.sleep(10)

    # Decide which break to take
    if break_time == 0:
        # First break of a day.
        print("Time for break one.")

    elif break_time == 1:
        # Second break of a day.
        print("Time for break two.")

    elif break_time == 2:
        # Third break of a day.
        print("Time for break three.")

    else:
        print("Congratulations You had a healthy day.")


print("Break taker Finished on ", time.ctime())
