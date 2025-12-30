banned_users={"Mobius_001","crimson3020","Speedway"}
user=input("Enter your username: ")
if user in banned_users:
    print(f"User{user}is banned,Access denied ")
else:
    print(f"Welcome user {user}")