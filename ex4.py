cars=100 #not clear,it's better to add space between "=", like in line 3.
space_in_a_car=4.0
drivers = 30
passengers=90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars,"cars available."
print "There are only", drivers, "dirvers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We can", passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

