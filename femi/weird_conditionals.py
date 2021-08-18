user_input=int(input())

if user_input%2!=0:
    print("Weird")
elif user_input%2==0 and user_input>1 and user_input<=5:
    print("Not weird")
elif user_input%2==0 and user_input>5 and user_input<21:
    print("Weird")
elif user_input%2==0 and user_input>20:
    print("Not weird")
        
        

    
