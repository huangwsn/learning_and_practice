# ***** Example 1 (PDF.P137) *****
print("\n***** Example 1 *****")
# def identity_ex1(f):
#     print("In identity_ex1")
#     return f

# @identity_ex1
# def foo_ex1():
#     print("In foo_ex1")
#     return "bar"

# val_ex1 = foo_ex1()
# print(val_ex1)

# ***** Example 2 (PDF.P137) *****
print("\n***** Example 2 *****")
# _functions = {}
# def register(f):
#     global _functions
#     _functions[f.__name__] = f
#     print(f.__name__)
#     return f
# @register
# def foo_ex2():
#     return 'bar'
# val_ex2 = foo_ex2()
# print(val_ex2)
# print(_functions)

# ***** Example 3.A (PDF.P138) *****
print("\n***** Example 3.A *****")
# class Store(object):
#     def get_food(self, username, food):
#         if username != 'admin':
#             raise Exception("This user is not allowed to get food")
#         return self.storage.get(food)
    
#     def put_food(self, username, food):
#         if username != 'admin':
#             raise Exception("This user is not allowed to put food")
#         self.storage.put(food)

# # ***** Example 3.B (PDF.P138) *****
# print("\n***** Example 3.B *****")
# class Store(object):
#     def check_is_admin(username):
#         if username != 'admin':
#             raise Exception("This user is not allowed to get or put food")
    
#     def get_food(self, username, food):
#         self.check_is_admin(username)
#         return self.storage.get(food)
    
#     def put_food(self, username, food):
#         self.check_is_admin(username)
#         self.storage.put(food)

# TODO - Below: To be revisited
# ***** Example 3.C (PDF.P139) *****
print("\n***** Example 3.C *****")

def check_is_admin(f):
    print(f)
    print(**kwargs)
    # def wrapper(*args, **kwargs):
    #     if kwargs.get('username') != 'admin':
    #         raise Exception("This user is not allowed to get or put food")
    #     return f(*args, **kwargs)
    return f

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        print("In get_food")

    @check_is_admin
    def put_food(self, username, food):
        print("In put_food")
    
store = Store()
store.get_food(username="admin", food="cake")
# TODO - Above: To be revisited