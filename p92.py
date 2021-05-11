from time import *

epoch = time()
print(epoch)

local = localtime(epoch)
print(local.tm_year)

today = strftime('%A', local)
print(today)

start_timer = time()
struct = localtime(start_timer)

print('\nStarting Countdown At:', strftime('%X', struct))

i = 10
while i > -1:
	print(i)
	i -= 1
	sleep(1)

end_timer = time()
struct = localtime(end_timer)
difference = round(end_timer - start_timer)

print('\nCountown Ended At:', strftime('%X', struct))
print('\nRuntime:', difference, 'Seconds')
