# Implement a function that adds new key value pairs to the programming_language list.
#  You can see the list below in which there is only two dictionaries, after insert method, 
# there should be three dictionaries. After insertion we need to print programming_language list to the console.

# programming_language = [
#     {"user_name" : "Elshad",
#      "favorite_languages" : ["Python", "Java", "C#"],
#      "experience": 10 
#     },
#     {"user_name":"Renad",
#      "favorite_languages" : ["Scratch","Python"],
#      "experience" : 2
#     },
# ]
# Example

# add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)
# Output

# [
#  {'user_name': 'Elshad', 
#   'favorite_languages': ['Python', 'Java', 'C#'], 
#   'experience': 10
#  },
#  {'user_name': 'Renad', 
#   'favorite_languages': ['Scratch', 'Python'], 
#   'experience': 2
#  },
#  {'user_name': 'Edy', 
#   'favorite_languages': ['Java', 'Kotlin', 'Swift'], 
#   'experience': 10
#  }
# ] 


import pprint
programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

def add_new_user(user,programing,experience):
    new_user={
                "user_name":user,
                "favorite_languages":programing,
                "experience": experience
                } 
    programming_language.append(new_user)
    return programming_language

add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)
print(programming_language)
