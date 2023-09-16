class bank:
     def sign_up(s):
          print("\n******************")
          print("1 - saving account")
          print("2 - current account")
          print("********************\n")
          a_ch = int(input("enter your choise:"))
          if a_ch == 1:
               s.acc_type = "saving accout"
               s.acc_bal = 1
               while s.acc_bal >= 1:
                    s.acc_bal = int(input("\nenter the account balance:"))
                    if s.acc_bal < 5000:
                         print("\nyour account balance is more than 5000 to open your saving account")
                    elif s.acc_bal>=5000:
                         print("\nyou open your saving account...")
                         break
          elif a_ch == 2:
               s.acc_type = "current account"
               s.acc_bal = 1
               while s.acc_bal >= 1:
                    s.acc_bal = int(input("enter the account balance:"))
                    if s.acc_bal < 10000:
                         print("\nyour account balance is more than 10000 to open your current account") 
                    elif s.acc_bal >= 10000:
                         print("\nyou open your current account.....")
                         break
          s.user_name = input("enter the name:")
          s.acc_no = 1
          while int(s.acc_no) >= 1:
               s.acc_no = input("enter the account no:")
               l = len(s.acc_no)
               if l >= 4:
                    break
          

          


     def write_data(s,c):
          if c == 1:
               w = open('bank.txt','a')
               dict_a = {"account no":s.acc_no,"name":s.user_name,"type" : s.acc_type,"account balance" : s.acc_bal}
               for key ,value in dict_a.items():
                    w.write('\n%s:%s' %(key,value))
               w.write("\n------------------------------------------")
          elif c == 2:
               k1=[]
               for i in range(len(s.s_l)):
                    k1.append('\n'.join(s.s_l[i]))
               j1=('\n------------------------------------------\n'.join(k1))
               s = open('bank.txt','w')
               s.write("\n"+j1)
          elif c == 3:
               w = open('bank.txt','w')
               for i in range(len(s.value_list)-1):
                    for j in range(len(s.value_list[i])):
                              if j == 0:
                                   w.write("\naccount no:"+s.value_list[i][0])
                              if j == 1:
                                   w.write("\nname:"+s.value_list[i][1])
                              if j == 2:
                                   w.write("\ntype:"+s.value_list[i][2])
                              if j == 3:
                                   w.write("\naccount balance:"+s.value_list[i][3])
                    w.write("\n------------------------------------------")

     def split_date(s):
          w = open('bank.txt','r')
          s.r = w.read()
          split_one = s.r.split("------------------------------------------") 

          # split array by \n 
          s.n_l = []
          for i in split_one:
               s.n_l.append(i.split("\n"))

          # remove all the blank space from the list
          s.s_l = []
          for i in s.n_l:
               temp = []
               for j in i:
                    if j:
                         temp.append(j)
               s.s_l.append(temp)

          # split the list by :  
          s.a_no = []
          for i in s.s_l:
               if len(i) >=2:
                    temp = i[0]
                    s.a_no.append(temp.split(":"))
                  
                            
     def login(s):
          s.split_date()
          cnt = 0
          s.acc_no = input("enter the account no :")
          # check the account number with to login
          for i in range(len(s.a_no)):
               if s.acc_no == s.a_no[i][1]:
                    s.user_acc = s.s_l[i]
                    cnt+=1
                    print("you have successfully login your account")

          if cnt == 0:
               print("invlid account number")
               s.login()

          s.choise()     
     def choise(s):
          print("----------------------------------")
          print(" 1 - show your account ")
          print(" 2 - diposit amount")
          print(" 3 - withdrawn amount")
          print(" 4 - delete my account")
          print(" 0 - logout your account")

          user_ch = 1
          
          while user_ch>=1:
               user_ch = int(input("enter your choise:"))
               if user_ch == 1:
                    s.show_account()
               elif user_ch == 2:
                    s.diposte()
               elif user_ch == 3:
                    s.withdrawn()
               elif user_ch == 4:
                    s.delte_acc()
               elif user_ch == 0:
                    print("you logout your account")
                    main_frame()
     
     def show_account(s):
          s.split_date()
          for i in range(len(s.a_no)):
               if s.acc_no == s.a_no[i][1]:
                    s.user_acc = s.s_l[i]
          for i in s.user_acc:
               print(i)
          

     def diposte(s): 
               # split the list : and store in dict
               con_dict = {}
               for i in s.user_acc:
                    if ":" in i:
                         Key,Value = i.split(":")
                         con_dict[Key] = Value

               # store the old amoutn in variable
               old_amt = con_dict["account balance"]

               dip = input("enter the diposite amount = ")
               if int(dip) > 10000:
                    print("you can not diposte more than 10000....")
                    s.choise()

               con_dict["account balance"] = int(dip) + int(old_amt)

               # store and convert dict into the list
               new_dict =[]
               for key , Value in con_dict.items():
                    new_dict.append([key,Value])
               
               # join the list by : 
               t1 = []
               for i in new_dict:
                    t1.append(f'{i[0]}:{i[1]}')

               # update the list by new value 
               for i in range(len(s.a_no)):
                    if  s.acc_no  == s.a_no[i][1]:
                         s.s_l[i] = t1
               print("you successfully diposite your amount...")
               s.write_data(2)   

     def withdrawn(s):
          # split the list : and store in dict
          con_dict = {}
          for i in s.user_acc:
               if ":" in i:
                    Key,Value = i.split(":")
                    con_dict[Key] = Value

          # store the old amoutn in variable
          old_amt = con_dict["account balance"]

          withdrawan_amt = input("enter the withdrawn amount = ")
          con_dict["account balance"] = int(old_amt) - int(withdrawan_amt)

          # store and convert dict into the list
          new_dict =[]
          for key , Value in con_dict.items():
               new_dict.append([key,Value])
          
          # join the list by : 
          t1 = []
          for i in new_dict:
               t1.append(f'{i[0]}:{i[1]}')

          # update the list by new value 
          for i in range(len(s.a_no)):
               if  s.acc_no  == s.a_no[i][1]:
                    s.s_l[i] = t1
          print("you successfully withdrawn your amount....")
          s.write_data(2)
          

     def delte_acc(s):
          s.split_date()
          print(s.s_l)
          # print(s.a_no)
          for i in range(len(s.s_l)):
               temp_split = []
               for j in range(len(s.s_l[i])):
                    temp_split.append(s.s_l[i][j].split(":"))
               s.s_l[i] = temp_split

          s.value_list = []
          for i in range(len(s.s_l)):
               temp_val_list = []
               for j in range(len(s.s_l[i])):
                    for k in range(len(s.s_l[i][j])):
                         if k == 1:
                              temp_val_list.append(s.s_l[i][j][k])
               s.value_list.append(temp_val_list)

          for i in range(len(s.value_list)):
               for j in range(len(s.value_list[i])):
                    if s.acc_no == s.value_list[i][j]:
                         index_val = i
          s.value_list.pop(index_val)
          s.write_data(3)






obj = bank()
def main_frame():
     print("\n************************")
     print("1 - sign up ")
     print("2 - login")
     print("0 - exit the program")
     
     print("************************\n")
     ch = 1
     while int(ch)>=1:
          ch = int(input("enter the choise:"))
          if ch == 1:
               obj.sign_up()
               obj.write_data(1)
          elif ch == 2:
               obj.login()
               # obj.split_date()
          elif ch == 0:
               print("***** logout successfully *****")
               break
main_frame()
     


