#using python Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# get car speed from user input
speed=int(input(' enter the car speed in km/h:'))
speed_limit=70
if speed<= speed_limit:
    print(" speed is ok")
elif  speed >=  speed_limit:
    print("give 1 demerit point")
elif  speed>=12:
    print("licence suspend")