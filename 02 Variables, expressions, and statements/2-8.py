x = int(input())
y = int(input())

total_run = x
days = 1

while total_run < y:
    total_run = total_run * 1.1
    days += 1

print(days)
