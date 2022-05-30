import pandas as pd
from tkinter import *
from tkinter import messagebox, ttk

window = Tk()
window.title("도서 관리 프로그램")
window.geometry("800x600")
window.resizable(width = False, height = False)

def Member_make(event) :
    def quit1() :
        toplevel.destroy()

    def register() :
        MsgBox = messagebox.askquestion ('등록 확인','등록하시겠습니까??')
        if MsgBox == 'yes':
            messagebox.showinfo("등록 완료", "등록이 완료되었습니다.")
            toplevel.destroy()
        else:
            messagebox.showinfo("등록 취소", "등록이 취소되었습니다.")
            toplevel.destroy()


    toplevel=Toplevel(window)
    toplevel.geometry("700x500")

    label=Label(toplevel, text="회원등록", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    phonelabel1 = Label(toplevel, text = "전화번호")
    phonelabel1.place(x = 225, y= 100)
    phonetext = Entry(toplevel, width = 20)
    phonetext.place(x = 325, y= 100)

    namelabel1 = Label(toplevel, text = "이름")
    namelabel1.place(x = 225, y= 150)
    nametext = Entry(toplevel, width = 20)
    nametext.place(x = 325, y= 150)

    birthdaylabel1 = Label(toplevel, text = "생일")
    birthdaylabel1.place(x = 225, y=200 )
    birthdaytext = Entry(toplevel, width = 20)
    birthdaytext.place(x = 325, y= 200)

    sexlabel1 = Label(toplevel, text = "성별")
    sexlabel1.place(x = 225, y= 250)
    sextext = Entry(toplevel, width = 20)
    sextext.place(x = 325, y= 250)

    maillabel1 = Label(toplevel, text = "메일")
    maillabel1.place(x = 225, y= 300)
    mailtext = Entry(toplevel, width = 20)
    mailtext.place(x = 325, y= 300)

    clearbutton = Button(toplevel, text = "등록", command = register)
    cancelbutton = Button(toplevel, text = "취소", command = quit1)
    clearbutton.place(x = 275, y = 400)
    cancelbutton.place(x = 375, y = 400)

def Member_search(event) : 
    def search() :
        treeview = ttk.Treeview(toplevel2, column = ["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"],
            displaycolumns=["이름", "생년월일", "전화번호", "성별", "탈퇴여부", "대여여부"])
        treeview.place(x= 50, y = 170)
        treeview.column("이름", width = 100, anchor = CENTER)
        treeview.heading("이름", text = "이름", anchor = CENTER)
        treeview.column("생년월일", width = 100, anchor = CENTER)
        treeview.heading("생년월일", text = "생년월일", anchor = CENTER)
        treeview.column("전화번호", width = 100, anchor = CENTER)
        treeview.heading("전화번호", text = "전화번호", anchor = CENTER)
        treeview.column("성별", width = 100, anchor = CENTER)
        treeview.heading("성별", text = "성별", anchor = CENTER)
        treeview.column("탈퇴여부", width = 100, anchor = CENTER)
        treeview.heading("탈퇴여부", text = "탈퇴여부", anchor = CENTER)
        treeview.column("대여여부", width = 100, anchor = CENTER)
        treeview.heading("대여여부", text = "대여여부", anchor = CENTER)
        treeview["show"] = "headings"

    def choice() :
        toplevel3 =Toplevel(window)
        toplevel3.geometry("700x500")

        label=Label(toplevel3, text="회원 정보 상세 창", font = ("돋움체", 20), anchor = N)
        label.place(x = 225, y = 30)

        phonelabel3 = Label(toplevel3, text = "전화번호")
        phonelabel3.place(x = 225, y= 90)
        phonetext2 = Entry(toplevel3, width = 20)
        phonetext2.place(x = 325, y= 90)

        namelabel3 = Label(toplevel3, text = "이름")
        namelabel3.place(x = 225, y= 140)
        nametext2 = Entry(toplevel3, width = 20)
        nametext2.place(x = 325, y= 140)

        birthdaylabel3 = Label(toplevel3, text = "생일")
        birthdaylabel3.place(x = 225, y=190 )
        birthdaytext2 = Entry(toplevel3, width = 20)
        birthdaytext2.place(x = 325, y= 190)

        sexlabel3 = Label(toplevel3, text = "성별")
        sexlabel3.place(x = 225, y= 240)
        sextext2 = Entry(toplevel3, width = 20)
        sextext2.place(x = 325, y= 240)

        maillabel3 = Label(toplevel3, text = "메일")
        maillabel3.place(x = 225, y= 290)
        mailtext2 = Entry(toplevel3, width = 20)
        mailtext2.place(x = 325, y= 290)

        rentlabel = Label(toplevel3, text = "대여 여부")
        rentlabel.place(x = 185, y= 340)
        renttext = Entry(toplevel3, width = 5)
        renttext.place(x = 255, y= 340)

        quitlabel1 = Label(toplevel3, text = "탈퇴 여부")
        quitlabel1.place(x = 385, y= 340)
        quittext = Entry(toplevel3, width = 5)
        quittext.place(x = 455, y= 340)

        def modify() :
            messagebox.showinfo("수정 완료", "수정이 완료되었습니다.")
            toplevel3.destroy()
            toplevel2.destroy()

        def out() :
            messagebox.showinfo("탈퇴 완료", "탈퇴가 완료되었습니다.")
            toplevel3.destroy()
            toplevel2.destroy()
        
        def cancel() :
            toplevel3.destroy()

        modifybutton = Button(toplevel3, text = "수정", command = modify)
        outbutton = Button(toplevel3, text = "탈퇴", command = out)
        cancelbutton = Button(toplevel3, text = "취소", command = cancel)
        modifybutton.place(x = 275, y = 400)
        outbutton.place(x = 325, y = 400)
        cancelbutton.place(x = 375, y = 400)

    def quit2() :
        toplevel2.destroy()

    toplevel2=Toplevel(window)
    toplevel2.geometry("700x500")

    label=Label(toplevel2, text="회원조회", font = ("돋움체", 20))
    label.place(x = 290, y = 30)

    phonelabel1 = Label(toplevel2, text = "전화번호")
    phonelabel1.place(x = 225, y= 80)
    phonetext2 = Entry(toplevel2, width = 20)
    phonetext2.place(x = 325, y = 80)

    namelabel2 = Label(toplevel2, text = "이름")
    namelabel2.place(x = 225, y = 130)
    nametext2 = Entry(toplevel2, width = 20)
    nametext2.place(x = 325, y = 130)

    searchbutton = Button(toplevel2, text = "조회", command = search)
    choicebutton = Button(toplevel2, text = "선택", command = choice)
    cancelbutton = Button(toplevel2, text = "취소", command = quit2)
    searchbutton.place(x = 275, y = 400)
    choicebutton.place(x = 325, y = 400)
    cancelbutton.place(x = 375, y = 400)


titlelabel = Label(window, text = "도서 관리 프로그램", font = ("돋움체",30))
titlelabel.place(x = 215, y = 30)

MemberRegi = Button(window, text = "회원 등록", width = 10, height = 2)
MemberRegi.place(x = 50, y = 150)
MemberRegi.bind("<Button-1>", Member_make)

MemberSearch = Button(window, text = "회원 조회", width = 10, height = 2)
MemberSearch.place(x = 200, y = 150)
MemberSearch.bind("<Button-1>", Member_search)

window.mainloop()