#Cards by Alex Huang
import random
import re

def main(): 
    valid_choice = False
    while valid_choice == False:
        print ("---------")
        print ("Main Menu")
        print ("---------")
        print ("Card Game")
        print ("1. Sign up <1>")
        print ("2. Log in <2>")
        print ("3. Quit Game <3>")
        choice = int(input())
        print ("---------")
        
        if choice == 1:
            valid_sign_up = sign_up ("", "")
            if valid_sign_up == 0:
                print ("User created successfully")
                #valid_choice = True
            elif valid_sign_up == 1:
                print ("Sign up cancelled")

        elif choice == 2:
            player1 = ""
            player2 = ""
            # Player 1 login
            player1 = player_login(1, "")
            #print (player1)
            player2 = player_login(2, player1)
            #print (player2)
            iPlayGame = 1
            while iPlayGame == 1:
                print ("Game beginning...")
                gameResult = play_game(player1, player2)
                #print (gameResult)
                record_result(gameResult[0], gameResult[1])
                print ("Top 5 Highscores are: ")
                print (display_topScores())
                userInput = int(input ("Do you want to play again? <1> for Yes <0> for No: "))
                if userInput == 1:
                    iPlayGame = 1
                else:
                    iPlayGame = 0
        elif choice == 3:
            print ("Game finished, goodbye")
            exit()
        
        else:
            print ("Error, please input a valid choice <1> or <2> or <3>")
            valid_choice = False

#Function to read user information from the text file
def read_user_info():
    credentials_found = False

    listUserInfo = list() # Puts the read material into this list
    Counter = 0 

    file = open ("UserData.txt", "r") # Opens the files and reads the contents
    for line in file: # Reading through the document line by line
        Counter = Counter + 1
        sCurrentLine = line.strip('\n') # To only focus on a specific line in the text document
        listUserInfo.append(sCurrentLine.split(":")) # Adds the name and password into a list with the name and password split
    
    file.close()
    return listUserInfo

# Generates a unique position for the cards
def random_number_array():
    arrCardPos = []
    for i in range(30): # Goes through 30 numbers to give to cards as a position in the deck
        ExitLoop = False 
        while not ExitLoop: 
            ExitLoop = True 
            CurrPos = random.randint(1,30) # Gives the current card a random number (position) between one and thirty
            for j in range (i): 
                if CurrPos == arrCardPos[j]: # Decides whether the current position already exists in the array
                    ExitLoop = False # If a value exists, it loops again to give a different position value
        arrCardPos.append(CurrPos) # Adds a unique number from one to thirty to the array
    return arrCardPos

def card_name_array():
    arrCardName = ["B:01","B:02","B:03","B:04","B:05","B:06","B:07","B:08","B:09","B:10","R:01","R:02","R:03","R:04","R:05","R:06","R:07","R:08","R:09","R:10","Y:01","Y:02","Y:03","Y:04","Y:05","Y:06","Y:07","Y:08","Y:09","Y:10"]
    return arrCardName
    
def shuffle_cards():
    arrCardP = random_number_array() # Calls random_number_array to give cards positions
    arrCardN = card_name_array() # Calls card_name_array to give card the value and colour
    arrCards = list() 
    for i in range (30):
        arrCards.append ([arrCardN[i], arrCardP[i]]) # Creates a 2D-array with the first being the colour and value. The second being the number or position
    return insertion_sort(arrCards)
    
def insertion_sort(arr):
    #print (len(arr)) # Finds the length of the array
    for x in range (1,len(arr)):
        y = x
        while arr[y - 1][1] > arr[y][1] and y > 0: # While the number on the left is larger than the current number and larger than 0. Since this is a 2D-array, I needed to display both values
            arr[y - 1][0], arr[y][0] = arr[y][0], arr[y - 1][0] # Swaps arr[y - 1][0] with arr[y][0] and vice versa
            arr[y - 1][1], arr[y][1] = arr[y][1], arr[y - 1][1] # This also had to be swapped since this is a 2D-array
            y -= 1 # Moves the value
    return arr

def verify_pwd(sPwd):
    # Allowed characters 0-9, A-Z and a-z. Also allows '<' '>' '=' '?' '@' '!'. [0-9a-zA-Z+\<\>\?\@\!\=]
    # Minimun length 6 characters
    # At least one capital letter, one digit and one special character [A-Z], [0-9], [\<\>\?\@\!\=]
    # Starts as a letter
    sRegPatt1 = "^[a-zA-Z][A-Z0-9a-z\=\<\>\?\@\!]+[A-Z0-9a-z\=\<\>\?\@\!]$"
    sRegPatt2 = "[A-Z]"
    sRegPatt3 = "[0-9]"
    sRegPatt4 = "[\=\<\>\?\@\!]"
    iPwdLen = len(sPwd)
    if iPwdLen < 6:
        return 3 #Error, minimun password requires 6 characters. Please try again
    else:
        match1 = re.search(sRegPatt1, sPwd)
        if match1 is None:
            return 2 #Error, disallowed characters. Please try again
        else:
            match2 = re.search(sRegPatt2, sPwd)
            match3 = re.search(sRegPatt3, sPwd)
            match4 = re.search(sRegPatt4, sPwd)
            if match2 is None or match3 is None or match4 is None:
                return 1 #"Error, you need at least one capital letter, one digit and one special character(<, >, =, ?, @, !). Please try again"
            else:
                return 0 #"Valid Password"

def pwd_encoding(password_en):
    encryptPwd = "" # Gives encryptPwd an empty variable
    ascii_array_en = [] # Creates an array to put characters into
    for i in range(len(password_en)): # Loops in range of the total letters in the password
        ascii_array_en.append (chr(ord(password_en[i]) + 3)) # Finds the ASCII values of the letters ands adds 3 ASCII values onto the letter and then appends it to the list
    for x in range(len(ascii_array_en)): 
        encryptPwd = encryptPwd + ascii_array_en[x] # The empty variable then adds all the individual characters back together into one string
    return(encryptPwd)

def pwd_decoding(password_de): # Same principal as encoding but take away 3 to decode it back to origial value
    decryptPwd = ""
    ascii_array_de = []
    for i in range(len(password_de)):
        ascii_array_de.append (chr(ord(password_de[i]) - 3))
    for x in range(len(ascii_array_de)):
        decryptPwd = decryptPwd + ascii_array_de[x]
    return(decryptPwd)

def sign_up(plyname,plypassword):
    user_exist = False
    exit_loop1 = False
    while exit_loop1 == False:
        if plyname == "":
            print ("Please enter a username or enter <quit> to cancel the signup")
            user_exist = False
            plyname = input()
            if plyname == "quit":
                return 1 # Goes back to the Main Menu
        if check_user(plyname):
            user_exist = True  
        if user_exist == True:
            print ("The username",plyname,"already exists")
            plyname = ""
            exit_loop1 = False # Asks the user to sign up again
        else:
            exit_loop1 = True # Sign up name was successful - didn't have a replicate in file
    
    exit_loop2 = False
    while exit_loop2 == False:
        print ("Please enter a password for",plyname, "(It must start as a letter, have at least one capital letter, one digit and one special character ('<' '>' '=' '?' '@' '!') and be at least 6 characters)")
        plypassword = input()
        is_pwd_valid = verify_pwd(plypassword)
       
        if is_pwd_valid == 0: # Means it is valid
            file = open ("UserData.txt", "a")
            file.write (plyname + ":" + pwd_encoding(plypassword) + "\n") # Possible error checking later
            file.close()
            exit_loop2 = True # Stops needing to ask for password as it is valid
            return 0 #User has been added added successfully
        elif is_pwd_valid == 1:
            print ("Error, you need at least one capital letter, one digit and one special character(<, >, =, ?, @, !). Please try again")
        elif is_pwd_valid == 2:
            print ("Error, disallowed characters. Please try again")
        elif is_pwd_valid == 3:
            print ("Error, minimun password requires 6 characters. Please try again")
    
def check_user(username): # Checks if username already exists in the file 
    currUsers = read_user_info()
    userFound = 0
    for user in currUsers:
        if username == user[0]:
            userFound = 1
    if userFound == 0:
        return 0
    else:
        return 1

def check_user_pwd(pwd):
    currUsers = read_user_info()
    pwdFound = 0
    for user in currUsers:
        if pwd == pwd_decoding(user[1]):
            pwdFound = 1 
    if pwdFound == 0:
        return 0
    else:
        return 1


def player_login(pNo, currPly):  
    exit_loop3 = False
    while exit_loop3 == False:
        player = input ("Player " + str(pNo) + " please enter username: ")
        if player == "":
            print ("Please enter a username") # Didn't input anything
            exit_loop3 = False
        elif player == currPly: 
            print ("Player " + player + " already logged in, please login in as a different user") 
            exit_loop3 = False # Asks the user to re-enter different login credentials
        elif check_user(player):
            exit_loop3 = True # User does not exist - leaves the loop of deciding whether user is existing/entered
            exit_loop4 = 0
            while exit_loop4 < 4:
                playerPwd = input("Please enter your password: ")       
                if check_user_pwd(playerPwd):
                    print ("Player " + player + " successfully logged in")
                    exit_loop4 = 4 
                else:
                    print ("Password is incorrect, please try again (Maximum 4 tries)")
                    exit_loop4 += 1 # Gives player, 4 tries to enter password
                    if exit_loop4 == 4:
                        print ("Maximum tries reached, returning to login menu...")
                        exit_loop3 = False
        
        else:
            print ("The user, " + player + " does not exist, do you want to try again <1>? Or would you like to add this user <2>?")
            choice2 = int(input("Your choice?: "))
            if choice2 == 1:
                exit_loop3 = False # Exits player login menu
            elif choice2 == 2:
                sign_up(player,"") # Stores the current username for the sign_up and asks for the password to be inputted in the sign_up function
                exit_loop3 = True
                print ("Player, " + player + " ,successfully logged in")
        
    return (player)

def play_game(p1,p2):
    arrCurrCards = shuffle_cards()
    #print (arrCurrCards)
    ply1cards = list()
    ply2cards = list()
    arrResult = list()
    for i in range (15):
        print ("----------")
        print ("Round " + str(i+1) + ":")
        print ("----------")
        input (p1 + " please press <return> to take a card ")
        p1card = arrCurrCards[2*i][0] # 2n - player 1 will always take the even numbers
        print("Card " + p1card)
        input (p2 + " please press <return> to take a card ")
        p2card = arrCurrCards[2*i + 1][0] # 2n+1 - player 2 will always take the odd numbers
        print("Card " + p2card)
        arrP1card = p1card.split(":") # splits the card into the colour (letter) and number (size)
        arrP2card = p2card.split(":")
        if arrP1card[0] == arrP2card[0]: # If the colours are the same. compare the numbers
            if int(arrP1card[1]) > int(arrP2card[1]): 
                print ("----------")
                print (p1 + " wins this round!")
                ply1cards.append(p1card)
                ply1cards.append(p2card)
            else:
                print ("----------")
                print (p2 + " wins this round!")
                ply2cards.append(p1card)
                ply2cards.append(p2card)
        elif (arrP1card[0] == "R" and arrP2card[0] == "B") or (arrP1card[0] == "Y" and arrP2card[0] == "R") or (arrP1card[0] == "B" and arrP2card[0] == "Y"): # Player 1 only has three winning possibilities 
            print ("----------")
            print (p1 + " wins this round!")
            ply1cards.append(p1card)
            ply1cards.append(p2card)
        else: # Player 2 would have the rest of the winning probablities
            print ("----------")
            print (p2 + " wins this round!")
            ply2cards.append(p1card)
            ply2cards.append(p2card)  
        
    p1score = len(ply1cards)
    p2score = len(ply2cards)
    if p1score > p2score:
        arrResult.append(p1)
        arrResult.append(p1score)
        print ("----------")
        print (p1 + " wins the game!")
        print ("----------")
        print (p1 + " you have the following cards: ")
        print (ply1cards)
        #win = 1
        #print (p2 + " you have the following cards: ")
        #print (ply2cards)
    else:
        arrResult.append(p2)
        arrResult.append(p2score)
        print ("----------")
        print (p2 + " wins the game!")
        print ("----------")
        print (p2 + " you have the following cards: ")
        print (ply2cards)
        #win = 2
        #print (p1 + " you have the following cards: ")
        #print (ply1cards)
    #print (win)
    return arrResult
        
        #print (i)
        
def record_result(pName, noCards):
    file = open ("ResultLogs.txt", "a+")
    file.write (pName + "," + str(noCards))
    file.write ("\n")

def display_topScores():
    file = open ("ResultLogs.txt", "r")
    allScores = list() 
    allScoresSorted = list()
    top5Scores = ""
    Counter = 0 
    #Same principal as read_user_info function
    for line in file: 
        Counter = Counter + 1
        sCurrentLine = line.strip('\n') 
        allScores.append(sCurrentLine.split(",")) # Put all the material read into a list
    file.close()
    allScoresSorted = insertion_sort(allScores) # Makes the number of cards players won with in ascending order
    totalGameCount = len(allScoresSorted)
    #print (allScoresSorted)
    for i in range (1,6): # Puts the number of cards won in descending order and only displays top 5
        #print (totalGameCount - i)
        #top5Scores.append([allScoresSorted[totalGameCount - i][0], allScoresSorted[totalGameCount - i][1]])
        top5Scores = top5Scores + allScoresSorted[totalGameCount - i][0] + ": " +  allScoresSorted[totalGameCount - i][1] + "\n"
    return top5Scores
    #return allScores

if __name__ == "__main__":
    main()
