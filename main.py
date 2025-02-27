import time

while(1 == 1):
    inputfile = open("input.txt", "r")
    accountfile = open("account.txt", "a")

    if(inputfile.read(1) != ''):
        inputfile.seek(0)
        ilines = inputfile.readlines()
        number = len(ilines[0].split(','))

        print(ilines[0] +"\n")

        if(number == 4):
            accountfile.close()
            accountfile = open("account.txt", "r")
            thing = ilines[0].split(",", 2)
            concat = thing[0].strip('\x00') + "," + thing[1].strip('\x00')
            found = accountfile.read().find(concat)
            if(found == -1):
                print("Account not found!")
            else:
                print("Account found! Adding principle!")
                principlefile = open("principle.txt", "a")
                principlefile.write(ilines[0].strip('\x00') + "\n")
                principlefile.flush()
        
        if(number == 3):
            accountfile.write(ilines[0] + "\n")
            accountfile.flush()
            print("Account created!")

        if(number == 2):
            accountfile.close()
            accountfile = open("account.txt", "r")
            found = accountfile.read().find(ilines[0].strip().strip('\x00'))
            if(found == -1):
                print("Account not found!")
            else:
                print("Account found!")
            

        inputfile.close()
        time.sleep(1)
        inputfile = open("input.txt", "w")
        inputfile.close()
