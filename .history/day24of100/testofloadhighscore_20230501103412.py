 try:
    with open("./data.txt", "r") as file:
        highscore = int(file.read())
        print(highscore)
except FilNotFoundError:
            # Handle the error
    print('Error: File not found.')