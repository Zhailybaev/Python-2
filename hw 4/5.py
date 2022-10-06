import re
class Wordplay():
    def __init__(self,words):
        self.words=words
    def words_with_length(self,length):
        a=list()
        for i in range(len(self.words)):
            if len(self.words[i])==length:
                a.append(self.words[i])
        return a
    def starts_with(self,s):
        b=list()
        for i in range(len(self.words)):
            if self.words[i].startswith(s):
                b.append(self.words[i])
        return b
    def ends_with(self,t):
        c=list()
        for i in range(len(self.words)):
            if self.words[i].endswith(t):
                c.append(self.words[i])
        return c
    def palindromes(self):
        d=list()
        for i in range(len(self.words)):
            r=self.words[i][::-1]
            if r==self.words[i]:
                d.append(self.words[i])
        return d
    def only(self,pattern):
        e=list()
        for i in range(len(self.words)):
            h=re.findall(pattern,self.words[i])
            e.append(h)
        return e
    def avoids(self,pattern):
        f=list()
        for i in range(len(self.words)):
            h=re.findall(pattern,self.words[i])
            f.append(h)
        return f   
    
words=["father", "mother", "book", "note", "boy", "sister", "nan", "enot", "abcd"]
w=Wordplay(words)
s=str(input("strats with "))
print(w.starts_with(s))
t=str(input("ends with "))
print(w.ends_with(t))
print("palindromes: ", w.palindromes())
pattern1="^[a-f]+$"
print("only ", w.only(pattern1))
pattern2="^[^a-b]+$"
print("only ", w.avoids(pattern2))