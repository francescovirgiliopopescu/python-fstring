from datetime import datetime;

str_val = 'apples'
num_val = 42
print(f'{str_val=}, {num_val = }') # str_val='apples', num_val = 42

print(f'{num_val % 2 = }') # num_val % 2 = 0

print(f'{str_val!r}') # 'apples'

price_val = 6.12658
print(f'{price_val:.2f}') # 6.13

date_val = datetime.utcnow()

print(f'{date_val=:%Y-%m-%d}') # date_val=2021-07-09