import time
import random

# Back story of the game
print
"You decide to run for president of The United States of America"
time.sleep(2)
print
"Before you run, you must answer some questions for the election"
time.sleep(2)
print
""
name = raw_input("What is your name?")
party = raw_input("Are you running as a Republican or Democrat?")

# The following is for the Democrat Version of the game
print
""
if party.lower() == "democrat":
    print
    "After a lengthy and difficult election, you are able to defeat your opponents"
    time.sleep(3)
    print
    "You are the President of The United States of America"
    time.sleep(2)
    print
    "Congratulations President " + name + " there are millions of people counting on your leadership!"
    print
    ""
    time.sleep(2)
    print
    "Your first crisis has come up during your Presidency! You must think fast."
    print
    ""
    time.sleep(2)
    print
    "The country is about to suffer a financial bankruptcy"
    print
    ""
    print
    "You must cut funding to avoid this catastrophe!"
    print
    ""
    demochoice1 = raw_input("Will you cut funding for military or education")
    if demochoice1 == "military":
        print
        "President " + name + " Im glad to inform you that you have avoided absolute bankruptcy..."
        time.sleep(3)
        print
        "but seeing your weakness Russia has invaded Alaska and Canada for oil"
        demominichoice1 = raw_input("Do you wish to 'fight' or 'not fight'?")
        if demochoice1 == 'fight':
            print
            "You go to war with  great acheivements with your allies in beating back the Russians..."
            time.sleep(2)
            print
            "but you quickly run out of troops"
            demochoice2 == raw_input("Will you start a draft or will you not start a draft?: 'yes' or 'no'")
            if demochoice2 == 'yes':
                print
                "Good job you have defeated the Russians and the US sees you as a person who will stop at noting to defend your allies"
            else:
                print
                "You saldy loose the war and you are seen as the President that lost Canda"
    else:
        time.sleep(2)
        print
        ""
        print
        "National IQ goes down and you are no longer able to compete in international markets the economy goes down even faster,you jumped out of the boiling pot and into the hot flames"

    # The following is for the republican Version of the game
if party.lower() == "republican":
    print
    "After a lengthy and difficult election, you are able to defeat your opponents"
    time.sleep(3)
    print
    "You are the President of The United States of America"
    time.sleep(2)
    print
    "Congratulations President " + name + " there are millions of people counting on your leadership!"
    print
    ""
    time.sleep(2)
    print
    "Your first crisis has come up during your Presidency!"
    print
    ""
    time.sleep(2)
    print
    "North Korean leader Kim Jung Un has surprisingly extends his hand in friendship to the United States to start diplomatic negotiations to make peace with the South..."
    Repchoice1 = raw_input(
        "Will you negotiate with our sworn enemies or reject an opportunity of a life time to end the North - South Korean rivalry and possibly unify Korea:'negotiate' or 'no negotiation' ")
    if Repchoice1 == "negotiate":
        print
        "President " + name + " Im glad to announce you have made massive strides in making peace between the Koreas and the rest of the world with this decision..."
        time.sleep(5)
        print
        ""
        print
        "but the Republican party as a whole and the people that voted for you say you're a 'traiter' to America for speaking with sworn enemies of America..."
        repminichoice = raw_input(
            "Will you take back all the things you accomplished for the sake of the people that got you into the oval office or will you stand firm on the accompliments you have already made?:'Stand firm' or 'I didnt mean it'")
        if repminichoice == "I didnt mean it":
            print
            "Now the whole country both Republican and Democrat see you are an untrust worthy President that does not mean what you say,your chances of re-election are slime"
        else:
            print
            "The people soon see that you are someone that mean what you say even though others may not like it, you gain the respect of the country"
    else:
        print
        "You have given up an opportunity of a life time to end hostility between North and South Korea the world community denounces your choice..."
        time.sleep(2)
        print
        "but your support in America increase as you refused to speak with sworn enemies of America"
        time.sleep(3)
        print
        ""
        print ""
        print
        "Your Presidency goes on to be one of the most successful Presidencies of all time the people will hate to see you leave office"






