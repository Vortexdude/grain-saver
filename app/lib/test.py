from app.api.user.model import User
import json

defaut_user_data = {
  "fname": "nitin",
  "lname": "namdev",
  "location": "vizag",
  "phone": "9630955003",
  "password": "notoosmart"
}

user_data = json.loads(defaut_user_data)
phone: str = user_data['phone']

_user = User.find_by_filter(phone=phone)
if not _user:
    user = User(user_data)
    user.save_to_db()
    """Default User creation message"""

# user = User(
#   fname = "Admin",
#   lname = "Developer",
#   location = "locahost",
#   phone = "1270001500",
#   password = "flask_api"
# )
