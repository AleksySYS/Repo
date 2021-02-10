date = int()
a = int(input("enter something:"))

if a > 2020 or a < 1900:
    date = 0
else:
    print("Ok")
print(f'Data to {date}')