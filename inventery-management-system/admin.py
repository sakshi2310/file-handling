from tabulate import tabulate
class inventery_managenent_admin:
     def add_category(s):
          print()

     def sign_up(s):
          s.id = int(input("enter the id:"))
          s.name = input("enter the name:")
          s.email = input("enter the email:")
          s.user_name = input("enter the user name:")
          s.password  = input("enter the password:")
          s.write_data(1)

     def write_data(s,c):
          if c == 1:
               f = open('admin.txt','a')
               f.write("\nId:"+str(s.id))
               f.write("\nname:"+s.name)
               f.write("\nemail:"+s.email)
               f.write("\nuser name:"+s.user_name)
               f.write("\npassword:"+s.password)
               f.write("\n-------------------------------------------")
          elif c == 2:
               f = open('category.txt','a')
               f.write("\nId:"+str(s.c_id))
               f.write("\ncategory name:"+s.c_name)
               f.write("\n-------------------------------------------")
          elif c == 3:
               f = open('category.txt','w')
               for i in range(len(s.s_v)-1):
                    for j in range(len(s.s_v[i])):
                         if j==0:
                              f.write("\nId:"+s.s_v[i][0])
                         elif j == 1:
                              f.write("\ncategory name:"+s.s_v[i][1])
                    f.write("\n-------------------------------------------")
          elif c == 4:
               f = open('users.txt','a')
               f.write("\nId:"+str(s.u_id))
               f.write("\nname:"+s.u_name)
               f.write("\nemail:"+s.u_email)
               f.write("\nuser name:"+s.u_user_name)
               f.write("\npassword:"+s.u_password)
               f.write("\n-------------------------------------------")

                    



     def split_data(s,choise):
          if choise == 1:
               f = open('admin.txt','r')
          elif choise == 2:
               f = open('category.txt','r')
          elif choise == 3:
               f = open('users.txt','r')
          r = f.read()

          single_data = r.split("-------------------------------------------")

          new_line = []
          for i in single_data:
               new_line.append(i.split("\n"))
          # print(new_line)

          single_value =[]
          for i in new_line:
               temp = []
               for j in i:
                    if j:
                         temp.append(j)
               single_value.append(temp)
          # print(single_value)

          for i in range(len(single_value)):
               temp_value = []
               for j in range(len(single_value[i])):
                    temp_value.append(single_value[i][j].split(":"))
               single_value[i] = temp_value
          # print(single_value)

          s.s_v = []
          for i in range(len(single_value)):
               val = []
               for j in range(len(single_value[i])):
                    for k in range(len(single_value[i][j])):
                         if k == 1:
                              val.append(single_value[i][j][k])
               s.s_v.append(val)

     def login(s):
          s.split_data(1)
          l_user_name = input("enter the user name:")
          l_password = input("enter the password:")

          c_e = 0
          c_p = 0
          for i in range(len(s.s_v)):
               for j in range(len(s.s_v[i])):
                    if j == 3:
                         if l_user_name == s.s_v[i][j]:
                              c_e+=1
                    if j == 4:
                         if l_password == s.s_v[i][j]:
                              c_p+=1
               
          if c_p==1 and c_e==1:
               print("login successfully...")
               s.login_choise()
          else:
               print("invalid password or email")
               s.login()
     
     def login_choise(s):
          print("\n-------------------------------------------")
          print("1 - add category")
          print("2 - view category")
          print("3 - delete category")
          print("4 - add users")
          print("5 - view all users")
          print("6 - delete user")
          print("7 - update user")
          print("0 - logout")
          print("\n-------------------------------------------")
          c = 1
          while int(c) >=1:
               c = input("enter your choise:")
               if int(c) == 1:
                    s.add_category()
               elif int(c) == 2:
                    s.view_category()
               elif int(c) == 3:
                    s.delte_category()
               elif int(c) == 4:
                    s.add_users() 
               elif int(c) == 5:
                    s.view_all_users()
               elif int(c) == 0:
                    break



     def add_category(s):
          s.c_id = int(input("enter the category Id:"))
          s.c_name = input("enter the category name:")
          s.write_data(2)

     def view_category(s):
          f = open('category.txt','r')
          s.split_data(2)
          head = ["id","category"]
          print(tabulate(s.s_v,headers=head,tablefmt="mixed_outline"))

     def delte_category(s):
          s.split_data(2)
          head = ["id","category"]
          print(tabulate(s.s_v,headers=head,tablefmt="mixed_outline"))
          del_cat = input("enter the category which you want to delete:")

          for i in range(len(s.s_v)):
               for j in range(len(s.s_v[i])):
                    if del_cat == s.s_v[i][j]:
                         index = i

          s.s_v.pop(index)
          s.write_data(3)

     def add_users(s):
          s.u_id = int(input("enter the id:"))
          s.u_name = input("enter the name:")
          s.u_email = input("enter the email:")
          s.u_user_name = input("enter the user name:")
          s.u_password  = input("enter the password:")
          s.write_data(4)

     def view_all_users(s):
          s.split_data(3)
          head = ["id","name","email","user name","password"]
          print(tabulate(s.s_v,headers=head,tablefmt="mixed_outline"))

     def delete_users(s):
          s.split_data(3)
          head = ["id","name","email","user name","password"]
          print(tabulate(s.s_v,headers=head,tablefmt="mixed_outline"))
          del_cat = input("enter the user id which you want to delete:")

          for i in range(len(s.s_v)):
               for j in range(len(s.s_v[i])):
                    if del_cat == s.s_v[i][j]:
                         index = i

          s.s_v.pop(index)
          s.write_data()









     







print("1 - admin")
print("2 - users")
p_ch = input("enter the choise to open portal:")
if int(p_ch) == 1:
     obj = inventery_managenent_admin()
     def main():
          print("-------------------------------------------")
          print("1 - sign up")
          print("2 - login")
          print("-------------------------------------------")

          ch = 1
          while int(ch)>=1:
               ch = input("enter the choise:")
               if int(ch) == 1:
                    obj.sign_up()
               elif int(ch) == 2:
                    # obj.split_data()
                    obj.login()
               elif int(ch) == 0:
                    break
     main()
