class student_result:

   def __init__(self):
      self.name = ''
      self.marks = []

   def insert(self):

      # Open the file 
      s = open('student_RESULT.TXT','w')

     
      self.id = int(input("enter the id ="))
      s.write("id = "+str(self.id))
      self.name = input("ente the student name = ")
      s.write("\nname = "+self.name)

      # enter the marks
      self.marks = []
      for i in range(5):
         self.marks.append(int(input("enter the marks:")))
         s.write("\nmarks = "+str(self.marks[i]))

      return self.name , self.marks


   def logic(self,name,marks):
      s = open('student_RESULT.TXT','w')
      total = 0
      cnt = 0
      self.name = name
      self.marks = marks
      s.write("name = "+self.name)
      for i in range(len(marks)):
         s.write("\nmarks = "+str(self.marks[i]))
      
         
  
      for i in range(len(self.marks)):
         # total 
         total = total + int(self.marks[i])

         if int(self.marks[i]) <= 33:
            cnt+=1
         # print("cnt = ",cnt)

      minimum = min(self.marks)
      maximum = max(self.marks)
      s.write("\n\ntotal =" +str(total))
   #    # find per
      if int(minimum)< 33:
         per = 0
      else:
         per = int(total) / 5

      s.write("\nper = "+str(per))
      s.write("\nmin = "+str(minimum))
      s.write("\nmaximum = "+str(maximum))

      # result
      if cnt == 1 or cnt == 2:
         result = "ATKT"
      elif cnt == 0:
         result = "PASS"
      else:
         result = "FAIl"
      s.write("\nresult = "+str(result))

      # grade
      if int(per) > 90:
         grade = "A1"
      elif int(per) > 80:
         grade = "A2"
      elif int(per) > 70:
         grade = "B1"
      elif int(per) >60:
         grade = "B2"
      elif int(per) > 50 :
         grade = "C1"
      elif int(per) > 40:
         grade = "C2"
      elif int(per) > 33:
         grade = "E1"
      else :
         grade = "F"

      s.write("\ngrade = "+str(grade))
      s.write("\n-------------------------------------------")


   def read_data(self):
      s = open('student_RESULT.TXT', 'r')
      read = s.read()
      print(read)

   
   def update_data(self):
      s = open('student_RESULT.TXT','r')
      r = s.read()
      # print(r)

      read = r.split("\n")
      # print(read)

      m = []
      for i in read:
         m.append(i.split(" = "))
      print("1 - name")
      print("2 - sub1")
      print("3 - sub2")
      print("4 - sub3")
      print("5 - sub4")
      print("6 - sub5")
      # print("\n-------------\n")
      # print(m)
      # print("\n-------------\n")
      update_data = int(input("enter the number which you want to update:"))
      if update_data == 1:
         new_name = input("enter the name:")
         m[0][1] = (new_name)
      elif update_data == 2:
         # print(m1)
         new_mark1 = input("enter the mark ")
         m[1][1] = (new_mark1)
      elif update_data == 3:
         # print(m2)
         new_mark2 = input("enter the mark ")
      elif update_data == 4:
         new_mark3 = input("enter the mark ")
         m[3][1] = (new_mark3)
      elif update_data == 5:
         new_mark4 = input("enter the mark ")
         m[4][1] = (new_mark4)
      elif update_data == 6:
         
         new_mark5 = input("enter the mark ")
         m[5][1] = (new_mark5)
         # read[5] = ' = '.join(m[5][1])

      sub = [m[1][1],m[2][1],m[3][1],m[4][1],m[5][1]]
      # print("****",sub)


      return m[0][1] , sub

   def delete(s):
      s = open('student_RESULT.TXT','w')
      s.write('')
      s.close()


      
         


          
      




obj = student_result()

marks = []
print("1 - insert data")
print("2 - view data")
print("3 - update data")
print("4 - delete data")
ch = 1
while int(ch) >= 1:
   ch = int(input("enter your choise = "))
   if ch == 1:
      name ,marks = obj.insert()
      # mode = 'w'
      obj.logic(name,marks)
   elif ch == 2:
      obj.read_data()
   elif ch == 3:
      name,sub = obj.update_data()
      obj.logic(name,sub)
   elif ch == 4:
      obj.delete()
   elif ch == 0:
      break
