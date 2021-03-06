""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['first_name']:
            errors.append('Name cannot be blank')
        elif info['first_name'].isalpha() == False:
            errors.append('Name must not contain numbers')
        elif len(info['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['last_name']:
            errors.append('Name cannot be blank')
        elif info['last_name'].isalpha() == False:
            errors.append('Name must not contain numbers')
        elif len(info['last_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirmpw']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            # Code to insert user goes here...
            # Then retrieve the last inserted user.
            password = info['password']
            create_query = "INSERT INTO users (first_name, last_name, email, hashed_pw) VALUES (:first_name, :last_name, :email, :hashed_pw)"
            info['hashed_pw'] = self.bcrypt.generate_password_hash(password)
            user_id = self.db.query_db(create_query, info)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def get_user_by_email(self, email, pwd):
        query = "SELECT * from users where email = :email"
        info = {'email': email}
        user = self.db.get_one(query, info)
        if user and self.bcrypt.check_password_hash(user.hashed_pw, pwd):
            return {'status': True, 'user': user}
        else:
            return {'status': False}

    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """