import math

PI = 3.14159
# 1. The volume of a sphere with radius r is (4/3)πr3What is the volume of a sphere with radius 5?
def volumeOfSphere(radius):
    return ((4/3)*PI)*(pow(radius, 3))
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
# the total wholesale cost for 60 copies?


def totalWholeSale(copies):
    coverPrice = 24.95
    DISCOUNT = 0.4
    shippingFee = 3.0
    additionalCopy = 0.75
    return (copies*coverPrice*DISCOUNT) + ((copies-1)*additionalCopy) + shippingFee
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
# 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I
# get home for breakfast?


def timeHomeForBreakfast(timesHours, timesMinutes):
    convertHoursToMinutes = (timesHours * 60) + timesMinutes
    EASY_PACE = 495 * 1
    TEMPO = 432 * 1
    timeAnswer = convertHoursToMinutes + (2*EASY_PACE) + TEMPO
    timeAnswerinHours = timeAnswer / 60
    timeAnswerinHoursClock = math.trunc(timeAnswerinHours) % 24
    timeAnswerinMinutes = round((timeAnswerinHours - math.trunc(timeAnswerinHours)) * 60)

    return timeAnswerinHoursClock, timeAnswerinMinutes


print("The answer is {} cube units.".format(round(volumeOfSphere(5), 2)))
print("The answer is ${} ".format(round(totalWholeSale(60)), 2))
print("The answer is: {}:{} in military time".format(timeHomeForBreakfast(6, 52)[0], timeHomeForBreakfast(6, 52)[1]))

