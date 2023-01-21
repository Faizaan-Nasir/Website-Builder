from pathlib import Path
import os
import index_2

O2=index_2.O2
O3=index_2.O3
O4=index_2.O4
navbar=index_2.navbar
extra_css=index_2.extra_css
title2=O2
heading2=O2
margin_heading2=index_2.margin_heading
align_heading2=index_2.align_heading
main_heading_size2=index_2.main_heading_size

second_file='page2.html'
css2_file='./css/style2.css'
if os.path.isfile(second_file):
    os.remove(second_file)
if os.path.isfile(css2_file):
    os.remove(css2_file)
    print("Pre-existing file(s) has been removed.")
website2=open('page2.txt','w')
stylesheet2=open('./css/style2.txt','w')

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
    extra_css+='<link rel="stylesheet" href="./library/products.css">'
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
print('''---------- WEBSITE CREATED (LOCATE INDEX.HTML IN DOWNLOADED FOLDER) ----------''')