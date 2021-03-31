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
        - [Contact Page](#contact-page)
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

9.[Reflection](#reflection)


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
In order for me to be bale to successfully meet both the user and business goals of this project, it was vital that i usnderstoof the wokr and mission of Juspreet Mahoon. 
I was lucky to be presented with her work and findings and used her many social media posts and videos on youtube, to get a feel of the kind of oerson she was and the message she wanted to share with the world. 

After learning about her, I then underwent some learning on the topics she is passionate about and would like to share across the site. 
I am passionate about many of the same subjects; female health is of utmost concern to me, being a woman and female only pre and post natal specialising, personal trainer. I have a unique insght into the anatomical journey women experience. 
I was able to bring this knowledge to the site. 

I used feedback from my clients on colour choices and read blogs about which colours and fonts would be most appealing to women. 


I knew that I wanted to create an app that would:
- Engage all women, not just women with a predetermined interest in the subjects discussed. 
- Provide a community feel, whereby users could gain information and feel acknowledged. 
- Encourage users to create a profile, so that they could gain the benefit of start discussions on the blog and also have their order information prefilled. 
- Ensure that my design would tell users that this site is a safe space for women, but also that this is an educational tool to hopefully enlighten women with similar interests, or those who have no idea. 

I based the checkout profiles and store functionality of the app on the module-[mini-project-boutique-ado]() expertly delivered by [code Institute](). Everything in this project is entirely fictionally and all content was created by me. 



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
This website is composed of 6 applications: `home`, `blog`, `checkout`, `products_and_services`, `bag`, `profiles`. There is a static navbar and footer throughout the site. 

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `Site Menu`, `My Account dropdown` and `Cart icon`.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `description` field of Product Model, `name` and `description` field of Service Model.(Details of these models will be described at the [Information Architecture](#information-architecture)) This function uses "or" condition not when searching the keywords, meaning, if the search query was "blood", the function will sesrch the names and descriptions of the products and services and return results where the search term was found in either the name or description. 
<br>
![search term 'blood'](readme_materials/logic_screenshots/search-logic(1).png)
<br>
!['blood' in description](readme_materials/logic_screenshots/search-logic(2).png)
<br>
I chose this logic because, the nature of the topics on this site, mean that there is likley to be some overlap in name and description of products and services and category that a particular item falls into. 


- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Cart icon: The number next to the cart icon shows the total of items added to the cart.


Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "" width=900></div>

Navbar for authenticated users
<div align="center"><img src = "" width=900></div>

### Footer
The footer section is just links to Social Media with their icons. In this milestone project, Social Media icons are linked to Juspreets personal social media accounts, as her brand is consistent on her social media.

<div><a href="#table-of-contents">Back to top</a></div>


## Landing Page
Landing Page is designed as a single page website to provide site visitors with all the information they need, in one place! The page has a `Navbar` and consists of the following sections; `About`, `info on specialisms` and `testimonies`. 

### About me
`About me` section explains who Juspreet is and the brand kaur health to the site visitor.

### info on specialisms
`info on specialisms` section showcases Juspreets areas of expertise.
I provide 3 cards each with a picture and body, comprising of a title and expalanation. 
This is to give the site visitor an insight into the nature and scope of Juspreets work. I was tempted to make the text show up on hover, however, I was aware that on smaller dervices this can be difficult to function and also, likely to cause bugs and delay which is bad ux. I deceided to simply have cards with and images and body. I have learnt through this experience that its important to remember, KISS!!

### Testimonial
`Testimonies ` section has a carousel of 3 testimonies, one from each area of exepertise. Testimonials can contribute to building the trust of potential customers and also explain the benefits of your products or services. Users can click forward and backward on the testimonies. 


## Product and services App

### Products and services 

When a user clicks on ` Product and services ` dropdown nav bar option, you are given a dropdown to the different categories of the products and services. I thought that the dropdown would provide better user experience than a direct link, which takes you to a page where you then have to sift through the categores that you are interested in. The nature of this site, is such that, as a user you are prpbably well aware of what you are looking and therefore which category to find it. Or, if you are new to the sites content, i felt it would be less overwhelming if you have some filtering control and could navigate to the category you were most interested in. 
By doing this I satisfy the ease of navihation in my user stories and adhere to my wireframes. 
![ The dropdown distinguishes the products and services by category ](readme_materials/logic_screenshots/navbar_dropdown(products).png)

After clicking on your chosen category, all of the products and services under this category, will be displayed. The category name will appear just beneath the consistent title of 'products and services' and there is a banner just above the title, with the free delivery minimum spend. 
# picture? 
In the top left corner the user will see a link to `Products and services home` which when clicked will take them to the `all products and services page `, here all of the categories will be clickable links beneath the title, so that a user can navigate to the other categories from here as well/ instead of the navbar dropdown.
Beside the `Products and services home` there is a product and service count, outlining how many products and how many services belong to this category. 
Originally I toyed with the idea of having the product and service count clickable links and sectioning the page so that the user would be taken to a products section if they clicked the product count link to 'products' and the same for services. However, this proved to be bad UI, as when and if the user chose to sort the products, the sections would make things very messy and hard to contain. 

I opted to distinguish services from products in a few ways;
1) Adding a consistent banner in each of the services' descriptions # picture
2) When a service is added to the users bag, the success message will clearly state that the user has just added a service and should read the terms and conditions carefully. 
3) On the order receipt, I have again stated, which of the items are services and that the user should therefore read the terms and conditions. 

# picture? 
After clicking any of the products and services dropdown options, the user can use the sorting function on the top right of the page to sort through the products on the page, however they desire. Initially I had planned to include category sorting in this tab, however, since the dropdown options are filtered by category, this was already satisfied.
# picture?

The products are displayed in cards that have `Product/ Service Name`, `Image`, `Category` `Price`, `rating`. As mentioned above, the product card format, ever so slightly differs if the product is a service. 
Product Card for products
<div align="center"><img src = "" width=500></div>

- Pagination Bar: Unnecessary for this site currently, however I would add this as kaur health grew as a brand and had more products on offer. 

### Product detail
When the product image is pressed, the user will be taken to the respective detail page and have the option to continue shopping, or add this item, with a chosen quantity to their bag. 
# picture?
As mentioned above, if the product is a service, it has a small banner in the decsription explaining that this is a service and therefore there are different terms and conditions. In the future i would potentially add a modal pop up box here so that users wuld have to scroll to the bottom of the terms and condiotons before adding to the service to their bag. Howver, for the sake of time, i decided against this, as i ran into enough compications with basic functionality! 

## Admin Product Managment
If the user is logged in as a superuser, Update / Delete option is also shown on each card.
#picture

### Adding product to bag (this functionality takes the user from the products and services app to the bag app)
When a user adds an item to the bag a success message appears in the top right corner. 
success_message(add_product_to_bag).png
the message gives a product and service count of the items in the bag, a small picture of the items and their quantity, it also has a slightly different message if a service is added. 
success_message(add_service_to_bag).png
By using these messages i am satisfying x in my user story. 

## Bag App

This page is simple, it outlines the products'; picture, name, price, quantity and the subtotal. I liked the idea of the items being clear and readable. This also satisfied 
| Site User | Easily select the quantity (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
this user story, by being clear and readable, there was less risk of the above occuring. 

When in the bag, the user can <strong>update the quantity of their products</strong>, <strong>remove a product entirely</strong> and choose to either <strong>continue shopping</strong> or <strong>checkout</strong>. 
#picture 
There are success/ alert messages to update user of each eventuality. Again this is satisfying x in my user stories. 
If the user chooses to checkout, they will be using the backend logic and functionality, created in the checkout app. However, if they choose to continue shopping, they will be taken back to all the products and services and can navigate via category to the category of items, in which they are interested in. 

## Checkout App

When clicking the 'checkout option' the user is taken to a page displaying an empty order form on the left, needing to be completed and a summary of their order on the right. This is more feedback to the user and an opportunity for them to make any adjustments to their shopping bag. 
If the user is logged in, beneath the form, there will be a checked option to save the info to their profile. 
this page satisfys 
| Site User | Have my delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Site User | Be reminded to log in if I did not log in | Smoothly proceed with my purchase and prefilled form |
#picture 
If they keep the box ticked, the delivery information will appear prefilled on their profile page. 
#picture 
When a order has gone through successfully, the user will be redirected to the checkout success page. Here they will have a summary of their order (which calls on the order line item models logic) a message to confirm that their order has gone through and an option to keep shopping. Their bag will now appear empty too. 

## profile app 

The profile app is just the users delivery information on the left and a history of their orders on the right. 
Users can update their details on their profile, this means the details will be updated for when the user carries out their next order. 
#picture 
The profile app can be accessed through the account option on the navbar. 
#picture 

## Blog app 

The blogs are available for any site visitor to browse, however only logged in users can write a blog.
#picture 
If you are logged in, you will have the option to view just your blog posts. If you are logged in, you will see a links to edit and delete your blog posts if you are looking at them on the all blogs page/ your blogs page and on the blog detail page.
#picture
You will be able to perform these functions if you are logged in.
#picture
If you are not logged in, you can view all the blog posts and then click on them and be taken to the blog detail page. 

### comment on  Blog

- comments of a post can be viewed if the user clicks on the blog post and is taken to the blog detail page. Here the user can also add a comment, however, if they are not authenticated, they cannot add a comment. 

- Initially i made a seperate view for the commenting functionality, however i deceided it would be better UX if the comment function could occur on the page of the blog post and not take users to a se[erate page. For this reason, i chose to use a modal, which would pop up when a user wrote a comment and when submitted, would simply reload the page, now displaying the users comment. 
- In the future, if developing this site further, i would look into using AJAX requests, to give the user the ability to edit and delete their comments. 
You will see the comments that other users have left on the blog you are looking at, you will also find a link to leave a comment, however, if you are not logged in, you will not be able to make a comment and will be notified with a message. 
#picture
I thought it was better UX for the edit and delete buttons to only be visible to a user if they are logged in, as it would otherwsise be misleading. However, I decided to have the 'make a comment' links visible to all site visitors, because when the none authenticated user attempts to make a comment, they may be more inclined to create a profile, for the prupose of being able to complete this action. This would in turn, build on the community and discussion aspect of the site - satisfying x in the user stories.
If you are logged in and want to comment on a blog post, you can do so after clicking on the link and completing the comment form, in the modal.
#picture
I thought the use of a modal, for comment functionality was good UX, the nature of a comment is that it is fast and on topic, i worried that if the commenting functionality, meant that users needede to leave the page they were currently visiting, so that they could leave their on topic comment, it would ruin the flow of a users experience. 
#picture

## contact

I thought it was necessary for a site like this to have a contact form, Kaur health is multi faceted and relies on the openess of site visitors. I felt that if i didnt include a contavt form, I would lose the opportunity to create a rapport between Kaur health and the user. I feel it helps to satisfy x in the user stories. 
The contact form is very simple and lives in the home app. 
When a user sends a message via the form, they will be taken to a reponse page, see a success message and recieve a copy of the message they sent! I felt this was a personal and 'extra-mile' feature, again leading to users feeeling acknowledged, which in turn helps build community and rapportt, satisfying x
#picture. 
To protect the site owner, I used a honeypot field, designed to catch and prohibit spam mail from bots. A honeypot field is a field that is hidden on your contavt form, that a bot will not be anble to distinguish. When they try to fill it out, they will reach the error page and their spam mail will not be sent! I could also use the honeypot admin functionality, which offers increased security and definsive programming. Anyone with minor developer exeprience will know that you just need to change a sites url and add admin to the end of the url to accesss the admin page. From there it would be easy to hack your way into the sites admin and cause some damage! To protect against this, honeypot admin, allows site owners to create a new admin area, whilst also providing a 'fake' admin area for bots/ hackers to attempt to login to! You will also be notified, how many login attempts there have been, so that you can guage whether this feature is fitting for your site or if you need to take extra measures to protect yourself.
#picture
I will definitely be using honeypot fields and honeypot admin functionality in the future, however for this project i felt that the honeypot field alone, would suffice. 
- As i will only ever be sending a total of two emails from this view, it is not necessary, howevre if i was to develop this aspect more and send more than two emails from this view, i would opt to use the send mass mail wrapper from the django.core.mail module.
- for the backend wiring up, i dcided to use aws email, as opposoised to gmail. I thought it made more sense as we are using aws to collect the static files etc. 



## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

## Features Left to Implement
- When a user tries to add blog post, currently due to the slug, I have put some defensive programming so that if a user tries to add a post, with an exisiting blog posts name, they will get an errro message. 
However ideally, if developing this site further, i would like to add 'title comparison/ checks' to the form validatioon, or use AJAX to esssntially check the title as the user types it and pause them there, if the title is preexitisng. 
- Honeypot admin
- AJAX requests for the user to update and make blog posts in the page as opposed to in seperate pages. 

## Defensive Design
### Error views (404 and 500 error)


### Form Validation
- Django Form Validation


# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

## Data Models

#### User
The user model utilised for this project is the standard model, provided by from django.contrib.auth.models 

#### Products app models
Within the products app, the <strong>Product</strong> model holds all the data necessary for the functionality of the store. The <strong>Category</strong> model, provides the categories for which the products depend on. 

##### Category Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Category | name| max_length=254, null=True, blank=True| CharField
Category | friendly_name  | max_length=254, null=True, blank=True| CharField


##### Product Model


| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Category | friendly_name | null=True,blank=True, on_delete=models.SET_NULL | ForeignKey 
Service | service_category | default=False, null=False, blank=True | BooleanField     
Product | name | max_length=254 | CharField
Description | description | none | TextField
Price | price | max_digits=6, decimal_places=2 | DecimalField 
Rating | rating | max_digits=6, decimal_places=2, null=True, blank=True | DecimalField
Product image | product_image | null=False, blank=True | ImageField

#### Checkout app models
Within the checkout app, the <strong>Order</strong> model holds all the data of the users' order. The <strong>OrderLineItem</strong> model, mainly extracts data from the order model, to get the order number, but also returns the user on the front end the information about each individual product. 

##### Order Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Order number | order_number| max_length=32, null=False, editable=False| CharField
User | user_profile  | on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'| ForeignKey
Full name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone number | phone_number | max_length=20, null=False, blank=False | CharField
Country | country | blank_label='Country *', null=False, blank=False | CountryField
Postcode | postcode | max_length=20, null=True, blank=True| CharField
Town or city | town_or_city | max_length=40, null=True, blank=True | CharField
Street address1 | street_address1 | max_length=80, null=True, blank=True | CharField
Street address2 | street_address2 | max_length=80, null=True, blank=True | CharField
County | county | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Delivery cost | delivery_cost | max_digits=6,decimal_places=2, null=False, default=0 | DecimalField
Order total | order_total | max_digits=10,decimal_places=2, null=False, default=0 | DecimalField
Grand total | grand_total | max_digits=10,decimal_places=2, null=False, default=0 | DecimalField
Original bag | original_bag | null=False, blank=False, default='' | TextField
Stripe pid | stripe_pid | max_length=254, blank=False, default='' | CharField

##### OrderLineItem Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Order | order | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey
Product | product | null=False, blank=False, on_delete=models.CASCADE | ForeignKey
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

#### Blog app models
Within the Blog app, the <strong>BlogPost</strong> model provides the structure for the blog posts. The <strong>Comment</strong> model, provides the structure necessary for users to comment on blog posts. 

##### BlogPost Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Title | title | max_length=254 | CharField
Date | date | auto_now_add=True, null=True, blank=True | DateTimeField
Slug | slug | max_length=254, null=False, unique=True | SlugField
Author | author | on_delete=models.CASCADE | ForeignKey
Category | category | null=True,blank=True, on_delete=models.SET_NULL | ForeignKey 
Body | body | none | TextField
Image | blog_image | null=False, blank=True| ImageField

##### Comment Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Comment | post_comment related_name="comments", on_delete=models.CASCADE | ForeignKey
Body | body | none | TextField
Name | name | max_length=254 | CharField
Date | date | auto_now_add=True, null=True, blank=True | DateTimeField


#### Profile app model
Within the profile app, the <strong>UserProfile</strong> model holds all the data necessary for the user to have a prefilled order form, if they create a profile. This saves them time and energy, when checking out. 
##### UserProfile Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
User | user | on_delete=models.CASCADE | OneToOneField
Full name | full_name | max_length=50, null=False, blank=False | CharField
Phone number | default_phone_number | max_length=20, null=False, blank=False | CharField
Country | default_country | blank_label='Country *', null=False, blank=False | CountryField
Postcode | default_postcode | max_length=20, null=True, blank=True| CharField
Town or city | default_town_or_city | max_length=40, null=True, blank=True | CharField
Street address1 | default_street_address1 | max_length=80, null=True, blank=True | CharField
Street address2 | default_street_address2 | max_length=80, null=True, blank=True | CharField
County | default_county | max_length=80, null=True, blank=True | CharField

# Bugs discovered

## Bug 1 - Service details not showing up 
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


## Bug 2 - Multiple items added to the bag each time a product/ service was added.  
Solution: add if statement in the contexts.py file

![Multiple items added to bag](readme-materials/bug_screenshots/bug_2(a)
![Multiple items added to bag](readme-materials/bug_screenshots/bug_2(b)

- I have 2 models that I needed to pull data from
this means I need to specify with actions, if I am pulling data from the service_id or the product_id.
- My Products and Services had identical pk's, i didnt think this was an issue because they were still two different models, however, with this issue arising, i decided to change the services' pks.

- First, I changed the pks of my services. To do this I, mistakenly used the `loaddata` command. This indeed added the services with new pks, however didnt UPDATE, I was left with two sets of services.. To resolve this I had to manually delete ALL of my services, via the admin on my site and then `loaddata` again. 
I researched and found out that in order to update models, you need to update the migrations used. I will do this if the issue arise again in the future, as it saves time. 
- Changing the pk's led to me continually getting this error 
![no service matches your query](readme-materials/bug_screenshots/bug_2(c).png)
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
![type error](readme-materials/bug_screenshots/bug_2(d).png)

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

## Bug 3 Unable to correctly format the bag_contents
Solution: created empty arrays for both products and services, within bag_items and appended products to the bag_items, to help decipher which item was coming from where. Then iterrate through the new array in the template. 

- After solving the above issues, i realised that with every item added, an extra empty row was added, because the server was being told to look for a product AND service everytime, by the contexts.py file. 
![Rendering empty respective products and services](readme-materials/bug_screenshots/bug_3(a).png)
- I didnt understand the lack of the seperation of the models and their end points as much as i do now, i thought that because i had seperated the products and services actions eg 
``` add_product_to_bag and add_service_to_bag ```
that this was sufficient.
- So i thought i could sperate the products and views from the template. 
![template logic, trying to seperate the bag contents](readme-materials/bug_screenshots/bug_3(b).png)
- However, this still gave the same errors that i had previously seen
![item confusion](readme-materials/bug_screenshots/bug_3(c).png)
and led to only the products or services displaying at any one time, not together and seamlesly. 
Here you can see from the total that there are other items in the bag (services) however only the products show, until you remove the products, then the services are displayed. 
- I realised i needed to go bag into the view_bag view and contexts.py file, both of which currently had little to no differentiation between items being products or services. 
![initial view_bag view](readme-materials/bug_screenshots/bug_3(f).png)
I changed the view_bag view to 
``` 
def view_bag(request):
    bag_items = {
        'products': [],
        'services': [],
        }

    return render(request, 'bag/bag.html', bag_items)
    print(request.session.get('bag', {})) 
```
similarly the bag_contents in the contexts.py file was 
```
def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    service_count = 0
    bag = request.session.get('bag', {})
    print("hello im working2")
    for item_id, quantity in bag.items():
        product = Product.objects.filter(pk=item_id).first()
        if product:
            total += quantity * product.price
            product_count += quantity
            print("hello im working3")
            bag_items({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
            print("hello im working1")
        else:
            service = get_object_or_404(Service, pk=item_id)
            total += quantity * service.price
            service_count += quantity
            bag_items({
                'item_id': item_id,
                'quantity': quantity,
                'service': service,
            })
        print("hello im working")
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
    print(request.session.get('bag', {}))
    return context

```
Which i changed to 
```
from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products_and_services.models import Product, Service


def bag_contents(request):
    bag_items = {
        'products': [],
        'services': [],
        }
    total = 0
    product_count = 0
    service_count = 0
    bag = request.session.get('bag', {})
    print("hello im working2")
    for item_id, quantity in bag.items():
        product = Product.objects.filter(pk=item_id).first()
        if product:
            total += quantity * product.price
            product_count += quantity
            print("hello im working3")
            bag_items['products'].append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
            print("hello im working1")
        else:
            service = get_object_or_404(Service, pk=item_id)
            total += quantity * service.price
            service_count += quantity
            bag_items['services'].append({
                'item_id': item_id,
                'quantity': quantity,
                'service': service,
            })
        print("hello im working")
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
    print(request.session.get('bag', {}))
    return context

```
By adding products and services as empty arrays, i could append them to the bag_items, depending on their condition and iterrate through them in the template.

- I changed the template logic to 
```
                    {% for item in bag_items['products'] %}
                    <!--products in the bag -->

                    {% endfor %}
                    {% for item in bag_items['services'] %}

                    <!--services in the bag -->

                    {% endfor %}
```

and got this error
![template error](readme-materials/bug_screenshots/bug_3(g).png)

Django and python dont like [''], within for loops 

so i changed it to 
```
                    {% for item in bag_items.products %}
                    <!--products in the bag -->

                    {% endfor %}
                    {% for item in bag_items.services %}

                    <!--services in the bag -->

                    {% endfor %}
```

which worked and my server is no longer looking for a product AND service everytime an item is added.
![issue solved!](readme-materials/bug_screenshots/bug_3(h).png)


## Bug 4 Cannot render images in bag
Solution: change pathway from 
```
<td class="p-3 w-25">
                            {% if item.service.image %}
                            <img class="w-100" src="{{ item.service.image.url }}" alt="{{ item.service.name }}">
                            {% else %}
                            <img class="w-100" src="{{ MEDIA_URL }}noimage.png" alt="{{ item.service.name }}">
                            {% endif %}
                        </td>
```
![Images not being rendered in bag](readme-materials/bug_screenshots/bug_4(a).png)

To
```
<td class="p-3 w-25">
                            {% if item.service.product_image %}
                            <img class="w-100" src="{{ item.service.product_image.url }}" alt="{{ item.service.name }}">
                            {% else %}
                            <img class="w-100" src="{{ MEDIA_URL }}noimage.png" alt="{{ item.service.name }}">
                            {% endif %}
                        </td>
```
![Images being rendered in bag](readme-materials/bug_scr-enshots/bug_4(b).png)

I used dev tools to compare the pathway written in the image source, on all_items.html and bag.html and quickly realised that i needed to use the exact field name from my models. 


## Bug 5 card number input field not working
solution: Typed '66' which triggered the num lock and was then able to type valid and invalid card numbers. 

I discovered this issue after adding the intial stripe functionality. 

I used dev tools to try and debug the issue, i assumed it was a styling overlap error at first. 

I could see the input was very cluttered with styles and believed this had somehting to do with the bug. 
![Card number field not inputtable](readme-materials/bug_screenshots/bug_5(a).png)

I made my port public, removed the environment variables from a previous project (in case there was confusion in the application of public and secret keys ) and looked into the ad block settings in my browser (chrome).

I then tried to input a card number into the mini project deployed site and another completed MS4 site. Both of which were not working! 
![Card number field not inputtable on other sites](readme-materials/bug_screenshots/bug_5(b).png)
![Card number field not inputtable on other sites](readme-materials/bug_screenshots/bug_5(c).png)

I was then convinced that it must be an ad setting in chrome somewhere, however to disable all security against the pop ups, would not be wise..

Finally, it was suggested that I type '66' into the card number field. 
![66 inputted into the card number field ](readme-materials/bug_screenshots/bug_5(d).png)

Initially, I thought I may have some numbers on my keyboard not working, however after typing '66' I was able to type every number. 
I then came to the conclusion that I had been trying to enter the numbers in using the number keypad without Num Lock turned on. '66' triggered the num lock and 77, 88, would have been just as effective! 

## Bug 6 Unable to correctly render the checkout success page
solution: chnage entire structure, by having one model!
- I was building the checkout logic, trying to replicate the logic from my contexts.py file, however, my contexts.py file was very specific to my two models. I was stumbling with the order_line_items.

![ views for checkout app ](readme-materials/bug_screenshots/bug_6(a).png)
![ contexts.py for bag app ](readme-materials/bug_screenshots/bug_6(b).png)

- I thought i needed to create similar variable as bag_items for order_line_items. I started looking into this and realised just how complicated the logic was becoming..
![ error ](readme-materials/bug_screenshots/bug_6(c).png)

- I continued to try and define the quantity, continuing to try and keep the products and services seperated. 
![ error ](readme-materials/bug_screenshots/bug_6(d).png)
![ error ](readme-materials/bug_screenshots/bug_6(e).png)

- eventually, i was advised to chnage my model structure or discuss with my mentor at least. I was very disheartened by this at first, but it was a great learning curve for me. We are taught KISS from the first lessons on the course and, personally, I find myself straying and not abiding by DRY. 
![ tutor advice ](readme-materials/bug_screenshots/bug_6(f).png)

- in order to honour the importance of seperating the products and services, i added a boolean field to the product model
```
service_category = models.BooleanField(default=False, null=True,
                                           blank=True)
```
However i wasnt sure how to list this field in the order model, in the order_line_item class, in the checkout app. 
![ error ](readme-materials/bug_screenshots/bug_6(g).png)

- i tried and it worked! 

## Bug 7 - updating add to bag view, so that service count is functional and messages relay service specific information
solution: correct logic in the view

- I adapted and used the logic from the mini project and tried to correctly define each evenutality of services being added to bag, with if statements. 
```
def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    service = bool(request.POST.get('product_is_service'))
    bag = request.session.get('bag', {})

    if service:
        if item_id in list(bag.keys()):
            if item_id in bag["services"]:
                bag["services"][item_id] += quantity
                messages.success(request, f' Updated service {product.name}'
                                 f'quantity to {bag[item_id]}'
                                 '[item_is_service"][service]!')
            else:
                bag[item_id]['product_is_service'][service] = quantity
                messages.success(request, f'added {product.name}'
                                 'to your bag! Please read the'
                                 'rules regarding services!')
        else:
            bag["services"] = {item_id: quantity}
            messages.success(request, f'added {product.name}'
                             'to your bag! Please read the'
                             'rules regarding services!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f' Updated {product.name}'
                             f'quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f' {product.name} added to your bag!')

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)
```
![ add to bag view ](readme-materials/bug_screenshots/bug_7(a).png)
![ add to bag view ](readme-materials/bug_screenshots/bug_7(b).png)
![ add to bag view ](readme-materials/bug_screenshots/bug_7(c).png)
![ add to bag view ](readme-materials/bug_screenshots/bug_7(d).png)

- I struggled to understand how to add to the dictionary, with a sub disctionary. To better understand the logic i loaded pythin in my cli and practised 
![ adding to subdictionary ](readme-materials/bug_screenshots/bug_7(e).png)
I finally understtod that i needed to do 
dict[key] = value

- However, my code was still wrong and if block which handled eventualities of a service being added to the bag, was getting completely skipped and the only logic was coming from the else block. 
![ adding to subdictionary ](readme-materials/bug_screenshots/bug_7(f).png)
![ adding to subdictionary ](readme-materials/bug_screenshots/bug_7(g).png)

- I then went to my Product_detail.html template, where i passed in `product_is_service` 
After more debugging and adjusting, i learnt that the issue was not that `product_is_service` was not being recognised/ passed in, but was definitely within my code, in views. 

- FINALLY after trial and error, debugging and support from peers.. I was able to understand that I needed a sub dictionary WITH a sub array inside. My current subdictionary 
``` 
bag["services"] = {item_id: quantity}
``` 
was throwing errors becuase a) plural of service was not a wise choice for the name. b) it was not nested correctly.
The correct sub dictionary, also had an array within it

```
bag[item_id] = {'item_is_service': {product.name: quantity}}
```
- After making these adjustments, the correct messages were displaying. In order to solve the service count issue, I simply added the varibale service_count into the else block for my service logic in the contexts.py file. 


## Bug 7 - 'This is a service' message displaying on order summary 
solution: assessed the logic necessary for desired outcome, adjusted the html template. 
- I followed the logic from the mini project to help achieve functionality for my boolean field on the product model. 
```
    service_category = models.BooleanField(default=False, null=True,
                                           blank=True)
```
I thought it was necessary for me to also add the new subdictionary 
```
'item_is_service'
```
to the order line item model, so that it would come up on the order summary. 
- I was trying to work out which field would be best, because I thought it was no longer a boolean field, because the boolean had already served its purpose, it was different to the example, because my boolean, did not serve as an input elsewhere. 
- After taking heed of the errors i have already made by not adhering to KISS, i reviewed the situation and realised that i didnt need to do ANYTHING to the order line item class and instead, just needed to put an if statement in the checkout successs template. 

```
{% if item.product.service_category %}
                        {{ item.product.name }}
                        <p>PLease rememebr the t's and c's</p>
                        {% endif %}
```

## Bug 8 - name not prefilled at checkout
![ updating info on profile ](readme-materials/bug_screenshots/bug_8(a).png)
![ info carried through except name.. ](readme-materials/bug_screenshots/bug_8(b).png)
![ no value for name ](readme-materials/bug_screenshots/bug_8(c).png)
![ full name field added to profiles model ](readme-materials/bug_screenshots/bug_8(d).png)

after playing around with this issue some more, i came to the conclusion that, in order to automatically update the order form and subsequently, profile details, with the users full name, from their first transation; I would have had to collect that information when they signed up. 

The sign up form does not collect their full name, only username and email address. The email address was an easy fix, however full name was uncooperative. 

Therefore to resolve this, I would need to extend the user model (using a class called 'abstract based user' ) this will let you customise user model and add first name and last name as required field for sign up. 
Then, I could use that data for the profile and the form would be prefilled from the first transaction. 

## Bug 9 - filtering the users blog posts
- I wanted to add a dropdown for users who are logged in, to view their blog posts. 
- The first step to doing this was specifying in the main nav that the 'my blogs' link would pertain to author equaling the user. 
```
            <div class="dropdown-menu border-0" aria-labelledby="#">
                <a href="{% url 'blog' %}" class="dropdown-item">All blog posts</a>
                {% if request.user.is_authenticated %}
                    <a href="{% url 'blog' %}?author={{ request.user }}"  class="dropdown-item">My blog posts</a>
                {% endif %}
            </div>
```
- then i needed to do the back end work, which wasnt as simple because the blogs were displayed via a class as opposed to a method. 
- I had to use a method within the class
```
class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/all_blogs.html'

# This method was used to place the filter on the main nav link. 
    def get_queryset(self):
        author_val = self.request.GET.get('author', '')
        if author_val:
            author_object = User.objects.get(username=author_val)
# Here i am adding 'author' to a new context (returned if 'my blogs' in nav is selected) 
            new_context = BlogPost.objects.filter(
                author=author_object,
            )
        else:
            new_context = BlogPost.objects.all()
        return new_context
 ```
 - This worked, however, it was easy to change name of the user to potentially view all the blogs, written by other users. 
 ![ all blog posts displaying ](readme-materials/bug_screenshots/bug_9(a).png)
 ![ users blog posts displaying ](readme-materials/bug_screenshots/bug_9(b).png)
 ![ users blog posts displaying ](readme-materials/bug_screenshots/bug_9(c).png)
 ![ lack of defensive programming, allowing user to filter to another authors blogs ](readme-materials/bug_screenshots/bug_9(d).png)
 ![ lack of defensive programming, allowing user to filter to another authors blogs ](readme-materials/bug_screenshots/bug_9(e).png)

- I needed to add another method, beneath the query set, so that i could add the new object('author') onto the context 
```
# This method was used to get the above context. 
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['author'] = self.request.GET.get('author')
        return context
```
- I also needed to accompany this new logic, with some logic in the all blogs template. 
![ template logic ](readme-materials/bug_screenshots/bug_9(f).png)

- Now the user is unable to manually change the url, to attain another users' blogs. 
![ defensive programming- working ](readme-materials/bug_screenshots/bug_9(g).png)


## Bug 10 add blog url not working, since slug implementation 
I needed to change my blog detail page url from 
```
urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', views.add_blog_post, name='add_blog_post'),
```
to 
```
urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', views.add_blog_post, name='add_blog_post'),
```
The blog detail path, with just slug:slug, was throwing django off, because the value of slug is just words and no actual path. without detail / before the slug:slug, when a user would try to add a blog post, the url, was referrring to the above view/ url. i needed to distinguish them, so. i added the 'detail/'

## Bug 11 sending email attempt rejected due to the region. 
- After setting up amazon aws SES backend email functionality, I tested an email in the python shell. It did not work. 
- ![ message rejected ](readme-materials/bug_screenshots/bug_10(a).png)
- I had already verfied my email, so knew it wasnt that. 
- ![ email verified ](readme-materials/bug_screenshots/bug_10(b).png)
- After doing some research I found two other variables that were necessary in order for amazon to know the region I was in when sending the email. 
- ![ added variables ](readme-materials/bug_screenshots/bug_10(c).png)
- After changing these variables and restarting the testing process, i successfully recieved the message.
- ![ email sent ](readme-materials/bug_screenshots/bug_10(d).png)
- However, after reading the documentation around aws ses regions, i was aware that i needed to request to not be in a 'sandbox' that way i would be able to send emails to any email address (as opposed to solely the email address i had verified.)
- To resove this issue, all i needed to do, was follow the given steps. 
- ![ removal from sandbox](readme-materials/bug_screenshots/bug_10(e).png)

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
- https://pythoncircle.com/post/703/using-if-else-condition-in-django-template/
- https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi (blog)
- https://learndjango.com/tutorials/django-slug-tutorial (slug)
- https://github.com/jamesturk/django-honeypot (honeypot documentation)
- https://medium.com/hackernoon/the-easiest-way-to-send-emails-with-django-using-ses-from-aws-62f3d3d33efd (amazon ses)

### Acknowledgements
- Thanks to: my Code Institute Mentor  advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.

### Disclaimer
This website is created for educational purpose only. content entirely fictional. 


### Reflection
At the start of this project I had two models with items. Products and Services. Having two models like this, both of equal importance to the main functionality of your site is a tremendous amount of work. I was having to cater for both models and their functionality all the way until building the checkout. It was at this point that I had to make the executive decision to change the entire structure of my project, by consolidating all of the items into one model (products). this was a great lesson, it taught me the true value of KISS and moving forward, simplicity will be at the forefront of my mind when approaching all projects. For me personally, I have found it tough to distinguish between what it necessary and what is extra. Throughout all of my projects at code Institute I have struggled to confine and adequately execute my ideas. I feel that this project, really taught me how to scale my ideas and the consequences of allowing your imagaination and ego, rule your decsions. In hindsight, I should have just had products as my model and i could have then got further along in my project faster and avoided the wasted time and energy, PLUS i would have had more time to focus on the functionality required to still distinguish between items in the shopping bag, both coming from the same model! However, if i had not had this bump in the road, it is very likely that i would have repeated this unhelpfil patterns of believeing that unecessaery ideas,should all be taken into developement. 


