
import random

def random_phone():
    list1 = ["135","182","147"]
    a = [random.choice("0123456789") for i in range(8)]
    print(a)
    phone = random.choice(list1) + "".join(a)
    print("-".join(a))
    return phone

if __name__ == '__main__':
    phone = random_phone()
    print(phone)
