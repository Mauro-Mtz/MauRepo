final_number = input('write your max of numbers; ')

try:
    n = int(final_number)
except ValueError:
    print('error')
    exit()

if n <1 or n > 20:
    print('invalid')
    exit()

f = [0, 1]

for _ in range(n - 2):
    f.append(f[-1] + f[-2])

print('your fibonacci series is: ')
for num in f[:n]:
    print(num)
