import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as
    Serializer, BadSignature, SignatureExpired)

class User(object):
    """Class user houses all of Notebook users."""
    notebook_users= []
    register_user_error_log = []
    login_user_error_log = []

    def __init__(self,viewer_id=False):
        if viewer_id:
            self.viewer_id = viewer_id
        else:
            self.viewer_id = 0

    def my_login(self,email,password):
        """This method is used for user login."""
        our_users = User.notebook_users

        for person in our_users:
            if person["email"] == email:
                if check_password_hash(person['password'], password):
                    key1 = Serializer("Kevo_The_Great", expires_in=21600)
                    tok = key1.dumps({
                        "user_id": person["user_id"]
                    }).decode("ascii")

                    payload = {
                        "Status":"GOOD",
                        "Token": tok,
                        "user_id": person["user_id"],
                        "message": "Logged in successfully."
                    }
                    return payload
            payload = {
                "Status":"BAD",
                "message":"Invalid login."
            }
            self.login_user_error_log.append(payload)
            return payload


    def user_registration(self,username,email,phone_number,
        role,password,confirm_password):
        """This method registers a user"""

        our_users = User.notebook_users

        for person in our_users:
            if person["username"] == username:
                answer = {
                    "Status":"BAD",
                    "message":"Username already in system"
                }
                self.register_user_error_log.append(answer)
                return answer

            if person["email"] == email:
                answer = {
                    "Status":"BAD",
                    "message":"Email already in system"
                }
                self.register_user_error_log.append(answer)
                return answer

            if person["phone_number"] == phone_number:
                answer = {
                    "Status":"BAD",
                    "message":"Phone already in system"
                }
                self.register_user_error_log.append(answer)
                return answer

            if password != confirm_password:
                answer = {
                    "Status":"BAD",
                    "message":"'Password' and 'confirm password' not matching"
                }
                self.register_user_error_log.append(answer)
                return answer

        payload = {
            "user_id": uuid.uuid4().int,
            "username": username,
            "email": email,
            "phone_number": phone_number,
            "password": generate_password_hash(password),
            "is_enabled": "True",
            "role": role
        }

        User.notebook_users.append(payload)
        person_actions = {
            "my_outbox":[],
            "my_inbox":[],
            "my_memos":[]
        }

        from notebook_memo import UserMemo
        UserMemo.data_storage[payload["user_id"]] = person_actions

        reply = {
            "user_id": payload["user_id"],
            "username": payload["username"],
            "email": payload["email"],
            "phone_number": payload["phone_number"],
            "role": payload["role"]
        }

        return reply

    def admin_view_all_users(self):
        for user in User.notebook_users:
            if user["user_id"] == self.viewer_id:
                if user["role"] == "Admin":
                    payload={
                        "Status":"GOOD",
                        "message":"Users fetched.",
                        "notebook_users":User.notebook_users
                    }
                    return payload

        bad_input ={
            "Status":"BAD",
            "message" :"You are unauthorized to view this data."
        }
        return bad_input


    def admin_delete_a_user(self,user_id):
        for user in User.notebook_users:
            if user["user_id"] == self.viewer_id:
                if user["role"] == "Admin":
                    for d_user in User.notebook_users:
                        if d_user["user_id"] == user_id:
                            User.notebook_users.remove(d_user)
                            payload={
                                "Status":"GOOD",
                                "message":"deleted"
                            }
                            return payload

        payload2={
            "Status":"BAD",
            "message":"You cannot delete this user contact admin."
        }
        return payload2


    def admin_view_a_user(self,user_id):
        for user in User.notebook_users:
            if user['user_id'] == self.viewer_id:
                if user["role"] == "Admin" or user["user_id"] == user_id:
                    payload ={
                        "Status":"GOOD",
                        "message":"user found",
                        "User Details":user
                    }
                    return payload
            payload2 = {
                "Status":"BAD",
                "message":"Unauthorized Access"
            }

        return payload2
