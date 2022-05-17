first_name = 'Dayananda'
last_name = 'BS'
country = 'India'
city = 'Hassan'
age = 28
skills = ['Linux', 'AWS', 'Devops',]
person_info = {
    'firstname':'Dayananda', 
    'lastname':'BS', 
    'country':'India',
    'city':'Hassan'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, = 'Dayananda', 'BS', 'India', 28

print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
