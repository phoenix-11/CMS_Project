import mysql.connector
con =mysql.connector.connect(host="localhost", user="root", passwd="", database="mydb")
cur=con.cursor()
query="insert into mycontact (Firstname,Lastname,Address,Age,Phone_number) values (%s,%s,%s,%s,%s)"
print("Add Contact\n")
c="yes"
while(c=="yes"):
    j=input("Firstname :")
    k=input("\nLastname :")
    l=input("\nAddress :")
    m=int(input("\nAge :"))
    n=int(input("\nPhonenumber :"))
    tup=(j,k,l,m,n)
    cur.execute(query,tup)
    con.commit()
    print("\nContact saved sucessfully\n")
    c=input("Want to continue yes or no\n");