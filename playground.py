# def add(*numbs):
#     total = 0
#     for n in numbs:
#         total += n
#     return total
        
        
        
        
# sumNumber = add(2,3,4,334,23)
# print(sumNumber)


# def calculate(n,**kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multi"]
#     print(n)
    


# calculate(3, add= 3, multi = 5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        
