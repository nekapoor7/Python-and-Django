# Python3 program to find compound
# interest for given values.

def compund_interest(princle,rate,time):

    CI = princle*(pow((1 + rate/100),time))
    print(CI)

compund_interest(1200,5.4,2)
