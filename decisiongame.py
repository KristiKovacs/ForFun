print("Where will you travel next! Do you like Cold or Warm weather?")

weather = input("")

if weather == "cold":
    print("What sounds like a great COLD weather vacation:")
    print("1 Skiing/Snowboarding with my pals at a winter resort")
    print("2 Taking a boozin' cruise")
    print("3 Alpine camping and taking in the scenery")
    print("Or tell me something else you'd like:")

    vacationcold = input("> ")

    if vacationcold == "1":
        print("Alyeska's Resort and Hotel in Alaska, how exquisite")
    elif vacationcold == "2":
        print("Norwegian Cruise to Iceland, let the fun begin!")
    elif vacationcold == "3":
        print("Backpacking Trip in Adirondacks Park, sounds lovely!")
    else:
        print(f"{vacationcold} sounds good too!")
        print("Have fun!")

elif weather == "warm":
    print("What sounds like a great WARM weather vacation:")
    print("1 Anywhere with sun and sand")
    print("2 Camping under the stars")
    print("3 Sightseeing ruins")
    print("Or tell me something else you'd like:")

    vacationwarm = input("> ")

    if vacationwarm == "1":
        print("Pack your bags and go to San Diego Beach!")
        print("Enjoy!")
    elif vacationwarm == "2" or vacationwarm == "3":
        print("Get ready to pack your tent Athens, Greece is the way to go!")
    else:
        print(f"Yes {vacationwarm} ... what a great idea too!")
        print("Have a wonderful time!")

else:
    print("Follow your heart and go take your vacation! You deserve it!")
