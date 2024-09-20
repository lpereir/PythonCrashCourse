from user import User
class Privileges:
    def __init__(self,privileges):
        self.privileges=privileges

    def show_privileges(self):
        print('-'*20)
        print("Admin's privileges:")
        print('-'*20)
        for privilege in self.privileges:
            print(f'{privilege}', end='\n')
        print('-'*20)

class Admin(User):
    def __init__(self, first_name, last_name, age, email, job_title, gender, privileges):
        super().__init__(first_name, last_name, age, email, job_title, gender)
        self.privileges = Privileges(privileges)