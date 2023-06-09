from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import Pizza,Pizzacategory,Cart,Cart_items,faker_test
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from faker import Faker
from django.db.models import Sum
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import enquryform
from .models import enqury
fake=Faker
# Create your views here.
api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.API_AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')
print(api)


class createView(CreateView):
    model=enqury
    fields=['email','username','phonenumber','message']
    success_url="/footer"
class genericview(ListView):
    model=Pizza
    #default template render location=model name/modelsnam_list.html
    #default context=modelname_list.html
    template_name='pizza_list.html'#custom template rendering
    context_object_name='pizza_detail'#custom context for template


@login_required(login_url="/login")
def success(request):
    if request.method=='GET':
        insert_this=request.GET.get('payment_id')
        compare_this=request.GET.get('payment_request_id')
        cart=Cart.objects.get(payment_id=compare_this)
        cart.payment_request_id=insert_this
        cart.is_paid=True
        cart.save()

     
    return render(request,'success.html')
@login_required(login_url="/login")
def process_payment(request):
    response = api.payment_request_create(
    amount='3499',
    purpose='FIFA 16',
    send_email=True,
    email="cssanand@gemis.in",
    redirect_url="http://127.0.0.1/success"
    )
@login_required(login_url="/login")
def order_api(request):
    mainlist=[]
    cart=Cart.objects.filter(is_paid=True)
    for items in cart:
        dict1={}
        dict1['user']=items.user.username
        dict1['is_paid']=items.is_paid
        dict1['payment_id']=items.payment_id
        dict1['request_payment_id']=items.payment_request_id
    mainlist.append(dict1)
    print(dict1)   
    return JsonResponse(mainlist,safe=False)
@login_required(login_url="/login")
def orders_list(request):
    print(request.user)
    order_items=Cart.objects.filter(is_paid=True,user=request.user)
    print(order_items)
    context={'orders':order_items}
    
    return render(request,'tests.html',context)
@login_required(login_url="/login")
def cart(request):
    try:
        cart=Cart.objects.filter(is_paid=False,user=request.user)[0]
    except:
        return render(request,'cart.html',{'Empty':"Your Cart Is empty"})


    total=0
    tt=Cart_items.objects.filter(cart=cart).aggregate(Sum('pizza__pizza_price'))
    print(tt['pizza__pizza_price__sum'])
    cartitems=cart.cart_item.all()
    

    
    for item in cartitems:
        price=item.pizza.pizza_price
        total=total+price
    print(total)
    response = api.payment_request_create(
    amount=total,
    purpose='FIFA 16',
    send_email=True,
    email="cssanand@gemis.in",
    redirect_url="http://127.0.0.1:8000/success"
    )
    #cart.payment_id=response['payment_request']['id']
    id=response['payment_request']['id']
    cart.payment_id=id
    print("id",id)
    cart.save()
    return render(request,'cart.html',{'carts':cart,'total':total,'payment_url':response['payment_request']['longurl']})
@login_required(login_url="/login")
def add_to_cart(request,uid):
    user=request.user
    print(user)
    pizza_obj=Pizza.objects.get(uid=uid)
    cart ,_=Cart.objects.get_or_create(user=user,is_paid=False)
    print(cart)
    Cart_items.objects.create(cart=cart,pizza=pizza_obj)
    return redirect('home')
@login_required(login_url="/login")
def delete_item(request,uid):
    print(uid)
    Cart_items.objects.get(uid=uid).delete()
   
    

    return redirect('cart')



    """    
    print(uid)
    #request.session['uid']=uid
    print("uid is",request.session.get('uid'))
    cart=request.session.get('cart')
    if cart:
        qty=cart.get(uid)
        if qty:
            cart[uid]=qty+1
        else:
            cart[uid]=1


    else:
        cart={}
        cart[uid]=1

        #print("not available")    
    request.session['cart']=cart
    print(request.session.get('cart'))
    return redirect('home')
 """    
def signout(request):
    logout(request)
    request.session.clear()
    return render(request,'login.html')
def home(request,data=None):
    categ=Pizzacategory.objects.all()
    if data:
        print(data)
        filterobj=Pizza.objects.filter(category=data)
        print(filterobj)
        for obj in filterobj:
            print(obj)
        return render(request,'home.html',{'obj1':filterobj,'categ':categ})    


   
    
    
    obj=Pizza.objects.all()
    return render(request,'home.html',{'obj1':obj,'categ':categ})

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        #request.session['name']=username
        #name=request.session['name']
        

        #print(name)
        password=request.POST.get('password')
        auth=authenticate(username=username,password=password)
        if auth is not None:
                
                print("logined")
                login(request,auth)
                request.session['customer_id']=username
                #request.session['customer_email']=cust.email
                cusid=request.session.get('customer_id')
                if cusid:

                    request.session.modified=True
                #messages.success(request,"Success Login")
                else:
                    return redirect('/home')

                return redirect('/home')
            #return render(request,'home.html')


    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        if User.objects.filter(username=username):
        
            print("user Existes")
            error_message="User Already Exists"
            return render(request,'register.html',{'errmsg':error_message})
           
        else:    
            cuser=User(username=username) 
            cuser.set_password(password)
            cuser.save()   
            return redirect('/login')
    return render(request,'register.html')    


def facker_fun(n):
    fake=Faker()
    for i in range(0,n):
        print(fake.name)
        faker_test.objects.create(name=fake.name)

def footer(request):
    if request.method=="POST":
        form=enquryform(request.POST)
        if form.is_valid:
            form.cleaned_data['email']
            form.cleaned_data['username']
            form.cleaned_data['phonenumber']
            form.cleaned_data['message']

    form=enquryform()
    return render(request,'footer.html',{'form':form})