import mysql.connector
import random


connection=mysql.connector.connect(host="remotemysql.com", user="5jBdUHTRPG", passwd = "QPMKcvQU51", database="5jBdUHTRPG")
cursor=connection.cursor()

def insert(product_code):
    serial_number=random.randint(1000,9999)
    if product_code!=0:
        print("The product_code exists")
    else:
        print("It doesn't exist")
        product_code=int(input("Enter the product code. Thank you!"))
    n='y'
    while n=="y" or n=="Y": 
        quantity=float(input(" Enter the quantity of the desired product"))
        expiry_date=input("Enter the expiry date of the product")
        storage_location=input(" Enter the place where the product is stored")
        purchase_price=float(input(" Enter the purchase price of the product"))
        es="insert into        ( serial_number,product_code,quantity,expiry_date,storage_location,purchase_price) values ({},{},{},'{}','{}',{})".format(serial_number,product_code,quantity,expiry_date,storage_location,purchase_price)
    #please enter the tablename
        cursor.execute(es)
        connection.commit()
        n=input("Enter y to insert more records or n to terminate")
        
    
def update():
    ch=0
    while ch==0:
        num=int(input(" Enter 1. To update product_code 2. To update the quantity 3. To update the expiry_date 4. To update the the storage_location 5. To update the purchase_price"))
        if num==1:
            new_pc=int(input("Enter the new product_code"))
            cursor.execute("update       set product_code={}".format(new_pc)) #Enter the table name
            connection.commit()               
        elif num==2:
            new_qt=float(input("Enter the new quantity"))
            cursor.execute("update       set quantity={}".format(new_qt)) #Enter the table name
            connection.commit()               
        elif num==3:
            new_ed=input("Enter the new expiry_date")
            cursor.execute("update       set expiry_date={}".format(new_ed)) #Enter the table name
            connection.commit()
        elif num==4:
            new_sl=input("Enter the new storage location")
            cursor.execute("update       set storage_location='{}'".format(new_sl)) #Enter the table name
            connection.commit()               
            
        elif num==5:
            new_pp=float(input("Enter the new purchase price"))
            cursor.execute("update       set purchase_price={}".format(new_pp)) #Enter the table name
            connection.commit()               
        else:
            ch=int(input("Enter a non null value to terminate the updation process"))
            break
            
                
        
                      
                                   



