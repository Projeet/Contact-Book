import psycopg2 as pg2

secret = 'password'

conn = pg2.connect(database = 'project_contact_book', user = 'postgres', password = secret)


cur = conn.cursor()

# Following function will fetch the table

def find_contact():
	cur.execute(""" Select * from contacts
		order by first_name""")
	data = cur.fetchall()
	print(data)

# This function will help userto enter the name and contact number

def insert_contact():
	insert_query = """ insert into contacts(first_name,last_name,contact_number) values (%s,%s,%s) """

	f_name = input("Enter the first name")

	l_name = input("Enter the last name")

	contact = int(input('Enter your contact number'))



	record_to_insert = (f_name,l_name,contact)
	cur.execute(insert_query,record_to_insert)

	conn.commit()

# This function will sort the table according to the first name alphabetically

def order_by():
	cur.execute(""" Select * from contacts
		order by first_name""")
	data_1 = cur.fetchall()
	print(data_1)

def serach_by_name():
	search_query = """ SELECT contact_number from contacts

	where first_name = %s """

	name = input('Enter the name whose contact number you want:') # When query is provided by the user,you should escape the values

	new_name = (name,)           # And escaping the values can be done in the following manner

	cur.execute(search_query,new_name)

	data_2 = cur.fetchall()

	print(data_2)

print("Welcome to your contact book!!")

while True:

	print("Choose from the following options---")
	print("1. Table Lookup ")
	print("2. Insert a new contact")
	print("3. Search a particular phone number")
	print("4. Exit")
	option = int(input("Press the number associated with the following options[1 2 3 4]:"))

	if option == 1:
		find_contact()
		


	elif option == 2:

		insert_contact()

		order_by()

	elif option == 3:

		serach_by_name()


	elif option == 4:  

		break            # This statement will break the loop 

	else:
		print("Invalid Input")

    


		



				
		
	


	





