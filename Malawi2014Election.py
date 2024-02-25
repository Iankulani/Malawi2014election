# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 02:31:52 2024

@author: IAN CARTER KULANI
"""

#This software prompts the user to enter total number of published centers, total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.

print("==============================MALAWI ELECTROL COMMISSION==============================\n") 

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered voters
TotalRegisteredvotes=int(input("Enter Total Registered Voters:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null and Void Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Valid Votes for Peter Wa Mutharika
Totavalidvotesfor_Petermutharika=int(input("Enter Total Valid Votes for Peter Wa Mutharika:"))
#Get Total Valid Votes for Dr Lazarus MacCarthy Chakwera
Totalvalidvotesfor_Lazaruschawera=int( input("Enter Total Valid Votes for Dr Lazarus MacCarthy Chakwera:"))
#Get Total Valid Votes for Joyce Banda
Totavalidvotesfor_Joycebanda=int(input("Enter Total Valid Votes for Joyce Banda:"))
#Get Total Valid Votes for Atupele Muluzi
Totalvalidvotesfor_Atupelemuluzi=int( input("Enter Total Valid Votes for Atupele Muluzi:"))
#Get  Total Valid Votes for Kamuzu Chibambo
Totavalidvotesfor_Kamuzuchibambo=int(input("Enter Total Valid Votes for Kamuzu Chibambo:"))
#Get Total Valid Votes for Mark Katsonga
Totalvalidvotesfor_Markkatsonga=int( input("Enter Total Valid Votes for Mark Katsonga:"))
#Get Total Valid Votes for John Chisi
Totavalidvotesfor_Johnchisi=int(input("Enter Total Valid Votes for John Chisi:"))
#Get Total Valid Votes for George Nnesa
Totalvalidvotesfor_Georgennesa=int( input("Enter Total Valid Votes for George Nnesa:"))
#Get Total Valid Votes for James Nyondo
Totavalidvotesfor_Jamesnyondo=int(input("Enter Total Valid Votes for James Nyondo:"))
#Get Total Valid Votes for Hellen Sighn
Totalvalidvotesfor_Hellensighn=int( input("Enter Total Valid Votes for Hellen Sighn:"))
#Get Total Valid Votes for Friday Jumbe
Totavalidvotesfor_Fridayjumbe=int(input("Enter Total Valid Votes for Friday Jumbe:"))
#Get Total Valid Votes for Davis Katsonga
Totalvalidvotesfor_Daviskatsonga=int( input("Enter Total Valid Votes for Davis Katsonga:"))
percent=100

if Totavalidvotesfor_Petermutharika>Totalvalidvotes/2+1:
   print("Congratulations Peter Wa Muthalika you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Lazaruschawera>Totalvalidvotes/2+1:
   print("Congratulations Dr Lazarus MacCarthy Chakwera you're the winner of 2014 presidentil Election")

elif Totavalidvotesfor_Joycebanda>Totalvalidvotes/2+1:
   print("Congratulations Joyce Banda you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Atupelemuluzi>Totalvalidvotes/2+1:
       print("Congratulations Atupele Muluzi you're the winner of 2014 presidentil Election")

elif Totavalidvotesfor_Kamuzuchibambo>Totalvalidvotes/2+1:
   print("Congratulations Kamuzu Chibambo you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Markkatsonga>Totalvalidvotes/2+1:
       print("Congratulations Mark Katsonga you're the winner of 2014 presidentil Election")

elif Totavalidvotesfor_Johnchisi>Totalvalidvotes/2+1:
   print("Congratulations John Chisi you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Georgennesa>Totalvalidvotes/2+1:
       print("Congratulations George Nnesa you're the winner of 2014 presidentil Election")


elif Totavalidvotesfor_Jamesnyondo>Totalvalidvotes/2+1:
   print("Congratulations James Nyondo you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Hellensighn>Totalvalidvotes/2+1:
   print("Congratulations Hellen Sighn you're the winner of 2014 presidentil Election")

elif Totavalidvotesfor_Fridayjumbe>Totalvalidvotes/2+1:
       print("Congratulations Friday Jumbe you're the winner of 2014 presidentil Election")

elif Totalvalidvotesfor_Daviskatsonga>Totalvalidvotes/2+1:
   print("Congratulations Davis Katsonga you're the winner of 2014 presidentil Election")

else:
    print("No majority winner was found RUNOF may be required Thank you.\n\n")

#Calculating Majority

print("_________________________________ELECTION STATISTICS_____________________________________\n")
majority_percent=Totavalidvotesfor_Petermutharika*percent/Totalvalidvotes;
print("Total Valid Votes for Peter Wa Mutharika in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Lazaruschawera*percent/Totalvalidvotes;
print("Total Valid Votes for Dr Lazarus MacCarthy Chakwera in percentage=",majority_percent)
majority_percent=Totavalidvotesfor_Joycebanda*percent/Totalvalidvotes;
print("Total Valid Votes for Joyce Banda in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Atupelemuluzi*percent/Totalvalidvotes;
print("Total Valid Votes for Atupele Muluzi in percentage=", majority_percent)
majority_percent=Totavalidvotesfor_Kamuzuchibambo*percent/Totalvalidvotes;
print("Total Valid Votes for Kamuzu Chibambo in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Markkatsonga*percent/Totalvalidvotes;
print("Total Valid Votes for Mark Katsongain percentage=",majority_percent)
majority_percent=Totavalidvotesfor_Johnchisi*percent/Totalvalidvotes;
print("Total Valid Votes for John Chisi in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Georgennesa*percent/Totalvalidvotes;
print("Total Valid Votes for George Nnesa in percentage=", majority_percent)
majority_percent=Totavalidvotesfor_Jamesnyondo*percent/Totalvalidvotes;
print("Total Valid Votes for James Nyondo in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Hellensighn*percent/Totalvalidvotes;
print("Total Valid Votes for Hellen Sighn in percentage=",majority_percent)
majority_percent=Totavalidvotesfor_Fridayjumbe*percent/Totalvalidvotes;
print("Total Valid Votes for Friday Jumbe in percentage=",majority_percent)
majority_percent=Totalvalidvotesfor_Daviskatsonga*percent/Totalvalidvotes;
print("Total Valid Votes for Davis Katsonga in percentage=",majority_percent)


print("==========================================================================================\n") 