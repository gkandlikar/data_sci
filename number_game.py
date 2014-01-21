x = 0
max_tries=10
count = 0
while True:
    x_new = int(raw_input("Enter a new number: "))
    if x_new > x:
        print " => it's bigger than the last!"
    elif x_new < x:
        print " => it's smaller than the last!"
    else:
        print " => no changes! I'll exit now"
        break
    x = x_new
    
    count += 1
    if count > max_tries:
        print "too many tries..."
        break