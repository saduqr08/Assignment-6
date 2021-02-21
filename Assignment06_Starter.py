#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def append_table(table,stID, strTitle,stArtist):
        """ Function to manage data ingestion and append data to the table
            passed the parameters listed below.
        

        Parameters
        ----------
        strID : TYPE
            DESCRIPTION.
        strTitle : TYPE
            DESCRIPTION.
        strArtist : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
   
   
        intID = int(stID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        return table
         
        
       
   
    @staticmethod
    def delete_inventory(lstTbl):
        """Function to manage data ingestion and delete user input
        
        Takes user input from memory and writes to CDInventory.txt in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
        None.

        """
        
        
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        
    @staticmethod
    def save_inventory(file_name, table):
        """Function to manage data ingestion from user to a txt file
        
        Takes user input from memory and writes to CDInventory.txt in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
        None.

        """
        
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            objFile = open(file_name, 'w')
            for row in lstTbl:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """Function to manage data ingestion from user to a txt file
        
        Takes user input from memory and display CDInventory in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        
        
        Returns:
            None.
        """
        
        table.write() #Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        pass
    
    


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    @staticmethod   
    def get_input():
         """Function to manage data ingestion from user.
        
        Takes user input put it in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
            strID, strTitle, stArtist
        

        """
         strID = input('Enter ID: ').strip()
         strTitle = input('What is the CD\'s title? ').strip()
         stArtist = input('What is the Artist\'s name? ').strip()
         return strID, strTitle, stArtist
        
       

    @staticmethod
    def load_inventory(file_name,table):
         """Function to manage data ingestion from user to a txt file
        
        Takes user input from memory and writes to CDInventory.txt in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
        None.

        """
        
         print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
         strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:')
         if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
         else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        IO.load_inventory(strFileName, lstTbl)   
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, stArtist, strTitle = IO.get_input()
        lstTbl = DataProcessor.append_table(lstTbl, strID, strTitle, stArtist)
        IO.show_inventory(lstTbl)
        # 3.3.2 Add item to the table
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to use
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        # 3.5.2 search thru table and delete CD
        DataProcessor.delete_inventory(lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        # 3.6.2.1 save data
        DataProcessor.save_inventory(strFileName,lstTbl)    
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




