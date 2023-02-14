def near_thousand(num):
    return (abs(1000-num) <= 100) or (abs(2000-num) <= 100)

print(near_thousand(999))
print(near_thousand(100))
print(near_thousand(1900))