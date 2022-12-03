

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
            raise ValueError
    except ValueError:
        print("The game rating should be a number between one and 10")
        return

    num_of_reviews = input("Enter the number of game reviews:\n")
    if not num_of_reviews.isdigit():
        print("The number of reviews must contain of digits only!")
        return

    price = input("Enter the price of the game:\n")
    if not price.isdigit():
        print("The price should contain digits only!")
        return

    year = input("Enter the year in which the game has been released:\n")
    if not year.isdigit():
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
                game_rating = float(input("Please enter the new rating from 1 to 10:\n"))
                if not 1 <= float(game_rating) <= 10:
                    raise TypeError
            except TypeError:
                print("The game rating should be a number between one and 10.")
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

def sortbyID(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items()))
    return sorted_dictionary
def sortbyName(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items(),key= lambda value : value[1][0]))
    return sorted_dictionary
def sortbyGenre(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda value : value[1][6]))
    return sorted_dictionary
def sortByRating(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda value: float(value[1][2]) ,reverse= True))
    return sorted_dictionary

def entry(times):
    for i in range(times):
        print("|" + " "*17, end = " ")
    print("|")

def content_line(element,dictionary):
    print("|"+element.center(18), end = "|")
    values = dictionary[element]

    for value in values:

        index = values.index(value)

        while len(value) > 18:
            print(value[:18], end = "")
            entry(8 - index - 2)
            value = value[18:]

            print("|" , end = "")
            for space in range(index + 1):
                print(" "* 18, end = "|")

        else:
            if index + 1 == len(values):
                print(value.center(18), end = "")
            else:
                print(value.center(18), end="|")

def displayTable(dictionary):
    header_list = ["GameID", "GameName", "GameDeveloper", "GamerRating", "NumOfReviews", "Price", "Year", "Genre"]

    print("\033[1m", end="")
    print("-" * 153)
    for header in header_list:
        print("|" + header.center(18), end="")

    print("|")
    print("-" * 153, end="")
    print("\033[0m")
    for element in dictionary:
        entry(8)
        entry(8)
        content_line(element,game_dict)
        entry(8)
        entry(8)
        entry(8)
        print("-" * 153)


def top_games_in_years(noOfGames,years_back,dictionary):
    new_dict = {}
    new_dict_no_of_games = 0
    for key in sortByRating(dictionary):
        if  (2022 - years_back) <= int(dictionary[key][5]) <= 2022:
            new_dict[key] = sortByRating(dictionary)[key]
            new_dict_no_of_games += 1
            if new_dict_no_of_games == noOfGames:
                break
    return new_dict

def games_price_per_year(year,dictionary):
        if type(year) == int:
            year = str(year)
        total_price = 0
        for key in dictionary:
            if dictionary[key][5] == year:
                total_price += float(dictionary[key][4])
        return round(total_price,3)

def avrg_games_prices_per_year(year,dictionary):
    if type(year) == int:
        year = str(year)
    total_price = 0
    total_games = 0
    for key in dictionary:
        if dictionary[key][5] == year:
            total_price += float(dictionary[key][4])
            total_games += 1
    return round(total_price / total_games,3)

def sorted_game_by_year_by_genre(year,genre,dictionary):
    if type(year) == int:
        year = str(year)
    new_dict = {}
    for key in dictionary:
        if dictionary[key][5] == year and dictionary[key][6] == genre:
            new_dict[key] = dictionary[key]
    return sortbyID(new_dict)


def saving_in_new_file(genre):
    genre_dict = {}
    for key in game_dict:
        if genre.lower() == game_dict[key][6].lower():
            genre_dict[key] = game_dict[key]
    if len(genre_dict) == 0:
        print("The genre you selected is not found.")
        
    else:
        with open("Genre.txt", "w") as new_file:
            for key in genre_dict:
                new_file.write("%s "%key)
                for i in range(7):
                    new_file.write("%s\t"%genre_dict[key][i])
                new_file.write("\n")
        print("The information has been saved successfully in Genre.txt !")




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
            sort_method = input("""Before displaying the table,how do you want to sort it?:
            \n1-By GameID
            \n2-By Game Name
            \n3-By Genre\n""")

            if sort_method == "1":
                displayTable(sortbyID(game_dict))
            elif sort_method == "2":
                displayTable(sortbyName(game_dict))
            elif sort_method == "3":
                displayTable(sortbyGenre(game_dict))
            else:
                print("Please enter 1, 2, or 3 only.")



        elif command == "4":
            category = input("""Choose one of the following to display:\n
            1-View top 50 selling Games in last 10 years\n
            2-Print Total Price for all Games per Year.\n
            3-Print Average Price of all Games per Year.\n
            4-View sorted list of Games (by GameID) for a given year for a given Genre\n""")
            if category == "1":
                displayTable(top_games_in_years(50,10,game_dict))

            elif category == "2":
                year = input("Please enter a year:\n")
                if year.isdigit():
                    if int(year) <= 2022:
                        print(games_price_per_year(year,game_dict))
                    else:
                        print("The year should be less than 2023.")
                else:
                    print("Only enter the year in numbers.")

            elif category == "3":
                year = input("Please enter a year:\n")
                if year.isdigit():
                    if int(year) <= 2022:
                        print(avrg_games_prices_per_year(year, game_dict))
                    else:
                        print("The year should be less than 2023.")
                else:
                    print("Only enter the year in numbers.")

            elif category == "4":
                year = input("Please enter a year:\n")
                if not year.isdigit():
                    print("Only enter the year in numbers.")

                else:
                    if int(year) <= 2022:

                        genre = input("Please enter a genre:\n")

                        if genre.isalpha():
                            genre = genre.capitalize()
                            displayTable(sorted_game_by_year_by_genre(year, genre, game_dict))
                        else:
                            print("Please enter a valid genre format.")
                    else:
                        print("The year should be less than 2023.")

            else:
                print("Please enter a number from 1 to 4.")

        elif command == "5":
            genre = input("Which genre do you want to save to a new file?\n")
            saving_in_new_file(genre)

        elif command.lower() == "q":
            done = True

        else:
            print("Please enter a number from 1-5 or \"Q\" to exit")


with open("Games.txt","r+") as games_file:
    try:
        game_dict = {}
        for line in games_file.readlines():
            game_dict[line.split("\t")[0]] = line.split("\t")[1:8]
        main()

    except UnicodeDecodeError:
        print("You have quit the program !")


