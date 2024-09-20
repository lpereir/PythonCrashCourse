''' 10-13. User Dictionary: The remember_me.py example only stores one piece of 
information, the username. Expand this example by asking for two more pieces 
of information about the user, then store all the information you collect in a 
dictionary. Write this dictionary to a file using json.dumps(), and read it back 
in using json.loads(). Print a summary showing exactly what your program 
remembers about the user.'''

from pathlib import Path
import json
def get_stored_userinfo(path):
  """Get stored username if available."""
  if path.exists():
    contents = path.read_text()
    userinfo = json.loads(contents)
    return userinfo
  else:
    return None

def get_new_userinfo(path):
    """Prompt for a new username."""
    userinfo=dict()
    userinfo['username']=str(input("What is your name? "))
    userinfo['email']=str(input("What is your e-mail? "))
    userinfo['phone']=str(input("What is your phone? "))
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def greet_user():
    """Greet the user by name."""
    path = Path('text_files/userinfo.json')
    userinfo = get_stored_userinfo(path)
    if userinfo:
       print(f"Welcome back, {userinfo['username']}!")
       print(f"Your e-mail is {userinfo['email']}")
       print(f"Your phone is {userinfo['phone']}")
    else:
        userinfo = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {userinfo['username']}!")

greet_user()