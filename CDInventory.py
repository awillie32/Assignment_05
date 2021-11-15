#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AWillie, 2021-Nov-14, Added to File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# replaced list of lists with list of dicts
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
lstKey = ['ID', 'CD Title', 'Artist'] # Dictionary defintion
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Added the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = dict(zip(lstKey,lstRow))
            lstTbl.append(dicRow)
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',')
    elif strChoice == 'd':
        # Added functionality of deleting an entry
        usinp = input('Select the ID # you would like to delete: ')
        i = 0
        found = False
        for row in lstTbl:
            ID = row['ID']
            if usinp == str(ID):
                del lstTbl[i]
                found = True
                break
            else:
                i += 1
        if not found:
            print('ID not found')
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        # Trying to open a clear new file so my load fucntion works, and doesn't pull up more saved info
        objFile = open(strFileName, 'w+')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(row[item]) + ', '
            strRow = strRow[:-2] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

