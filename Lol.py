def entry(times):
    for i in range(times):
        print("|" + " "*17, end = " ")
    print("|")

def content_line(element):
    print("|"+element.center(18), end = "|")
    values = games_dict[element]

    for value in values:

        index = values.index(value)

        while len(value) > 18:
            print(value[:18] , end = "")
            entry(8 - index - 2)
            value = value[18:]
            #print("|" +" "*(19*(index+1) - 1),end = "|")
            print("|" , end = "")
            for space in range(index + 1):
                print(" "* 18, end = "|")

        else:
            if index + 1 == len(values):
                print(value.center(18), end = "")
            else:
                print(value.center(18), end="|")




with open("Games.txt", "r+") as f:
    games_dict = {}
    for line in f.readlines():
        games_dict[line.split("\t")[0]] = line.split("\t")[1:8]
    games_dict = dict(sorted(games_dict.items()))
    header_list = ["GameID","GameName","GameDeveloper","GamerRating","NumOfReviews","Price","Year","Genre"]

    print("\033[1m" , end = "")
    print("-"*153)
    for header in header_list:
        print("|" + header.center(18), end = "")

    print("|")
    print("-"*153, end = "")
    print("\033[0m")
    for element in games_dict:
        entry(8)
        entry(8)
        content_line(element)
        entry(8)
        entry(8)
        entry(8)
        print("-" * 153)

