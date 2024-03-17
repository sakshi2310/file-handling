class result:
    marks = []
    def saperate(s):
        file = open('data.txt','r')
        r = file.read()
        file.close()
        k = r.split('\n-----------------------------------------------\n\n')
        s.f = []
        for i in range(len(k)):
            s.f.append(k[i].split(' \n '))
        for i in range(len(s.f)):
            l=[]
            for j in range(len(s.f[i])):
                l.append(s.f[i][j].split(' = '))
            s.f[i]=l
    def calculate(s):
        s.total = 0
        s.min = s.marks[0]
        s.max = s.marks[0]
        cnt = 0
        for i in s.marks:
            s.total = s.total + i
            if s.min>i:
                s.min = i
            if s.max<i:
                s.max = i
            if i<35:
                cnt += 1
        # Percentge
        if s.min>=35:
            s.per = s.total/5
        else :
            s.per = 0
        # result
        if cnt==0:
            s.result = 'PASS'
        elif cnt<=2:
            s.result = 'AT_KT'
        else:
            s.result = 'FAIL'
        # Grade
        if s.per>=80:
            s.grade = 'First Class'
        elif s.per>=50:
            s.grade = 'Second Class'
        elif s.per>=35:
            s.grade = 'Third Class'
        else :
            s.grade = '---'
    def insert(s):
        f = open('data.txt','a')
        s.roll = int(input("Enter Roll Number : "))
        s.name = input("Enter Name : ")
        s.marks = []
        for i in range(5):
            s.marks.append(int(input("Enter marks of sub "+str(i+1)+" : ")))
        s.calculate()
        marge = ("Roll_no. = "+str(s.roll)+" \n Name = "+s.name+" \n sub1 = "+str(s.marks[0])+" \n sub2 = "+str(s.marks[1])+" \n sub3 = "+str(s.marks[2])+" \n sub4 = "+str(s.marks[3])+" \n sub5 = "+str(s.marks[4])+" \n Total = "+str(s.total)+" \n Per = "+str(s.per)+" \n Min = "+str(s.min)+" \n Max = "+str(s.max)+" \n Result = "+s.result+" \n Grade = "+s.grade+" \n \n-----------------------------------------------\n\n")
        f.write(marge)
        f.close()
    def update(s):
        s.saperate()
        choice = (input("enter your Roll Number : "))
        j=0
        k=1
        for i in range(len(s.f)):
            for j in range(len(s.f[i])):
                for k in range(len(s.f[i][j])):
                    if j==0 and k==1:
                        if s.f[i][j][k]==choice:
                            r = i
        print("1->Name    2->Marks")
        ch = int(input("Enter Your Choice : "))
        if ch==1:
            name = input("Enter Name : ")
            s.f[r][1][1] = name
        elif ch==2:
            sub = int(input("Which Subject Marks You Want to Change : "))
            mark_new = input("Enter Marks of sub "+str(sub)+" : ")
            s.f[r][sub+1][1] = mark_new
            s.marks = []
            for i in range(5):
                s.marks.append(int(s.f[r][i+2][1]))
            s.calculate()
            s.f[r][7][1] = str(s.total)
            s.f[r][8][1] = str(s.per)
            s.f[r][9][1] = str(s.min)
            s.f[r][10][1] = str(s.max)
            s.f[r][11][1] = s.result
            s.f[r][12][1] = s.grade
        j1 = []
        for i in range(len(s.f)):
            k1 = []
            for j in range(len(s.f[i])):
                k1.append(' = '.join(s.f[i][j]))
            j1.append(' \n '.join(k1))
        i1 = "\n-----------------------------------------------\n\n".join(j1)
        file = open('data.txt','w')
        file.write(i1)
        file.close()
    def view(s):
        s.saperate()
        from tabulate import tabulate
        stu = []
        for i in range(len(s.f)-1):
            stu_1 = []
            for j in range(len(s.f[i])):
                for k in range(len(s.f[i][j])):
                    if k == 1:
                        stu_1.append(s.f[i][j][k])
            stu.append(stu_1)
        head = ["Roll_no", "Name", "Sub1", "Sub2", "Sub3", "Sub4", "Sub5", "Total", "Per", "Min", "Max", "Result", "Grade"]
        print(tabulate(stu, headers=head, tablefmt="mixed_outline"))  
    def delete(s):
        s.saperate()
        choice = (input("enter your Roll Number : "))
        for i in range(len(s.f)):
            for j in range(len(s.f[i])):
                for k in range(len(s.f[i][j])):
                    if j==0 and k==1:
                        if s.f[i][j][k]==choice:
                            r = i
        for i in range(r,len(s.f)-1):
            s.f[i] = s.f[i+1]
        j1 = []
        for i in range(len(s.f)-1):
            k1 = []
            for j in range(len(s.f[i])):
                k1.append(' = '.join(s.f[i][j]))
            j1.append(' \n '.join(k1))
        i1 = "\n-----------------------------------------------\n\n".join(j1)
        file = open('data.txt','w')
        file.write(i1)
        file.close() 

# Main ---------------------------------------------------------------------------------------
ch = 1
while ch!=0:
    print("1->Insert  2->Update  3->View   4->Delete   0->Exit")
    ch = int(input("Enter Your Choice : "))
    obj = result()
    if ch==1:
        obj.insert()
    elif ch==2:
        obj.update()
    elif ch==3:
        obj.view()
    elif ch==4:
        obj.delete()
    elif ch==0:
        print("Thank You")
    else :
        print("Enter Valid Choice")