name = input("Enter your name! ")
print("Welcome ", name, "! \n ")

answer = input("I hope you are ready for your adventure, now as you can see there is 2 portals infront of you, One on the right and one the left and each one has it's own result. Which one would you choose?: \n").lower()

if answer == "left":
    answer = input("You were transported to the realm of magic and angels, everything looks beautiful, you were amazed by the scenery, people who ride brooms, talking plants and flying books \n but you are stuck between staying here and enjoy the greenery and following the path that leads to the shining city. Type Stay to stay and follow to follow the path: ").lower()
    if answer == "follow":
        answer = input("as you walk the path to the city you found a Burning sword calling you, seducing you to use it. which choice would you like to make? Type pull to Pull it and use it or fight to fight the urge and ignore the sword: ").lower()
        if answer == "pull":
            answer = input("the sword was happy that you helped him out and decided to return the favor and granted you 30% of his Powers. Now you are able to call out the Fire of hell to slay your Enemies. \n after few Hours of walking you have reached the Shining city. It was guarded by the most beautiful creatures, they were white as snow, Glowing with a Goldish Aura and had wings, using some weird Weapons that you never saw before. One of the Guards stopped you asking you for your Purpose. What is going to be Your Answer? \n A. I am here to Discover the City \n B. I am here to deliver a Message \n C. I am here to learn Magic \n D. I am from another world and looking for information about this realm. \n").lower()
            if answer == "a":
                print("test 1 successfully")
            elif answer == "b":
                print("test 2 successfully")
            elif answer == "c":
                print("test 3 successfully")
            elif answer == "d":
                print("test 4 successfully")
        elif answer == "ignore":
            print("You ignored the sword and while you are passing it another adventurer took the sword and gained godly powers and when he wanted to test it he slashed everything in front of him and you died in the process. \n")    
    elif answer == "stay":
        print("you chose to stay but the gods were disappointed by your fragilty and weakness. and decided to struck you with Lighting and regenerating your flesh until the end of time...")
elif answer == "right":
    print("you spawn in hell and die  (only for testing)")
else:
    print("Not a valid answer! you loose")