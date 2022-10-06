class Investment():
    def __init__(self,principal, interest):
        self.principal=principal
        self.interest=interest
    def value_after(self,n):
        return self.principal*(1+((self.interest/100)*n))
    def __str__(self):
        return f'Principal-${self.principal}, Interset rate - {self.interest}'
stavka=int(input("stavka: "))
summa=int(input("summa: "))
d=Investment(summa,stavka)
print(d)
n=int(input())
print(d.value_after(n))
        