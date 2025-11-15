
#deleting dictionary keys
user = {
    "user_name": "my_user",
    "address":"ole",
    "pass":"ele",
    "value":"dele"

}
sens_info=["pass","address"]
for i in sens_info:
        user.pop(i)
print(user)

