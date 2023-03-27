# ---------------------------------------------------------------
# Name: Yehyun Lee
# Purpose: Recursion
# Created: 06 03, 2021
# ---------------------------------------------------------------



# Question 1 - Yehyun
# ---------------------------------------------------------------
# start = 1
# answer = 0
# x = 1
# y = 2
# for i in range(1, 100):
#     answer = answer + x/y
#     x += 1
#     y += 1
# print(answer)

# total = 0
# for i in range(1, 100):
#     total = total + i/(i+1)
# print(total)

# Question 3 - Yehyun
# ---------------------------------------------------------------
def countdown(n):
    if n<=0:
        print("Happy New years!")
    else:
        print(n)
        time.sleep(.2)
        countdown(n-1)
countdown(20)