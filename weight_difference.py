#takes weight and tells you how much you'd weight if the earth 
#didn't spin

weight_input = raw_input("how much do you weight? ")
weight = float(weight_input)
radius_earth = 6371*1000 
speed = 460
grav = 9.81

force_out = weight*speed*speed/radius_earth
mass_out = force_out/grav
diff = weight +  mass_out
print "you would weigh" , diff
