class User:

    def __init__(self,user_id,username):
        print("new user being created...")
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
        pass

    def follow(self,user):
        user.followers+=1
        self.following+=1
        pass

user_1=User("007","aakruti")
user_2=User("002","aishi")

user_1.follow(user_2)

print(user_1.following,user_2.followers)