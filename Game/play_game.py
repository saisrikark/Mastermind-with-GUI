from check_compare_return import *
import sys
sys.path.append('C:/Users/Srikar/Desktop/withgraphics')
#from frontEnd import *
    
def play_game(rand_patt):
    turns=9
    outcome=0
    while(turns>=0):
        flag=0
        print("\nYou have ",turns+1," turns")
        user_patt=input("Enter your pattern :").split()
        check_patt=check_compare(user_patt,rand_patt)
        check_patt.sort()
        print("Your referecnce is:",check_patt)
        for i in check_patt:
            if(not i=='r'):
                flag=1
        if(flag==1):
            print("\nNot identical pattern")
            print("Try again")
            turns-=1
        else:
            print("\nIdentical patterns")
            print("You have won")
            print("You had ",turns," turns left")
            outcome=1
            break
    if(outcome==0):
        print("\nSorry you have spent all your turns")
        print("Enter 1 to try again or 0 to exit")
        sys.exit(0)

    name=input("Please Enter Your Name :")
    f=open("C:/Users/Srikar/Desktop/withgraphics/User.txt","a")
    f.write(name+" "+str(turns)+"\n")
    print("Data Stored")
    f.close()
