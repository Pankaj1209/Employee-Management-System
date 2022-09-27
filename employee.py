from msilib.schema import ComboBox
from optparse import Values
# from selectors import EpollSelector
from sre_constants import SUCCESS
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        #variables

        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_degi = StringVar()
        self.var_email = StringVar()
        self.var_address= StringVar()
        self.var_married = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_id_proofcomb = StringVar()
        self.var_idproof = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_salary = StringVar()

        Ibl_title = Label(root, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        Ibl_title.place(x=0,y=0,width=1530,height=50)


        #logo

        img_logo = Image.open('images/t.jfif')
        img_logo = img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo =  Label(self.root, image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)
#first image
        img1 = Image.open('images/t1.jfif')
        img1 = img1.resize((540,160),Image.ANTIALIAS)
        self.photo1= ImageTk.PhotoImage(img1)

        self.img1 =  Label(img_frame, image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=160)

#second image
        img2 = Image.open('images/t2.jfif')
        img2 = img2.resize((540,160),Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img2 =  Label(img_frame, image=self.photo2)
        self.img2.place(x=540,y=0,width=540,height=160)

#third image
        img3 = Image.open('images/t3.jpg')
        img3 = img3.resize((540,160),Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img3 =  Label(img_frame, image=self.photo3)
        self.img3.place(x=1000,y=0,width=540,height=160)

        # Main frame

        main_frame = Frame(self.root, bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1500, height=560)

    #upper frame
        upper_frame = LabelFrame(main_frame,bg='white', bd='2',relief=RIDGE,text='Employee Information',font=('times new roman',15,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)


    # Lables and Entry fields
        lbl_dep = Label(upper_frame, text="Department",font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep = ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('select department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    #name
        lbl_name = Label(upper_frame, font=('arial',12,'bold'),text='Name:',bg='white')
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

    #label_designation
        lbl_designition = Label(upper_frame,font=("arial",12,'bold'),text='Designition:',bg='white')
        lbl_designition.grid(row=1,column=0,sticky=W,padx=2,pady=2)

        txt_designition= ttk.Entry(upper_frame,textvariable=self.var_degi, width=22,font=('arial',11,'bold'))
        txt_designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

    #email
        lbl_email = Label(upper_frame,font=("arial",12,'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email= ttk.Entry(upper_frame,textvariable=self.var_email, width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)

    #address
        lbl_address = Label(upper_frame,font=("arial",12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address= ttk.Entry(upper_frame,textvariable=self.var_address, width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

    #married
        lbl_married = Label(upper_frame, text="Married Statement",font=('arial',11,'bold'),bg='white')
        lbl_married.grid(row=2,column=2,padx=2,sticky=W)

        combo_married = ttk.Combobox(upper_frame,textvariable=self.var_married , font=('arial',12,'bold'),width=17,state='readonly')
        combo_married['value']=('Married','Unmarried')
        combo_married.current(0)
        combo_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)
    #DOb
        lbl_dob = Label(upper_frame,font=("arial",12,'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob= ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,sticky=W,padx=2,pady=7)
    #DOJ
        lbl_doj = Label(upper_frame,font=("arial",12,'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj= ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)
    #ID proof
        combo_txt_proof = ttk.Combobox(upper_frame,textvariable=self.var_id_proofcomb,font=('arial',12,'bold'),width=17,state='readonly')
        combo_txt_proof['value']=('Select ID proof','PAN CARD','ADHAR CARD','DRIVING LICENSE')
        combo_txt_proof.current(0)
        combo_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof= ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,sticky=W,padx=2,pady=7)

    #gender
        lbl_gender = Label(upper_frame,font=("arial",12,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        combo_txt_gender = ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_txt_gender['value']=('Male','Female','Other')
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)
    #phone
        lbl_phone = Label(upper_frame,font=("arial",12,'bold'),text='Phone NO:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone= ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,sticky=W,padx=2,pady=7)
    #countnry
        lbl_country = Label(upper_frame,font=("arial",12,'bold'),text='Country:',bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country= ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,sticky=W,padx=2,pady=7)
    #ctc
        lbl_ctc = Label(upper_frame,font=("arial",12,'bold'),text='Salary CTC:',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc= ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,sticky=W,padx=2,pady=7)
    #button frame

        button_frame = Frame(upper_frame, bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1100,y=10,width=330, height=110)

        btn_add = Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=27,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        # btn_update = Button(button_frame,text='Update',command=self.update_data,font=('arial',15,'bold'),width=27,bg='blue',fg='white')
        # btn_update.grid(row=1,column=0,padx=1,pady=5)

        # btn_delete = Button(button_frame,text='Delete',command = self.delete_data,font=('arial',15,'bold'),width=27,bg='blue',fg='white')
        # btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear = Button(button_frame,text='Clear',command=self.reset_data,font=('arial',15,'bold'),width=27,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)



        
    #down frame
        down_frame = LabelFrame(main_frame,bg='white', bd='2',relief=RIDGE,text='Employee Information Tables',font=('times new roman',15,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

    #search frame
        search_frame = LabelFrame(down_frame,bg='white', bd='2',relief=RIDGE,text='Search Employee',font=('times new roman',15,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by = Label(search_frame,bg='red', bd='2',relief=RIDGE,text='Search By:',font=('arial',11,'bold'),fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
    
    #search
        self.var_com_search=StringVar()
        combo_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search, font=('arial',12,'bold'),width=17,state='readonly')
        combo_txt_search['value']=('Select Option','Phone','Id_proof')
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0,column=1,padx=5,sticky=W)


        self.var_search=StringVar()
        txt_search= ttk.Entry(search_frame,textvariable=self.var_search,width=14,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search = Button(search_frame,text='Search',command=self.search_data, font=('arial',11,'bold'),width=30,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall = Button(search_frame,text='Show All',command=self.fetch_data, font=('arial',11,'bold'),width=30,bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)

    #employee table

        table_frame = Frame(down_frame, bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','id_proofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('id_proofcomb',text='ID_PROOF_COMB')
        self.employee_table.heading('idproof',text='ID_PROOF')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        self.employee_table.column('dep', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('degi', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('married', width=100)
        self.employee_table.column('dob', width=100)
        self.employee_table.column('doj', width=100)
        self.employee_table.column('id_proofcomb', width=100)
        self.employee_table.column('idproof', width=100)
        self.employee_table.column('gender', width=100)
        self.employee_table.column('phone', width=100)
        self.employee_table.column('country', width=100)
        self.employee_table.column('salary', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind('<ButtonRelease>',self.get_cursor)
        self.fetch_data()

    #fucntion
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Qwerty@123',database='alpha')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into emp  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                    self.var_dep.get(),
                                                    self.var_name.get(), 
                                                    self.var_degi.get(),
                                                    self.var_email.get(),
                                                    self.var_address.get(),
                                                    self.var_married.get(),
                                                    self.var_dob.get(),
                                                    self.var_doj.get(),
                                                    self.var_id_proofcomb.get(), 
                                                    self.var_idproof.get(),
                                                    self.var_gender.get(),
                                                    self.var_phone.get(),
                                                    self.var_country.get(), 
                                                    self.var_salary.get() 


                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo('success','Employee added',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)  

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Qwerty@123',database='alpha')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from emp')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i) 
            conn.commit()
        conn.close()   

    #get cursor

    def get_cursor(self,event=''):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_degi.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_id_proofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        
    

    #reset
    def reset_data(self):
        self.var_dep.set('Select Department')
        self.var_name.set('')
        self.var_degi.set('')
        self.var_email.set('')
        self.var_address.set('')
        self.var_married.set('Married')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_id_proofcomb.set('')
        self.var_idproof.set('select ID Proof')
        self.var_gender.set('')
        self.var_phone.set('')
        self.var_country.set('')
        self.var_salary.set('')

    #search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Qwerty@123',database='alpha')
                my_cursor = conn.cursor()
                my_cursor.execute('Select * from emp where ' + str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)







if __name__=="__main__":
    root=Tk()
    obj = Employee(root)
    root.mainloop()
