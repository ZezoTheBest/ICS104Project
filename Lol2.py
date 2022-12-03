

header_list = ["GameID", "GameName", "GameDeveloper", "GamerRating", "NumOfReviews", "Price", "Year", "Genre"]
def entry(times):
    for i in range(times):
        file.write("|" + " "*18)
    file.write("|\n")

def content_line(element,dictionary):
    file.write("|"+element.center(18)+ "|")
    values = dictionary[element]

    for value in values:

        index = values.index(value)

        while len(value) > 18:
            file.write(value[:18])
            entry(8 - index - 2)
            value = value[18:]
            file.write("|")
            for space in range(index + 1):
                file.write(" "* 18 + "|")

        else:
            if index + 1 == len(values):
                file.write(value.center(18))
            else:
                file.write(value.center(18) + "|")


with open("Games.txt", "r") as games_file:
    game_dict = {}
    for line in games_file.readlines():
        game_dict[line.split("\t")[0]] = line.split("\t")[1:8]
    with open("Table.txt", "w") as file:
        file.write("-"*153)
        file.write("\n")
        for header in header_list:
            file.write("|" + header.center(18))
        file.write("|\n")
        file.write("-" * 152)
        for element in game_dict:
            entry(8)
            entry(8)
            content_line(element,game_dict)
            entry(8)
            entry(8)
            entry(8)
            file.write("-"*152)