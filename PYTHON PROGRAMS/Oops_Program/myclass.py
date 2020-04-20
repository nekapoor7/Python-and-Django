class Myclass:

    number = 0
    name = "noname"

def main():
    me = Myclass()

    me.number = 1337
    me.name = "Harsh"

    print(me.name + " " + str(me.number))

# telling python that there is main in the program.
if __name__=='__main__':
    main()