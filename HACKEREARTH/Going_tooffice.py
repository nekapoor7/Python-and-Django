D = int(input())
Oc,Of,Od = map(int,input().split())
Cs,Cb,Cm,Cd = map(int,input().split())

Online_Cost = Oc + ((D - Of) * Od)
print(Online_Cost)
Classic_Cost = Cb +((D/Cs)*Cm+D*Cd)
print(Classic_Cost)

if (Online_Cost < Classic_Cost) or (Online_Cost == Classic_Cost):
    print("Online Taxi")
else:
    print("Classic Taxi")