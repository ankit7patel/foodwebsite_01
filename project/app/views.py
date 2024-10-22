from django.shortcuts import render , redirect
from .models import student ,Query , Order

# Create your views here.

def home(request):
    user_name = request.GET.get('name', '')  # Get user name from URL
    return render(request, 'home.html', {'user_name': user_name})

def about(request):
    
    return render (request, 'about.html')

def gallery(request):
    return render (request, 'gallery.html')

def menu(request):
    return render (request, 'menu.html')

def order(request):
    return render (request, 'order.html')

def review(request):
    return render (request, 'review.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = student.objects.filter(stu_email=email)
        print(user)
        if user:
            user_data=student.objects.get(stu_email=email)
            print(user_data)
            email1=user_data.stu_email
            name1=user_data.stu_name
            contact1=user_data.stu_contact
            password1=user_data.stu_password
            print(name1,email1,contact1,password1)

            if password1==password:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'password':password1
                }
                # return render(request,'home.html',{'data':data})
                query_data=Query.objects.filter(email=email1) 
                return render(request ,'home.html' , {'data':data , 'query_data':query_data})
            
            else:
                msg="You Entered Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="email not register"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request, 'login.html')



def register(request):
    if request.method=='POST':
        print(request.POST)  
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpass = request.POST.get('confirm_password')
        print(name,email,contact,password,cpass)
        if password==cpass:
            user=student.objects.filter(stu_email=email)   #  database me email ni hai fr bhi empt dega 
            # user=student.objects.get(stu_email=email)     # database me email ni hai to error dega 
            # print(user)
            if user:
                user_name=student.objects.filter (stu_name=name)
                if user_name:
                    msg="email alredy exist"
                else:
                    msg="Email ID and Name already exist"    
                    return render (request, 'register.html',{'msg':msg})
            else:
                student.objects.create(
                            stu_name=name,
                            stu_email=email,
                            stu_contact=contact,
                            stu_password=password)
                msg="registration successfully "
                return render (request,'login.html',{'msg':msg}) 
        else: 
            msg="password & cpass not match"
            return render (request, 'register.html',{'msg':msg})
    else: 
        return render (request , 'register.html')
    
def dashboard(request):
    return render (request, 'dashboard.html')



def query(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        query1=request.POST.get('query')
        # print(name1,email1,query1)
        Query.objects.create(
        name=name1,
        email=email1,
        query=query1
    )
        data=student.objects.get(stu_email=email1)
        print(data)
        my_data={
        'name':data.stu_name,
        'email':data.stu_email,
        'contact':data.stu_contact,
        'password':data.stu_password
        }
      
        query_data=Query.objects.filter(email=email1) 

        return render(request ,'dashboard.html' , {'data':my_data , 'query_data':query_data})





def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        count = request.POST.get('count')
        food_name = request.POST.get('food_name')
        address = request.POST.get('address')

        # Create a new order
        Order.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            count=count,
            food_name=food_name,
            address=address
        )
        return redirect('order')  # Redirect to order list after creation

    return render(request, 'order.html')

# def order_list(request):
#     email = request.user.email 
#     # orders = Order.objects.filter(stu_email=email)
#     orders = Order.objects.filter(stu_email=email).first()
#     return render(request, 'order_list.html', {'orders': orders})


  
    # m
 
def order_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        count = request.POST.get('count')
        food_name = request.POST.get('food_name')
        address = request.POST.get('address')

        # Create a new order
        try:
            Order.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                count=count,
                food_name=food_name,
                address=address
            )
        except Exception as e:
            print(f"Error creating order: {e}")  

       
        return redirect('order_list')  

    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_update(request, pk):
    order = Order.objects.filter(pk=pk).first() 
    if order:
        if request.method == 'POST':
            order.name = request.POST.get('name')
            order.email = request.POST.get('email')
            order.phone_number = request.POST.get('number')
            order.count = request.POST.get('count')
            order.food_name = request.POST.get('food_name')
            order.address = request.POST.get('address')
            order.save()
            return redirect('order_list')

        return render(request, 'order_form.html', {'order': order})
    else:
        return redirect('order_list')  # Redirect if the order doesn't exist

def order_delete(request, pk):
    order = Order.objects.filter(pk=pk).first()  # Use filter() to get the order
    if order:
        if request.method == 'POST':
            order.delete()
            return redirect('order_list')
        return render(request, 'order_confirm_delete.html', {'order': order})
    else:
        return redirect('order_list')  # Redirect if the order doesn't exist

def logout(request):

    return render(request,'home.html')

