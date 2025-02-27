import time

inputfile = open("input.txt", "w")

inputfile.write("Dan, password, bio") #account creation
inputfile.flush()
time.sleep(3) 

inputfile.truncate(0)
inputfile.write("Dan, password") #account login
inputfile.flush()
time.sleep(3)

inputfile.truncate(0)
inputfile.write("Ben, asdasd") #login fail
inputfile.flush()
time.sleep(3)

inputfile.truncate(0)
inputfile.write("Dan, password, Newtons, Every action") #save principle
inputfile.flush()
time.sleep(3)

inputfile.truncate(0)
inputfile.write("Ben, asdasd, Newtons, Every action") #save principle fail
inputfile.flush()
time.sleep(3)
