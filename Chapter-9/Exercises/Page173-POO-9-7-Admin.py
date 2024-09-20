class User:
    def __init__(self, first_name, last_name, age, email,job_title,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.email=email
        self.job_title=job_title
        self.gender=gender
        self.login_attempts=0
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
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    def __init__(self, first_name, last_name, age, email, job_title, gender, privileges):
        super().__init__(first_name, last_name, age, email, job_title, gender)
        self.privileges=privileges
    
    def show_privileges(self):
        print('-'*20)
        print("Admin's privileges:")
        print('-'*20)
        for privilege in self.privileges:
            print(f'{privilege}', end='\n')
        print('-'*20)


user1=Admin('Carla','Bent',34,'carla.bent@jobs.com','Doctor','female',{"Can add post", "Can ban a user", "Can delete post"})

user1.describe_user()
print(f'Numero de tentativas de login: {user1.login_attempts}')
print()
for i in range(0,15):
    user1.increment_login_attempts()
print(f'Numero de tentativas de login: {user1.login_attempts}')
print()
user1.reset_login_attempts()
print(f'Numero de tentativas de login: {user1.login_attempts}')

user1.show_privileges()



