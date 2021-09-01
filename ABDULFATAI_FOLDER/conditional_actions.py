n = input("Enter an integer number:")

n_int = int(n)
if n_int  % 2 > 0:
    print("Weird")
    if n_int % 2 == 0 and n_int < 2  and n_int <= 5:
        print("Not weird") 
        if n_int % 2 == 0 and n_int < 6 and n_int > 20:
            print("Weird")
            if n_int % 2 == 0 and n_int > 20:
                print("Weird")
