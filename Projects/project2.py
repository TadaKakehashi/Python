
start_count = 0
stop_count = 0
car_running = False

while True:
    user_move = str(input("Enter user move: (start/stop/quit) ")).lower()
    if user_move == "start":
        print("Car started...")
        if car_running:
            print(f'Car is already running!')
        else:
            car_running = True
            start_count += 1

    elif user_move == "stop":
        print("Car stopped...")
        if not car_running:
            print(f'Car is already stopped!')
        else:
            car_running = False
            stop_count += 1

    elif user_move == "quit":
        print(f"Game stopped! You started the car {start_count} times and stopped it {stop_count} times. Bye!")
        break
    else:
        print("Invalid move! Please enter 'start', 'stop', or 'quit'.")