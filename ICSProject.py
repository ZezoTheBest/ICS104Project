# This work done by group RandomNameGenerator:
# Ziad Tariq Al Alami, 202271820, 77, 50%
# Omar Bahaeldin Abdalla, 202259760, 77, 50%



#This function displays a nicely formatted for the user. These print functions are placed in a function to avoid repetition.
def menu():

    #prints a bold title for the menu
    print('\033[1m' + '%75s'%('Game Recommendation System'))
    print('\033[0m', end="") #stops the bold printing

    #prints a straight line below the title
    print(" "* 17 + 90 * "_")

    print() #aesthetic reasons

    #Each part is assigned suitable spaces to align them under each other.
    print("%71s"%("1. Add new Game information"))
    print("%70s"%("2. Update Game information"))
    print("%80s"%("3. Display information for all Games"))
    print("%75s"%("4. Display specific information"))
    print("%78s"%("5. Save specific data in new files"))
    print("%51s"%("6. Exit"))

    #A line signaling the end of the menu
    print(" "* 17 + 90 * "_")


# This function allows user to add games information to the system
def add_game():
    # Asks for game ID
    game_id = input("Please enter a Game ID (use five digits):\n")
    # If game ID already exists , display message and exit
    if game_id in game_dict:
        print("The Game ID already exists!")
        return
    # If the game ID is not 5 characters long or not a number, display a message and exit
    if len(game_id) != 5 or not game_id.isnumeric():
        print("Please enter five digits as a Game ID!")
        return
    # Ask for game name
    game_name = input("Please enter the name of the game:\n")
    # Ask for game developers
    game_developers = input("Please enter the name of the developer:\n")

    try:
        # Ask for game rating
        game_rating = float(input("Please enter the rating from 1 to 10\n"))

        # If the game rating is not between 1 and 10 and is not a number, raise an error and display a message
        if not 1 <= float(game_rating) <= 10:
            raise ValueError
    except ValueError:
        print("The game rating should be a number between one and 10")
        return

    # Ask for the number of reviews
    num_of_reviews = input("Enter the number of game reviews:\n")
    # If the number of reviews is not a number, display a message and exit
    if not num_of_reviews.isdigit():
        print("The number of reviews must contain of digits only!")
        return
    # Ask for new price
    price = input("Enter the price of the game:\n")
    # If the price is not a number , display a message and exit
    if not price.isdigit():
        print("The price should contain digits only!")
        return
    # Ask the user for the year
    year = input("Enter the year in which the game has been released:\n")

    # If the year is not a digit or larger than 2022 , display a message and exit
    if not year.isdigit():
        print("The year needs to be in digits!")
        return
    elif int(year) > 2022:
        print("The year can not be larger than 2022.")
        return

    # Ask for the genre of the game
    genre = input("Enter the genre of the game:\n")

    # Create new key and assign to it the game ID, and assign the other values in the value as a list
    game_dict[game_id] = [game_name, game_developers, str(game_rating), num_of_reviews, price, year, genre]

    # Move the pointer to the beginning of the file
    games_file.seek(0)
    # Read the whole file
    file = games_file.read()
    # Move the pointer to the beginning
    games_file.seek(0)
    # Read the whole file as lines in a list
    file_list = games_file.readlines()
    # Move the pointer to the character before the last
    games_file.seek(len(file) - 1 + len(file_list))
    # Read the last character
    char = games_file.read()

    # If the last character is not a new line , add a new line
    if char != "\n":
        games_file.write("\n")

    # Write the new information in the file and display an appropriate message
    games_file.write("%s\t%s\t%s\t%s\t%s\t" % (game_id, game_name, game_developers, game_rating, num_of_reviews))
    games_file.write("%s\t%s\t%s" % (price, year, genre))
    print("The info has been added successfully!")


"""This function updates the game information based on user input"""


def update_game():
    game_id = input("Please enter the Game ID:\n")  # Ask the user for game ID
    if game_id in game_dict:  # If the game ID exists as a key

        # Ask the user if he wants to change the game rating
        game_rating_change = input("Enter Y to change gamer rating or any key to proceed:\n")

        if game_rating_change.lower() == "y":
            try:
                # Ask for the new gamer rating
                game_rating = float(input("Please enter the new rating from 1 to 10:\n"))

                # if the new game rating is not between 1 and 10 or not a number
                if not 1 <= float(game_rating) <= 10:
                    raise ValueError

            except ValueError:  # display the error message
                print("The game rating should be a number between one and 10.")
                return

            # Assign the new game rating to the dictionary
            game_dict[game_id][3] = str(game_rating)

        num_reviews_change = input("Enter Y to change number of reviews or any key to proceed:\n")

        if num_reviews_change.lower() == "y":
            # Ask for new number of reviews
            num_of_reviews = input("Enter the new number of game reviews:\n")

            # If the number of reviews is not a number , display a message
            if not num_of_reviews.isnumeric():
                print("The number of reviews must contain of digits only!")
                return
            # Assign the new number of reviews to the dictionary
            game_dict[game_id][4] = num_of_reviews

        price_change = input("Enter Y to change the price or any key to proceed:\n")

        if price_change.lower() == "y":
            price = input("Enter the price of the game:\n")  # Inputs the new price
            # If the price is not a number , display an error message
            if not price.isnumeric():
                print("The price should contain digits only!")
                return
            # Assign the new price to the dictionary
            game_dict[game_id][5] = price + "\n"

        # Move the file pointer to the beginning
        games_file.seek(0)
        # Delete all info in the file
        games_file.truncate(0)

        # Add updated info in the file in the end
        for game_id in game_dict:
            games_file.write(game_id + "\t")
            for value in game_dict[game_id]:
                games_file.write(value.strip() + "\t")
            games_file.write("\n")

        # Display message and end the function
        print("Saved!")
        return

    # If the game ID does not exist
    print("The Game ID does not exist!")
    return

def sortbyID(dictionary): # Returns dictionary sorted by the key (game ID)
    sorted_dictionary = dict(sorted(dictionary.items()))
    return sorted_dictionary

def sortbyName(dictionary): # Returns dictionary sorted by the games names
    #The lambda function sorts by the values then by the game name
    sorted_dictionary = dict(sorted(dictionary.items(),key= lambda value : value[1][0]))
    return sorted_dictionary

def sortbyGenre(dictionary): # Returns dictionary sorted by genre
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda value : value[1][6]))
    return sorted_dictionary

def sortByRating(dictionary): # Returns dictionary sorted by game rating
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda value: float(value[1][2]) ,reverse= True))
    return sorted_dictionary


"""This function prints a number of lines based on a given input"""


def entry(times):
    for i in range(times):
        print("|" + " " * 17, end=" ")
    print("|")


"""This function prints the content of a dictionary along a given lines """


def content_line(element, dictionary):
    print("|" + element.center(18), end="|")  # Displays two lines with the element in the middle

    values = dictionary[element]

    for value in values:  # For every value in values

        index = values.index(value)  # Get the index of the value

        while len(value) > 18:  # While the length of value more than 18 characters
            print(value[:18], end="")  # Print the first 18 characters
            entry(8 - index - 2)  # Then display number of lines based on its position
            value = value[18:]  # Then assign the value to be what is after 18 characters
            print("|", end="")  # Start a new line in the next row
            for space in range(index + 1):  # Display lines depending on the position of the value
                print(" " * 18, end="|")

        else:
            if index + 1 == len(values):  # if the value is at the end of the line
                print(value.center(18), end="")  # Print the element
            else:  # If the value is not at the end
                print(value.center(18), end="|")  # Print the element with a | beside it

"""This function takes a dictionary as an input and displays a table based on the info in it"""

def displayTable(dictionary):
    #Main Keys and Values
    header_list = ["GameID", "GameName", "GameDeveloper", "GamerRating", "NumOfReviews", "Price", "Year", "Genre"]

    print("\033[1m", end="")
    print("-" * 153)
    for header in header_list: #Print the header centered in the middle using 18 characters
        print("|" + header.center(18), end="")

    print("|")
    print("-" * 153, end="")
    print("\033[0m")
    for element in dictionary:
        entry(8) # Makes 8 lines
        entry(8)
        content_line(element,dictionary) #Prints the key and the values
        entry(8)
        entry(8)
        entry(8)
        print("-" * 153) # Makes a new row for the next entry

"""This function returns the top games for a 
given number of games as an input
for the last years given as an input"""

def top_games_in_years(noOfGames,years_back,dictionary):
    new_dict = {}
    new_dict_no_of_games = 0
    sorted_dict = sortByRating(dictionary)
    for key in sorted_dict:# for key in the sorted dictionary
        if  (2022 - years_back) <= int(dictionary[key][5]) <= 2022: # if the year is in the given range
            new_dict[key] = sorted_dict[key] #Assign the key and value to the new dictionary
            new_dict_no_of_games += 1
            if new_dict_no_of_games == noOfGames: # If the number of games reach the given , break the loop
                break
    return new_dict

"""This function returns the total price of games for a given year"""

def games_price_per_year(year,dictionary):
        if type(year) == int: # If the year is an integer , convert it to a string
            year = str(year)
        total_price = 0 #Total price variable
        for key in dictionary:
            if dictionary[key][5] == year: # If the year is the same as the yeaar in dictionary
                total_price += float(dictionary[key][4]) # Add the price to the total price
        # Returns the total rounded to 3 decimals
        return "The total price of games in " + year + " is "  + str(round(total_price,3))+"$"

"""This function returns the average price of games per year
This function is the same as the total price of game per year
but this function divides by the total number of games in that year"""

def avrg_games_prices_per_year(year,dictionary):
    if type(year) == int:
        year = str(year)
    total_price = 0
    total_games = 0
    for key in dictionary:
        if dictionary[key][5] == year:
            total_price += float(dictionary[key][4])
            total_games += 1
    return "The average price of games in " + year + " is "  + str(round(total_price / total_games,3)) + "$"

"""This method returns a dictionary 
where the genre and the year in the
original dictionary matches
the given year and genre"""

def sorted_game_by_year_by_genre(year,genre,dictionary):
    if type(year) == int: # If the type of year is integer, convert it to string
        year = str(year)
    new_dict = {}
    for key in dictionary:
        if dictionary[key][5] == year and dictionary[key][6] == genre: #If the year and genre match the ones in the dictionary
            new_dict[key] = dictionary[key] # Add the key and value to the new dictionary
    return new_dict


"""This function takes a specific genre as an input 
and writes the game info in a new file 
where the genre corresponds
with the given genre
"""


def saving_in_new_file(genre):
    genre_dict = {}  # Create an empty dictionary
    for key in game_dict:  # Iterates over the keys of the original dictionary
        if genre.lower() == game_dict[key][6].lower():  # If the genre given exists in the dictionary
            genre_dict[key] = game_dict[key]  # Add the key and value to the empty dictionary

    if len(genre_dict) == 0:  # If the genre does not exist in the dictionary,display a message
        print("The genre you selected is not found.")

    else:  # If the genre exists
        with open("Genre.txt", "w") as new_file:  # Open a new file called Genre.txt
            for key in genre_dict:
                new_file.write("%s " % key)  # Write the key
                for value in genre_dict[key]:  # Iterate through the value
                    new_file.write("%s\t" % value)  # Write the values
                new_file.write("\n")  # Enter a new line
        print("The information has been saved successfully in Genre.txt !")  # Display a message to the user


""" This is the main function that interacts with the user input , 
it joins between the other defined functions that work behind the scenes
and the user's input
"""


def main():
    done = False  # The program will keep running until the user is done
    while not done:
        menu()  # Display the meny that the user will read
        command = input("Please insert a number or \"Q\" for  exit:\n")  # Prompt the user for input
        if command == "1":
            add_game()  # Add the game to the dictionary and write it to the file

        elif command == "2":
            update_game()  # Update the game info in the dictionary and update it in the file

        elif command == "3":
            sort_method = input("""Before displaying the table,how do you want to sort it?:
            \n1-By GameID
            \n2-By Game Name
            \n3-By Genre\n""")  # Prompts the user to choose a sorting method to display the table

            if sort_method == "1":
                displayTable(sortbyID(game_dict))  # Display the table sorted by game ID
            elif sort_method == "2":
                displayTable(sortbyName(game_dict))  # Display the table sorted by game name
            elif sort_method == "3":
                displayTable(sortbyGenre(game_dict))  # Display the table sorted by game genre
            else:  # Input validation from the user
                print("Please enter 1, 2, or 3 only.")



        elif command == "4":
            category = input("""Choose one of the following to display:\n
            1-View top 50 selling Games in last 10 years\n
            2-Print Total Price for all Games per Year.\n
            3-Print Average Price of all Games per Year.\n
            4-View sorted list of Games (by GameID) for a given year for a given Genre\n""")  # Prompts the user to display specific info
            if category == "1":
                displayTable(
                    top_games_in_years(50, 10, game_dict))  # displays the table for top 50 games in last 10 years

            elif category == "2":
                year = input("Please enter a year:\n")  # Inputs the year from the user
                if year.isdigit():  # If the year is a number
                    if int(year) <= 2022:  # If the year is less than 2022
                        print(games_price_per_year(year, game_dict))  # Print the total price for games in that year
                    else:  # If year is larger than 2022 , display an error
                        print("The year should be less than 2023.")
                else:  # If the year is not a number
                    print("Only enter the year in numbers.")

            elif category == "3":
                year = input("Please enter a year:\n")  # Inputs the year from the user
                if year.isdigit():  # If the year is a number
                    if int(year) <= 2022:  # If the year is less than or equal to 2022
                        print(avrg_games_prices_per_year(year,
                                                         game_dict))  # Display the average games prices for that year
                    else:  # If the year is larger than 2022, display a message
                        print("The year should be less than 2023.")
                else:  # If the year is not a number
                    print("Only enter the year in numbers.")

            elif category == "4":
                year = input("Please enter a year:\n")  # Inputs the year from the user
                if not year.isdigit():  # If the year is not a number, display a message
                    print("Only enter the year in numbers.")

                else:
                    if int(year) <= 2022:  # If the year is less than or 2022
                        genre = input("Please enter a genre:\n")  # Ask the user for to input the genre
                        found = False  # Tells if the genre is found
                        for value in game_dict.values():
                            if genre.capitalize() == value[6] and year == value[5]:
                                # Displays table for given year and genre
                                displayTable(sorted_game_by_year_by_genre(year, genre,game_dict))
                                found = True
                                break
                        if found == False:  # If the genre does not consist fully of characters
                            print("No game found with given information.")
                    else:  # If the year entered is larger than 2022
                        print("The year should be less than 2023.")

            else:  # If the display input is not in the range of options
                print("Please enter a number from 1 to 4.")

        elif command == "5":
            genre = input("Which genre do you want to save to a new file?\n")  # Inputs the genre from the user

            if genre.isalpha():  # If the genre consists of letters only
                genre = genre.capitalize()  # Capitalize the genre

            else:  # If the genre doesnt consist fully of characters
                print("Please enter a valid genre format.")

            saving_in_new_file(genre)  # Save the genre in a new file

        elif command.lower() == "q":  # If the menu input is Q , the user is done and exit the program
            done = True

        else:  # If the input is not one of the following options
            print("Please enter a number from 1-5 or \"Q\" to exit")


with open("Games.txt", "r+") as games_file:  # Opens the file in read and append mode
    from IPython.display import display, HTML

    display(HTML("<style>.container { width:100% !important; }</style>"))  # Maximizes column width on Jupyter Notebook

    try:
        game_dict = {}  # Dictionary to read the file
        for line in games_file.readlines():
            game_dict[line.split("\t")[0]] = line.split("\t")[1:8]  # Assign the ID as key and the rest as value
        main()  # run the main function

    except UnicodeDecodeError:  # The program gets interrupted by the user
        print("You have quit the program !")
