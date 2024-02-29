"""
english_to_spanish = {
    "one" : "uno",
    "two" : "dos",
    "three" : "tres",
    "four" : "cuatro",
    "five" : "cinco",
    "six" : "seis",
}
"""
"""
my_dict = {'name': 'John', 'age': 30}

for key in my_dict:
    value = my_dict.get('country', 'USA')
    print(key, my_dict[key])
"""

def main(): 

    mydictionary = {"color":"green","food":"sushi","pet":"dog","hotel":"trivago"}
    print(mydictionary["color"])
    mydictionary.update({"name":"justin"})
    mydictionary.pop("hotel")
    for key in mydictionary:
        print(key, mydictionary[key])
    for x in mydictionary:
        print(x)

    if "color" in mydictionary:
        print("my dictionary has", mydictionary["color"])


    print(f"My dictionary has {len(mydictionary)} items")

main()