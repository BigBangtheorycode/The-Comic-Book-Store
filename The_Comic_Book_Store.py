import time, sys, os
time_lost = 0
my_money = 10
inventory = 0
message = (r"""
 _____  _                ___                               
(_   _)( )              (  _`\                    _        
  | |  | |__     __     | ( (_)   _     ___ ___  (_)   ___ 
  | |  |  _ `\ /'__`\   | |  _  /'_`\ /' _ ` _ `\| | /'___)
  | |  | | | |(  ___/   | (_( )( (_) )| ( ) ( ) || |( (___ 
  (_)  (_) (_)`\____)   (____/'`\___/'(_) (_) (_)(_)`\____)                                                      
 ___                  _     
(  _`\               ( )    
| (_) )   _      _   | |/') 
|  _ <' /'_`\  /'_`\ | , <  
| (_) )( (_) )( (_) )| |\`\ 
(____/'`\___/'`\___/'(_) (_)                             
 ___    _                      
(  _`\ ( )_                    
| (_(_)| ,_)   _    _ __   __  
`\__ \ | |   /'_`\ ( '__)/'__`\
( )_) || |_ ( (_) )| |  (  ___/
`\____)`\__)`\___/'(_)  `\____)
""")
def anything(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
def start_game():
    global time_lost
    global my_money
    global inventory
    anything('Your name is Max, you’re an 11 year-old comic fan who has to spend way too much of his time \ndoing things other than reading comics… \nThis is your journey to..')
    time.sleep(1)
    print(message)
    time.sleep(3)
    anything('You have to get to The Comic Book Store within 60 minutes \nI might leave school early...')
    time.sleep(2)
    response = input('\nShould I sneak out the front, back way or do not leave school early at all[F/B/D]?>')
    if response.lower() == 'f':
        time_lost += 30
        anything('You got caught! Detention after school! \nYou lost {} minutes due to detention.'.format(time_lost))
    elif response.lower() == 'b':
        anything('YES!!! You got away with it!')
    elif response.lower() == 'd':
        anything('You stayed at school until the bell.')
        time_lost += 15
        anything('You need to hurry if you want to make it in time!')
    else:
        anything('Invalid character') 
        start_game()
start_game()
def take_bus():
    global time_lost
    global my_money
    anything('\nYou could walk and save the money, or get the bus and save time...')
    time.sleep(2)
    response = input('\nWalk or bus [W/B]?>')
    if response.lower() == 'w':
        time_lost += 10
        anything('You walk, this adds {} minutes to time behind schedule'.format(time_lost))
    elif response.lower() == 'b':
        my_money -= 5
        anything('You got the bus... for an extortionate 5 pounds! \nYou have {} pounds left '.format(my_money))
    else:
        anything('Invalid input')
        take_bus()
take_bus()
def home_():
    global time_lost
    global my_money
    time.sleep(2)
    anything('\nNow we are home, should we ask Mum or Dad for some money?')
    time.sleep(2)
    response = input('\nMum or dad? [M/D]?>')
    if response.lower() == 'm':
        time.sleep(2)
        anything('\nYour Mum asks you to do housework for 10 pounds extra pocket money')
        response = input('\nAre you going to do housework [Y/N]?>')
        if response.lower() == 'y':
            my_money += 20 
            time_lost -= 10
            time.sleep(2)
            anything('\nThis added 10 minutes to your journey... \nThis made you {} minutes behind schedule! \nYou now have {} pounds'.format(time_lost, my_money))
        elif response.lower() == 'n':
            time.sleep(2)
            my_money += 10
            anything('\nYou get 10 pounds pocket money')
        else:
            anything('\ninvalid input')
            home_()
    elif response.lower() == 'd':
        time.sleep(2)
        my_money += 10 
        anything('\nYou ask your dad and get your pocket money \nYou now have {} pounds'.format(my_money))
    else:
        anything('\nInvalid input')
home_()
def take_bike():
    global time_lost
    global my_money
    time.sleep(2)
    anything('\nWalking down the street, \nyou bump into your friend Bob, he has a bike you could borrow. \nTime is of the esscence! Will you walk into town or borrow his bike?')
    time.sleep(2)
    response = input('\nWalk or bike [W/B]?>')
    if response.lower() == 'w':
        time_lost += 10
        anything('You walk \nYou are {} minutes nehind schedule'.format(time_lost))
    elif response.lower() == 'b':
        time_lost -= 10 
        anything('You took the bike \nYou have {} pounds left '.format(my_money))
    else:
        anything('Invalid input')
take_bike()
def sweet_shop():
    global time_lost
    global my_money
    global inventory
    inventory = 0
    anything('\nYou are about to pass by the sweet shop... \nwill you stop to buy some sweets?')
    time.sleep(2)
    response = input('\nGo straight to comic shop or buy sweets [G/B]?>')
    if response.lower() == 'g':
        time_lost -= 5
        anything('\nYou hurry on {} minutes'.format(time_lost))
    elif response.lower() == 'b':
        anything('\nWhich sweets would you like?')
        time.sleep(2)
        response = input('\nKitkat, Haribo, Skittles [K/H/S]?>')
        if  response.lower() == 'k':
            anything('\nYou bought a Kitkat for 1 pound')
            my_money -= 5 
            inventory += 1
            anything('\nYou have {} pounds left \nyou are {} beind schedule {} item in inventory'.format(my_money, time_lost, inventory))
        elif response.lower() == 'h':
            anything('\nYou bought a bag of Haribo for 1 pound')
            my_money -= 1
            inventory += 1
            anything('\nYou have {} pounds left \nYou have {} item in inventory'.format(my_money, inventory))
        elif response.lower() == 's':
            anything('\nYou bought a bag of Skittles for 1 pound')
            my_money -= 1
            inventory += 1
            anything('\nYou have {} pounds left \nYou have {} item in inventory'.format(my_money, inventory))
        else:
            anything('\nInvalid input')
            sweet_shop()
sweet_shop()
def encounter_bully():
    global my_money
    global time_lost
    global inventory
    anything("\nJust outside the comic shop an older boy \njumps out in front of you and waves his fist menacingly...")
    time.sleep(2)
    anything("\nIf you don't buy him off he might beat you up!")
    time.sleep(2)
    response = input('\nMoney, Sweets, take a chance  [M/S/C]?>')
    if response.lower() == "c":
        time.sleep(2)
        time_lost += 5
        anything('\nThe bully beats you up. It takes you 5 minutes to get the wedgie out \nYou have now lost {} minutes in total'.format(time_lost))
    elif response.lower() == 's':
        time.sleep(2)
        inventory -= 1
        anything('\nHe takes your sweets and leaves you alone... \n Inventory has {} items in it'.format(inventory))
    elif response.lower() == 'm':
        time.sleep(2)
        my_money -= 10
        anything('\nHe takes 10 pounds from you \nYou {} pounds left')
            # Dollars used instead of Pounds because my machine doesn't like Pounds
    else:
        anything('\nInvalid Input')
        encounter_bully()  
encounter_bully()
def arrive_store():
    anything("\nFinally! You have arrived at the Comic Book Store!")
    time.sleep(2)
    if time_lost > 100:
        anything("\nUnfortunately, it is now closed. No comic for you.")
        time.sleep(2)
        print(message, '\n GAME OVER')
    elif my_money >= 20:
        anything("\nYou bought the No.1 Comic Book of All Time!")
        time.sleep(2)
        anything("\nWell done! This is the best possible result.")
        time.sleep(2)
        print(message, '\n GAME OVER')
    elif my_money >= 15:
        anything("\nYou bought a Spiderman comic!")
        time.sleep(2)
        anything("\nWell done! But maybe you could have done better.")
        time.sleep(2)
        print(message, '\n GAME OVER')
    elif my_money >= 10:
        anything("\nYou bought a Peppa Pig comic...")
        time.sleep(2)
        anything("\nMaybe you could give it to your little sister?")
        time.sleep(2)
        anything("\nSurely you could have done better.")
        time.sleep(2)
        print(message, '\n GAME OVER')
    else:
        anything("\nBut you don't have enough to buy anything.")
        time.sleep(2)
        anything("\nThat sucks, doesn't it?")
        print(message, '\n GAME OVER')
arrive_store()