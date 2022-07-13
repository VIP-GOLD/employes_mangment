from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database
db = database("employes.db")

#======= program =========#
root=Tk()
root.title('نظام ادارة الموظفين')
root.geometry('1110x630+0+0')
root.resizable(False,False)
root.configure(bg='#148F77')#148F77
print("Program Is Started")
print("تم تصميم البرنامج من قبل احمد سلام الذهب")
messagebox.showinfo("البرنامج", "مرحبا بك عزيزي\nالبرنامج مجاني ويمنع بيعهُ")
name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
phone = StringVar()
#======= Logo frame ========#

logo = PhotoImage(file='logo2.png')
lbl_logo=Label(root, image=logo, bg='#148F77')
lbl_logo.place(x=10,y=510)


#======= Entry frame ========#

entries_frame=Frame(root, bg='#148F77')
entries_frame.place(x=1,y=1,width=306,height=510)
logo_user = PhotoImage(file='logouser.png')
lbl_logo_user=Label(root, image=logo_user, bg='#148F77')
lbl_logo_user.place(x=1,y=1)
title = Label(entries_frame,text='مـعـلــومـات الـمـوظــف', font=('simplified arabic',18,'bold'),bg='#148F77', fg='white')
title.place(x=60,y=1)
lblname = Label(entries_frame,text='الاسم', font=('simplified arabic',18),bg='#148F77', fg='white')
lblname.place(x=10,y=50)
txtname = Entry(entries_frame,textvariable=name, width=20, bg='white', font=('simplified arabic',18))
txtname.place(x=90,y=50)
lblage = Label(entries_frame,text='العمر', font=('simplified arabic',18),bg='#148F77', fg='white')
lblage.place(x=10,y=100)
txtage = Entry(entries_frame,textvariable=age,width=20, bg='white', font=('simplified arabic',18))
txtage.place(x=90,y=100)
lblgender = Label(entries_frame,text='الجنس', font=('simplified arabic',18),bg='#148F77', fg='white')
lblgender.place(x=10,y=150)
combogender = ttk.Combobox(entries_frame, textvariable=gender, state='readonly', width=15 ,font=('simplified arabic',18))
combogender['values']=("ذكر","أنثى")
combogender.place(x=90,y=150)
lbljob = Label(entries_frame ,text='الوظيفة', font=('simplified arabic',18),bg='#148F77', fg='white')
lbljob.place(x=10,y=200)
txtjob = Entry(entries_frame, textvariable=job, width=20, bg='white', font=('simplified arabic',18))
txtjob.place(x=90,y=200)
lblphone = Label(entries_frame,text='الهاتف', font=('simplified arabic',18),bg='#148F77', fg='white')
lblphone.place(x=10,y=250)
txtphone = Entry(entries_frame,width=20, textvariable=phone, bg='white', font=('simplified arabic',18))
txtphone.place(x=90,y=250)
lbllocation = Label(entries_frame,text='السكن', font=('simplified arabic',18),bg='#148F77', fg='white')
lbllocation.place(x=10,y=300)
txtlocation = Text(entries_frame,width=30, height=2 ,bg='white' , font=('simplified arabic',18))
txtlocation.place(x=90,y=300)
#======= Define ========#
class Particle:
   def __init__(self, name, charge):
       self.name = name
       self.charge = charge
   def show_particle(self):
       print(f'The particle {self.name} has a charge of {self.charge}')
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    gender.set(row[5])
    job.set(row[3])
    phone.set(row[4])
    txtlocation.delete(1.0, END)
    txtlocation.insert(END, row[6])
    messagebox.showinfo("تم لاحضار","تم جلب معلومات الموظف")
def upd(event):
    if txtname.get() == "" or combogender.get() == "" or txtage.get() == "" or txtjob.get() == "" or txtjob.get() == "" or txtphone.get() == "" or txtlocation.get(
            1.0, END) == "":
        messagebox.showerror("هناك خطا ما", "يرجى اختيار موظف بداية الامر")
        return
    db.update(row[0],
              txtname.get(),
              txtage.get(),
              txtjob.get(),
              txtphone.get(),
              combogender.get(),
              txtlocation.get(1.0, END))
    messagebox.showinfo("تم التحديث","تم تحديث معلومات الموظف")
    clear()
    displayAll()
def delete(event):
    db.remove(row[0])
    clear()
    displayAll()
def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def showinfo():
    messagebox.showinfo("--- المبرمج ---","### مبرمج التطبيق ###\n\nاحمد سلام الذهب\n\nالعراق - صلاح الدين\n\n!!! نسخة مجانية  الاستعمال!!!\n\nفيس بوك: احمد سلام الذهب\n\n- instagram: @a0g0a\n\n- telegram @amody7")
def clear():
    name.set("")
    age.set("")
    gender.set("")
    job.set("")
    phone.set("")
    txtlocation.delete(1.0,END)
def addemploy():
    if txtname.get() == "" or combogender.get() == "" or txtage.get() == "" or txtjob.get() == "" or txtjob.get() == "" or txtphone.get() == "" or txtlocation.get(1.0,END) == "":
        messagebox.showerror("هناك خطا ما","رجاءا املئ جميع الحقول")
        return
    db.insert(
        txtname.get(),
        txtage.get(),
        txtjob.get(),
        txtphone.get(),
        combogender.get(),
        txtlocation.get(1.0,END))
    messagebox.showinfo("Success","تم ادخال موظف جديد")
    clear()
    displayAll()
#======= Button ========#
btn_Frame=Frame(entries_frame,bg='#148F77', relief=SOLID ,bd=1)
btn_Frame.place(x=1,y=400,width=355, height=110)
btnAdd= Button(btn_Frame,
               text="اضافة معلومات",
               width=18,
               height=1,
               font=('simplified arabic',12),
               fg='white',
               cursor='hand2',
               bg='#58D68D',
               bd=0,
               command=addemploy
               ).place(x=4,y=5)
btnEdit= Button(btn_Frame,
               text="تعديل معلومات",
               width=18,
               height=1,
               font=('simplified arabic',12),
               fg='white',
               cursor='hand2',
               bg='#2980b9',
               bd=0,
               command=upd
               ).place(x=4,y=52)
btnDel= Button(btn_Frame,
               text="حذف موظف",
               width=16,
               height=1,
               font=('simplified arabic',12),
               fg='white',
               cursor='hand2',
               bg='red',
               bd=0,
               command=delete
               ).place(x=160,y=5)
btnClr= Button(btn_Frame,
               text="افراغ الحقول",
               width=16,
               height=1,
               font=('simplified arabic',12),
               fg='white',
               cursor='hand2',
               bg='#f39c12',
               command=clear,
               bd=0
               ).place(x=160,y=52)
##########################
btninfo_Frame=Frame(entries_frame,bg='#148F77', relief=SOLID ,bd=0)
btninfo_Frame.place(x=1,y=340,width=75, height=50)
btnshowinfo= Button(btninfo_Frame,
               text="المبرمج",
               width=5,
               height=1,
               font=('Arial',14),
               fg='white',
               cursor='hand2',
               bg='#CB4335',
               bd=0,
               command=showinfo
               ).place(x=4,y=5)
#======= Define ========#

def hide():
    root.geometry("315x630")
def show():
    root.geometry('1110x630+0+0')
btnhide = Button(entries_frame, text="اخفاء", command=hide, cursor='hand2', relief=SOLID, bd=1, font=('Arial',12),fg='white', bg='#F28B40')
btnhide.place(x=270, y=5)
btnshow = Button(entries_frame, text="اظهار", command=show, cursor='hand2', relief=SOLID, bd=1, font=('Arial',12),fg='white', bg='#2B2FE1')
btnshow.place(x=227, y=5)

#======= Table Frame ========#
tree_frame = Frame(root, bg='white', bd=2)
tree_frame.place(x=315,y=1,width=940,height=623)
style = ttk.Style()
style.configure("mystyle.Treeview",bg='#148F77', font=('Times New Roman',15), rowheight=50, rowwidth=100)
style.configure("mystyle.Treeview.Heading",font=('Times New Roman',13))
tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7), style="mystyle.Treeview" )
tv.heading("1",text="الرقم الوظيفي")
tv.column("1",width="100")
tv.heading("2",text="الاسم")
tv.column("2",width="140")
tv.heading("3",text="العمر")
tv.column("3",width="50")
tv.heading("4",text="الوظيفة")
tv.column("4",width="100")
tv.heading("5",text="الهاتف")
tv.column("5",width="120")
tv.heading("6",text="الجنس")
tv.column("6",width="70")
tv.heading("7",text="العنوان")
tv.column("7",width="130")
tv['show']= 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=10,height=620, width=785)
displayAll()
root.mainloop()