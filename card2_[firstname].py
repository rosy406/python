 # -----------------------------------------+
  # Quinn, Tjabe, Brady                      |
  # Computer Science, Project 2              |
  # Last Updated: September 20, 2022         |
  # -----------------------------------------|
  # This project asks for a name and phone   |
  # number, and then outputs a buissness card|
  # for the user.                            |
  # Brady created the input values.          |
  # Quinn formated the name line. Tjabe      | 
  # formated the phone number and email line |
  # -----------------------------------------+

#ask for inputs
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
phone = input("Please enter your telephone number: ")

#define variables
name = first_name.capitalize() + " " + last_name.capitalize()
email = "@:" + first_name.lower() + "@cornell.edu"

#output results
print('''
Here is your buisness card...
''')
print('+------------------------------------------------+')
print('|     ,,                                         |')
print('|    >`)                                         |')
print('|    ( |          ',name.ljust(30) + '|')
print('|     ^            eBird Data Processor          |')
print('| -------          Cornell Lab of Ornithology    |')
print('|    _                                           |')
print('|   ("<                                          |')
print('|   / )            159 Sapsucker Woods Rd.       |')
print('|    L             Ithaca, New York 373737       |')
print('| ---------        birds.cornell.edu             |')
print('|                                                |')
print('|                                                |')
print('|  P:' ,phone.ljust(16),email.ljust(26) + '|')
print('|                                                |')
print('+------------------------------------------------+')