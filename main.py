import random

def password():
    s1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s3 = ['1','2','3','4','5','6','7','8','9','0']
    result = ''
    for i in range(11):
        result += random.choice(s1+s3)
    return result

p = password()
print(p)