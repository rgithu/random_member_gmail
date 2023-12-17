

from tkinter import *
import random
root=Tk()
root.title("Member and gmail id ")
root.geometry("500x500")
root.configure(bg="red")
member_list = ["rudra , rudra@gmail.com ","preetham , preetham@gmail.com ","paras , paras@gmail.com ","anish , anish@gmail.com ","devansh , devanshbadereddi@gmail.com ","abhinav.s , abhinavsharma@gmail.com ","abhinav , abhinav@gmail.com "]
print(member_list)

label=Label(root)
label.place(relx=0.5,rely=0.7,anchor=CENTER)


def random_member():
    ran_no=random.randint(0,6)
    print(ran_no)
    random_member2=member_list[ran_no]
    print(random_member2)
    label["text"]="member is "+str(random_member2)+" "+str(ran_no)

btn = Button(root,text="Member is ",command=random_member)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)    

root.mainloop()