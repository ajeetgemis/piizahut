print("seed is here")
from .models import faker_test
from faker import Faker
fake=Faker()
for _ in range(10):
   # print(fake.name())
    #print(fake.address())
    faker_test.objects.create(name=fake.name())

def facker_fun(n):
  
    for i in range(0,n):
       # print(fake.name())
        print(fake.address())
        faker_test.objects.create(name=fake.name())