import sqlite3
import os #Operating system

#Putting the connection in one function will help immensely. e.g. if you have to change the name of your database, you do not then have to update the rest of the code.

#Checking database exists
def getDB():
    try:
        conn = sqlite3.connect('phonebook_database.db')
        cursor = conn.cursor()
        return cursor
    except TimeoutError:
        print ('Connection timed out.')

#Making sure SQL queries are running appropriately
def query_db():
    db = getDB()
    try:
        test_query = "SELECT * FROM business_table"
        db.execute(test_query)
    except:
        return None


#--------------BUSINESS FUNCTIONS-----------------------------------------------------------------

#Retrieves relevant database info for businesses
def get_businesses(): #Passes tests
    try:
        db = getDB() #Connecting to database
        query = 'SELECT business_name, business_category, postcode, telephone_number FROM business_table' #Specifying the query (the information we want to get)
        #executing the query
        db.execute(query)
        results = db.fetchall()
        return results
    except:
        print ('Sorry. There has been an error retrieving information from the database.')
        return False


#Gets user input from user and returns it with title function
def search_business_by_name(name):
    results = get_businesses()
    # name = find_businesses_by_name()
    try:
        for row in results:
            if name in row[0].lower():
                print (row)
                return True
    except:
        return False


# def search_business_by_category(category):
#     results = get_businesses() #Gets business_name, business_category, postcode, telephone_number from business_table
#     for item in results: #For row in table
#         if category.title() in item[1]: #if user input matches category field in results.



# search_business_by_name('buzz') #returns infor for Buzzshare
# search_business_by_category('computers') #returns all businesses listed under 'computers category'


#--------------PEOPLE FUNCTIONS--------------------------------------------------------------------



def get_people():
    try:
        db = getDB()
        query = "SELECT DISTINCT first_name, last_name, postcode, telephone_number FROM people_table"
        db.execute(query)
        results = db.fetchall()
        return results
    except:
        return False

def find_person_by_name(name):
    results = get_people() #Gets first_name, last_name, postcode, telephone_number
    for row in results:
        firstName = row[0]
        lastName = row[1]
        if name.lower() == firstName.lower() or name.lower() == lastName.lower():
            print (row)

find_person_by_name('Erika') #Finds info for Erika Shulem


def find_person_by_postcode(postcode):
    input_postcode = str(postcode).replace(' ','').strip().lower()
    results = get_people()
    for row in results:
        db_postcode = str(row[2]).replace(' ','').strip().lower() #Converting postcodes from table into lower case with stripped whitespace
        if input_postcode == db_postcode:
            print (row)
            return input_postcode

find_person_by_postcode('SW19 1ZW') #Pulls info for Erika Shulem and Isabelita Wyllcocks by postcode
