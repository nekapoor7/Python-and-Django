def temparture(t):
    def celsius2farenhit(x):
        return 9 * x / 5 + 32

    result = " It is " + str(celsius2farenhit(t)) +" farenhit's "+ "tempature"
    return result

temp = int(input())
print(temparture(temp))
