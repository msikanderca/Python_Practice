command  =""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car is already stated')
        else:
            started =True
            print('Car started')
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            stopped = False
    elif command =='help':
        print ("""
start - to start the car
stop - to stop the car
quit - to quit """)
    elif command == 'quit':
        break
    else:
        print('Sorry,dono')
