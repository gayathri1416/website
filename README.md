# Ex.07 Restaurant Website
# Date:05.10.2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
```
views.py:
from django.shortcuts import render
def p1(request):
    return render(request,'Entrance.html')
def p2(request):
    return render(request,'Menu.html')
def p3(request):
    return render(request,'Adminstration.html')
def p4(request):
    return render(request,'Contact.html')

urls.py :

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.p1,name='home'),
    path('MENU/',views.p2,name='menu'),
    path('ADMINSTRATION/',views.p3,name='adminstration'),
    path('CONTACT US/',views.p4,name='contact'),
]

entrance.html :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KAMESH'S DELIGHTS</title>
</head>
<style>
    
.Grid {
    position: absolute; 
    top: 59%; 
    left: 10%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap:2cm;
    width: 80%;
    text-align: center;
}


.Grid .col {
    background-color: rgba(0, 0, 0, 0.5);
    box-shadow: 2px 2px 4px white;
    padding: 0.4cm;
    border-radius: 0.2cm;
    color: white;
}

.Grid .col h3,
.Grid .col h4,
.Grid .col p {
    margin: 0.4cm 0;
}
    body{
        margin:0;
        padding: 0;
        position: relative;
    }
    .main{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        text-align: center;
        color: white;
        font-size: 25px;
        padding: 1cm; 
    }
    img {
  width: 100%;
  height: 100vh;
  object-fit: cover;
  filter: brightness(50%);

}
nav a {
  text-decoration:none;
  color: rgb(91, 241, 244);
  margin: 100px;
  font-weight: bold;
}

nav a:hover {
  text-decoration:underline;
}
nav p{
    text-align: center;
    font-size:1.8cm;
    letter-spacing: 0.3cm;
    margin-top:  2cm;
    margin-bottom: 2cm;
    font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    text-shadow: 2px 2px 4px black;
}
</style>
<body>
    {% load static %}
    <img src="{% static 'interior.jpg' %}">
    
    <div class="main">
        <nav>
            <p>GAYATHRI DELIGHTS</p>
            <span style="color: aqua;">HOME</span> <a href="{% url 'menu' %}">MENU</a> <a href="{% url 'adminstration' %}">ADMINSTRATION</a> <a href="{% url 'contact' %}">CONTACT US</a>
            
        </nav>
    </div>
    <div class="Grid">
        <div class="col">
            <h3>ICONIC DISH</h3>
            <h4>5 Scoops of Ice Cream</h4>
            <p>The 5 Scoops of Ice Cream is the iconic dish of our restaurant.  
            Most guests love it and often order it after every meal. Some even visit just to enjoy this delightful treat!</p>
        </div>

    
    
        <div class="col">
            <h3>PRE-BOOK A TABLE</h3>
            <p>You can book your table up to 3 days in advance. On our Contact page, you will find our WhatsApp number.
            Send us a message, and we will ask you for details like date, time, and number of guests. Please answer all questions to confirm your booking and enjoy a wonderful dining experience!</p>
        </div>
        <div class="col">
            <h3>OPENING HOURS</h3>
            <p>
            MON – FRI: 8:00 AM – 10:00 PM
            SAT & SUN: 10:00 AM – 11:00 PM
            </p>

        </div>
    </div>

</body>
</html>

menu.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    .Grid{
        display:grid;
        grid-template-columns: repeat(4,1fr);
        row-gap: 0.0005cm;
        column-gap: 1cm;
    }
    .food-items{
        padding:15px;
    }
    .food-items img{
        width:70%;
        height: 40%;
        object-fit: cover;
        box-shadow: 6px 6px 16px rgb(10, 10, 10);
        border-radius: 50%;
        position:relative;
        display: flex;
        margin-right: auto;
        margin-left: auto;
    }
   
    p,h4{
        color: rgb(11, 1, 1);
        font-size:0.6cm;
        font-weight: 600;
        text-shadow: 2px 1px 4px white;
        text-align: center;
    }
    h1{
        color: white;
        text-shadow: 6px 6px 16px rgb(12, 0, 0);
        text-align: center;
       
        
    }
    .main{
        text-align: center;
        
        padding: 0.5cm;
    }
        a {
    text-decoration: none; 
    color: black;           
    margin: 0 100px;        
    font-weight: bold;
    font-size: x-large;
    font-family: 'Times New Roman', Times, serif;
    
}
nav {
    text-align: center;
    
    padding: 1px;
    
   }
    nav a:hover{
        text-decoration: underline;
        
    }
    .bg-img{
        position:fixed;
        object-fit: cover;
        height: 100%;
        width: 100%;
        top: 0;
        left: 0;
        
    }
    .all{
        position:relative;
        color:rgb(11, 0, 0);
        
    }


</style>
<body>
    {% load static %}
    <img src="{% static 'b.jpg' %}" class="bg-img">
<div class="all">
    <div class="main">
        <nav>
            <a href="{% url 'home' %}">HOME</a> MENU <a href="{% url 'adminstration' %}">ADMINSTRATION</a> <a href="{% url 'contact' %}">CONTACT US</a>
            
        </nav>
    </div>
    <h1>DELICIOUS FOOD MENU</h1>
    <div class="Grid">
       <div class="food-items">
        {% load static %}
       <img src="{% static 'chicken fired rice.jpg' %}" alt="picture">
       <h4>CHICKEN FIRED RICE</h4>
       <p>PRICE : Rs.200</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'beef biriyani.jpg' %}" alt="picture">
       <h4>BEEF BIRIYANI</h4>
       <p>PRICE : Rs.300</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'dosa.jpg' %}" alt="picture">
       <h4>DOSA</h4>
       <p>PRICE : Rs.150</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'chapathi and gravy.jpg' %}" alt="picture">
       <h4>CHAPATHI AND GRAVY</h4>
       <p>PRICE : Rs.150</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'parato.jpg' %}" alt="picture">
       <h4>PARATO</h4>
       <p>PRICE : Rs.160</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'burger.jpg' %}" alt="picture">
       <h4>BURGER</h4>
       <p>PRICE : Rs.300</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'pasta.jpg' %}" alt="picture">
       <h4>PASTA</h4>
       <p>PRICE : Rs.300</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'Sizzler.jpg' %}" alt="picture">
       <h4>SIZZLER</h4>
       <p>PRICE : Rs.400</p>
       </div>


       <div class="food-items">
        {% load static %}
       <img src="{% static  'french fries.jpg' %}" alt="picture">
       <h4>FRECH FRIES</h4>
       <p>PRICE : Rs.200</p>
       </div>


       <div class="food-items">
        {% load static %}
       <img src="{% static  'cold cofee1.jpg' %}" alt="picture">
       <h4>COLD COFFEE</h4>
       <p>PRICE : Rs.200</p>
       </div>

       <div class="food-items">
        {% load static %}
       <img src="{% static  'mocktail.jpg' %}" alt="picture">
       <h4>LIME MOCKTAIL</h4>
       <p>PRICE : Rs.150</p>
       </div>

 
       <div class="food-items">
        {% load static %}
       <img src="{% static  'ice cream.jpg' %}" alt="picture">
       <h4>5 SCOPES OF ICE CREAM</h4>
       <p>PRICE : Rs.400</p>
       </div>

    </div>
</div>
</body>
</html>

administration.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administration</title>
</head>
<style>
    body{
        background-color:darkmagenta;
        color:white;
    }
    h1{
        text-align: center;
        margin-bottom: 1cm;
    }
    .row1{
        display: flex;
        justify-content: center;
        gap: 10cm;
        margin-bottom: 20px;
        flex-wrap:wrap;
    }
    .row2{
        display:flex;
        justify-content: center;
        gap:8cm;
        flex-wrap:wrap;
    }
    .row1 div,.row2 div{
        text-align:center;
        width:200px;
        text-shadow: 3px 3px 13px rgb(116, 5, 5);
    }
    .row1 img,.row2 img{
        width:150px;
        height:150px;
        object-fit: cover;
        border-radius: 1cm;
        border: 1cm;
        border-color:white;
        margin-bottom:10px;
        box-shadow: 4px 4px 6px rgb(17, 15, 9);
        
    }
        a {
    text-decoration: none; 
    color: rgb(9, 0, 0);           
    margin: 0 100px;        
    font-weight: bold;
    font-size: x-large;
    font-family: 'Times New Roman', Times, serif;
    
}
nav {
    text-align: center;
    background-color: rgba(43, 239, 242, 0.871);
    padding: 1px;
    color: black;
    box-shadow: 2px 2px 16px black;
    
   }


</style>
<body>
<div class="main">
        <nav>
            <p><a href="{% url 'home' %}">HOME</a> <a href="{% url 'menu' %}">MENU</a> ADMINSTRATION <a href="{% url 'contact' %}">CONTACT US</a>
            </p>
        </nav>
    </div>
    
    <h1>MEET OUR TEAM</h1>
    <div class="row1">
    <div class="Founder">
        {% load static %}
        <img src="{% static 'founder.jpg' %}" alt="Founder img">
        <h2>MRS.SELVI</h2>
        <h4>FOUNDER</h4>
        <p></p>
    </div>
    <div class="co-Founder" >
        {% load static %}
        <img src="{% static 'co founder.jpg' %}" alt="co-founder img">
        <h2>MR.CHANDRU</h2>
        <h4>CO-FOUNDER</h4>
        <p></p>
    </div>
    </div>
    <div class="row2">
    <div class="CHEF1">
         {% load static %}
        <img src="{% static 'bhat.jpg' %}" alt="Chef img">
        <h2>CHEF VENKATESH BHAT</h2> 
        <p>ASIAN CUISINE SPECIALIST</p>
    </div>
    <div class="CHEF2">
         {% load static %}
        <img src="{% static 'shreeya.jpg' %}" alt="Chef img">
        <h2>CHEF SHREEYA ADKA</h2>
        <p>PASTRY & COCKTAIL SPECIALIST</p>
    </div>
    <div class="CHEF3">
        {% load static %}
        <img src="{% static 'mad.jpg' %}" alt="Chef img">
        <h2>CHEF KOUSHIK SHANKAR</h2>
        <p>CONTINENTAL & FAST FOOD SPECIALIST</p>
    </div>
</div>
</body>
</html>

contact us.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<style>
       a {
    text-decoration: none; 
    color: black;           
    margin: 0 100px;        
    font-weight: bold;
    font-size: x-large;
    font-family: 'Times New Roman', Times, serif;
    
}
nav {
    text-align: center;
    background-color: rgba(43, 239, 242, 0.871);
    padding: 1px;
    
   }
   h2{
    color: darkmagenta;
    text-align: center;
   }
   pre{
    
    color: rgb(248, 236, 15);
    font-size: larger;
    font-family:cursive;
   }
   .main{
    font-size: x-large;
   }
   .a{
    background-color:maroon;
    box-shadow: 4px 4px 10px rgb(28, 11, 11);
    padding: 0.5cm;
    display: flex;
    justify-content: center; 
    align-items: center;     
    text-align: center;
    margin-left: auto;
    margin-right:auto;
    width: 90%;
    margin: 0 2cm;

  
   }
   .b{
    background-color:maroon;
    box-shadow: 4px 4px 10px rgb(28, 11, 11);
    padding: 0.5cm;
    display: flex;
    justify-content: center; 
    align-items: center;     
    text-align: center;
    margin-left: auto;
    margin-right:auto;
    width: 90%;
    margin: 0 2cm;
   }
   .c{
    background-color:maroon;
    box-shadow: 4px 4px 10px rgb(28, 11, 11);
    padding: 0.5cm;
    display: flex;
    justify-content: center; 
    align-items: center;     
    text-align: center;
    margin-left: auto;
    margin-right:auto;
    width: 90%;
    margin: 0 2cm;
    
   }
</style>
<body>
<div class="main">
        <nav>
            <p><a href="{% url 'home' %}">HOME</a> <a href="{% url 'menu' %}">MENU</a> <a href="{% url 'adminstration' %}">ADMINSTRATION</a> CONTACT US
            </p>
        </nav>
    
    <h2>CONNECT WITH US :</h2>
    <div class="a"><pre>
📸Instagram        : Kamesh_Delights06
▶️Youtube Channel  : Kamesh_world
🌐Facebook         : KameshDelights</div>

    </pre>
    <h2>FOR PRE-BOOKING:</h2>
  <div class="b">
    <pre>📞 Whatsapp:+91 9094722116
    </pre></div>

    <h2>SUPPORT/QUERIES:</h2>
  <div class="c">
    <pre>CONTACT:
        📞 Call :+91 9094722118
        ✉️ Email:kameshdelights26@gmail.com</pre></div>
</div>
</body>
</html>
```
# OUTPUT:

![alt text](<Screenshot 2025-10-05 191707.png>)
![alt text](<Screenshot 2025-10-05 191917.png>)
![alt text](<Screenshot 2025-10-05 192108.png>)
![alt text](<Screenshot 2025-10-05 192215.png>)
![alt text](<Screenshot 2025-10-05 192336.png>)
![alt text](<Screenshot 2025-10-05 192402.png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
