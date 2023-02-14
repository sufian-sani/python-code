number_plant = int(input())
plant_height=list(map(int, input().split()))

u_plant_height = set(plant_height)
quentity = len(u_plant_height)
n=0
for i in u_plant_height:
    n=i+n

average_height=n/quentity

print(average_height)