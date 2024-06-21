

#Run this command (python -m pip install --upgrade pip) to upgrade the version of Pip otherwise its showing some error.
import os
import platform
import mysql.connector #run this (pip install mysql-connector-python)command to instaal the package of connector
import pandas as pd
import datetime


mysql=mysql.connector.connect(host="localhost",user="root",passwd="root",database="fashion_store")

mycursor=mysql.cursor()

def Add_Product():
    l=[]
    stk=[]
    
    
    Pid=input("Enter the product Id : ")
    l.append(Pid)
    
    Pname=input("Enter the Product Name : ")
    l.append(Pname)
    
    brand=input("Enter the  Product brand name : ")
    l.append(brand)
    
    FM=input("Enter the Male/ Female : ")
    l.append(FM)
    
    Seasion=input("Enter the Winter/Summer/Raining : ")
    l.append(Seasion)
    
    Prate=int(input("Enter the Rate range for product : "))
    l.append(Prate)
    
    product=(l)
    
    sql="insert into product(Product_Id,Product_Name,Product_Brand,Product_for male/female,Seasion,Rate)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,product)
    mysql.commit()
    
    stk.append(Pid)
    stk.append(0)
    stk.append("NO")
    
    st=(stk)
    
    sql="insert into stock(Item_id,Instock,status)values(%s%s%s)"
    mycursor.execute(sql,st)
    mysql.commit()
    
    print("One Product inserted")


def Edit_Product():
    Pid=int(input("Enter the product Id to be Edited : "))
    sql="select * from Product where Product_Id=%S"
    
    ed=(Pid)
    
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    print("")
    
    field=input("Enter the field which you want to edit : ")
    val=input("Enter the value that you want to set : ")
    
    sql="Update Product set "+field+" = "+val+" where Product_Id = "+Pid+"'"
    sq=sql
    mycursor.execute(sql)
    
    print("Editing Done")
    
    print("After the correction the record is : ")
    
    sql="select*from where Product_id = %s"
    ed(Pid)
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    mysql.commit()



def Delete_Product():
    Pid=input("Enter the Pid to delete the Product : ")
    sql="delete from Sales where item_Id = %s"
    id=(Pid)
    mycursor.execute(sql,id)
    mysql.commit()
    
    sql="delete from Purchase where item_id=%s"
    mycursor.execute(sql,id)
    mysql.commit()
    
    sql="delete from stock where item_Id=%s"
    mycursor.execute(sql,id)
    mysql.commit()
    
    sql="delete from Product where Product_Id=%s"
    mycursor.execute(sql,id)
    mysql.commit()
    
    print("One Item Deleted...")
    


def View_Product():
    print("Select one to display the data : ")
    print("1. All Details : ")
    print("2. Product name : ")
    print("3. Product Brand : ")
    print("4. Product For Male/Female : ")
    print("5. Product Seasion : ")
    print("6. Product Id : ")
    
    x=0 
    
    ch=int(input("Enter your Choice to display : "))
    
    if ch==1:
        sql="select *from Product"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        for x in res:
            print(x)
        x=1
    elif ch==2:
        var="Product_Name"
        val=input("Enter the name of Product : ")
    elif ch==3:
        var="Product_Brand"
        val=input("Enter the Brand of Product : ")
    elif ch==4:
        var="Product_For Male/Female"
        val=input("Enter the Product for Male/Female : ")
    elif ch==5:
        var="Seasion"
        val=input("Enter the Seasion of Product : ")
    elif ch==6:
        var="Product_Id"
        val=input("Enter the Id of Product : ")
    if x==0:
        sql="select *from Product where "+var+"=%s"
        sq=(sql)
        tp=(val,)
        mycursor.execute(sq,tp)
        res=mycursor.fetchall()
        for x in res:
            print(x)


def Purchase_Product():
    mon=""
    dy=""
    now=datetime.datetime.now()
    purchaseId="P"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    
    l=[]
    lst=[]
    l.append(purchaseId)
    itemId=input("Enter the Product Id : ")
    l.append(itemId)
    
    itemNo=int(input("Enter the number of items : "))
    l.append(itemNo)
    sql="select rate from Product where Product_Id=%s"
    Pid=(itemId,)
    
    mycursor.execute(sql,Pid)
    res=mycursor.fetchall()
    for x in res:
        print("Rate is : ",x)
    amount=x*itemNo
    print("Amount is : ",amount)
    l.append(amount)
    mnth=now.month()
    if mnth<=9:
        mon="0"+str(mnth)
    else:
        mn=str(mnth)
    day=now.day
    if day <= 9:
        dy="0"+str(day)
    else:
        dy=str(day)
    dt=str(now.year)+"-"+mn+"-"+dy
    l.append(dt)
    tp(l)
    
    sql="insert into purchase(purshase_Id,Item_Id,No-of-item,amount,Purchase_date)values(%s%s%s%s%s)"
    mycursor.execute(sql,tp)
    mysql.commit()
    
    sql="select inStock from Stock where item_Id=%s"
    mycursor.execute(sql,Pid)
    res=mycursor.fetchall()
    status="No"
    for x in res:
        print(x)
    instock=x[0]+itemNo
    if instock>0:
        status="Yes"
    lst.append(instock)
    lst.append(status)
    lst.append(itemId)
    tp=(lst)
     
    sql="update stock set instock=%s,status=%s,where item_Id=%s"
    mycursor.execute(sql,tp)
    mysql.commit()
    
    print("1.Item Puchase and save in database : ")
    
def View_Purchase():
    item=input("Enter Product Name : ")
    sql="select Product.product_id,Product.Product_Name,Product.brand,purchase.no_of_items,purchase.purchase_date,purchase.amount from product INNER JOIN purchase ON product.product_id=purchase.item_id and product.PName=%s"
    itm=(item,)
    mycursor.execute(sql,itm)
    res=mycursor.fetchall()
    for x in res:
        print(x)


def View_stock():
    item=input("Enter Product name : ")
    sql="select Product.Product_Id,Product.Product_Name,stock.Instock,\stock.status from stock,Product where \ Product.Product_Id=stock.item_Id and Product.Product_Name=%s"
    item=(item,)
    
    mycursor.execute(sql,item)
    res=mycursor.fetchall()
    for x in res:
        print(x)

def Sale_Product():
    now=datetime.datetime.now()
    saleId="S"+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    l=[]
    l.append(saleId)
    itemId=input("Enter Product Id : ")
    l.aapend(itemId)
    
    itemNo=int(input("Enter the Number of Items : "))
    l.append(itemNo)
    
    sql="select rate from Product where Product_Id=%s"
    Pid=(itemId)
    mycursor.execute(sql,Pid)
    res=mycursor.fetchall()
    for x in res:
        print("rate of the Items: ",x)
    dis=int(input("Enter the discount : "))
    saleRate=x[0]-(x[0]*dis/100)
    l.append(saleRate)  
    amount=itemNo * saleRate 
    l.append(amount)
    mnth=now.month
    
    if mnth<=9:
        mn="0"+str(mnth)
    else:
        mn=str(mnth)
    day=now.day
    
    if day<=9:
        dy="0"+str(day)
    else:
        dy=str(day)
    dt=str(now.year)+"-"+mn+"-"+dy
    l.append(dt)
    tp=(l)
    
    sql="insert into sales(sale_id,item_id,no_of_item_solid,\sale_rate,amount,date_of_sale)values(%s%s%s%s%s%s)"
    mycursor.execute(sql,tp)
    mysql.commit()
    
    sql="select Instock from stock where item_id=%s"
    mycursor.execute()
    mysql.commit()
    
    sql="select Instock from stock where item_id=%s"
    mycursor.execute()
    res=mycursor.fetchall()
    for x in res:
        print("Total itme in stock are : ",x )
    instock=x[0]-itemNo
    if instock > 0:
        status="Yes"
    tp=(instock,status,itemId)
    sql="update stock set instock=%s,status=%s where item_id=%s"
    print("remaining item in stock are : ",instock)
    mycursor.execute(sql,tp)
    mysql.commit()
    
def View_sales():
    item=input("Enter Product Name : ")
    
    sql="select Product.Product_Id,Product.Product_Name,Product.Brand,\sales.no_of_item_sold,sales.date_of_sale,sales_amount\from sales,Product where Product.Product_Id=sales.item_id\and Product.Product_Name=%s"
    item=(item,)
    mycursor.execute(sql,item)
    res=mycursor.fetchall()
    for x in res:
        print(x)
def Menu_set():
    print("Enter 1 : To Add Product ")
    print("Enter 2 : To Edit Product ")
    print("Enter 3 : To Delete Product ")
    print("Enter 4 : To View Product ")
    print("Enter 5 : To Purchase Product ")  
    print("Enter 6 : To View  Purshase ")
    print("Enter 7 : To view Stock details ")
    print("Enter 8 : To sale the item ")
    print("Enter 9 : To View sale detail ")
    try:
        userInput=int(input("Please Select an Above Option : "))
    except ValueError:
        exit("that's Not a Number ")
    else:
        print("\n")
    if (userInput==1):
        Add_Product()
        
    elif (userInput==2):
        Edit_Product()
        
    elif(userInput==3):
        Delete_Product()
        
    elif(userInput==4):
        View_Product()
        
    elif(userInput==5):
        Purchase_Product()
        
    elif(userInput==6):
        View_Purchase()
        
    elif(userInput==7):
        View_stock()
        
    elif(userInput==8):
        Sale_Product()
        
    elif(userInput==9):
        View_sales()
        
    else:
        print("Enter Correct Choice ....")
        
        
print("Welcome to my Store ....")
print("developed by .....BABAJII GROUP.....")

Menu_set()
    
def Run_Again():
    run=input("Do Yu Want To Run Again y/n..")
    while(run.lower()=='y'):
        if(platform.system()=="Window"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menu_set()
Run_Again()
        
                


    