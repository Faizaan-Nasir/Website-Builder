from pathlib import Path
import os

second_file='page2.html'
css2_file='./css/style2.css'
if os.path.isfile(second_file):
    os.remove(second_file)
if os.path.isfile(css2_file):
    os.remove(css2_file)
    print("Pre-existing file(s) has been removed.")
website2=open('page2.txt','w')
stylesheet2=open('./css/style2.txt','w')

title2=input("Enter the title for your page number 2: ")
heading2=input("Enter the main heading for your page number 2: ")
design_ques2=input("Would you like to change the looks of your heading? (yes/no): ")
margin_heading2='0'
align_heading2='left'
main_heading_size2='10'
if design_ques2=='yes':
    main_heading_size2=input("What font size would you like for your heading? (in px): ")
    align_heading_ques2=input("Would you like to align your text or indent it? (indent/align): ")
    if align_heading_ques2=='indent':
        margin_heading2=input("Enter left padding (in px): ")
    elif align_heading_ques2=='align':
        align_heading2=input("Horizontally align the heading (left/right/center/justify): ")
extra_html2=''
main_img_opt2=input("Would you like to add a main image to your website? (yes/no): ")
if main_img_opt2=='yes':
    main_img2=input("Enter the link for the main image: ")
    extra_html2='''<div style='text-align:center;'><img src= "'''+main_img2+'''
"  class="main-img"></div>'''

purpose=input("What would you like to do with this page? (display products/create a checklist/none): ")
extra_feature=str()
if purpose=="display products":
    display_prod_opt="yes"
    extra_css='<link rel="stylesheet" href="./library/products.css">'
    while display_prod_opt=="yes":
        prod_img=input("Enter link to image of product: ")
        prod_head=input("Enter the product name: ")
        prod_des=input("Enter the product description: ")
        display_prod_opt=input("Would you like to add another product? (yes/no): ")
        extra_feature+=str('''<div class="container">
  <img src="'''+prod_img+'''
" alt="product image" class="image">
  <div class="overlay">
    <div class="text">
    <h2>'''+prod_head+'''</h2>
    '''+prod_des+'''
    </div>
  </div>
</div>''')

navbar_ques=input("Would you like to add a side navbar or a top navbar? (side/top): ")
if navbar_ques=='side':
    navbar_doc=open('./library/side-navbar.txt','r')
    extra_css='<link rel="stylesheet" href="./library/side-navbar.css">'
elif navbar_ques=='top':
    navbar_doc=open('./library/top-navbar.txt','r')
    extra_css+='<link rel="stylesheet" href="./library/top-navbar.css">'
O2=input("Enter the title of page 2 on navbar (page 1 is home): ")
O3=input("Enter the title of page 3 on navbar (page 1 is home): ")
O4=input("Enter the title of page 4 on navbar (page 1 is home): ")
navbar=navbar_doc.read()

stylesheet_content2='''.main-heading{
    font-size: '''+main_heading_size2+'''px;
    padding-left: '''+margin_heading2+'''px;
    text-align: '''+align_heading2+''';
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
'''

html_content2='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'''+title2+'''</title>
    <link rel="stylesheet" href="./css/style2.css">
    '''+extra_css+'''
</head>
<body>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a class="active" href='page2.html'>'''+O2+'''</a></li>
        <li><a href='page3.html'>'''+O3+'''</a></li>
        <li><a href='page4.html'>'''+O4+'''</a></li>
    </ul>
    '''+navbar+'''
    '''+extra_html2+'''
    <h1 class="main-heading">'''+heading2+'''</h1>
    <div class="main-container">
    '''+extra_feature+'''
    </div>
    </div>
</body>
</html>'''

website2.write(html_content2)
website2.close()
stylesheet2.write(stylesheet_content2)
stylesheet2.close()
website_ext2 = Path('page2.txt')
website_ext2.rename(website_ext2.with_suffix('.html'))
stylesheet_ext2 = Path('./css/style2.txt')
stylesheet_ext2.rename(stylesheet_ext2.with_suffix('.css'))
