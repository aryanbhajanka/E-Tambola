import random 
import time
nl=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
nd=[]
al=[]
print("Welcome to E-Tambola By Aryan Bhajanka!\n")
time.sleep(2)
print("Following are the winning criteria:\n- Four corners\n- 1st Row\n- 2nd Row\n- 3rd Row\n- Full House 1\n- Full House 2\n")
print("Following are the game instruction for the host:\n- Hit enter to shuffle numbers\n- Type 1 for 1st Row\n- Type 2 for second row\n- Type 3 for 3rd row\n-Type 4 for 4 corners\n- Type h1 for 1st Full House\n- Type h2 for 2nd Full House\n- Press Ctrl + F to find numbers\n")
x=input("Press 'x' and enter to continue  ")
if (x=="x"):
    print("\nWohooo! Let's Start The Game\n")
    time.sleep(3)
    for i in range (91):
        n = random.choice(nl)
        nd.append(n)
        print("     ",n,"\n")
        print("Numbers Done:",nd,"\n")
        print("Criterias Done:",al,"\n\n")
        nl.remove(n)
        a=input()
        if (a=="1"):
            a1=input("Did someone get the 1st row? y/n  ")
            if(a1=="y"):
                al.append("1st Row")
                print("Great!\n")
                time.sleep(2)
            elif(a1=="n"):
                pass
        elif (a=="2"):
            a1=input("Did someone get the 2nd row? y/n  ")
            if(a1=="y"):
                al.append("2nd Row")
                print("Nice!\n")
                time.sleep(2)
            elif(a1=="n"):
                pass
        elif (a=="3"):
            a1=input("Did someone get the 3rd row? y/n  ")
            if(a1=="y"):
                al.append("3nd Row")
                print("Cool!\n")
                time.sleep(2)
            elif(a1=="n"):
                pass
        elif (a=="4"):
            a1=input("Did someone get the four corners? y/n  ")
            if(a1=="y"):
                al.append("4 corners")
                print("Nice!\n")
                time.sleep(2)
            elif(a1=="n"):
                pass
        elif (a=="h1"):
            a1=input("Did someone get the Full House? y/n  ")
            if(a1=="y"):
                al.append("1st Full House")
                print("Woah!\n")
                time.sleep(2)
            elif(a1=="n"):
                pass
        elif (a=="h2"):
            a1=input("Did someone get the 2nd Full House? y/n  ")
            if(a1=="y"):
                al.append("2nd Full House")
                print("Woah!\n")
                time.sleep(1)
                print("Alrighty Then...Guess the game's over.\nCongratualtions To The Winners!!!")
                break 
            elif(a1=="n"):
                pass
        elif (a==""):
            print("Shuffling!\n\n")
            time.sleep(2)
    print("GAME OVER")
    while True:
        input()
            
