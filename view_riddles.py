from all_riddles import riddles_json


def main():
    riddles_list = riddles_json['riddles']

    for riddle in riddles_list:
        print("{}".format(riddle['id']))



main()
