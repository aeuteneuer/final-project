import time

def intro():
    print("It was just a normal day.\n") 
    time.sleep(2)
    print("I was on the app store when I came across a radio tuner application.\n")
    time.sleep(3)
    print("My friend told me you could listen in on differnt types of signals.\n")
    time.sleep(3)
    print("So I decided to download it and give it a try.\n")
    time.sleep(3)
    print("That's when this happened...\n")
    time.sleep(2)
    print("*static*")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Hello!?")
    time.sleep(1)
    print("Hello, is anyone there?\n")
    time.sleep(1)
    print("1.) H-hello?\n2.) I am here. Who is this?")

def one():
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("... oh thank god!")
        time.sleep(1)
        print("Seriously. Thank god. I have been trying to get a hold of someone for 4 days!")
        time.sleep(3)
        choiceA()
    elif userinput == "2":
        time.sleep(1)
        print("My name is Joseph Fields")
        time.sleep(1)
        print("I have....be...oh...where do I even begin?!")
        time.sleep(2)
        choiceB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        one()

def choiceA():
    print("1.) Four days!?\n2.) Where are you?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("Yes. I have been stranded on this island.")
        time.sleep(2)
        print("...my plane crashed")
        time.sleep(2)
        choiceAA()
    elif userinput == "2":
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("I have no idea....")
        time.sleep(2)
        choiceAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceA()

def choiceB():
    print("1.) Okay slow down!\n2.) Start from the beginning.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("You are right I need to calm down. ")
        time.sleep(2)
        choiceBA()
    elif userinput == "2":
        time.sleep(1)
        print("Okay... for a business trip.")
        time.sleep(1)
        print("I was on a plane going from Miami to the bahamas...")
        time.sleep(1)
        print("Then it just....")
        time.sleep(1)
        print("...exploded...")
        time.sleep(2)
        choiceBB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceB()

def choiceAA():
    print("1.) Plane...what plane?\n2.) An island? Can you be more specific?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("It was a Delta flight.")
        time.sleep(1)
        print("I was traveling from Miami to the Bahamas for a business trip.")
        time.sleep(2)
        choiceAAA()
    elif userinput == "2":
        time.sleep(1)
        print("I really can't.")
        time.sleep(1)
        print("The plane crashed and I barely made it out alive.")
        time.sleep(2)
        print("I was floating on a piece of debris and just woke up here.")
        time.sleep(2)
        choiceAAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAA()

def choiceAAB():
    print("1.) Wow. You got really lucky.\n2.) Are there any other survivors?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("I know.")
        time.sleep(1)
        print("Everything is such a blur...")
        time.sleep(1)
        print("I can't really remember anything.")
        time.sleep(2)
        choiceAABA()
    elif userinput == "2":
        time.sleep(1)
        print("Survivors...")
        time.sleep(1)
        print("well as far as I know...")
        time.sleep(1)
        print("I am the only survivor...")
        time.sleep(2)
        choiceAABB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAAB()

def choiceAABA():
    print("1.) Thats understandable.\n2.) Try and think back to the beginning.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAABA()

def choiceAABB():
    print("1.) The only survivor!?\n2.) How many other were there...")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAABB()
    

def choiceAAA():
    print("1.) Business trip? Who do you work for?\n2.) Delta? Wait...DELTA #3489!?!?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("I just work for a tech company by South Beach in Miami.")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Can you please try and help me?")
        time.sleep(2)
        choiceAAAA()
    elif userinput == "2":
        time.sleep(1)
        print("oh...my....god.....YES!!!")
        time.sleep(1)
        print("YES! HOW DO YOU KNOW!?")
        time.sleep(2)
        choiceAAAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAAA()

def choiceAAAB():
    print("1.) It's all over the news!\n2.) There were supposed to be no survivors from that crash!")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAAAB()

def choiceAAAA():
    print("1.) Yes.\n2.) No.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAAAA()
        
    
def choiceAB():
    print("1.) Okay?\n2.) Well try and help me out here. What is around you?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...transmission lost...")
        time.sleep(1)
        print("GAME OVER")
    elif userinput == "2":
        time.sleep(1)
        print("Okay...well... palm trees.")
        time.sleep(1)
        print("I see...")
        time.sleep(1)
        print("A lot of palm trees.")
        time.sleep(2)
        choiceABB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceAB()

def choiceABB():
    print("1.) What type of palm tress?\n2.) Okay is there anything else? How big is the island?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...how the hell am I supposed to know that.")
        time.sleep(1)
        print("I am not a botanist.")
        time.sleep(2)
        choiceABBA()
    elif userinput == "2":
        time.sleep(1)
        print("Not really.")
        time.sleep(1)
        print("Have you ever seen the movie Castaway?")
        time.sleep(1)
        print("Well its prety much like that.")
        time.sleep(1)
        print("I'm on an island...")
        time.sleep(1)
        print("surrounded by water...")
        time.sleep(2)
        choiceABBB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceABB()

def choiceABBB():
    print("1.) Okay, okay Tom Hanks, lets get you and Wilson home.\n2.) This is going to be tough to find you.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceABBB()

def choiceBA():
    print("1.) What is happening?\n2.) Start from where you rememeber.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...I dont know.")
        time.sleep(1)
        print("I have been stranded on this island...")
        time.sleep(2)
        choiceBAA()
    elif userinput == "2":
        time.sleep(1)
        print("Okay well we were flying over the Atlantic when...")
        time.sleep(1)
        print("...the plane")
        time.sleep(1)
        print("the...plane just ripped in half!")
        time.sleep()
        choiceBAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBA()

def choiceBAB():
    print("1.) What do you mean ripped in half!?\n2.) How..what!?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("I mean literally ripped in half.")
        time.sleep(1)
        print("Listen...")
        time.sleep(1)
        print("I now this sounds crazy...")
        time.sleep(1)
        print("I need help. ASAP!")
        time.sleep(2)
        choiceBABA()
    elif userinput == "2":
        time.sleep(1)
        print("I dont exactly know whats happening...")
        time.sleep(1)
        print("I should have been dead by now.")
        time.sleep(2)
        choiceBABB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBAB()

def choiceBABB():
    print("1.) Do you have food?\n2.) Are you in any immediate danger?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBABB()

def choiceBABA():
    print("1.) Okay. You are right.\n2.) This is so crazy.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBABA()

def choiceBAA():
    print("1.) An Island. Whereabouts?\n2.) How long?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...I dont know.")
        time.sleep(1)
        print("I beleive I was somewhere over the North Atlantic before the accident.")
        time.sleep(2)
        choiceBAAA()
    elif userinput == "2":
        time.sleep(1)
        print("About 4 days...")
        time.sleep(1)
        print("...I think...")
        time.sleep(2)
        choiceBAAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBAA()

def choiceBAAB():
    print("1.) Wow. Do you have food?\n2.) Are there any others?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBAAB()

def choiceBAAA():
    print("1.) Okay..the accident?\n2.) The North Atlantic is very big...")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBAAA()
    
def choiceBB():
    print("1.) What exploded?\n2.) How are you alive!?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...The...")
        time.sleep(1)
        print("...The F@#%ING plane exploded!")
        time.sleep(1)
        print("I cant get any more clear than that!")
        time.sleep(2)
        choiceBBA()
    elif userinput == "2":
        time.sleep(1)
        print("Great question.")
        time.sleep(1)
        print("I have no idea.")
        time.sleep(2)
        choiceBBB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBB()

def choiceBBA():
    print("1.) Hey you need to calm down! I am only trying to help!\n2.) How are you alive?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...okay..okay..")
        time.sleep(1)
        print("...I'm sorry..")
        time.sleep(2)
        choiceBBAA()
    elif userinput == "2":
        time.sleep(1)
        print("I blacked out...")
        time.sleep(1)
        print("...I think...")
        time.sleep(1)
        print("I had this dream...")
        time.sleep(2)
        choiceBBAB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBA()

def choiceBBAB():
    print("1.) What was it about?\n2.) Are you hurt?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBAB()

def choiceBBAA():
    print("1.) Not cool!\n2.) Yeah. Thank you.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBAA()

def choiceBBB():
    print("1.) This makes no sense...\n2.) Are you hurt at all?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print("...I know.")
        time.sleep(1)
        print("I beleive there is some...")
        time.sleep(1)
        print("mystical stuff going on here man")
        time.sleep(2)
        choiceBBBA()
    elif userinput == "2":
        time.sleep(1)
        print("No that is what is so strange...")
        time.sleep(1)
        print("...people literally...")
        time.sleep(1)
        print(".....")
        time.sleep(1)
        print("blew up....")
        time.sleep(1)
        print("but somehow I don't even have a scratch.")
        time.sleep(2)
        choiceBBBB()
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBB()

def choiceBBBB():
    print("1.) *vomit*\n2.) This is not normal.")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBBB()

def choiceBBBA():
    print("1.) You're nuts...\n2.) Mystical stuff?")
    userinput = input("-->: ")
    if userinput == "1":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    elif userinput == "2":
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("To be continued")
    else:
        print("****PLEASE SELECT ONE OF THE TWO CHOICES****")
        choiceBBBA()
