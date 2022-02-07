import time


print('Welcome to cal program')
# print(""" \nEnter m for mean\nmo for mode\nmed for median\nsd for standard deviation, and \nv for variance""")

# choice = input(">").lower()

# if choice == "m":
#     print("Enter a list of numbers")
#     user_num = int(input("").split())
#     user_num_plus = sum(user_num)
#     print(user_num)
    # user_num2 = len(user_num)
    # mean_num = user_num.sum()/user_num2 
    # print(f"{mean_num}")

user_input = input("Enter you number seperated by comma:\n")
num = [int(i) for i in user_input.split(",")]

#Calculate the mean 
# mean = sum(num)/len(num)

# calculating the median 
# num.sort()

# midpoint = len(num)//2
# print(midpoint)
# if len(num)%1 == 0:
#     median = (num[midpoint] + num[midpoint-1])/2
# else:
#     median = num[midpoint]

# # calaculating the mode
# freq = {}
# for i in num:
#     freq[i] = freq.get(i,0) + 1

# print(freq)
# mode = max(freq, key=lambda x:freq[x])
# print(mode)

# # calaculating the standard
# standard_deviation = (sum([(x-mean)**2 for x in num])/len(num))**0.5

# #delay
# print("Calculating...\n")
# time.sleep(3)
# print("View results below:\n")

# #variance
# variance = standard_deviation**2


# print(f"The mean is {round(mean,2)}")
# print(f"The median is {median}")
# print(f"The mode is {mode}")
# print(f"The standard_deviation is {round(standard_deviation,2)}")
# print(f"The variance is {round(variance,2)}")

#USEFUL----------------------ZIP
# print(dict(zip([1,2,3,4,5], [1,4,9,16,25])))

# user_input = input("Enter you number seperated by comma:\n")
num = [int(i) for i in user_input.split(",")] #USING LIST COMMPREHENSION

#Altrnatively, we can use mapping to map a function to the list 
num = list(map(int, user_input.split(",")))
#num = list(map(lambda x : int(x), user_input.split(","))) #--->>YOU CAN USE THE TOP ALSO
print(num)
print(user_input.split(","))

# CLASSWORK TWO ------
# prin = int(input("Enter principle\n"))
# rate = int(input("Enter rate\n"))
# time = int(input("Enter time\n"))

# interest = prin*rate*time
# simple_in = interest/100
# total_sum = prin + interest
# print(simple_in)
# print(total_sum)