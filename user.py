from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Nom?",
    },
]

class User:
    def __init__(self, name):
        self.name = name


def add_user():
    # This function should create a new user, asking for its name
    name = prompt(user_questions)
    user = User(name['name'])

    f = open('users.csv', 'a', newline='')
    f.write(user.name + "\n")

    return user