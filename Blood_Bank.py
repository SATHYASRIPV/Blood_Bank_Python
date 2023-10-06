from mysql import connector
import User_name_Password as UP
import SQL_Queries1
import re
try:
    connection = connector.connect(host="localhost",user=UP.user_name,password = UP.password,database = 'sathya')
    if connection.is_connected() == True:
        print("Connected.")
        curser = connection.cursor(buffered=True)
        curser.execute(SQL_Queries1.create)
        print("Select the option:\n1.PRINT\n2.INSERT\n3.DELETE\n4.EXIT")
        opt = int(input("SELECT OPTION:"))
        while opt != 4:
            if opt == 1:
                curser.execute(SQL_Queries1.select)
                ans = curser.fetchall()
                for i in ans:
                    print(i)
                print("Select the option:\n1.PRINT\n2.INSERT\n3.DELETE\n4.EXIT")
            elif opt == 2:
                n = int(input("Enter the number of persons data to be entered:"))
                for i in range(1,n+1):
                    name = input("Enter your name:")
                    assert name.isalpha() and len(name)<=20,"Name should contain only alphabets and should be within 20 characters"
                    mobile_no = input("Enter mobile number:")
                    assert len(mobile_no)==10 and bool(re.match('^[0-9]*$', mobile_no)), "Mobile should be 10 digit and only contain integers."
                    blood_grp = input("Blood group(A+)or(AB-):")
                    assert len(blood_grp)<=3 and bool(re.match('^(AB|A|B|O)[+-]$',blood_grp)), "Blood group should be a valid one."
                    gender = input("ENter gender(F/M)or(f/m):")
                    assert len(gender)==1 and bool(re.match('[FfMm]',gender)),"Gender should be specified as sindle character and only contain either f or m in any case."
                    age = int(input("Enter your age:"))
                    assert age>=18,"Age should be greater than or equal to 18."
                    city = input("Enter Your city:")
                    insert_query = SQL_Queries1.insert()+f" VALUES('{name}','{mobile_no}','{blood_grp}','{gender}',{age},'{city}');"
                    curser.execute(insert_query)
                    connection.commit()
                curser.execute(SQL_Queries1.select)
                res = curser.fetchall()
                print("TABLE AFTER UPDATION.\n")
                for row in res:
                    print(row)
                print("Select the option:\n1.PRINT\n2.INSERT\n3.DELETE\n4.EXIT")
            elif opt == 3:
                id = int(input("Enter ID to delete their datas:"))
                ID_list_query = "SELECT ID FROM blood_bank;"
                curser.execute(ID_list_query)
                list_ID = curser.fetchall()
                for ID in list_ID:
                    if ID == id:
                        present = 1
                    else:
                        present = 0
                assert present, "ID should be present in the table."
                delete_query = SQL_Queries1.delete().replace("replace_id",str(id))
                curser.execute(delete_query)
                connection.commit()
                curser.execute(SQL_Queries1.select)
                res = curser.fetchall()
                print("TABLE AFTER DELETION.\n")
                for row in res:
                    print(row)
                print("Select the option:\n1.PRINT\n2.INSERT\n3.DELETE\n4.EXIT")
            elif opt == 4:
                break
            else:
                print("Enter valid number from 1 to 4:")
            opt = int(input("SELECT OPTION:"))
            curser.execute(SQL_Queries1.select)
        res = curser.fetchall()
        print("TABLE AFTER ALL OPERATIONS.\n")
        for row in res:
            print(row)
    curser.close()
    connection.close()
except Exception as err:
    print(err)