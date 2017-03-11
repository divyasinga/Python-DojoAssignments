import random

def cointoss():
    hcounter = 0
    tcounter = 0
    print "Starting the program..."
    for x in range(5001):
        random_num = round(random.random())
        print "Attempt #", str(x), "Throwing a coin... It's",
        if random_num == 0:
            hcounter += 1
            print "heads! Got", str(hcounter), "head(s) and", str(tcounter), "tails so far."
        else:
            tcounter += 1
            print "tails! Got", str(tcounter), "head(s) and", str(hcounter), "tails so far."
        x+=1
    print "Ending the program. Thank you!"
        
cointoss()
