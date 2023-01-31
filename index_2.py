#creating a website using python
from pathlib import Path
import os
from tkinter import *

#DEFINING NECESSARY FUNCTIONS
def get_text():
    global title
    global heading
    global O2
    global O3
    global O4
    global link1_name
    global link1_link
    global link2_name
    global link2_link
    global extra_html
    if extra_html!="":
        extra_html='''<div style='text-align:center;'><img src= "'''+main_img.get()+'''
    "  class="main-img"></div>'''
    link1_name=link1_name.get()
    link1_link=link1_link.get()
    link2_name=link2_name.get()
    link2_link=link2_link.get()
    O2=O2.get()
    O3=O3.get()
    O4=O4.get()
    title=title_e.get()
    heading=heading_e.get()
    top.destroy()

def padding_heading():
    global margin_heading
    global align_heading
    margin_heading_l=Label(child, text="Padding left (px): ", font=("Sans",12))
    margin_heading_l.pack()
    margin_heading_l.place(relx=0.1, rely=0.35)
    margin_heading=Entry(child, bd=0, font=("Sans",12))
    margin_heading.pack()
    margin_heading.place(relx=0.5, rely=0.35)
    align_heading='left'
    margin_heading=margin_heading.get()

def align_heading():
    global align_heading
    global margin_heading
    align_heading_l=Label(child, text="Align (center/right/left): ", font=("Sans",12))
    align_heading_l.pack()
    align_heading_l.place(relx=0.1, rely=0.35)
    align_heading=Entry(child, bd=0, font=("Sans",12))
    align_heading.pack()
    align_heading.place(relx=0.5, rely=0.35)
    margin_heading='0'
    align_heading=align_heading.get()

def change_design():
    global child
    child=Toplevel(top)
    child.title("Heading Designs")
    child.geometry("800x250")
    global main_heading_size
    global align_heading_size
    global margin_heading
    global align_heading
    Align_Indent=IntVar()
    main_heading_size_l=Label(child, text="Enter your heading size: ", font=("Sans",12))
    main_heading_size_l.pack()
    main_heading_size_l.place(relx=0.1, rely=0.12)
    main_heading_size=Entry(child, bd=0, font=("Sans",12))
    main_heading_size.pack()
    main_heading_size.place(relx=0.5, rely=0.12)
    align_heading_ques_l=Label(child, text="Align or Indent heading: ", font=("Sans",12))
    align_heading_ques_l.pack()
    align_heading_ques_l.place(relx=0.1, rely=0.25)
    r1 = Radiobutton(child, text="Align", value=1, command=align_heading, font=("Sans",10), variable=Align_Indent)
    r1.pack( anchor = W )
    r1.place(relx=0.5, rely=0.25)
    r2 = Radiobutton(child, text="Indent", value=2, font=("Sans",10), command=padding_heading, variable=Align_Indent)
    r2.pack( anchor = W )
    r2.place(relx=0.6, rely=0.25)
    def close():
        global main_heading_size
        main_heading_size=main_heading_size.get()
        child.destroy()
    close=Button(child, text="SUBMIT", bd=0, bg="white", command=close)
    close.pack()
    close.place(relx=0.5, rely=0.6, anchor=CENTER)

def change_design_no():
    global main_heading_size
    global margin_heading
    global align_heading
    margin_heading='0'
    align_heading='center'
    main_heading_size='40'

def add_image():
    global main_img
    global extra_html
    main_img_l=Label(top, text="Image link: ", font=("Sans",18))
    main_img_l.pack()
    main_img_l.place(relx=0.5,rely=0.25)
    main_img=Entry(top,bd=0,font=("Sans",18))
    main_img.pack()
    main_img.place(relx=0.7,rely=0.25)
    extra_html="place-holder"
    
def add_image_no():
    global extra_html
    extra_html=""

def submitpage():
    global main_content
    main_content+='''<h2 class="subheading">'''+subheading_e.get()+'''</h2>
<div class="content">
    '''+content.get('1.0',END)+'''
</div>'''
    global i
    i+=1
    subheading_page.destroy()
    add_subheading()
def subheading():
    global main_content
    global subheading_add
    global i
    i=0
    main_content=""
    subheading_add=int(subheading_add.get())
    add_subheading()
def add_subheading():
    global subheading_page
    global subheading_e
    global content
    if i<subheading_add:
        subheading_page=Toplevel(top)
        subheading_page.geometry("800x800")
        subheading_page.title(("Subheading "+str(i+1)))
        subheading_l=Label(subheading_page, text="Enter Subheading "+str(i+1), font=("Sans",12))
        subheading_l.pack()
        subheading_l.place(relx=0.5,rely=0.2, anchor=CENTER)
        subheading_e=Entry(subheading_page, font=("Sans",12),bd=0)
        subheading_e.pack()
        subheading_e.place(relx=0.5, rely=0.25, anchor=CENTER)
        content_l=Label(subheading_page, text="Enter your content under this subheading:", font=("Sans",12))
        content_l.pack()
        content_l.place(relx=0.5, rely=0.3, anchor=CENTER)
        content=Text(subheading_page,width=20,height=3,font=("Sans",12),bd=0,wrap = WORD)
        content.pack()
        content.place(relx=0.5,rely=0.38,anchor=CENTER)
        submit_page=Button(subheading_page,text="SUBMIT", command=submitpage)
        submit_page.pack()
        submit_page.place(relx=0.5,rely=0.5,anchor=CENTER)

def top_nav():
    global navbar_ques
    navbar_ques='top'
def side_nav():
    global navbar_ques
    navbar_ques='side'
#Tkinter creates an application
top = Tk()
top.title("Website Constructor")
top.geometry("1800x900")
# top.configure(bg='#D3D3D3')

#TKINTER DISPLAY ELEMENTS
page_heading=Label(top, text="Website Constructor", font=("Sans",30))
page_heading.pack()
page_heading.place(relx=0.5, anchor=CENTER, rely=0.05)

#Title of webpage
title_l=Label(top, text="Title for your website: ", font=("Sans",18))
title_l.pack()
title_l.place(relx=0.10, rely=0.1)
title_e=Entry(top,bd=0, font=("Sans",18))
title_e.pack()
title_e.place(rely=0.1, relx=0.30)

#Heading of webpage
heading_l=Label(top, text="Heading for your website: ", font=("Sans",18))
heading_l.pack()
heading_l.place(relx=0.1, rely=0.15)
heading_e=Entry(top,bd=0, font=("Sans",18))
heading_e.pack()
heading_e.place(rely=0.15, relx=0.30)

#Would you like to change the design of heading?
design_ques_l=Label(top, text="Change heading style?: ", font=("Sans",18))
design_ques_l.pack()
design_ques_l.place(relx=0.1, rely=0.20)
Y_N_1=IntVar()
R1 = Radiobutton(top, text="Yes", value=1,command=change_design, font=("Sans",18), variable=Y_N_1)
R1.pack( anchor = W )
R1.place(relx=0.3, rely=0.20)
R2 = Radiobutton(top, text="No", value=2, font=("Sans",18), command=change_design_no, variable=Y_N_1)
R2.pack( anchor = W )
R2.place(relx=0.4, rely=0.20)


#Would you like to add an image to your webpage?
image_l=Label(top, text="Image for your website? ", font=("Sans",18))
image_l.pack()
image_l.place(relx=0.1,rely=0.25)
Y_N_2=IntVar()
R3 = Radiobutton(top, text="Yes", value=1,command=add_image, font=("Sans",18), variable=Y_N_2)
R3.pack( anchor = W )
R3.place(relx=0.3, rely=0.25)
R4 = Radiobutton(top, text="No", value=2, font=("Sans",18), command=add_image_no, variable=Y_N_2)
R4.pack( anchor = W )
R4.place(relx=0.4, rely=0.25)

#Number of subheading you'd like to enter
subheading_no_l=Label(top,text="No. of Subheadings: ", font=("Sans",18))
subheading_no_l.pack()
subheading_no_l.place(relx=0.1, rely=0.30)
subheading_add=Entry(top,font=("Sans",18),bd=0)
subheading_add.pack()
subheading_add.place(relx=0.3, rely=0.3)
request=Button(top, text="Enter Subheadings", command=subheading)
request.pack()
request.place(relx=0.5,rely=0.3)

#Navbar selection
navbar_opt=Label(top, text="Type of Navbar: ", font=("Sans",18))
navbar_opt.pack()
navbar_opt.place(relx=0.1,rely=0.35)
Y_N_3=IntVar()
R5 = Radiobutton(top, text="Top", value=1,command=top_nav, font=("Sans",18), variable=Y_N_3)
R5.pack( anchor = W )
R5.place(relx=0.3, rely=0.35)
R6 = Radiobutton(top, text="Side", value=2, font=("Sans",18), command=side_nav, variable=Y_N_3)
R6.pack( anchor = W )
R6.place(relx=0.4, rely=0.35)

#Navbar options
navbar_lO1=Label(top,text="Title of Page 2: ", font=("Sans",18))
navbar_lO1.pack()
navbar_lO1.place(relx=0.1, rely=0.40)
O2=Entry(top,font=("Sans",18),bd=0)
O2.pack()
O2.place(relx=0.3, rely=0.4)
navbar_lO2=Label(top,text="Title of Page 3: ", font=("Sans",18))
navbar_lO2.pack()
navbar_lO2.place(relx=0.1, rely=0.45)
O3=Entry(top,font=("Sans",18),bd=0)
O3.pack()
O3.place(relx=0.3, rely=0.45)
navbar_lO3=Label(top,text="Title of Page 4: ", font=("Sans",18))
navbar_lO3.pack()
navbar_lO3.place(relx=0.1, rely=0.50)
O4=Entry(top,font=("Sans",18),bd=0)
O4.pack()
O4.place(relx=0.3, rely=0.50)

#Footer
link1_name_l=Label(top,text="Title 1 Footer: ", font=("Sans",18))
link1_name_l.pack()
link1_name_l.place(relx=0.1, rely=0.55)
link1_name=Entry(top,font=("Sans",18),bd=0)
link1_name.pack()
link1_name.place(relx=0.3, rely=0.55)
link1_link_l=Label(top,text="Link 1 Footer: ", font=("Sans",18))
link1_link_l.pack()
link1_link_l.place(relx=0.1, rely=0.60)
link1_link=Entry(top,font=("Sans",18),bd=0)
link1_link.pack()
link1_link.place(relx=0.3, rely=0.60)
link2_name_l=Label(top,text="Title 2 Footer: ", font=("Sans",18))
link2_name_l.pack()
link2_name_l.place(relx=0.5, rely=0.55)
link2_name=Entry(top,font=("Sans",18),bd=0)
link2_name.pack()
link2_name.place(relx=0.7, rely=0.55)
link2_link_l=Label(top,text="Link 2 Footer: ", font=("Sans",18))
link2_link_l.pack()
link2_link_l.place(relx=0.5, rely=0.60)
link2_link=Entry(top,font=("Sans",18),bd=0)
link2_link.pack()
link2_link.place(relx=0.7, rely=0.60)

#Submit button
submit = Button(top, text='SUBMIT', bd=0, bg='white', command=get_text)
submit.pack()
submit.place(height=35, width=100, relx=0.5, rely=0.9, anchor=CENTER)
top.mainloop()
#END OF TKINTER

#removing files if they exist (currently only for developers)
main_file='index.html'
css_file='./css/style.css'
if os.path.isfile(main_file):
    os.remove(main_file)
if os.path.isfile(css_file):
    os.remove(css_file)
    print("Pre-existing file(s) has been removed.")
website=open('index.txt','w')
stylesheet=open('./css/style.txt','w')
    
#inputing choices (content)
subheading_add='yes'
margin_subheading='20'
align_subheading='left'
margin_content='35'
align_content='left'
subheading_size='30'
content_size='20'
# print("You will now be asked a series of questions for the subheadings on your webpage.")
# subheading_design_choice=input("Would you like to edit the style of your subheadings? (yes/no): ")
# if subheading_design_choice=='yes':
#     subheading_size=input("What font size would you like for your subheading? (in px): ")
#     align_subheading_ques=input("Would you like to align your text or indent it? (indent/align): ")
#     if align_subheading_ques=='indent':
#         margin_subheading=input("Enter left padding (in px): ")
#     elif align_subheading_ques=='align':
#         align_subheading=input("Horizontally align the subheading (left/right/center/justify): ")
# content_design_choice=input("Would you like to edit the style of your content that falls under the subheadings? (yes/no): ")
# if content_design_choice=='yes':
#     content_size=input("What font size would you like for your content? (in px): ")
#     align_content_ques=input("Would you like to align your text or indent it? (indent/align): ")
#     if align_content_ques=='indent':
#         margin_content=input("Enter left padding (in px): ")
#     elif align_content_ques=='align':
#         align_content=input("Horizontally align the content (left/right/center/justify): ")

#navbar questions and adding a navbar
if navbar_ques=='side':
    navbar_doc=open('./library/side-navbar.txt','r')
    extra_css='<link rel="stylesheet" href="./library/side-navbar.css">'
elif navbar_ques=='top':
    navbar_doc=open('./library/top-navbar.txt','r')
    extra_css='<link rel="stylesheet" href="./library/top-navbar.css">'
navbar=navbar_doc.read()

#footer
footer=""
# link1_name=input("Enter name for link 1 in footer: ")
# link1_link=input("Enter link for the name 1: ")
# link2_name=input("Enter name for link 2 in footer: ")
# link2_link=input("Enter link for the name 2: ")
footer=str('''<footer>
    <div class="footer-links"><a href="'''+link1_link+'''
    ">'''+link1_name+'''</a><br><br>
    <a href="'''+link2_link+'''
    ">'''+link2_name+'''</a></div>
</footer>''')

#everything combines here
stylesheet_content='''.main-heading{
    font-size: '''+main_heading_size+'''px;
    padding-left: '''+margin_heading+'''px;
    text-align: '''+align_heading+''';
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.subheading {
    font-size: '''+subheading_size+'''px;
    padding-left: '''+margin_subheading+'''px;
    text-align: '''+align_subheading+''';
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.content {
    font-size: '''+content_size+'''px;
    padding-left: '''+margin_content+'''px;
    padding-right: '''+margin_content+'''px;
    text-align: '''+align_content+''';
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.main-img{
    border-radius:20px;
    margin-top:40px;
}

.footer-links{
    text-decoration: none;
    vertical-align: middle;
    margin-left: 50px;
    color: white;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    position: absolute;
    top: 50%;
    transform: translate(0%, -50%);
}

a{
    color: inherit;
    text-decoration: none;
}

footer{
    background-color: rgb(52, 52, 52);
    height: 180px;
    margin-top: 30px;
    position: relative;
}

body {
    background-color: aliceblue;
}
'''
html_content='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'''+title+'''</title>
    <link rel="stylesheet" href="./css/style.css">
    '''+extra_css+'''
</head>
<body>
    <ul>
        <li><a class="active" href="index.html">Home</a></li>
        <li><a href='page2.html'>'''+O2+'''</a></li>
        <li><a href='page3.html'>'''+O3+'''</a></li>
        <li><a href='page4.html'>'''+O4+'''</a></li>
    </ul>
    '''+navbar+'''
    <h1 class="main-heading">'''+heading+'''</h1>
    '''+extra_html+'''
    '''+main_content+'''
    </div>
    '''+footer+'''
</body>
</html>'''

#everything gets written into the documents here (prog. will create one if it doesn't exists)
website.write(html_content)
website.close()
stylesheet.write(stylesheet_content)
stylesheet.close()
website_ext = Path('index.txt')
website_ext.rename(website_ext.with_suffix('.html'))
stylesheet_ext = Path('./css/style.txt')
stylesheet_ext.rename(stylesheet_ext.with_suffix('.css'))
print("--------------------",O2," (Questions for next page) --------------------")