from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from online_prestige_watch_marketplace_app.models import *
from datetime import date, datetime
# Create your views here.
def public_home(request):
    return render(request,'publicpages/public_home.html')

def Login(request):
    if 'submit' in request.POST : 
        Username=request.POST['Username']
        Password=request.POST['Password']
        if tbl_Login.objects.filter(Username=Username,Password=Password,User_Status="active").exists():
            q1=tbl_Login.objects.get(Username=Username,Password=Password,User_Status="active")
            request.session['lid']=q1.pk
            request.session['utype']=q1.User_Type 
            if q1.User_Type=='admin':
                return HttpResponse("<script>alert('succesfully logged in');window.location='/adminhome'</script>")
            elif q1.User_Type=='Working Staff':
                q2=tbl_Staff.objects.get(USERNAME_id=request.session['lid'])
                if q2:
                    request.session['sid']=q2.pk
                    return HttpResponse("<script>alert('succesfully logged in');window.location='/wstaff_home'</script>")
            elif q1.User_Type=='Customer':
                q3=tbl_Customer.objects.get(USERNAME_id=request.session['lid'])
                if q3:
                    request.session['cid']=q3.pk
                return HttpResponse("<script>alert('succesfully logged in');window.location='/customer_home'</script>")
            elif q1.User_Type=='Field Staff':
                q3=tbl_Staff.objects.get(USERNAME_id=request.session['lid'])
                if q3:
                    request.session['fid']=q3.pk
                return HttpResponse("<script>alert('succesfully logged in');window.location='/fstaff_home'</script>")
        else:
            return HttpResponse("<script>alert('invalid crediantials');window.location='/log'</script>")     
    return render(request,'publicpages/public_login.html')   

def signup(request):
    if 'submit' in request.POST :
        Username=request.POST['Username']
        Password=request.POST['Password']
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Phone=request.POST['Phone']
        House=request.POST['House']
        District=request.POST['Dist']
        City=request.POST['City']
        Pincode=request.POST['Pin']
        Place=request.POST['Place']
        DOB=request.POST['DOB']
        Gender=request.POST['Gender']

        
      
        q4=tbl_Login(Username=Username,Password=Password,User_Type='Customer',User_Status='active')
        q4.save()
        q2=tbl_Customer(Customer_Fname=Fname,Customer_Lname=Lname,Customer_City=City,Customer_House=House,
                     Customer_Dist=District,Customer_Pin=Pincode,Customer_Place=Place,Customer_Phone=Phone,
                     Customer_Gender=Gender,Customer_DOB=DOB,Customer_Status='active',USERNAME_id=Username,
                     )
        q2.save()
        return HttpResponse("<script>alert('Successfully Signed up');window.location='/signup'</script>")
    
    return render(request,'publicpages/public_signup.html')

def adminhome(request):
    return render(request,'adminpages/adminhome.html')

def Customer(request):
    q3=tbl_Customer.objects.all()
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time 
    return render(request,'adminpages/Customer.html',{'q3':q3, 'today_date': today_date, 'current_time': current_time})
# /////////////////////////////////////////


def Staff(request):
    q3=tbl_Staff.objects.all()
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time
    if 'submit' in request.POST :
        Username=request.POST['Username']
        Password=request.POST['password']
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Number=request.POST['Number']
        House=request.POST['House']
        District=request.POST['District']
        City=request.POST['City']
        Pincode=request.POST['Pincode']
        Place=request.POST['Place']
        DOB=request.POST['DOB']
        Gender=request.POST['Gender']
        Type=request.POST['Type']
        Photo=request.FILES['Photo']
       
        
        
        
        q2=tbl_Login(Username=Username,Password=Password,User_Type=Type,User_Status='active')
        q2.save()
        q1=tbl_Staff(Staff_Fname=Fname,Staff_Lname=Lname,Staff_City=City,Staff_House=House,
                     Staff_Dist=District,Staff_Pin=Pincode,Staff_Place=Place,Staff_Phone=Number,
                     Staff_Gender=Gender,Staff_Photo=Photo,Staff_DOB=DOB,Staff_Status='active',USERNAME_id=Username,
                     Staff_Type=Type)
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Staff'</script>")
        
    return render(request,'adminpages/Staff.html',{'q3':q3, 'today_date': today_date, 'current_time': current_time})

def adminupdatestaff(request,id):
    q4=tbl_Staff.objects.get(id=id)
    if 'update' in request.POST :
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Number=request.POST['Number']
        House=request.POST['House']
        District=request.POST['District']
        City=request.POST['City']
        Pincode=request.POST['Pincode']
        Place=request.POST['Place']
        DOB=request.POST['DOB']
        Gender=request.POST['Gender']
        Type=request.POST['Type']
        Photo=request.FILES['Photo']
        q4.Staff_Fname=Fname
        q4.Staff_Lname=Lname
        q4.Staff_Phone=Number
        q4.Staff_House=House
        q4.Staff_Dist=District
        q4.Staff_City=City
        q4.Staff_Pin=Pincode
        q4.Staff_Place=Place
        q4.Staff_DOB=DOB
        q4.Staff_Gender=Gender
        q4.Staff_Type=Type
        q4.Staff_Photo=Photo
        
        q4.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/Staff'</script>")
        
    return render(request,'adminpages/Staff.html',{'q4':q4})

def admin_inactive_staff(request,id):
    q4=tbl_Login.objects.get(Username=id)
    q4.User_Status="inactive"
    q4.save()
    up=tbl_Staff.objects.get(USERNAME_id=id)
    up.Staff_Status="inactive"
    up.save()
    return HttpResponse("<script>alert('Inactivated');window.location='/Staff'</script>")

def admin_active_staff(request,id):
    q4=tbl_Login.objects.get(Username=id)
    q4.User_Status="active"
    q4.save()
    up=tbl_Staff.objects.get(USERNAME_id=id)
    up.Staff_Status="active"
    up.save()
    return HttpResponse("<script>alert('Activated');window.location='/Staff'</script>")

def Category(request):
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time
    q1=tbl_Category.objects.all()
    if 'submit' in request.POST :
        Categoryname=request.POST['Categoryname']
        Description=request.POST['Description']
        q1=tbl_Category(Cat_Name=Categoryname,Cat_Desc=Description)
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Category'</script>")
    
    return render(request,'adminpages/Category.html',{'q1':q1, 'today_date': today_date, 'current_time': current_time})

def adminupdatecategory(request,id):
    q3=tbl_Category.objects.get(id=id)
    if 'update' in request.POST :
        Categoryname=request.POST['Categoryname']
        Description=request.POST['Description']
       
        q3.Cat_Name=Categoryname
        q3.Cat_Desc=Description
        q3.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/Category'</script>")
    return render(request,'adminpages/Category.html',{'q3':q3})

def Subcategory(request):
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time
    q1=tbl_Subcategory.objects.all()
    if 'submit' in request.POST :
        Subcatname=request.POST['Subcategoryname']
        Description=request.POST['Description']
       
        
        q1=tbl_Subcategory(Subcat_Name=Subcatname,Subcat_Desc=Description)
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Subcategory'</script>")
    return render(request,'adminpages/Subcategory.html',{'q1':q1, 'today_date': today_date, 'current_time': current_time})

def adminupdatesubcategory(request,id):
    q3=tbl_Subcategory.objects.get(id=id)
    if 'update' in request.POST :
        Subcatname=request.POST['Subcategoryname']
        Description=request.POST['Description']
        
        q3.Subcat_Name=Subcatname
        q3.Subcat_Desc=Description
        q3.save()
       
        
        return HttpResponse("<script>alert('Successfully updated');window.location='/Subcategory'</script>")
    return render(request,'adminpages/Subcategory.html',{'q3':q3})

def Brand(request):
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time
    q4=tbl_Brand.objects.all()
    if 'submit' in request.POST :
        Brandname=request.POST['Brandname']
        Description=request.POST['Description']
       
        
        q4=tbl_Brand(Brand_Name=Brandname,Brand_Desc=Description)
        q4.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Brand'</script>")
    return render(request,'adminpages/Brand.html',{'q4':q4, 'today_date': today_date, 'current_time': current_time})

def adminupdatebrand(request,id):
    q2=tbl_Brand.objects.get(id=id)
    if 'update' in request.POST :
        Brandname=request.POST['Brandname']
        Description=request.POST['Description']
       
        q2.Brand_Name=Brandname
        q2.Brand_Desc=Description
        q2.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/Brand'</script>")
    return render(request,'adminpages/Brand.html',{'q2':q2})

    

def view_item(request):
    q1=tbl_Item.objects.all()
    q4=tbl_Category.objects.all()
    q5=tbl_Subcategory.objects.all()
    q6=tbl_Brand.objects.all()
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time() 
    if 'submit' in request.POST :
        Itemname=request.POST['Itemname']
        Itemimg=request.FILES['Itemimg']
        Price=request.POST['Price']
        Category=request.POST['Category']
        Subcategory=request.POST['Subcategory']
        Brand=request.POST['Brand']
        Description=request.POST['Description']  
        q1=tbl_Item(Item_Name=Itemname,Item_Image=Itemimg,Item_Price=Price,CAT_id=Category,SUBCAT_id=Subcategory,BRAND_id=Brand,Item_Desc=Description,Item_Status=1,year_of_ownership="nil",second_status=1,third_status="productadded",CUSTOMER_id="10000")
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/view_item'</script>")  
    return render(request,'adminpages/Item.html',{'q1':q1,'q4':q4,'q5':q5,'q6':q6, 'today_date': today_date, 'current_time': current_time})

def adminupdateitem(request,id):
    q3=tbl_Item.objects.get(id=id)
    q4=tbl_Category.objects.all()
    for i in q4:
        print(i)
    q5=tbl_Subcategory.objects.all()
    q6=tbl_Brand.objects.all()
    if 'update' in request.POST :
        Itemname=request.POST['Itemname']

        Price=request.POST['Price']
        Category=request.POST['Category']
        Subcategory=request.POST['Subcategory']
        Brand=request.POST['Brand']
        Description=request.POST['Description']  
        if 'Itemimg' in request.FILES:
                Itemimg=request.FILES['Itemimg']
         
        q3.Item_Name=Itemname
        q3.Item_Image=Itemimg
        q3.Item_Price=Price
        q3.CAT_id=Category
        q3.SUBCAT_id=Subcategory
        q3.BRAND_id=Brand
        q3.Item_Desc=Description
        q3.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/view_item'</script>")  
    return render(request,'adminpages/Item.html',{'q3':q3,'q4':q4,'q5':q5,'q6':q6})

from datetime import date, datetime

def adminsales(request):
    q = tbl_Order.objects.all()
    today_date = date.today()  # Get today's date
    current_time = datetime.now().time()  # Get current time
    return render(request, 'adminpages/admin_sales.html', {'q': q, 'today_date': today_date, 'current_time': current_time})


def adminreview(request):
    q3=tbl_Review.objects.all()
    return render(request,'adminpages/admin_review.html',{'q3':q3})



def admin_assign_verification(request):
    q = tbl_Item.objects.filter(
        Q(Item_Status='selling') | Q(Item_Status="assigned") | Q(Item_Status="verified") | Q(Item_Status="product added") | Q(Item_Status="on the way")
    )
    return render(request, 'adminpages/admin_assign_verification.html', {'q': q})



def verify_item(request,id):
    q=tbl_Staff.objects.filter(Staff_Type="Field Staff")
    if 'submit' in request.POST:
        staff=request.POST['staff']
        q=tbl_Item.objects.get(id=id)
        q.Item_Status='assigned'
        q.save()
        q=tbl_Vassign(Vassign_Date=datetime.now().date(),Status='pending',ITEM_id=id,STAFF_id=staff)
        q.save()
        return HttpResponse("<script>alert('assigned');window.location='/admin_assign_verification';</script>")
    return render(request,'adminpages/admin_assign_order.html',{'q':q})


def product_add(request,id):
    q=tbl_Item.objects.get(id=id)
    q.Item_Status='product added'
    q.third_status='productadded'
    q.save()
    return HttpResponse("<script>alert('product added');window.location='/admin_assign_verification';</script>")


def admin_delivery_status(request):
    q=tbl_Dassign.objects.all()
    return render(request,'adminpages/admin_delivery_status.html',{'q':q})

def wstaff_home(request):
    return render(request,'working_staff_pages/wstaff_home.html')

def Staff_customer(request):
     q4=tbl_Customer.objects.all()
     return render(request,'working_staff_pages/Staff_customer.html',{'q4':q4})

def Staff_Category(request):
    q1=tbl_Category.objects.all()
    if 'submit' in request.POST :
        Categoryname=request.POST['Categoryname']
        Description=request.POST['Description']
        q1=tbl_Category(Cat_Name=Categoryname,Cat_Desc=Description)
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Category'</script>")
    
    return render(request,'working_staff_pages/Staff_Category.html',{'q1':q1})

def staffupdatecategory(request,id):
    q3=tbl_Category.objects.get(id=id)
    if 'update' in request.POST :
        Categoryname=request.POST['Categoryname']
        Description=request.POST['Description']
       
        q3.Cat_Name=Categoryname
        q3.Cat_Desc=Description
        q3.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/Category'</script>")
    return render(request,'working_staff_pages/Staff_Category.html',{'q3':q3})

def Staff_Subcategory(request):
    q1=tbl_Subcategory.objects.all()
    if 'submit' in request.POST :
        Subcatname=request.POST['Subcategoryname']
        Description=request.POST['Description']
       
        
        q1=tbl_Subcategory(Subcat_Name=Subcatname,Subcat_Desc=Description)
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Subcategory'</script>")
    return render(request,'working_staff_pages/Staff_Subcategory.html',{'q1':q1})

def staffupdatesubcategory(request,id):
    q3=tbl_Subcategory.objects.get(id=id)
    if 'update' in request.POST :
        Subcatname=request.POST['Subcategoryname']
        Description=request.POST['Description']
        
        q3.Subcat_Name=Subcatname
        q3.Subcat_Desc=Description
        q3.save()
       
        
        return HttpResponse("<script>alert('Successfully updated');window.location='/Subcategory'</script>")
    return render(request,'working_staff_pages/Staff_Subcategory.html',{'q3':q3})
    
def Staff_Brand(request):
    q4=tbl_Brand.objects.all()
    if 'submit' in request.POST :
        Brandname=request.POST['Brandname']
        Description=request.POST['Description']
       
        
        q4=tbl_Brand(Brand_Name=Brandname,Brand_Desc=Description)
        q4.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/Brand'</script>")
    return render(request,'working_staff_pages/Staff_Brand.html',{'q4':q4})

def staffupdatebrand(request,id):
    q2=tbl_Brand.objects.get(id=id)
    if 'update' in request.POST :
        Brandname=request.POST['Brandname']
        Description=request.POST['Description']
       
        q2.Brand_Name=Brandname
        q2.Brand_Desc=Description
        q2.save()
        
        return HttpResponse("<script>alert('Successfully Updated');window.location='/Brand'</script>")
    return render(request,'working_staff_pages/Staff_Brand.html',{'q2':q2})

def Staff_item(request):
    return render(request,'working_staff_pages/Staff_item.html')
def Assign_field(request):
    return render(request,'working_staff_pages/Assign_field.html')
def Staff_sales(request):
    return render(request,'working_staff_pages/Staff_sales.html')
def Staff_review(request):
    return render(request,'working_staff_pages/Staff_review.html')


def customer_home(request):
    return render(request,'customer_pages/customer_home.html')

def customer_order(request):
    return render(request,'customer_pages/cust_view_order.html')

def customer_review(request):
    if 'submit' in request.POST:
        description=request.POST['description']
        y=tbl_Review(Review_Desc=description,CUSTOMER_id=request.session['cid'],ITEM_id=1)
        y.save()
    return render(request,'customer_pages/cust_add_review.html')

def customer_profile(request):
    return render(request,'customer_pages/cust_profile.html')
def customer_aboutus(request):
    return render(request,'customer_pages/cust_aboutus.html')

def cust_view_products(request):
    q=tbl_Item.objects.filter(third_status="productadded")
    
    x=tbl_Category.objects.filter()
    y=tbl_Subcategory.objects.filter()
    z=tbl_Brand.objects.filter()
    return render(request,'customer_pages/cust_view_products.html',{'q':q,'x':x,'y':y,'z':z})

# def cust_Search_product(request):


def temp(request):
    return render(request,'index.html')

def tempy(request):
    return render(request,'adminpages/admin_index.html')

def addtocart(request,id):
    q=tbl_Item.objects.get(id=id)
    amount=q.Item_Price
    if tbl_Cartmast.objects.filter(CUSTOMER_id=request.session['cid'],Cart_Status='pending').exists():
        f=tbl_Cartmast.objects.get(CUSTOMER_id=request.session['cid'],Cart_Status='pending')
        if tbl_Cartchild.objects.filter(CART_MASTER_id=f.pk,Item=id).exists():
             return HttpResponse("<script>alert('Already in cart');window.location='/cust_view_products';</script>")
        else:
            ff=tbl_Cartchild(Cart_Quantity=1,CART_MASTER_id=f.pk,Item_id=id)
            ff.save()
            f.Total_Amount = str(int(f.Total_Amount) + int(amount))
            print(f)
            f.save()
            return HttpResponse("<script>alert('success');window.location='/cust_view_products';</script>")
    else:
        qi=tbl_Cartmast(Total_Amount=amount,Cart_Status='pending',CUSTOMER_id=request.session['cid'])
        qi.save()
        qt=tbl_Cartchild(Cart_Quantity=1,CART_MASTER_id=qi.pk,Item_id=id)
        qt.save()
        return HttpResponse("<script>alert('success');window.location='/cust_view_products';</script>")


def customer_cart(request):
    if tbl_Cartmast.objects.filter(CUSTOMER_id=request.session.get('cid'),Cart_Status='pending').exists():
        q = tbl_Cartmast.objects.get(CUSTOMER_id=request.session.get('cid'),Cart_Status='pending')
        cid=q.pk
        qi = tbl_Cartchild.objects.filter(CART_MASTER_id=cid)
    else:
        cid=None
        qi=None
    return render(request, 'customer_pages/cust_view_cart.html', {'qi': qi,'cid':cid})


def delete_cart(request,id):
    q=tbl_Cartchild.objects.get(id=id)
    cid=q.CART_MASTER_id
    cq=tbl_Cartmast.objects.get(id=cid)
    tamount=int(q.Item.Item_Price)*int(q.Cart_Quantity)
    cq.Total_Amount=str(int(cq.Total_Amount)-int(tamount))
    cq.save()
    q.delete()
    return HttpResponse("<script>alert('removed');window.location='/customer_cart'</script>")

def increase_qty(request, id):
    q = tbl_Cartchild.objects.get(id=id)
    q.Cart_Quantity = str(int(q.Cart_Quantity) + 1)
    q.save()
    cid = q.CART_MASTER_id
    qi = tbl_Cartmast.objects.get(id=cid)
    qi.Total_Amount = str(int(qi.Total_Amount) + int(q.Item.Item_Price))
    qi.save()
    return HttpResponse("<script>window.location='/customer_cart'</script>")

def decrease_qty(request, id):
    q = tbl_Cartchild.objects.get(id=id)
    if int(q.Cart_Quantity) >= 2:
        q.Cart_Quantity = str(int(q.Cart_Quantity) - 1)
        q.save()
        
        cid = q.CART_MASTER_id
        qi = tbl_Cartmast.objects.get(id=cid)
        qi.Total_Amount = str(int(qi.Total_Amount) - int(q.Item.Item_Price))
        qi.save()
    
    return HttpResponse("<script>window.location='/customer_cart'</script>")

from django.db.models import Max


def customer_order(request, id):
    kkk=tbl_Customer.objects.get(id=request.session['cid'])
    q = tbl_Cartmast.objects.get(id=id)
    amount = q.Total_Amount
    q.Cart_Status='ordered'
    q.save()
    
    if 'submit' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        city = request.POST['city']
        house = request.POST['house']
        district = request.POST['district']
        pincode = request.POST['pincode']
        place = request.POST['place']
        phone = request.POST['phone']
        

        latest_bill_no = tbl_Order.objects.aggregate(Max('Bill_No'))['Bill_No__max']
        if latest_bill_no is None:
            latest_bill_no = 1000  
        

        new_bill_no = int(latest_bill_no) + 1
        
      
        q = tbl_Order(
            A_Fname=fname, A_Lname=lname, A_City=city, A_House=house, A_Dist=district, A_Pin=pincode,
            A_Place=place, A_Phone=phone, Order_Status='pending', Order_Date=datetime.now().date(),
            Order_Amount=amount, Bill_No=new_bill_no,CART_MASTER_id=id
        )
        q.save()
        id2=q.pk
        return HttpResponse(f"<script>alert('ordered');window.location='/customer_payment/{id2}'</script>")
    elif 'alternate' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        city = request.POST['city']
        house = request.POST['house']
        district = request.POST['district']
        pincode = request.POST['pincode']
        place = request.POST['place']
        phone = request.POST['phone']
        

        latest_bill_no = tbl_Order.objects.aggregate(Max('Bill_No'))['Bill_No__max']
        if latest_bill_no is None:
            latest_bill_no = 1000  
        

        new_bill_no = int(latest_bill_no) + 1
        
      
        q = tbl_Order(
            A_Fname=fname, A_Lname=lname, A_City=city, A_House=house, A_Dist=district, A_Pin=pincode,
            A_Place=place, A_Phone=phone, Order_Status='pending', Order_Date=datetime.now().date(),
            Order_Amount=amount, Bill_No=new_bill_no,CART_MASTER_id=id
        )
        q.save()
        id2=q.pk
        return HttpResponse(f"<script>alert('ordered');window.location='/customer_payment/{id2}'</script>")
        
    return render(request, 'customer_pages/customer_order.html',{'kkk':kkk})


# def cust_view_order(request):
#     return render(request,'customer_pages/cust_view_order.html')

# def event(request):
#     return render(request,'customer_pages/event.html')

def customer_payment(request, id):
    s=tbl_Order.objects.get(id=id)
    f = None  
    if tbl_Card.objects.filter(CUSTOMER_id=request.session['cid']).exists():
     
        f = tbl_Card.objects.filter(CUSTOMER_id=request.session['cid']).latest('id')

    if 'submit' in request.POST:
        dd=id
        cardno = request.POST.get('cardno')
        holdername = request.POST.get('holdername') 
        expdate = request.POST.get('expdate')

        if not f:
            
            f = tbl_Card(Card_No=cardno, Card_Holdername=holdername, Expire_Date=expdate, CUSTOMER_id=request.session['cid'])
            f.save()

       
        qi = tbl_Payment(Payment_Date=datetime.now().date(), Payment_Status='paid', CARD_id=f.pk, ORDER_id=id)
        qi.save()
        o=tbl_Order.objects.get(id=id)
        o.Order_Status="paid"
        o.save()

       
        order_id = id  
        order = tbl_Order.objects.get(id=order_id)

        # Access the associated cart master
        cart_master = order.CART_MASTER

        # Access the items in the cart master
        cart_items = cart_master.tbl_cartchild_set.all()

        # Iterate through each item and update the third_status field
        for cart_item in cart_items:
            item = cart_item.Item
            # Assuming third_status field is in tbl_Item model
            item.third_status = "sold"
            item.save()
            

        return HttpResponse(f"<script>alert('payment successful');window.location='/cust_view_bill/{dd}'</script>")
        
    return render(request, 'customer_pages/customer_payment.html', {'f': f,'s':s})

def cust_view_bill(request,id):
    q=tbl_Order.objects.get(id=id)
    qt=tbl_Payment.objects.get(ORDER_id=id)
    qi=tbl_Cartchild.objects.filter(CART_MASTER_id=q.CART_MASTER_id)
    return render(request,'customer_pages/cust_view_bill.html',{'q':q,'qi':qi,'qt':qt})

def cust_view_paid_orders(request):
    orders = tbl_Order.objects.filter(CART_MASTER__CUSTOMER_id=request.session.get('cid', None))
    
    return render(request, 'customer_pages/cust_view_paid_orders.html', {'orders': orders})


def cust_view_single_product_bill(request, id):
    q=tbl_Order.objects.get(id=id)
    qt=tbl_Payment.objects.get(ORDER_id=id)
    qi=tbl_Cartchild.objects.filter(CART_MASTER_id=q.CART_MASTER_id)
    
    return render(request, 'customer_pages/cust_view_single_product_bill.html', {'q':q,'qi':qi,'qt':qt})

def cust_view_orderd_items(request,id):
    q=tbl_Order.objects.filter(id=id)
    for i in q:
        qi=tbl_Cartchild.objects.filter(CART_MASTER_id=i.CART_MASTER_id)
 
    return render(request,'customer_pages/cust_view_orderd_items.html',{'qi':qi})


def cust_add_item_review(request,id):
    if 'submit' in request.POST:
        description=request.POST['description']
        q=tbl_Review(Review_Desc=description,CUSTOMER_id=request.session['cid'],ITEM_id=id)
        q.save()
        return HttpResponse("<script>alert('Thanks for your review');window.location='/cust_view_paid_orders'</script>")
    return render(request,'customer_pages/cust_add_item_review.html')



def cust_sell_itemss(request):
    q1=tbl_Item.objects.filter(second_status="pending")
    q4=tbl_Category.objects.all()
    q5=tbl_Subcategory.objects.all()
    q6=tbl_Brand.objects.all()
    if 'submit' in request.POST :
        Itemname=request.POST['Itemname']
        Itemimg=request.FILES['Itemimg']
        Price=request.POST['Price']
        Category=request.POST['Category']
        Subcategory=request.POST['Subcategory']
        Brand=request.POST['Brand']
        Description=request.POST['Description'] 
        ownership=request.POST['ownership'] 
        q1=tbl_Item(Item_Name=Itemname,Item_Image=Itemimg,Item_Price=Price,CAT_id=Category,SUBCAT_id=Subcategory,BRAND_id=Brand,Item_Desc=Description,Item_Status="pending",year_of_ownership=ownership,second_status="pending",third_status="not verified",CUSTOMER_id=request.session['cid'])
        q1.save()
        return HttpResponse("<script>alert('Successfully Saved');window.location='/cust_sell_itemss'</script>")  
    return render(request, 'customer_pages/cust_sell_itemss.html',{'q1':q1,'q4':q4,'q5':q5,'q6':q6})

def cust_sell_itemss_update(request,id):
    # q1=tbl_Item.objects.filter(second_status="pending")
    q3=tbl_Item.objects.get(id=id)
    q4=tbl_Category.objects.all()
    for i in q4:
        print(i)
    q5=tbl_Subcategory.objects.all()
    q6=tbl_Brand.objects.all()
    if 'update' in request.POST :
        Itemname=request.POST['Itemname']
        Price=request.POST['Price']
        Category=request.POST['Category']
        Subcategory=request.POST['Subcategory']
        Brand=request.POST['Brand']
        Description=request.POST['Description']  
        ownership=request.POST['ownership'] 
        if 'Itemimg' in request.FILES:
                Itemimg=request.FILES['Itemimg']
         
        q3.Item_Name=Itemname
        q3.Item_Image=Itemimg
        q3.Item_Price=Price
        q3.CAT_id=Category
        q3.SUBCAT_id=Subcategory
        q3.BRAND_id=Brand
        q3.Item_Desc=Description
        q3.year_of_ownership=ownership
        q3.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/cust_sell_itemss'</script>")  
    return render(request,'customer_pages/cust_sell_itemss.html',{'q3':q3,'q4':q4,'q5':q5,'q6':q6})

def Sell_now_button(request, id):
    q = tbl_Item.objects.get(id=id)
    q.Item_Status="selling"
    q.save()
    return HttpResponse("<script>window.location='/cust_sell_itemss'</script>")

def selling_product_status(request):
    q1 = tbl_Item.objects.filter(CUSTOMER_id=request.session['cid'])
    return render(request, 'customer_pages/selling_product_status.html', {'q1': q1})


import random
from datetime import date
def cust_view_bill_for_sold_product(request, itemid):
    q = tbl_Item.objects.filter(id=itemid)
    rand_num = random.randint(1000, 1999)  # Generate a random number between 1000 and 1999
    today_date = date.today()  # Get today's date
    return render(request, 'customer_pages/cust_view_bill_for_sold_product.html', {'q': q, 'rand_num': rand_num, 'today_date': today_date})



def disclaimer(request):
    confirmation_message = """
        var confirmMessage = '5% of the total amount claimed by the seller will be granted to the admin.';
        var confirmLogout = confirm(confirmMessage);
        if (confirmLogout) {
            window.location = '/cust_sell_items';
        } else {
            window.history.back();
        }
    """
    return HttpResponse("<script>" + confirmation_message + "</script>")


from django.db.models import Q

def adminorderview(request):
    q = tbl_Order.objects.filter(
        Q(Order_Status="paid") | 
        Q(Order_Status="assigned") |
        Q(Order_Status="on the way") |
        Q(Order_Status="delivered")
    )
    return render(request, 'adminpages/adminorderview.html', {'q': q}) 

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

# def update_order_status(sender, instance, **kwargs):
#     if instance.Delivery_Status != 'Delivered':
       
#         dassign_date = datetime.strptime(instance.Dassign_Date, '%Y-%m-%d')
#         if datetime.now() - dassign_date <= timedelta(days=7):
            
#             instance.ORDER.Order_Status = 'paid'
#             instance.ORDER.save()
#             return HttpResponse("<script>alert('assigned');window.location='/adminorderview'</script>")


def admin_assign_order(request,id): 
    q=tbl_Staff.objects.filter(Staff_Type="Field Staff")
    if 'submit' in request.POST:
        staff=request.POST['staff']
        q=tbl_Dassign(Dassign_Date=datetime.now().date(),Delivery_Date='pending',Delivery_Status='pending',ORDER_id=id,STAFF_id=staff)
        q.save()
        j=tbl_Order.objects.get(id=id)
        j.Order_Status="assigned"
        j.save()
        return HttpResponse("<script>alert('assigned');window.location='/adminorderview'</script>")
    return render(request,'adminpages/admin_assign_order.html',{'q':q})


###############################################################################

#fstaff

def fstaff_home(request):
    return render(request,'Field_staff_pages/fstaff_home.html')

from django.db.models import Q

def fwork_view_order(request):
    q = tbl_Dassign.objects.filter(
        Q(Delivery_Status="pending") | Q(Delivery_Status="on the way"),
        STAFF_id=request.session['fid']
    )
    return render(request, 'Field_staff_pages/view_order.html', {'q': q})

def fstaff_update_staff(request,id):
    if 'submit' in request.POST:
        status=request.POST['status']
        q=tbl_Dassign.objects.get(id=id)
        q.Delivery_Status=status
        q.save()
        orderid=q.ORDER_id
        qi=tbl_Order.objects.get(id=orderid)
        qi.Order_Status=status
        qi.save()
        return HttpResponse("<script>alert('updated');window.location='/fwork_view_order'</script>")
        
    return render(request,'Field_staff_pages/update_status.html')

def fwork_view_verifyy(request):
    q=tbl_Vassign.objects.filter(STAFF_id=request.session['fid'])
    return render(request,'Field_staff_pages/view_item_verify.html',{'q':q})

def fstaff_verify_update_status(request, id):
    if 'submit' in request.POST:
        status = request.POST['status']
        q = tbl_Vassign.objects.get(id=id)
        q.Status = status
        q.save()
        
        # Get the item_id from tbl_Vassign
        item_id = q.ITEM_id
        
        # Update the corresponding item's status
        qi = tbl_Item.objects.get(id=item_id)
        qi.Item_Status = status
        qi.save()
        
        return HttpResponse("<script>alert('updated');window.location='/fwork_view_verifyy'</script>")
        
    return render(request, 'Field_staff_pages/fstaff_verify_update_status.html')
