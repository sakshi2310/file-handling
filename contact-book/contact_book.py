from tabulate import tabulate
class contact_book: 
     def signin(s):
          s.ID = input("enter the Id :")
          s.name = input("enter the name:")
          s.email = input("enter the email:")
          s.password = input("enter the password:")
          s.write_data(1)

     def write_data(s,c):
          if c == 1:
               f = open('contact_book.txt','a')
               f.write("\nId:"+s.ID)
               f.write("\nname:"+s.name)
               f.write("\nemail:"+s.email)
               f.write("\npassword:"+s.password)
               f.write("\n----------------------------------------")
          elif c == 2:
               f = open('contacts.txt','a')
               f.write("\nId:"+s.contact_id  )
               f.write("\nreference id:"+s.referce_id)
               f.write("\nname:"+s.contact_name)
               f.write("\nemail:"+s.contact_email)
               f.write("\ncontact:"+s.contact)
               f.write("\n----------------------------------------")

     def split_data(s,choise):
          print(choise)
          if int(choise) == 1:
               f = open('contact_book.txt','r')
          elif int(choise) == 2:
               f = open('contacts.txt','r')
               
          s.r = f.read()
          s.sp_line = s.r.split("----------------------------------------")
          # print(s.sp_line)

          s.new_line = []
          for i in s.sp_line:
               s.new_line.append(i.split("\n"))
          # print(s.new_line)

          s.remove_space = []
          for i in s.new_line:
               temp = []
               if i :
                    for j in i:
                         if j:
                              temp.append(j)
                    s.remove_space.append(temp)
          # print(s.remove_space)

          s.emails = []
          s.passwords = []
          for i in s.remove_space:
               if len(i) >=2:
                    temp_email = i[2]
                    temp_ps = i[3]
                    s.emails.append(temp_email.split(":"))
                    s.passwords.append(temp_ps.split(":"))

     def login(s):
          s.split_data(1)
          s.l_email = input("enter the email:")
          s.l_ps = input("enter the password:")
          for i in range(len(s.emails)):
               if s.l_email == s.emails[i][1]:
                    s.temp_ac_e= s.remove_space[i] 
          # print(s.user_acc_e) 
          for i in range(len(s.passwords)):
               if s.l_ps == s.passwords[i][1]:
                    s.temp_ac_ps = s.remove_space[i] 
          if s.temp_ac_e!= '' and s.temp_ac_ps!='':
               print("login successfully")
               s.login_choise()
          else:
               print("invalid password and email..")
               s.login()

          
          
     def login_choise(s):
          print("\n---------------------------------------")
          print("1 - add contact")
          print("2 - delete contact")
          print("3 - update contact")
          print("4 - view contact")
          print("0 - logout")
          print("\n----------------------------------------")
          c = 1
          while int(c) >= 1:
               c = input("\nenter the choise:")
               if int(c) == 1:
                    print("add contact")
                    s.add_data()
               elif int(c) == 2:
                    print("delte contact")
               elif int(c) == 3:
                    s.update_data()
                    print("update contact")
               elif int(c) == 4:
                    s.view_contact()
                    print("view contact")
               elif int(c) == 0:
                    print("logout")

     
     def add_data(s):
          s.s_l = []
          for i in s.temp_ac_e:
               s.s_l.append(i.split(":"))

          s.contact_id = input("enter the Id:")
          s.referce_id = s.s_l[0][1]
          s.contact_name = input("entert the name:")
          s.contact_email = input("enter the email:")
          s.contact = input("enter the contact number:")

          s.write_data(2)
     
     def view_contact(s):
          s.split_data(2)
          s.referce_ids = []
          for i in s.remove_space:
               if len(i) >=2:
                    temp_referce_id = i[1]
                    s.referce_ids.append(temp_referce_id.split(":"))
          # print(s.referce_ids)

          temp_user = []
          for i in s.temp_ac_e:
               temp_user.append(i.split(":"))

          user_id = temp_user[0][1]

          final_list = []
          for i in range(len(s.referce_ids)):
               if user_id == s.referce_ids[i][1]:
                    final_list.append(s.remove_space[i])


          for i in range(len(final_list)):
               temp_split = []
               for j in range(len(final_list[i])):
                    temp_split.append(final_list[i][j].split(":"))
               final_list[i] = temp_split

          con = []
          for i in range(len(final_list)):
               temp_con = []
               for j in range(len(final_list[i])):
                    for k in range(len(final_list[i][j])):
                         if k == 1:
                              temp_con.append(final_list[i][j][k])

               con.append(temp_con)
          head = ["id","referecnce id ","name","email","contact"]
          print(tabulate(con,headers=head,tablefmt="mixed_outline"))



     def update_data(s):

          print()


                

obj = contact_book()
def main_page():
     print("--------------------------------")
     print("1 - sign in")
     print("2 - login")
     print("0 - exit")
     print("---------------------------------")
     ch = 1
     while int(ch) >=1:
          ch = input("enter the choise = ")
          if int(ch) == 1:
               print("sign in ")
               obj.signin()
          elif int(ch) == 2:
               # obj.split_data()
               obj.login()
               print("login")
          elif int(ch) == 0:
               print("logout")
               break

main_page()
