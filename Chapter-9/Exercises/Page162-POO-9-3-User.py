class User:
    def __init__(self, first_name, last_name, age, email,job_title,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.email=email
        self.job_title=job_title
        self.gender=gender
    def describe_user(self):
        '''Prints a summary os the user's information'''
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'e-Mail: {self.email}')
        print(f'Job Title: {self.job_title}')
    def greet_user(self):
        '''Prints Personalized greeting to the user'''
        print(f'Welcome {self.first_name} {self.last_name},')
        print(f'{self.first_name} is {self.age} years old and work as {self.job_title}')
        if self.gender[0] in 'Mm':
            print(f'His email is: {self.email}')
        elif self.gender[0] in 'Ff':
            print(f'Her email is: {self.email}')

user1=User('Carla','Bent',34,'carla.bent@jobs.com','Doctor','female')
user2=User('Mike','McDuff',40,'mikee@gmail.com','Driver','male')
user3=User('Jannett','McCain',25,'jannet.maccain@yahoo.com','Secretary','female')
user4=User('John','Espinosa',47,'johnesp@mail.com','IT Analyst','male')

lista=[user1,user2,user3,user4]

for i in lista:
    i.describe_user()
    print()
    i.greet_user()
    print()






