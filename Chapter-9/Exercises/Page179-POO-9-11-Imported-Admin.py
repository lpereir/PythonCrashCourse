from admin import Admin

user1=Admin('Carla','Bent',34,'carla.bent@jobs.com','Doctor','female',{"Can add post", "Can ban a user", "Can delete post"})
user1.privileges.show_privileges()