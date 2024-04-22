from django.db import models

# Create your models here.
class tbl_Login(models.Model):
    Username=models.CharField(max_length=100,primary_key=True)
    Password=models.CharField(max_length=100)
    User_Type=models.CharField(max_length=100)
    User_Status=models.CharField(max_length=100)

class tbl_Staff(models.Model):
    USERNAME=models.ForeignKey(tbl_Login,on_delete=models.CASCADE)
    Staff_Fname=models.CharField(max_length=100)
    Staff_Lname=models.CharField(max_length=100)
    Staff_City=models.CharField(max_length=100)
    Staff_House=models.CharField(max_length=100)
    Staff_Dist=models.CharField(max_length=100)
    Staff_Pin=models.CharField(max_length=100)
    Staff_Place=models.CharField(max_length=100)
    Staff_Phone=models.CharField(max_length=100)
    Staff_Gender=models.CharField(max_length=100)
    Staff_Photo=models.ImageField(upload_to='static/staff')
    Staff_DOB=models.CharField(max_length=100)
    Staff_Status=models.CharField(max_length=100)
    Staff_Type=models.CharField(max_length=100)
    
class tbl_Customer(models.Model):
    USERNAME=models.ForeignKey(tbl_Login,on_delete=models.CASCADE)
    Customer_Fname=models.CharField(max_length=100)
    Customer_Lname=models.CharField(max_length=100)
    Customer_City=models.CharField(max_length=100)
    Customer_House=models.CharField(max_length=100)
    Customer_Dist=models.CharField(max_length=100)
    Customer_Pin=models.CharField(max_length=100)
    Customer_Place=models.CharField(max_length=100)
    Customer_Phone=models.CharField(max_length=100)
    Customer_Gender=models.CharField(max_length=100)
    Customer_DOB=models.CharField(max_length=100)
    Customer_Status=models.CharField(max_length=100)
    
class tbl_Category(models.Model):
    Cat_Name=models.CharField(max_length=100)
    Cat_Desc=models.CharField(max_length=100)

class tbl_Subcategory(models.Model):
    Subcat_Name=models.CharField(max_length=100)
    Subcat_Desc=models.CharField(max_length=100)
    
class tbl_Subcategory(models.Model):
    Subcat_Name=models.CharField(max_length=100)
    Subcat_Desc=models.CharField(max_length=100)

class tbl_Brand(models.Model):
    Brand_Name=models.CharField(max_length=100)
    Brand_Desc=models.CharField(max_length=100)
    
class tbl_Item(models.Model):
    Item_Name=models.CharField(max_length=100)
    Item_Image=models.ImageField(upload_to='static/item')
    CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
    CAT=models.ForeignKey(tbl_Category,on_delete=models.CASCADE)
    SUBCAT=models.ForeignKey(tbl_Subcategory,on_delete=models.CASCADE)
    BRAND=models.ForeignKey(tbl_Brand,on_delete=models.CASCADE)
    Item_Price=models.CharField(max_length=100)
    Item_Desc=models.CharField(max_length=100)
    Item_Status=models.CharField(max_length=100)
    year_of_ownership=models.CharField(max_length=100)
    second_status=models.CharField(max_length=100)
    third_status=models.CharField(max_length=100)
    
class tbl_Cartmast(models.Model):
    CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
    Total_Amount=models.CharField(max_length=100)
    Cart_Status=models.CharField(max_length=100)
    
class tbl_Cartchild(models.Model):
    CART_MASTER=models.ForeignKey(tbl_Cartmast,on_delete=models.CASCADE)
    Item=models.ForeignKey(tbl_Item,on_delete=models.CASCADE)
    Cart_Quantity=models.CharField(max_length=100)
    
class tbl_Order(models.Model):
      CART_MASTER=models.ForeignKey(tbl_Cartmast,on_delete=models.CASCADE)
      Order_Date=models.CharField(max_length=100)
      Order_Amount=models.CharField(max_length=100)
      Bill_No=models.CharField(max_length=100)
      A_Fname=models.CharField(max_length=100)
      A_Lname=models.CharField(max_length=100)
      A_City=models.CharField(max_length=100)
      A_House=models.CharField(max_length=100)
      A_Dist=models.CharField(max_length=100)
      A_Pin=models.CharField(max_length=100)
      A_Place=models.CharField(max_length=100)
      A_Phone=models.CharField(max_length=100)
      Order_Status=models.CharField(max_length=100)
      
class tbl_Card(models.Model):
      Card_No=models.CharField(max_length=100)
      CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
      Card_Holdername=models.CharField(max_length=100)
      Expire_Date=models.CharField(max_length=100)
      
class tbl_Payment(models.Model):
      CARD=models.ForeignKey(tbl_Cartmast,on_delete=models.CASCADE)
      Payment_Date=models.CharField(max_length=100)
      ORDER=models.ForeignKey(tbl_Order,on_delete=models.CASCADE)
      Payment_Status=models.CharField(max_length=100)
      
class tbl_Dassign(models.Model):
      STAFF=models.ForeignKey(tbl_Staff,on_delete=models.CASCADE)
      ORDER=models.ForeignKey(tbl_Order,on_delete=models.CASCADE)
      Dassign_Date=models.CharField(max_length=100)
      Delivery_Date=models.CharField(max_length=100)
      Delivery_Status=models.CharField(max_length=100)

class tbl_Vassign(models.Model):
      STAFF=models.ForeignKey(tbl_Staff,on_delete=models.CASCADE)
      ITEM=models.ForeignKey(tbl_Item,on_delete=models.CASCADE)
      Vassign_Date=models.CharField(max_length=100)
      Status=models.CharField(max_length=100)
      
class tbl_Review(models.Model):
      CUSTOMER=models.ForeignKey(tbl_Customer,on_delete=models.CASCADE)
      Review_Desc=models.CharField(max_length=100)
      ITEM=models.ForeignKey(tbl_Item,on_delete=models.CASCADE)

  
