#Name:Nikhil Braganza
#Student_ID:29977770
#Start_Date: 4_Aug_2018
#Last_Modified: 5_Aug_2018
#               9_Aug_2018
#               14_Aug_2018
#Version 1.0.0


#accepting player names
print ("welcome to combat simulator")
p1=input("Player one, please enter your name: ")


#initialising variables
p1_army=[]
p2_army=[]
p1_money=10 #setting default money for players
p2_money=10

Winner=""

#creating dictionary for index number and troops
index_number=["1","2","3"]
troop_name=["archer","soldier","knight"]
zipped_list= zip (index_number,troop_name)
dictionary= dict (zipped_list)

#display menu
print("List of troops:       cost\n 1.Archer              $1\n 2.Soldier             $1\n 3.Knight              $1\n 4.Exit") 


#selection of troops (player 1)
while p1_money>=1:
    print (p1,"has $",p1_money,"left")
    p1_army.append(input("select your troops: "))
    
    if p1_army[-1]=="1" or p1_army[-1]=="2" or p1_army[-1]=="3":
        
        p1_money=p1_money-1
        print ("\n current selected army: ")
        for items in p1_army :
            print(dictionary[items])
    elif p1_army[-1]=="":
        print ("please select troops")
        p1_army.remove("")
        
    elif p1_army[-1]=="4":
        p1_army.remove("4")
        break
    else:
        print("please select a valid troop!!")
        del p1_army[-1]

p2=input("Player two, please enter your name: ")
#selection of troops (player 2)
while p2_money >= 1:
    print (p2 ,"has $",p2_money,"left")
    p2_army.append(input("select your troops: "))
    
    if p2_army[-1]=="1" or p2_army[-1]=="2" or p2_army[-1]=="3":
        p2_money=p2_money-1
        print ("\n current selected army: ")
        for items in p2_army :
            print(dictionary[items])
    elif p2_army[-1]=="":
        print ("please select troops")
        p2_army.remove("")
    elif p2_army[-1]=="4":
        p2_army.remove("4")
        break
    else:
        print("please select a valid troop!!")
        del p1_army[-1]

#Fight scenarios        
while len (p1_army) >=1 and len(p2_army)>=1:
    #player 1 winning scenarios
    if p1_army[0]=="1" and p2_army[0]=="2":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n", dictionary[p1_army[0]],"wins\n")
        Winner="p1"
    elif p1_army[0]=="2" and p2_army[0]=="3":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n", dictionary[p1_army[0]],"wins\n")
        Winner="p1"
    elif p1_army[0]=="3" and p2_army[0]=="1":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n", dictionary[p1_army[0]],"wins\n")
        Winner="p1"
        
#player 2 winning scenarios    
    elif p1_army[0]=="2" and p2_army[0]=="1":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n" ,dictionary[p2_army[0]], "wins")
        Winner="p2"
    elif p1_army[0]=="3" and p2_army[0]=="2":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n" ,dictionary[p2_army[0]], "wins")
        Winner="p2"
    elif p1_army[0]=="1" and p2_army[0]=="3":
        print (dictionary[p1_army[0]],"vs",dictionary[p2_army[0]],"\n" ,dictionary[p2_army[0]], "wins")
        Winner="p2"

    elif (p1_army[0]== p2_army[0]):
        print("same opponents, its a draw")
        
#Draw scenarios      
    else:
        print("no selection")
        


    if Winner=="p1":
        del p2_army[0]      
    elif Winner=="p2":
        del p1_army[0]   
    else:
        del p2_army[0]
        del p1_army[0]
    if len(p1_army)==0 or len(p2_army)==0:
        break

    
#Declaring winner
if (Winner=="p1") or (len(p1_army)>=1 and len(p2_army)==0):
    print("FINAL RESULT:\ncongratulations",p1,"you won!")
elif (Winner=="p2") or (len(p1_army)==0 and len(p2_army)>=1):
    print("FINAL RESULT:\ncongratulations",p2,"you won!")
else:
    print ("FINAL RESULT: \n its a draw")
      

