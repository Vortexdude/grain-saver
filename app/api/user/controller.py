from .model import User

class UserController:
    """This controller used for controlling the flow of api and dabases"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def register_user(userdata):

        new_user = User(**userdata)
        new_user.save_to_db()

        if new_user:
            return {"status": str(new_user)}
        else:
            return {"status": "There is an error in the database"}

    @staticmethod
    def fetch_user(fname):

        user = User.find_by_filter(fname=fname)

        if user:
            return {"data": user.lname}
        else:
            return {"status": "User not found"}

    def login(data):

        phone = data['phone']
        password = data['password']

        user = User.login(phone, password)
        if user:
            return {"data": "Login Success!"}
        else:
            return {"data": "Authorization Error!"}
