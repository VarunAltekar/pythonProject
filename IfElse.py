import time
timestamp = time.strftime('%H:%M:%S')
print(type(timestamp))

hour = time.strftime('%H')

if(6 <= int(hour) < 12):
    print("Good Morning")
elif(12 <= int(hour) < 17):
    print("Good Afternoon")
elif(17 <= int(hour) < 20):
    print("Good Evening")
else:
    print("Good Night")
