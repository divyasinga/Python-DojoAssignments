import random
import math

def scores():
    print "Scores and Grades"
    for x in range(10):
        random_num = math.floor(random.random()*100)
        print "Score:", str(random_num) + "; Your grade is",
        if random_num > 89:
            print "A"
        elif random_num > 79:
            print "B"
        elif random_num > 69:
            print "C"
        elif random_num > 59:
            print "D"
        else:
            print "F"
        x = x + 1
    print "End of the program. Bye!"
        
scores()
