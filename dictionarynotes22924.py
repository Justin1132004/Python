def main():
    emoji={"duck":"🐥", "python":"🐍", "monkey":"🙈🙉🙊",
            "dog":"🐶", "cat":"🙀", "fish":"🐠", "bird":"🦜"}
    
    # print(emoji)
    # # accessing an item by its key
    # print(emoji["duck"])
    # animal = emoji.get("cat")
    # print(animal)

    # # get the keys
    # print(emoji.keys())

    # # get the values
    # print('\n\n')
    # print(emoji.values())

    # # get the key value pair
    # print('\n\n')
    # print(emoji.items())

    # if "duck" in emoji:
    #     print(emoji["duck"])

    # emoji["duck"] ="🦆"
    # print(emoji["duck"])

    # emoji.update({"raccoon": "🦝"})

    emoji.pop("cat")
    print(emoji)

    emoji.pop("duck")
main()