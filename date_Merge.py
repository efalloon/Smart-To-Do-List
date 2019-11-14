# Name: date_Merge.py
# By: Euan Traynor
# Date: 13/05/19
# Version: 1.2.3

from datetime import date
today = date.today() #gets date from computer database
date = today.strftime("%m/%d") #sets structure/ look of date format

# This creates function which can be recalled later (or specific elements can be recalled)
def mergeSort(family_List): # import family_List from bottom of code which is not defined in the function
    #print("Splitting ",family_List) # to show viewer the process on the terminal line. #the first time it will print the whole list
    if len(family_List)>1: #identifies how many objects are in the list and if greater then one, it will do the following code.
        mid = len(family_List)//2 #identifies number of objects in list and then uses pythons own version of interger division which identifies how many numbers are on left or right of middle number/s.
        lefthalf = family_List[:mid] # variable defines left side of the middle
        righthalf = family_List[mid:] # variable defines right side of the middle

        mergeSort(lefthalf) # tells function to recall lefthalf and operates it.
        mergeSort(righthalf) # tells function to recall righthalf and operates it.

        #these values will be recalled later to make sure that the code (if statements) will eventially end
        valueI=0
        valueX=0
        valueY=0

        while valueX < len(lefthalf) and valueY < len(righthalf): # if values X and Y are less than length of family_List lefthalf and righthalf, do the following code
            if lefthalf[valueX] < righthalf[valueY]: # check if lefthalf is smaller than right (append valueX to store the new half of the main list/array). 
                family_List[valueI]=lefthalf[valueX] # If smaller, split list into two lists.
                valueX = valueX + 1 # add one to value X in order to eventially stop the loop
            else: # if it is not smaller, it will split the right half into two
                family_List[valueI]=righthalf[valueY]
                valueY = valueY + 1 # add one to value Y in order to eventially stop the loop
            valueI = valueI + 1 # and 1 to value I to eventially stop the while loop

        while valueX < len(lefthalf): # once new arrays have been made, start to split them.
            family_List[valueI]=lefthalf[valueX]
            valueX = valueX + 1
            valueI = valueI + 1

        while valueY < len(righthalf):
            family_List[valueI]=righthalf[valueY]
            valueY = valueY + 1
            valueI = valueI + 1
    #print("Merging ",family_List) # once completed merege the lefthalf and righthalf together
    # once all values are equal to length of family_List, finish

#tells user that program has started without any errors in the Merge sort
print("START")
family_List = []

def startMerge(family_List):
    #input to choose what function you would like to run
    choice = int(input("\nAdd TO DO item [1]\nRemove TO DO item [2]\nManual Merge [3]\nList Objects [4]\nExit [5]\nChoice: "))
    #if the choice is equal to the following digit, it will do the following
    if choice == 1:
        times(theEND)
    if choice == 2:
        remove()
    if choice == 3:
        mergeEND(family_List, date)
    if choice == 4:
        mergeEND(family_List, date)
    elif choice == 5:
        exit()
    else:
        print("NOT valid ../")
        startMerge(family_List)

def mergeEND(family_List, date):
    #saves information to data document to allow merge algorithm to access values of Objects later.
    output = open("./dates.txt", "r") # open this document
    
    lines = output.readlines() #Identifies and reads the lines which is store in variable lines
    for i in range(len(lines)): #identifies how many objects are in document accroding to each line
        lines[i]=lines[i].replace('\n','') # creates a list to store values which will be merged later.
    output.close() # close document in case of error.

    #writes lines on data document with a new line per each object
    with open("./dates.txt", "w") as output:
        #for item in alist:
        #    output.write("%s\n" % item)
        output.writelines("%s\n" % num for num in lines)

    nums = []

    #adding items in data document to list
    with open('./dates.txt', 'r') as filehandle:  
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            lines = line[:-1]

            # add item to the list
            nums.append(lines)
        family_List = nums

    #print final copy of list and restart main menu
    output.close()
    end(family_List)
    # if choice == 3:
    #    end(family_List)
    # if choice == 4:
    #     cleanList(family_List)
    # else:
    #     print("Error \n- Reloading data")
    #     mergeEND(family_List, date, choice)
        

def end(family_List):
    newAdd = date + " {(TODAY)}"
    family_List.append(newAdd)
    index = family_List.index(newAdd) - 1
    # listLen = len(family_List)
    # index = (listLen - index)
    if newAdd in family_List:
        print("\n | Current Date: " + date)
        print(" | Pos:",  index)
        
        print("\nOriginal Array:")
        #starts merge algorithm
        mergeSort(family_List)
        print(family_List)
        print("\nNew Array:")
        mid = index
        lefthalf = family_List[:mid]
        righthalf = family_List[mid:]
        finalDates = righthalf + lefthalf
        index = finalDates.index(newAdd)
        finalDates.pop(index)
        print(finalDates)
        startMerge(family_List)
    else:
        print("Error\n - Reloading")
        startMerge(family_List)

#convert the list into string
def convert(theEND):
    # initialization of string to "" 
    newEND = "" 
    # traverse in the string  
    for x in theEND: 
        newEND += x  + "\n"
    # return string
    return newEND

def times(theEND):
    #set score at begining to zero
    total = 0
    #gets name of new To Do
    nameList = []
    name = input("\nNAME (no numbers or symbols): ")
    nameList.append(name)

    #asks what type of job it is.
    Type = input("Type\n[1]Homework\n[2]Assignment\n[3]Test Revision\n[4]Chore\nPLEASE INSERT NUMBER: ")
    Type = int(Type)
    #depending on importance of job, it is given a value to its total value.
    #The lower the number, the more important it is.
    if Type == 1:
        total = total + 3
    elif Type == 2:
        total = total + 2
    elif Type == 3: 
        total = total + 1
    elif Type == 4:
        total = total + 4

    #identifies difficulty of the task, it is given a value to its total value.
    #The lower the number, the more important it is.
    diff = input("DIIFICULTY\n[1, 2 or 3]: ")
    diff = int(diff)
    if diff == 1:
        total = total + 3
    elif diff == 2:
        total = total + 2
    elif diff == 3: 
        total = total + 1

    #Date sorter
    askDate(total, name)

def askDate(total, name):
    dueDate = input("Due Date (dd/MM): ")
    #check if letter is in due date input

    if len(dueDate) != 5:
        print("Invalid...")
        askDate(total, name)
    else:
        dueDate = dueDate.replace("/", "")
        mid = len(dueDate)//2 #identifies number of objects in list and then uses pythons own version of interger division which identifies how many numbers are on left or right of middle number/s.
        lefthalf = str(dueDate[:mid]) # variable defines left side of the middle
        righthalf = str(dueDate[mid:]) # variable defines right side of the middle
        dueDate = (righthalf + "/" + lefthalf)
        dueDateChecker(dueDate, total, name)

def ifDouble(total, name):
    #gets the data stored in data document and inserts it into the main list so that
    #when data from document is reset, the data can be saved and re-inserted after merge.
    before = []
    with open('./dates.txt', 'r') as filehandle:  
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            lines = line[:-1]

            # add item to the list
            before.append(lines)
        theEND = before
    
    #Re-insert list with previous and new values back into data document,
    #data seperated with new line
    with open('./dates.txt', 'w') as output:  
        for listitem in theEND:
            output.write('%s\n' % listitem)

    #merge sort final new input with list 
    #and go back to main menu
    mergeEND(family_List, date)

#allows user to remove object from data stored.              
def remove():
    #name of object you would like to remove
    nameObject = input("\nName of TO DO: ")
    #open data file and seek all lines.
    with open("./dates.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f: #for each individual line in data document
            if nameObject not in line: #if the input is in that line, it will break loop and...
                f.write(line) #replace the line with a blank line
        f.truncate()

    #go back to main menu
    startMerge(family_List)

def cleanList(family_List):
    newAdd = date + " {(TODAY)}"
    family_List.append(newAdd)
    index = family_List.index(newAdd)
    listLen = len(family_List)
    indexMid = (listLen - index) - 1
    #starts merge algorithm
    mergeSort(family_List)
    mid = indexMid
    lefthalf = family_List[:mid]
    righthalf = family_List[mid:]
    finalDates = righthalf + lefthalf
    index = finalDates.index(newAdd)
    finalDates.pop(index)
    listObjects(family_List, index)

#to list objects downwards
def listObjects(family_List, index):
    print("\n")
    mid = index
    lefthalf = family_List[:mid]
    righthalf = family_List[mid:]
    family_List = righthalf + lefthalf
    family_List.pop(index)
    for x in family_List: 
        print(x)
    startMerge(family_List)

def dueDateChecker(dueDate, total, name):
    #gets the data stored in data document and inserts it into the main list so that
    #when data from document is reset, the data can be saved and re-inserted after merge.
    before = []
    with open('./dates.txt', 'r') as filehandle:  
        filecontents = filehandle.readlines()

        for line in filecontents:
            # remove linebreak which is the last character of the string
            lines = line[:-1]

            # add item to the list
            before.append(lines)
        theEND = before

    #print total and name of Object
    dueDate = str(dueDate)
    total = str(total)
    dueDate = dueDate + " {" + total +"(" + name + ")}"
    theEND.append(dueDate)

    #convert the list into string
    print("\n" + convert(theEND))
    
    #Re-insert list with previous and new values back into data document,
    #data seperated with new line
    with open('./dates.txt', 'w') as output:  
        for listitem in theEND:
            output.write('%s\n' % listitem)
    
    ifDouble(total, name)


#declaring main list and start variable
theEND = []
start = 0
#starting main menu function
startMerge(family_List)
