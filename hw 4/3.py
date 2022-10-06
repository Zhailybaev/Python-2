class Password_manager():
    def __init__(self, old_passwords):
        self.old_passwords=old_passwords
    def get_password(self):
        return self.old_passwords[len(self.old_passwords)-1]
    def set_password(self, b):
        if b not in self.old_passwords:
            self.old_passwords.append(b)
        
        
    def is_correct(self,a):
        if Password_manager.get_password(self)==a:
            return True
        else:
            return False

old_passwords=["adfg", "qwer", "tyui"]
p=Password_manager(old_passwords)

print(p.get_password())
a=str(input("password: "))
print(p.is_correct(a))
b=str(input("change "))
p.set_password(b)
print("password is chanded: ", p.get_password())

