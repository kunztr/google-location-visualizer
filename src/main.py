from json import load


class Main:
    j = open("data/2020_SEPTEMBER.json")

    data = load(j)

    for i in data["timelineObjects"]:
        print(i)

    j.close()


Main()
