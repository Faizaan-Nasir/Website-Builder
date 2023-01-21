#creating a website using python
from pathlib import Path
import os

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

#inputing choices (main outline)
title=input("Enter the title for your website: ")
heading=input("Enter the main heading for your website: ")
design_ques=input("Would you like to change the looks of your heading? (yes/no): ")
margin_heading='0'
align_heading='left'
main_heading_size='10'
if design_ques=='yes':
    main_heading_size=input("What font size would you like for your heading? (in px): ")
    align_heading_ques=input("Would you like to align your text or indent it? (indent/align): ")
    if align_heading_ques=='indent':
        margin_heading=input("Enter left padding (in px): ")
    elif align_heading_ques=='align':
        align_heading=input("Horizontally align the heading (left/right/center/justify): ")

#add an image
extra_html=''
main_img_opt=input("Would you like to add a main image to your website? (yes/no): ")
if main_img_opt=='yes':
    main_img=input("Enter the link for the main image: ")
    extra_html='''<div style='text-align:center;'><img src= "'''+main_img+'''
"  class="main-img"></div>'''
    
#inputing choices (content)
subheading_add='yes'
main_content=''
margin_subheading='0'
align_subheading='left'
margin_content='0'
align_content='left'
subheading_size='10'
content_size='10'
print("You will now be asked a series of questions for the subheadings on your webpage.")
subheading_design_choice=input("Would you like to edit the style of your subheadings? (yes/no): ")
if subheading_design_choice=='yes':
    subheading_size=input("What font size would you like for your subheading? (in px): ")
    align_subheading_ques=input("Would you like to align your text or indent it? (indent/align): ")
    if align_subheading_ques=='indent':
        margin_subheading=input("Enter left padding (in px): ")
    elif align_subheading_ques=='align':
        align_subheading=input("Horizontally align the subheading (left/right/center/justify): ")
content_design_choice=input("Would you like to edit the style of your content that falls under the subheadings? (yes/no): ")
if content_design_choice=='yes':
    content_size=input("What font size would you like for your content? (in px): ")
    align_content_ques=input("Would you like to align your text or indent it? (indent/align): ")
    if align_content_ques=='indent':
        margin_content=input("Enter left padding (in px): ")
    elif align_content_ques=='align':
        align_content=input("Horizontally align the content (left/right/center/justify): ")
while subheading_add=='yes':
    subheading_img_opt=input("Would you like to add an image under this subheading? (yes/no): ")
    subheading=input("Enter your subheading: ")
    content=input("Enter the content you'd like to have under this subheading?: ")
    main_content+='''<h2 class="subheading">'''+subheading+'''</h2>
<div class="content">
    '''+content+'''
</div>'''
    subheading_add=input("Would you like to add another subheading? (yes/no): ")

#navbar questions and adding a navbar
navbar_ques=input("Would you like to add a side navbar or a top navbar? (side/top): ")
if navbar_ques=='side':
    navbar_doc=open('./library/side-navbar.txt','r')
    extra_css='<link rel="stylesheet" href="./library/side-navbar.css">'
elif navbar_ques=='top':
    navbar_doc=open('./library/top-navbar.txt','r')
    extra_css='<link rel="stylesheet" href="./library/top-navbar.css">'
O2=input("Enter the title of page 2 on navbar (page 1 is home): ")
O3=input("Enter the title of page 3 on navbar (page 1 is home): ")
O4=input("Enter the title of page 4 on navbar (page 1 is home): ")
navbar=navbar_doc.read()

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
    '''+extra_html+'''
    <h1 class="main-heading">'''+heading+'''</h1>
    '''+main_content+'''
    </div>
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
print("--------------------",O2,"--------------------")