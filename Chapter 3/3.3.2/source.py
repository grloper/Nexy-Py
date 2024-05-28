class UnderAge(Exception):
    def __str__(self, age):
        return "You are under 18 years old. You can come to Idan's birthday in " + str(18 - int(age)) + " years."

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge()
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
       print(e.__str__(age))  

        
send_invitation("Sarah", 20)
send_invitation("John", 17)
