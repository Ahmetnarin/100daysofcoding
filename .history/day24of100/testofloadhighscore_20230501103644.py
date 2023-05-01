try:
    with open("data.txt", "r") as file:
        highscore = file.read()
        print(highscore)
except FileNotFoundError:
    # Handle the error
    print('Error: File not found.')