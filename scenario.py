class Numbers:

     def __iter__(self):

        self.a = 1

        return self



     def __next__(self):

        x = self.a

        self.a +=1

        return x



mynum=Numbers ()

myiterator=iter(mynum)



print(next(myiterator))

print(next(myiterator))

print(next(myiterator))

print(next(myiterator))
