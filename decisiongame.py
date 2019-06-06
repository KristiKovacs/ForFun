print("Where will you travel next! Do you like cold or warm weather?")

weather = input("").lower()

if weather == "cold":
    print("Pick a # that sounds like a great COLD weather vacation:")
    print("1 Skiing/Snowboarding with my pals at a winter resort")
    print("2 Taking a boozin' cruise")
    print("3 Alpine camping and taking in the scenery")
    print("Or tell me something else you'd like:")

    vacationcold = input("> ")

    if vacationcold == "1":
        print("You'd enjoy a stay at the Alyeska's Resort and Hotel in Alaska, how exquisite.")
    elif vacationcold == "2":
        print("You'd enjoy a Norwegian Cruise to Iceland, let the fun begin!")
    elif vacationcold == "3":
        print("You'd enjoy a backpacking Trip in Adirondacks Park. Don't forget your tent!")
    else:
        print(f"{vacationcold} sounds good too!")
        print("Have fun!")

elif weather == "warm":
    print("Pick a # that sounds like a great WARM weather vacation:")
    print("1 Anywhere with sun and sand")
    print("2 Camping under the stars")
    print("3 Sightseeing ruins")
    print("Or tell me something else you'd like:")

    vacationwarm = input("> ")

    if vacationwarm == "1":
        print("Pack your bags and go to San Diego Beach! Don't forget the suscreen!")
        print("Enjoy!")
    elif vacationwarm == "2" or vacationwarm == "3":
        print("You'd enjoy a trip to Athens, Greece! History, culture, great weather... what's not to love!")
    else:
        print(f"Yes {vacationwarm} ... that's a great idea too!")
        print("Have a wonderful time, don't forget to write!")

else:
    print("Follow your heart and go take your vacation! You deserve it!")
