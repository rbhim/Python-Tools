#1=============================================================================
# When below is run it open and prints all countries
# Prolem is that Python insert a new line character and give a space
'''
f = open("Countries.txt", "r")

for line in f:
    print(line)
    
f.close()
'''

#2==============================================================================

# Below is one where you fix the new line issue
'''
f = open("Countries.txt", "r")

for line in f:
    line = line.strip()
    print(line)
    
f.close()
'''

#3==============================================================================

# Now we read and build up a list from the file.
'''
f = open("Countries.txt", "r")

countries = [] #Starting with Empty list

for line in f:
    line = line.strip()
    countries.append(line)
    
f.close()

print(countries)# print list
print len(countries) # print out the numer of lines in list
'''
#4==============================================================================

# Now we read and build up a list from the file but only select specific ones
'''
f = open("Countries.txt", "r")

countries = [] #Starting with Empty list

for line in f:
    line = line.strip()
    countries.append(line)
    
f.close()

print(countries)# print list
print len(countries) # print out the numer of lines in list

for i in countries: # here we iterate over the list and only select 
    if i[0] == "T":
        print(i)
'''
#5==============================================================================

# Now we write data to files
'''
f = open("scores.txt", "w")#note we use mode w as we are now writing data

while True:
    Name = raw_input("What is your name?> ")
    """Use a break method to quit while loop if some type 'quit'. If no,
    then it continues to ask for score and continue until quit is called."""    
    if Name == "quit":
        print("Quitting...")
        break
    Score = raw_input("Score for " + Name + "> " )
    """method to write to text file. Note that we are created a comma separate
    with a new line"""
    f.write(Name + "," + Score + "\n") 

f.close()
'''
#6==============================================================================

# now reading what we just created from score.txt
"""
f = open("scores.txt", "r")

for line in f:
    '''Produce a list of item on each side of comma.
    Notice how two methods are chained together to br run one after the other.
    The line.strip() removes the new line character and then split() method
    separate the text into two elemtns of the list...that is between comma'''
    print (line.strip().split(",")) #produce a list of item on each side of comma.
"""
#7==============================================================================

# Same as above but now we insert into empth dictionary.
"""
f = open("scores.txt", "r")

name = {} #empty dictionaty which we will populate as we look fore score.txt

for line in f:
    '''Produce a list of item on each side of comma.
    Notice how two methods are chained together to br run one after the other.
    The line.strip() removes the new line character and then split() method
    separate the text into two elemtns of the list...that is between comma'''
    entry = (line.strip().split(",")) #produce a list of item on each side of comma.
    Name = entry[0] #assign first item in list to Name variable
    Score = entry[1] #assign second item in list to Score variable
    name[Name] = Score #assign to empy dictionary where key is Name and value is score
    print (Name + ":" + Score)
        
f.close()

print(name)
"""
        

