import uuid
from datetime import datetime


class UserMemo(object):
    """This class houses the memos for users"""
    data_storage ={}
        
    
    
    def __init__(self,viewer_id=False):
        if viewer_id:
            self.viewer_id = viewer_id
        else:
            self.viewer_id = 0


    def create_my_memo(self,the_memo):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id and the_memo != "":
                data= {
                    "memo_id":uuid.uuid4().int,
                    "the_memo":the_memo,
                    "date_created":str(datetime.utcnow())

                }
                UserMemo.data_storage[user_id]["my_memos"].append(data)
                payload = {
                    "Status":"GOOD",
                    "message":"You have successfully inserted your memo"
                }
                return payload

        payload2 = {
            "Status":"BAD",
            "message":"Failed to add message"
        }
        return payload2


    def view_my_memos(self):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id:
                reply = []
                for memo in UserMemo.data_storage[user_id]["my_memos"]:
                    payload = {
                        "status":"GOOD",
                        "message":"Memos found.",
                        "The Memos": memo
                    }
                    reply.append(payload)                
                return reply

        payload2 = {
            "status":"BAD",
            "message":"Cannot view the Memos"
        }
        return payload2

    def update_my_memo(self,memo):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id:
                UserMemo.data_storage[user_id]["my_memos"]["the_memo"] = memo
                payload ={
                    "status":"GOOD",
                    "message":"Successfully updated your memos"
                }
            return payload
        payload2 = {
                "status":"BAD",
                "message":"Failed to update your memos"
            }
        return payload2

    def delete_my_memo(self,my_memo_id):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id:
                for memo_d in UserMemo.data_storage[user_id]["my_memos"]:
                    if memo_d["memo_id"] == my_memo_id:
                        UserMemo.data_storage[user_id]["my_memos"].remove(memo_d)
                    payload ={
                        "status":"GOOD",
                        "message":"Successfully deleted your memos"
                    }
                    return payload
        payload2 = {
                "status":"BAD",
                "message":"Cannot delete the Memos"
            }
        return payload2


    def admin_memo_deletion(self,memo_id):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id:
                if user["role"] == "Admin":
                    del(UserMemo.data_storage[user_id]["my_memos"][memo_id])
                payload = {
                    "Status":"GOOD",
                    "Message":"Successfully deleted the user memo"
                }
                return payload
        payload2 = {
            "status":"BAD",
            "message":"Cannot delete message"
        }
        return payload2
            

    def user_send_message(self,recipient_id, message):
        from models.notebook_users import User
        user_id = self.viewer_id
        for user in User.notebook_users:
            if user["user_id"] == user_id:
                UserMemo.data_storage[recipient_id]["inbox"] = message
                UserMemo.data_storage[user_id]["outbox"] = message
            payload = {
                "status":"GOOD",
                "message":"Successfully sent message"
            }
            return payload
        payload2 = {
            "Status":"BAD",
            "message":"Failed to send the message"
        }
        return payload2

    def view_all_my_inbox(self):
        from models.notebook_users import User
        for user in User.notebook_users:
            for inbox in data_storage[self.viewer_id]["inbox"]:
                payload = {
                    "status":"GOOD",
                    "message":"Currently on your inbox",
                    "inbox": inbox
                }
            return payload
        payload2 = {
            "status":"BAD",
            "message":"Failed to access inbox"
        }

        return payload2
    
    def delete_message():
        #from models.notebook_users import user
        for user in User.notebook_users:
            for message in data_storage["my_inbox"]:
                del(message)
            return payload{
                "status":"GOOD",
                "message":"Successfully deleted messages"
            }
        return payload2{
            "status":"BAD",
            "message":"Failed to delete message"
        }


    def user_view_a_message():
        from models.notebook_users import user
        for user in User.notebook_users:
            for message in data_storage["my_inbox"]:
                return message
            return payload{
                "status":"GOOD",
                "message":"You can view your messages"
            }
        return payload2{
            "status":"BAD",
            "message":"Failed not allowed to view message"
        }

    def user_view_a_memo():
        pass
        