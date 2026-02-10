from .repositories import UserRepository

class UserService:
    
    def create_user(data):
        # if UserRepository.get_user_by_user(data.username):
        #     return None
        user = UserRepository.create_user(data)
        return user 
