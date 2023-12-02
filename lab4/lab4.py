class User:
    def __init__(self, name, profession, phone_number, friends=[]):
        self.name = name
        self.profession = profession
        self.phone_number = phone_number
        self.friends = friends

    def add_friend(self, friend):
        self.friends.append(friend)

    def __str__(self):
        return f"{self.name} ({self.profession}): {self.phone_number}, friends: {', '.join(self.friends)}"


def find_users_by_name(users, name):
    found_users = [user for user in users if user.name.lower() == name.lower()]
    return found_users


def find_user_by_phone(users, phone_number):
    for user in users:
        if user.phone_number == phone_number:
            return user
    return None

users = [
        User("You", "Eng teacher", "+75985896217", ["Bob", "Alice", "Claire"]),
        User("Alice", "Medic", "+71964986091", ["You", "Peggi"]),
        User("Peggi", "Theoretic", "+75921303909", ["Alice", "Bob"]),
        User("Bob", "Programmer", "+70747160887", ["You", "Anuj"]),
        User("Anuj", "Programmer", "+72594872940", ["Bob"]),
        User("Claire", "Postman", "+79533784527", ["You", "Tom", "Jonny"]),
        User("Tom", "Theoretic", "+71087045836", ["Claire", "Tom"]),
        User("Jonny", "Medic", "+73707318802", ["Claire"]),
        User("Tom", "unemployed", "+79922208976", ["Tom"])
    ]

search_criteria = input("Input how u want to find user by name (1) or phone number (2): ")

if search_criteria == "1":
    name_to_search = input("Input user's name: ")
    found_users = find_users_by_name(users, name_to_search)
    if found_users:
        print("Users found:")
        for user in found_users:
            print(user)
    else:
        print("Users not found.")
elif search_criteria == "2":
    phone_to_search = input("Input user's phone number: ")
    found_user = find_user_by_phone(users, phone_to_search)
    if found_user:
        print("User found:")
        print(found_user)
    else:
        print("User not found.")
else:
   print("Uncorrect.")


