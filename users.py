users= [
  {
    'name': 'John',
    'telephone': '000000',
    'age': 24
  },
  {
    'name': 'Jane',
    'telephone': '111111',
    'age': 26
  },
  {
    'name': 'Laura',
    'telephone': '222222',
    'age': 28
  }
]

users.append({'name': 'Jose', 'telephone': '333333', 'age': 30})

# print(users)

# for user in users:
#   print(user['name'])

# for user in users:
#   print(f"{user['name']} | {user['age']} | {user['telephone']}")

name_reply=input('What is your name?')
age_reply=input('How young are you?')
telephone_reply=input('What is your phone number?')
users.append({
  'name': name_reply,
  'age': age_reply,
  'telephone': telephone_reply
})

print(users)
