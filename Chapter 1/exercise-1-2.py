# Exercise 1-2.
# Start the Python interpreter and use it as a calculator.
# 1. How many seconds are there in 42 minutes 42 seconds?
def convertMinutesToSeconds(minutes, seconds):
    return (minutes * 60) + seconds
# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
# mile.


def convertKMtoMiles(kilometers):
    return kilometers / 1.609
# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
# pace (time per mile in minutes and seconds)? What is your average speed in
# miles per hour?


print("It is {} seconds".format(convertMinutesToSeconds(42, 42)))
print("It is {} miles".format(round(convertKMtoMiles(1.61), 3)))
