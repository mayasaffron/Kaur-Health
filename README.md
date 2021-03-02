# Kaur Health

[picture]

Link to [Deployed Site]()

Juspreet Kaur is a health coach specialising in the following areas of female health; 

- Health coaching for women to improve general attitude toward food
- Natural Family Planning for couples to conceive  or avoid pregnancy (natural, non-medical contraception)
- DIY cheimcal-free skin care products

[Kaur Health]() is the colation of Juspreets services, which offers the opportunity for potential clients to learn a little more about her and herjourney and how she can potentially hekp them on theirs. 
The site also publishes blog posts about relevant topics, where the site visitors can leave a comment.



This image is created with [ami.responsivedesign]().

## Table of Contents

1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Personas](#personas)
    - [Design](#design)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Landing Page](#landing-page)
        - [Product Page](#product-page)
        - [Cart Page](#cart-page)
        - [Checkout Page](#checkout-page)
        - [Blog Page](#blog-page)
        - [Profiles Page](#profiles-page)
        - [Admin Product Managment](#admin-product-managment)
        - [Django allauth features](#django-allauth-features)
    - [Features Left to Implement](#features-left-to-implement)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#data-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Packages](#libraries-and-packages)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment with AWS](#heroku-deployment-with-aws)
    - [Local Deployment](#local-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)


# UX
## Project Goals
### Target Audience
- People who are interested in gaining support with; intuitive eating; menstrual health; natural family planning and natural skin care.
- People who want to learn more about any of these topics. 
- People who want to read interesting blog articles about intuitive eating; menstrual health; natural family planning.
- People who seek Juspreets services for a loved one struggling with any of the issues. 
- couples who want to learn how to manage their fertility. 

### Visitor / User Goals
- Purchase services and products in a smooth and secure way
- Get informed on the services/products before buying, with product reviews / product information
- Gain interesting knowledge about iintuitive eating; menstrual health; natural family planning and natural skin care, from blog articles and leave a comment on blog articles
- have login details which provide them with prefilled forms with their information, to save time.

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish Kaur health as a credible brand
- Expand Kaur health effectively
- Make profit from selling products / services
- Increasing client retention by providing a login and special benefits as a result

<div><a href="#table-of-contents">Back to top</a></div>

## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Access the website on both larger and smaller screened devices | Access the website on my phone and PC |
| Site User | Easily navigate to the Products and services available | Find the product or service I want to purchase |  
| Site User | Read all content clearly | Enjoy using the site. |
| Site User | See a shopping cart icon on nav bar | Always check the current order and checkout when I want |
| Site User | Be able to easily access information about Juspreet and the services she offers | Trust the validity of her and her services. |


<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information and access blog articles |  
| Site User | View my order history | Purchase the same product again in the next order |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site User | Post a blog about any of my areas of expertise | Provide site visitors interesting information and hopefully make a sale as a result |
| Site User | Add comments to the blog posts | Write down my thoughts on the post |
| Site User | Have the ability to remove unsavoury comments | Protect my brand and the site visitors' experince |
<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | View individual product pages that have prices and descriptions | Get detailed information about the product before purchasing |
| Site User| Filter by a specific category | Easily find products in a specific category |
| Site User | Leave/View product reviews with scores | Understand which products are popular with other customers |
| Site User | Easily add a new product | Make sure the online site has the latest catalogue |
| Site User | Easily remove a product | Make sure the online site has the latest catalogue |

<br/>

- Cart, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily select the quantity (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
| Site User | Have my delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Site User | Be reminded to log in if I did not log in | Smoothly proceed with my purchase and prefilled form | 


<br/>

<div><a href="#table-of-contents">Back to top</a></div>


## Personas 

| MY NAME IS    | I AM.. | KAUR HEALTH SERVES ME BECAUSE.. |
| ----------- | ----------- | ----------- |
| Evelyn,  | 31, mother of 2 children under 5 | I do not want ANY more children, but hormonal contraception does not agree with my body. I need to learn how to naturally manage my fertility. |
| Luke | 28, skincare influencer | People rely on my to tell them which brands have the best skincare products available. I have been in the industry long enough to know, DIY skincare is always better than anything shop bought, I just need to know what to do and how to do it, so that I can share with my followers! |  
| Jocelyn | 23, University graduate | I have suffered with period pain my entire life and recently read some research about how foods can trigger PMS. There is so little out there, I want to read relevant articles/ opinions on the topic.  |
| Kaya | 28, teacher in a committed relationship | My partner and I are trying for a baby and could really use some assistance. I want to speak to a profesional about when I am most fertile and how to navigate ovulation windows. |



## UX Design process

### UX Research 
<!-- fill this in w/ updated stuff-->
Initially, I had the idea to make an app which I would use in my career as a Personal Trainer, however, with the help of my wonderful [mentor](https://github.com/SinCron) I recognised that my emotional investment in the fruition of this project idea, was blocking my ability to see the importance of the functionality. It was also an idea, which required the user to already be aware of other such apps/ technology and was therefore not as accessible as the current idea I have run with. 

I went for a COVID test and in the booking stages, I was being asked about what symptoms I have had to make me think that I may have contracted the virus. 

This triggered my idea, I thought that the average person, may not be able to accurately track when they started experiencing symptoms and unless faced with a format that asked you the right questions, the person may not recognise the severity of their symptoms. 

I used the easy to understand the format of the [official gov- NHS site](https://www.gov.uk/get-coronavirus-test) and understood that user accessibility was of the utmost importance. 

I knew that I wanted to create an app that would:
- Relieve the average person of the task of remembering what exactly their symptoms were and when they developed. 
- Provide a mechanism so that these symptoms could be updated/ deleted and created EASILY.
- Ensure that my design would tell users that this site is for functional use, but also that this is a tool to hopefully serve for a good outcome. 
- I was also adamant that I didn't want the site to be inundated with 'news' or 'information' forced upon the user. As we all know, the pandemic is a very emotional topic and causes unease for much of the population. 

I based my simplistic functional aspect of the app on the module-[mini-project-task-application]() expertly delivered by [code Institute](). Everything in this project is entirely fictionally and all content was created by me. 



## Design
### Wireframes
Wireframes were created with [balsamiq](https://balsamiq.com/) 

You can find the wireframes [here]()

### Brand Identity
- Vision: Aesthetically pleasing, none pretentious site, empowering people who are in search of Kaur Health's services or curious about them.  
- Mission: Provide clients with support on intuitive eating, menstruation, skincare and natural family planning, not jus in the UK, but worldwide. Use the site as a mechanism to bring conversations on these topics to the forefront of society and eventually use the site to host virtual consultations, webinars etc. Doing everything possoible, to minimise the distance between the user/ client and saccess to this valuable information. 
- Values: 1. Female Health - Improving a womans understanding of her bodyily functions and how they relate to her fertility, menstrual cycle, physical appearance and ultimately mental health. 2. 

### Color Scheme
Color scheme is important as this is one of the first things site visitors notice when visiting the site. I chose persian indigo and avacado for the site's primary colors because these colors are bold and strong, not typically 'female' but statistically, very inticing for women . In addition to that, for the secondary colors of the site, I wanted to create a balance of bold to calm, whilst providing continuity in the colours too . For the secondary colour i chose medium slate blue. I used [Coolors.co](https://coolors.co/) to create a color pallet, which you can find below.

[This article](https://neilpatel.com/blog/psychology-of-color-and-conversions/) explained the importance of recognising the effect of colurs on your audiences mood. the article explains that "35% of women said blue was their favorite color, followed by purple (23%) and green (14%). 33% of women confessed that orange was their least favorite color, followed by brown (33%) and gray (17%)." as the content of this site will appeal mainly to women, i decided i needed colours that would be most inviting to them. 

[This pallet] ()
totally enages and appeals to women, whilst not being sterotypically 'girly and therefore offputtting to men! 

### Typography
To reflect the kaur Helath's brand identity, the typeface chosen for main headings was Mulish, (formerly known as Muli) and I coupled this with Nunito for the body text, both of these fonts fall under the sans serif family. I chose this duo, after doing some research and realising that I needed the font to reflect; strength; empowerment; practicality and most importantly readability. Due to the nature of the sites content, being quite woman centric, i was tempted to select a playful font, such as Oleo script, however i decided this woud take away from the profesional feel i was aiming to achieve. [This article]("https://piktochart.com/blog/fonts-and-colors/#:~:text=For%20subheadings%20and%20body%20text,partially%20for%20titles%20or%20headlines") by Natasya Sunarto was very insightful, as it compared a range of industries and i was able to work out where Kaur Health fits within the examples and make an informed decision about which typeface would be most fitting. 

- Icon: [kaur Health]() is used for the main icon library accross the site.
- Favicon: I got the favicon by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/).

### Brand Logo
Logo design is the cornerstone in your brand identity and presents a company's name, product and brand. I consulted with Juspreet to capture a balance of vision mission and culture, used []( to create the brand logo file. The font represents the brand value `x` and the image of x was added to represent `x` brand value.


<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
This website is composed of 6 applications: `home`, `blog`, `cart`, `checkout`, `products`, `services`, `profiles`.

## Landing Page
Landing Page is designed as a single page website to provide site visitors with all the information they need, in one place! This pages content consists of; an explanation of who juspreet is and the brand kaur health, Juspreets areas of expertise, testimonies about each of these areas and a call to action to drop her a line on the contact form. This is to let the site visitors take next actions. The page has a `Navbar` and consists of the following sections; `About`, `info on specialisms` and `testimonies`. 

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `Site Menu`, `My Account dropdown` and `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `description` field of Product Model, `name` and `description` field of Service Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "or" condition not when searching the keywords, meaning, if the search query was "blood", the function will sesrch the names and descriptions of the products and services and return results where the search term was found in either the name or description. 
<br>
![search term 'blood'](readme_materials/logic_screenshots/search-logic(1).png)
<br>
!['blood' in description](readme_materials/logic_screenshots/search-logic(2).png)
<br>
I chose this logic because, the nature of the tooics on this site, mean that there is likley to be some overlap in name and description of products and services and category that a particular item falls into. 


- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: The number next to the cart icon shows the total of items added to the cart.


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "" width=900></div>

Navbar for authenticated users
<div align="center"><img src = "" width=900></div>




### About me
`About me` section explains who Juspreet is to the site visitor.

### info on specialisms
`info on specialisms` section showcases Juspreets areas of expertise, i provide 3 cards each with a picture and body, comprising of a title and expalanation. 
This is to give the site visitor an insight into the nature and scope of Juspreets work. i was tempted to make the text show up on hover, however, i was aware that on smaller dervices this can be difficult to function and also, lilkely to cause bugs and dely which is bad ux. i deceided to simply have cards with and images and body. i have learnt through this experience that its important to remember, KISS!!

### Testimonial
`Testimonies ` section has a carousel of 3 testimonies, one from each area of exepertise. Testimonials can contribute to building the trust of potential customers and also explain the benefits of your products or services.

### Footer
The footer section is just links to Social Media with their icons. In this milestone project, Social Media icons are linked to Juspreets personal social media accounts, as her brand is consistent on her social media.

<div><a href="#table-of-contents">Back to top</a></div>

## Product and services Page
### Online Shop Page
By clicking 'products and services' on the site menu, you are given a dropdown to the different categories of profucts and services and an option for all products and services. I thought that the dropdown would provide better user experience than a direct link, which takes you to a page where you then have to sift through the categores that you are interested in. The nature of this site, is such that, as a user you are prpbably well aware of what you are looking and therefore which category to find it. Or, if you are new to the sites content, i felt it would be less overwhelming if you have some filtering control and could navigate to the category you were most interested in. 
By doing this I satisfy the ease of navihation in my user stories and adhere to my wireframes. Initially I had planned to have a sorting tab and functionlaity on the left side of the page, where the user could filter to the category they were interested in, however this way is more effeicient. 

- when a user chooses a catrgory from the dropdown, when clicked, they arrive on a page with product at the top and services beneath. there is also and products and service count, which shows jsers how many of each there are in this category. 

- Product Card: The products are displayed in cards that have `Product/ Service Name`, `Price`, `rating`. When the product image is pressed, the user will be taken to the respective detail page and have the option to continue shopping, or add this item, with a chosen quantity to their bag. If the user is logged in as a superuser, Update / Delete option is also shown on each card.

Product Card for products
<div align="center"><img src = "" width=500></div>

Product Card for services
<div align="center"><img src = "" width=250></div>

- Pagination Bar: unnecessary here..




### Product Detail Page

<div align="center"><img src = "" width=700></div>


## Cart Page

<div align="center"><img src = "" width=700></div>

## Checkout Page
### Checkout Page


### Checkout Success Page


<div><a href="#table-of-contents">Back to top</a></div>

## Blog Page
### Blog Feed Page


### Blog Post Detail Page


<div align="center"><img src = ""></div>

### Add/Edit Blog
- 

## Profiles Page

### My Profile Page


## Admin Product Managment

## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

## Features Left to Implement



## Defensive Design
### Error views (404 and 500 error)


### Form Validation
- Django Form Validation

### Product Quantity Counter Validation


<div><a href="#table-of-contents">Back to top</a></div>

# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

## Data Modeling
Following is Entity Relationship Diagram of this project. I created this diagram with [dbdiagram.io](https://dbdiagram.io/home).
When I designed this ERD, I referred to [this article](https://launchschool.com/books/sql/read/table_relationships). 
<p align="center"><img src = "https://github.com/AsunaMasuda/FloweryDays/blob/master/readme_materials/Entity_Relationship_Diagrams.png?raw=true" width=900></p>

# Bugs discovered

Service details not showing up 
Solution: Correct the URLs for the app
- I have three models categories, services and products. Products and services, rely on the categories model. 
- When i built the template for the product and service details, the product detail worked fine, but the service details would not. 
- if i clicked on a service, i would be taken to the details of a product with the same pk as the service i had clicked on. 
- I thought it was an issue with the primary keys, but i couldnt work out what the issue was, because the primary keys were from different models. 
- In an attempt to rule this out, I displayed the ids (primary keys) of each service using 
``` {{ service.id }} ```
- Then i changed the pk of one of my services to a number that was entirely different to any of the pk values of the products or services. 
- when i clicked on this service, i got an error.
![bug1](readme-materials/bug_screenshots/bug_1.png)
- This told me, the service details were reliant on the product id's. The new pk of the service i had tried to access, was out of range of the current product ids.
- this led me to check the link path of the items when they were clicked. this revealed all items were following the ``` all_items/<pk_value> ``` path. 
- this in turn led me to change my products and services app urls from 
``` path('<int:product_id>/', ```
```        views.product_detail, name='product_detail'), ```
``` path('<int:service_id>/', ```
```        views.service_detail, name='service_detail'), ```
 to 
``` path('product_detail/<int:product_id>/', ```
```        views.product_detail, name='product_detail'), ```
``` path('service_detail/<int:service_id>/', ```
```        views.service_detail, name='service_detail'), ```
- this solved the issue


Multiple items added to the bag each time a product/ service was added.  
Solution: add if statement in the contexts.py file

![Multiple items added to bag](readme_materials/bug_screenshots/bug_2(a)
![Multiple items added to bag](readme_materials/bug_screenshots/bug_2(b)

- I have 2 models that I needed to pull data from
this means I need to specify with actions, if I am pulling data from the service_id or the product_id.
- My Products and Services had identical pk's, i didnt think this was an issue because they were still two different models, however, with this issue arising, i decided to change the services' pks.

- First, I changed the pks of my services. To do this I, mistakenly used the `loaddata` command. This indeed added the services with new pks, however didnt UPDATE, I was left with two sets of services.. To resolve this I had to manually delete ALL of my services, via the admin on my site and then `loaddata` again. 
I researched and found out that in order to update models, you need to update the migrations used. I will do this if the issue arise again in the future, as it saves time. 
- Changing the pk's led to me continually getting this error 
![no service matches your query](readme_materials/bug_screenshots/bug_2(c))
<br>
when i tried to add a product or service. If i added a product, the error would say 'no service matches your query' and if i added a service, the error would say 'no product matches your query'.

- I believed my issue was in my views and urls and started to seperate the logic. 
```
 def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f' Updated {product.name}'
                         f'quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {product.name}'
                         ' added to your bag! ')

    request.session['bag'] = bag
   print("here")  
 return redirect("view_bag") 
 ```
 ```
 urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_product/<item_id>/',
         views.add_product_to_bag,
         name='add_product_to_bag'),
```
- I was still getting the error, so came to the conclusion that I needed to define the item specifically to check if its a service or product. To do this I added a parameter of `product.id` in the add product to bag view, however i would get this error;
![type error](readme_materials/bug_screenshots/bug_2(d))

- Eventually after I had made all of the changes I could think of, to my views and urls, i took a look at the `contexts.py` file. <strong> In hindsight, I should have loooked st this file earlier on in the process, as it was the only other file in the bag app, which handled functions specfic to the bag. </strong>  
- In the `contexts.py` file;
I changed the `bag contents` method from 
```
def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)(pk=item_id)
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * product.price
        total += quantity * service.price
        service_count += quantity
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'service': service,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'service_count': service_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context

```
to: 
```
def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = Product.objects.filter(pk=item_id).first()
        if product:
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            service = get_object_or_404(Service, pk=item_id)
            total += quantity * service.price
            service_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'service': service,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'service_count': service_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context

```
- In the original method, essentially, I had stated that in order to add an item to the bag contents, there needed to be both products and services. This is why originally, two items would simultaneously be added to the bag and thereafter i got the query error. 
- the change to the contexts.py solved the issue. 




### Product App



### Order App

### Blog App

### Profile App

<div><a href="#table-of-contents">Back to top</a></div>

# Technologies Used
The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [JQuery-UI](https://jqueryui.com/)
- [Popper.js](https://popper.js.org/)
- [Font Awesome](https://fontawesome.com/)
- [Animate.css](https://animate.style/)
- [Wow.js](https://www.delac.io/wow/)
- [Stripe](https://stripe.com/ie)
- [Google Fonts](https://fonts.google.com/)

## Tools
- Git/GitHub
- Gitpod
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
- [dbdiagram.io](https://dbdiagram.io/home)
- [AWS S3 bucket](https://aws.amazon.com/)

## Databases
- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.

# Testing
Testing was conducted and recorded in a different file: [Testing.md]().

<div><a href="#table-of-contents">Back to top</a></div>

# Deployment
## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

* I used []()to generate Django Secret Key.

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
10. Load the data fixtures(color_table, flower_table, image_table, product_table) into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
13. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
14. Add `'flowerydays.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
15. In Stripe, add Heroku app URL a new webhook endpoint.
16. Update the settings.py with the new Stripe environment variables and email settings.
17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.

### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'flowerydays'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/AsunaMasuda/FloweryDays/blob/master/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

1. In the IDE you are using, copy and paste the following commane into the terminal to clone this repository.
    `git clone `
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Load the data fixtures(color_table, flower_table, image_table, product_table) into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`

<div><a href="#table-of-contents">Back to top</a></div>

# Credits

### Content & Code
-
- I was inspired by the flow and structure of flowery days project by []() and used her read me as a template. 
- This project was developed refering to the Boutique Ado Django mini-project from Code Institute course materials. The codes are customized and modified to fit the purpose of this milestone project.

### Images & Media
- https://www.healthline.com/health/magnesium-oil-benefits
- medlife.com/blog/5-natural-ways-relieve-menstrual-cramps/#:~:text=2.-,Fennel,honey%20and%20mix%20it%20well.
- template tags : https://engineertodeveloper.com/a-better-way-to-route-back-to-a-section-ids-in-django/
- <span>Photo by <a href="https://unsplash.com/@sharonmccutcheon?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Sharon McCutcheon</a> on <a href="https://unsplash.com/s/photos/periods?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- https://unsplash.com/photos/eCJiD00AJqs
- https://unsplash.com/photos/2oegF67ikOM
- <span>Photo by <a href="https://unsplash.com/@prophsee?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Prophsee Journals</a> on <a href="https://unsplash.com/s/photos/food-diary?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- <span>Photo by <a href="https://unsplash.com/@socialcut?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">S O C I A L . C U T</a> on <a href="https://unsplash.com/s/photos/food-diary?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- <span>Photo by <a href="https://unsplash.com/@edgardo1987?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Edgar Soto</a> on <a href="https://unsplash.com/s/photos/thermometer?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- <span>Photo by <a href="https://unsplash.com/@anshu18?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Anshu A</a> on <a href="https://unsplash.com/s/photos/oil?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- <span>Photo by <a href="https://unsplash.com/@rhsupplies?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Reproductive Health Supplies Coalition</a> on <a href="https://unsplash.com/s/photos/fertility?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
- dame website 
- 

### Acknowledgements
- Thanks to: my Code Institute Mentor  advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.

### Disclaimer
This website is created for educational purpose only. content entirely fictional. 