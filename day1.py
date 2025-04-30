# ✨ Desafio 100 Dias de Código - Dia 1/100 💻

def users():
    user_data = {}
    user_data['name'] = input('Enter the name: ')
    user_data['last name'] = input('Enter the last name: ')
    user_data['age'] = input('Enter the age: ')
    user_data['email'] = input('Enter the email: ')
    
    print('Data saved successfully!')
    return user_data

def list_users(users_list):
    print('\n📋 List of users:')
    for user in users_list:
        print(f"Name: {user['name']}, Last Name: {user['last name']}, Age: {user['age']}, Email: {user['email']}")

all_users = []


all_users.append(users())


while input('Do you want to continue? (y/n): ').lower() == 'y':
    all_users.append(users())


list_users(all_users)
