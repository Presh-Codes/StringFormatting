def shit():
    name = "Precious"
    age = 13
    height = 4.7
    txt = "Hey there, my name is {} and I'm {} years old. My height is {}"
    print(txt.format(name, age, height))


def Person():
    name = "Patrick"
    age = 16
    height = 5.6
    txt = "There's a boy named {0} and he is {1} years old. {0}'s height is {2}"
    print(txt.format(name, age, height))


def damn():
    price = 49.5
    txt = "The cost of one back pack here is {:.2f} bucks"
    print(txt.format(price))


def order():
    quantity = 50
    item = "rice"
    price = 250
    txt = "I want {} bags of {} for {} dollars"
    print(txt.format(quantity, item, price))


def ohmy():
    txt = "I would like a plate of {food} for {price} bucks"
    print(txt.format(food="Spaghetti", price="25"))


shit()
Person()
damn()
order()
ohmy()