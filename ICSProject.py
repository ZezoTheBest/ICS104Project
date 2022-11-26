

# This function displays a nicely formatted for the user.
def menu():
    # prints a bold title for the menu
    print('\033[1m' + '%75s' % ('Game Recommendation System'))
    print('\033[0m', end="")  # stops the bold printing

    # prints a straight line below the title
    print(" " * 17 + 90 * "_")

    print()  # aesthetic reasons

    # Each part is assigned suitable spaces to align them under each other.
    print("%71s" % ("1. Add new Game information"))
    print("%70s" % ("2. Update Game information"))
    print("%80s" % ("3. Display information for all Games"))
    print("%75s" % ("4. Display specific information"))
    print("%78s" % ("5. Save specific data in new files"))
    print("%51s" % ("6. Exit"))

    # A line signaling the end of the menu
    print(" " * 17 + 90 * "_")

#class Game:
    #with open("Games.txt", "r+") as file:
        #def __init__(self):




# This function allows user to add Games information to the system
def add_game():


    game_id = input("Please enter a Game ID (use five digits):\n")
    if game_id in game_dict:
        print("The Game ID already exists!")
        return

    if len(game_id) != 5 or not game_id.isnumeric():
        print("Please enter five digits as a Game ID!")
        return

    game_name = input("Please enter the name of the game:\n")

    game_developers = input("Please enter the name of the developer:\n")

    try:
        game_rating = float(input("Please enter the rating from 1 to 10\n"))
        if not 1 <= float(game_rating) <= 10:
            raise TypeError
    except TypeError:
        print("The game rating should be a number between one and 10")
        return

    num_of_reviews = input("Enter the number of game reviews:\n")
    if not num_of_reviews.isnumeric():
        print("The number of reviews must contain of digits only!")
        return

    price = input("Enter the price of the game:\n")
    if not price.isnumeric():
        print("The price should contain digits only!")
        return

    year = input("Enter the year in which the game has been released:\n")
    if not year.isnumeric():
        print("The year needs to be in digits!")
        return
    elif int(year) > 2022:
        print("The year can not be larger than 2022.")
        return

    genre = input("Enter the genre of the game:\n")
    game_dict[game_id] = [game_name,game_developers,str(game_rating),num_of_reviews,price,year,genre]

    games_file.seek(0)
    file = games_file.read()
    games_file.seek(0)
    file_list = games_file.readlines()
    games_file.seek(len(file) -1 + len(file_list))
    char = games_file.read()
    print(char)
    if char != "\n":
        games_file.write("\n")

    games_file.write("%s\t%s\t%s\t%s\t%s\t"%(game_id,game_name,game_developers,game_rating,num_of_reviews))
    games_file.write("%s\t%s\t%s"%(price,year,genre))
    print("The info has been added successfully!")


def update_game():
    game_id = input("Please enter the Game ID:\n")
    if game_id in game_dict:
        game_rating_change = input("Enter Y to change gamer rating or any key to proceed:\n")

        if game_rating_change.lower() == "y":
            try:
                game_rating = float(input("Please enter the new rating from 1 to 10\n"))
                if not 1 <= float(game_rating) <= 10:
                    raise TypeError
            except TypeError:
                print("The game rating should be a number between one and 10")
                return
            game_dict[game_id][3] = str(game_rating)

        num_reviews_change = input("Enter Y to change number of reviews or any key to proceed:\n")

        if num_reviews_change.lower() == "y":

            num_of_reviews = input("Enter the new number of game reviews:\n")

            if not num_of_reviews.isnumeric():

                print("The number of reviews must contain of digits only!")
                return
            game_dict[game_id][4] = num_of_reviews

        price_change = input("Enter Y to change the price or any key to proceed:\n")

        if price_change.lower() == "y":
            price = input("Enter the price of the game:\n")
            if not price.isnumeric():
                print("The price should contain digits only!")
                return
            game_dict[game_id][5] = price + "\n"

        games_file.seek(0)
        games_file.truncate(0)

        for game_id in game_dict:
            games_file.write(game_id + "\t")
            for value in game_dict[game_id]:
                games_file.write(value.strip() + "\t")
            games_file.write("\n")


        print("Saved!")
        return


    print("The Game ID does not exist!")
    return






def main():
    done = False
    while not done:
        menu()
        command = input("Please insert a number or \"Q\" for  exit:\n")
        if command == "1":
            add_game()

        elif command == "2":
            update_game()

        elif command == "3":
            pass

        elif command == "4":
            pass

        elif command == "5":
            pass

        elif command.lower() == "q":
            done = True

        else:
            print("Please enter a number from 1-5 or \"Q\" to exit")


with open("Games.txt","r+") as games_file:

    game_dict = {}
    for line in games_file.readlines():
        game_dict[line.split("\t")[0]] = line.split("\t")[1:]

    main()


