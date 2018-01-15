import random
import os as matrix

from platform import system

#colors
R = "\033[31m" #red
G = "\033[32m" #green
W = "\033[0m" #Normal

#command line...
if system() == 'Linux' :
    clear = "clear"
elif system() == 'Windows' :
    clear = "cls"
play_again = "python remember-me.py"

#start...    
print("""

██████╗ ███████╗███╗   ███╗███████╗███╗   ███╗██████╗ ███████╗██████╗     ███╗   ███╗███████╗
██╔══██╗██╔════╝████╗ ████║██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗    ████╗ ████║██╔════╝
██████╔╝█████╗  ██╔████╔██║█████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝    ██╔████╔██║█████╗  
██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══╝  
██║  ██║███████╗██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝
                                                                                             
  Programmed by https://www.instagram.com/laser01/  Version 0.0.1
  to help read README.md
  
""")

Continue = input('Enter to continue...')
matrix.system( "{}".format(clear))

#Choose the level...
level = 1 #input('Enter level : ')  #I have problem here!

#Lists for every level...
if level == 1 :
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
elif level == 2 :
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
elif level == 3 :
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
elif level == 4 :
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
elif level == 5 :
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41']

#New list...
list2 = []

def main():
    try:
        for _ in range(99) : #Number in range not important .
            #Choose random number .
            secure_random = random.SystemRandom()
            random_num = (secure_random.choice(list1))
            num = input('{} : '.format(random_num)) #Enter number .
            if num == random_num : #If num like random_num...
                print("\n\n[LOST] You lost the game :(")
                again = input('Enter to play again...')
                matrix.system( "{}".format(play_again)) #Play again...
            elif num != random_num : #If num not like random_num...
                if num in list2 : #If num in list2...
                    print("\n\n[LOST] You lost the game :(")
                    again = input('Enter to play again...')
                    matrix.system( "{}".format(play_again))
                elif num not in list2 : #If num not in list2...
                    list2.append(num) #Add num value in list2...
                    list2.append(random_num) #Add random_num value in list2...
                    list1.remove(num) #Delete num value in list1...
                    list1.remove(random_num) #Delete random_num value in list1...
                    matrix.system( "{}".format(clear))
    except IndexError:  #Winner         
        print(G+"\n\n[WINNER] You winner in level {} !".format(level)+W)
    except ValueError: #Enter error value
        print(R+"\n\n[ERROR] This game just numbers in range nothing else!"+W)
        again = input('Enter to play again...')
        matrix.system( "{}".format(play_again))
        
if __name__ == '__main__' :
    main()
