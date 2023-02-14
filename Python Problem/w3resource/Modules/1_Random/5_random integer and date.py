import random
import datetime
print('generate a random integer between 0 and 6:')
print(random.randrange(5))

print('random integer between 5 and 10:')
print(random.randrange(start=5, stop=10))

print('random integer between 0 and 10:')
print(random.randrange(start=0, stop=10, step=3))

print("\nRandom date between two dates:")

start_dt = datetime.date(2019, 2, 1)
end_dt = datetime.date(2019, 3, 1)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)