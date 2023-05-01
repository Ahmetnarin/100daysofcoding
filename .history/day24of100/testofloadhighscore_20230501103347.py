 try:
    with open("./data.txt", "r") as file:
                self.highscore = int(file.read())
            return self.highscore
        except FileNotFoundError:
            # Handle the error
            print('Error: File not found.')