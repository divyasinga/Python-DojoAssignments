# Part I

def nameprint(names):
    for i in names:
        # for data in i.itervalues():
        #     print data
        print i['first_name'], i['last_name']

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
nameprint(students)

# Part 2
def usersprint(names):
    for key, data in names.items():
        print key
        for value in data:
            print data.index(value)+1, value['first_name'], value['last_name'], len(value['first_name']) + len(value['last_name'])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

usersprint(users)