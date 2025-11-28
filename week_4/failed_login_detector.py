
#sample Data: 
login_attempt =[("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

#Dictionary to count failed attempts:
failed_attempts = {}

#for_loop to go through each login attempt:

for user, attempt in login_attempt:
    
    if attempt == "failed":
        failed_attempts[user] = failed_attempts.get(user, 0) + 1
    

#for_loop to go through failed_attempts and give alert if needed:\
print("Checking login attempts: ")

for user,count in failed_attempts.items():
    if count >= 3:
        print(f"Alert!\n {user} has {count} failed login attempts ")

