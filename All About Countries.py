# 1) Create a class `India` with three methods:
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.
class India():
    def capital(self):
        print("The capital of India is Dehli.")
    def language(self):
        print("Hindi is the most commonly spoken language in India.")
    def type(self):
        print("India is a develping country.")
# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.
class Australia():
    def capital(self):
        print("The capital of Australia is Canberra.")
    def language(self):
        print("English is the primary language in Australia.")
    def type(self):
        print("Australia is a develped country.")
# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`
obj_india = India()
obj_aus = Australia()
# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)
for country in (obj_aus, obj_india):
    country.capital()
    country.language()
    country.type()