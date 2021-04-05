# Kaur health - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://kaur-health.herokuapp.com/

## Table of Contents

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
    - [Jasmine](#jasmine)
    - [Python Testing](#python-testing)
    - [Coverage](#coverage)
    - [Travis](#travis)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)
    -[Accessibility](#Accessibility)
    -[Usability](#Usability)

## Accessibility
* I used [wave](https://wave.webaim.org/) to achieve better accessibility on my site. 

### Symptoms

![First attempt with wave](/testing/accesibility/wave-test-1-(homepage).png)  
* I had a serious contrast issue, so I immediately resolved this on every page. 

![After resolving contrast issue](/testing/screenshots/wave-test-2-(homepage).png). 
* I started to understand the importance of the contrast issues and labelling objects that I wouldn't assume necessary to label. For example, lists and navbars. 
![After adding more aria-labels where necessary](/testing/screenshots/wave-test-3-(homepage).png)
![Final wave test on homepage](/testing/screenshots/wave-test-final.png)

* Due to my sites restrictions on what content can be seen by other users, I was not able to run the 'my symptoms' page through the wave test. To ensure I was able to maintain the same diligence to the accessibility of the site, across all pages, I added wave's google chrome extension to my browser. 
[google chrome extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh/related) 


 ### Login

![Login page](/testing/screenshots/wave-login.png)
* The empty link being sighted on the page is the scroll to top function which appears as dormant on the login and register pages because, the pages have so little contnet that the function is not activated. To add clarity to the scroll to top button/ link, i added a aria- label, explaiinng that it was a scroll to top link. 

 ### Register
![register page](/testing/screenshots/wave-register.png)
* On the register page, I also had a link button to 'log in' (if users already had an account). The wave test pointed out that this was in fact bad usability and could actually be confusing for a user, therefore contributing to bad user experience. 

* I removed the login link. 

* In aiming to be an 'easy to use site', I had added surplus buttons for user ease. However, I had overpopulated the site with excessive buttons, which had the opposite effect! 

 ### My symptoms

![My symptoms](/testing/screenshots/wave-my_symptoms.png)
* The missing 'form label' is for the first question on the add symptom form 
``` <div class="input-field status-options">
                    <select id="isolation_status" name="isolation_status" class="validate" aria-label="isolation-status dropdown" required> 
                    <label for="isolation_status"> </label>
                        <option value="" disabled selected>What is your Self-isolation status?</option>
                        {% for stat in status %}
                        <option value="{{ stat.isolation_status }}">
                            {{ stat.isolation_status }}
                        </option>
                        {% endfor %}
                       
                    </select>                    
                    </div> 
```

* Due to the nature of this input field, it was less aesthetically pleasing, responsive to have a label AND a disabled selected option. I opted for the disabled selected option instead of a label because the disabled selected option could function as a label. I also added an aria-label for users who rely on labels. 

## Responsiveness
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
- It was through this boolean field, that i was als able to filter down to just the services. I simply added some code to my views and template so that just the services would be displayed when a user clicks on the services. 
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


## Responsiveness
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | All the important services are accessible from nav bar| Don't need to scroll to find important information | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 
### Test conducted:
- Access each page in the site with different screen sizes with Google Dev Tool's Emulator and check the layout and format of site elements
### Result:
1. Navbar: I have the search bar collapsed for smaller than medium screen size (width < 992px) because the search bar with input field conflicted with other navbar components. 
'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
2. Home page: The image size responsiveness on Carousel at landing(home) page was adjusted by media queries.
### Verdict:
Passed all tests.


* Bootstrap is made for responsive and upwards, therefore I kept the use of col sizes minimal and made sure everything would fit a small screen first and mainly used the col size of s12. 

### Footer
* Just at desktop/ iPad pro screen size, my main issue was the footer on all pages sitting at the bottom of the page, this happens when an object is too big for its container and overspills outside of the main HTML. 
![footer on homepage](/testing/responsiveness/ipad-pro-homepage(2).png)
![login on homepage](/testing/responsiveness/login.png)
![registeration on homepage](/testing/responsiveness/ipad-pro-register.png)

* My first action was to change the position of the footer to 'relative' and 'absolute' in turn. neither of these options made all three pages' footers responsive.

* I then added an id to the footer and trialled different positions through the id. This was again no help. 

#### Solution 

- I referred back to materialize, which was where I had used the footer template and added some positioning to the body and main. This made the footer responsive on all pages. 
```
body{
    background-color: #FFE1A8;
    font-family: 'Roboto', 'sans-serif';
    color: #472D30;
    text-align: center;
    font-size: 20px;
    padding: 1rem 0rem 0rem 0rem;
    display: flex;
    min-height: 100vh;
    flex-direction: column;

}

  main {
    flex: 1 0 auto;
  }
```

- Something I learnt with this error, is that if you are going to use a library and templates from the library in your developing process, you must be aware that the entire framework, relies on (sometimes hidden) positioning/ sizing, these will affect aspects of your entire project. although it may seem like the easiest option in early development, to use libraries, it may not always be the easiest option in the long run. 

### footer layout on mobile 

- Similarly, on the iPhone 5 screen size, I was troubled by the layout of the footer. 

![footer layout](/testing/responsiveness/iphone-5-footer-layout.png)

I made some changes and simplified the content, but I was still unhappy that at the small device size it was still 3 columns. I thought I had understood the materialize grid system to mean that s12 m4 l4 meant that, the columns would take up all 12 spaces (the entire screen width) when being viewed at this size. 4/12 for each column when viewed on medium and large screens. 

- To try to solve this I adjusted the column sizes and kept checking them again. 

#### Solution 
- unresolved. 

### add symptom form 

- On the add symptom form, when a user clicks on the input fields, the labels became slightly obstructed. 
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(1).png)

* Using inspect in dev tools, I adjusted the position of the label in the input field.

#### Solution 

- I added a bit of extra room to the top and left of the input field label so that when the field is clicked on and being added to, the labels are still not obstructed 
-*I did the same for the text area's of the input fields and eventually managed to make the form more aesthetically pleasing and readable 
```
.input-field>label {
color: black;
left:2rem;
top:.50rem;
}
```
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(2).png)
![add symptom form](/testing/responsiveness/ipad-pro-add-symptom-form(3).png)
![add symptom form- iPhone 5](/testing/responsiveness/iphone-5-add-symptom-form.png)

### Overspill from content causing responsiveness issue
- At desktop screen size there was a vertical overspill of content, causing the page to jiggle from side to side. I also saw a horizontal overspill too.

![Overspill](/testing/responsiveness/footer-overspill(1).png)
![horizontal overspill](/testing/responsiveness/horizontal-overspill(1).png)
#### solution 
- Using the [unicorn revealer tool](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) 
I scrolled to see the issue and where the overspills lie. 
![Overspill](/testing/responsiveness/footer-overspill(2).png)
![horizontal overspill](/testing/responsiveness/horizontal-overspill(2).png)

- Eventually, I saw the overspill was in the footer.
![Overspill](/testing/responsiveness/footer-overspill(3).png)
- Also in the `body` element.

- To solve this I added a `div` with the class of `container`
![Solved](/testing/responsiveness/overspill-solved(1).png)
![Solved](/testing/responsiveness/overspill-solved(2).png)

- To solve the overspill in the body, I removed some extra padding I had added. 
![Solved](/testing/responsiveness/horizontal-overspill-solved.png)

## User stories testing

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Access the website on both larger and smaller screened devices | Access the website on my phone and PC |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily navigate to the Products and services available | Find the product or service I want to purchase |




| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Read all content clearly | Enjoy using the site. |




| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | See a shopping cart icon on nav bar | Always check the current order and checkout when I want |




| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Be able to easily access information about Juspreet and the services she offers | Trust the validity of her and her services. |


<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information and access blog articles |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | View my order history | Purchase the same product again in the next order |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily recover my password in case I forget it | Recover access to my account |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Post a blog about any of my areas of expertise | Provide site visitors interesting information and hopefully make a sale as a result |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Add comments to the blog posts | Write down my thoughts on the post |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Have the ability to remove unsavoury comments | Protect my brand and the site visitors' experince |
<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | View individual product pages that have prices and descriptions | Get detailed information about the product before purchasing |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User| Filter by a specific category | Easily find products in a specific category |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Leave/View product reviews with scores | Understand which products are popular with other customers |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily add a new product | Make sure the online site has the latest catalogue |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily remove a product | Make sure the online site has the latest catalogue |

<br/>

- Cart, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily select the quantity (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Have my delivery information is prefilled if logged in | Smoothly proceed with my purchase |





| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Be reminded to log in if I did not log in | Smoothly proceed with my purchase and prefilled form | 


<br/>

updating_quantity of item from product detail:


webhook creates the order:
- had a small issue initially because, i had not added the json loads to the bag:
```
for item_id, item_data in bag.items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=item_data,
                            product=product,
                        )
                        order_line_item.save()
```
changed to:
```
for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=item_data,
                            product=product,
                        )
                        order_line_item.save()
```
the other issue i had is; i had mistakenly carried across a dictionary object to the webhook handler context; in the condition of if a product is a service:
```
else:
    for service, quantity in item_data['item_is_service'.items():
        order_line_item = OrderLineItem(
            order=order,
            product=product,
            quantity=quantity,
            product_is_service=service,
        )
        order_line_item.save()
```
this was throwing an errror in the webhook handler, because the last line was an unexpected item, i realised that this line was unecessary here and it was only important that i distinguish between products and services, if i was adding/ updating or deleteing from the bag. 
I changed the else statement to 
```
else:
    for service, quantity in item_data['item_is_service'.items():
        order_line_item = OrderLineItem(
            order=order,
            product=product,
            quantity=quantity,
        )
        order_line_item.save()
```
this solved the issue! 

## Usability testing

### Symptoms page usability 

![user lands on homepage](/testing/usability/home(1).png)
* Name of the page is highlighted in navbar, user knows they are on the symptoms page. 

* User reads the text and clicks 'get started now'.
![user clicks on 'get started now'](/testing/usability/home(2).png)

* Button highlights- aesthetically pleasing, the user is given feedback that they have hovered/ clicked on the button.
![User is taken to register page](/testing/usability/home(3).png)

* User is taken to register page after clicking, again register is highlighted and page is simple and functional. 

* *If user is already logged in and clicks this same button, they are redirected to the add add symptom form* 

![search bar on homepage](/testing/usability/home(4).png)
* If the user comes back to the homepage, they are met with the search bar. If they perform a none format fitting search, they are told what is wrong and how to solve the issue. 
![none formatting search item](/testing/usability/home(5).png)

* If, search item does not match any of the listed symptoms, the user sees a message explaining that with a link. 

- This message could be stronger and more obviously a feedback message. 

!['search item doesnt exist' message](/testing/usability/home(13).png)
Here I have added a div with class 'alert' around the if statement which actions the feedback text, letting the user know that their search item was unmatched and what they should do next. I checked its accessibility too and found no issues with style. 

- *If user clicks on the link to add the symptom, they are redirected to the login page.*

- *If user is already logged in and clicks this same button, they are redirected to the add add symptom form* 

* User resets and scrolls down to find the list of added symptoms.
![user resets search item](/testing/usability/home(6).png) 

* User is informed with text that the list is clickable after clicking, they see the description. 
![user clicks symptom on list- description appears](/testing/usability/home(7).png) 
![user clicks symptom on list- description disappears](/testing/usability/home(8).png)

* Scrolling down to bottom of page, copy url functionality is hovered, clicked and gives feedback. 
![copy url functionality is hovered](/testing/usability/home(9).png)
![copy url functionality is clicked](/testing/usability/home(10).png)
![copy url functionality gives feedback](/testing/usability/home(11).png)


* Link in footer works, however when testing I noticed I had forgotten to add `"_blank"` attribute. I have since added and the link now opens to a new tab. 
![user lands on homepage](/testing/usability/home(12).png)


### Register page usability
- After clicking one of the homepage links or after clicking register in the nav bar, user arrives at the registration page 
![register](/testing/usability/register(1).png)
![register](/testing/usability/register(2).png)

* The registration page nav bar link is highlighted, the registration form provides feedback of the allowances of choosing a username and or password. 

* Originally, I had added a pattern that the user must adhere when choosing a username and password. I did this because I wanted to improve my defensive programing, however, after testing, I realised that these features actually inhibited a good UX. I since removed them and now the only requirements for a username/ password are the minimum lengths. 

* After successfully registering, the user is taken directly to the 'my symptoms' page where they are informed that they have no symptoms currently and are encouraged to add one.
![register](/testing/usability/register(3).png)

* Initially I had a link to the add symptom form, however again when testing, I realised that it was actually confusing to have an additional link for a process which is a mere scroll away! 
![register](/testing/usability/register(4).png)

* If the user tries to login with a username that is already in use they are taken to the login page 
![register](/testing/usability/register(5).png)

### Login page usability 
- When logging in with an error, the user is taken to an error page, which does not say the specific reason they have not successfully logged in, but gives all possible reasons. I felt this was better defensive programming than a mere flash message. 
![login](/testing/usability/login(1).png)
![login](/testing/usability/login(2).png)

- The link in error page, brings user back to login. 
![login](/testing/usability/login(3).png)
![login](/testing/usability/login(4).png)

- If login is successful; 
![login](/testing/usability/login(5).png)

### Add symptom usability
- When the user has logged in / registered and now wants to add a symptom,
![add symptom](/testing/usability/add_symptom(1).png)

- The user fills in the form and receives feedback once complete. 
![add symptom](/testing/usability/add_symptom(2).png)

### Edit symptom usability
- When the user wants to edit;

![edit symptom](/testing/usability/edit_symptom(1).png)

- The text at the top of the page explains to the user why it is important to continually update their symptoms.

![edit symptom](/testing/usability/edit_symptom(2).png)

- The users' original form is loaded.

![edit symptom](/testing/usability/edit_symptom(3).png)

- When changes are made to the form, the user clicks the save button. 

![edit symptom](/testing/usability/edit_symptom(4).png)

- At this point, the user is given feedback that the symptom is updated and where it can be found. 

### Delete symptom usability
- When deleting a symptom; 
![deleting symptom](/testing/usability/delete-symptom(1).png)
![deleting symptom](/testing/usability/delete-symptom(2).png)

- A modal will appear asking the user if they are sure they want to delete. 
- If yes, they will be given a feedback message, prompting them to add another. I didn't think a link to 'add symptom' was necessary, again,  it may have contributed to bad UX.
![deleting symptom](/testing/usability/delete-symptom(3).png)

- If no, the box simply closes. 
![deleting symptom](/testing/usability/delete-symptom(4).png)

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

## Bug 12 Deployment errors 
solution: update aws keys, add static root.
- As I already set up a user so that I could access the amazon aws SES email functoionality, I had some confusion over which aws settings to add. 
- When I began deployment, I got the user I had made for the email purpose ( which was not in a group ), looked at the permissions of the user, and simply added that permission to the user in the group in my bucket. 
- ![ added permission to group user ](readme-materials/bug_screenshots/bug_12(a).png)
- When i tried to deploy i got a few errors, one being an unrecognised AWS_ACCESS_KEY_ID. This made sense because, the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in my heroku and env settings, were that of the user I had now deleted. 
- ![ AWS_ACCESS_KEY_ID error ](readme-materials/bug_screenshots/bug_12(a).png)
- I ran the deployment again and got another error, this time about the static root.
- ![ STATIC ROOT error ](readme-materials/bug_screenshots/bug_12(c).png)
- I did some research and read [ this ](https://docs.djangoproject.com/en/dev/ref/settings/#static-root) and added 
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
to my settings.py file. when setting your static root, a common mistake is setting the name to 'static' however, this will throw an error as 'static' will refer to your 'STATICFILES_DIRS' variable. 
After changing these varibales, i successfully deployed. 
On reflection, I will insure that with future projects I deploy a lot earlier into the journey than I have with this project. Although I am still not quite finished and it is a weight off my shoulders, it would have been even better to iron out these issues and learn about things like the static roote varibale , even eaelier in the project. 

## Bug 13 modal confusion errors
- Initially I had thought it was good UX to have the action aoptions; edit, delete and comment, accessible on all blog pages (all blogs, my blogs, blog detail).
- This was fine for the update and comment options, but if the user hit delete, I wanted to add a modal in so that the user could double check whether they really wanted to delete. 
- The modal relies on links that exist inside the for loop, therefore, if i placed the delete confirmation button (linked to the modal) in the loop and the modal outside the loop. The confirmation button and relative data-target, toggle etc, were not recognised and would throw a loop. 
- An obvious solution would be to place the modal functionality inside the loop, however this would result in generating a modal for all of the products on the page, which would undoubtedly lead to many bugs. 
- I decided that it was arguably better to have all the action buttons in one destination and UX would not be damaged if, edit delete and comment functionality was only accessible via blog detail. 
- However, when it came to the same logic for confirming delete modal for the store items (accessible to admin user) I felt it was none negotiable that the admin should be able to delete an item from both the all items and product detail page. 
- again, this was straight forward on the product detail page, becuase the functionality is only referring to ONE item, however i ran into errors on the all items page. 
- ![ URL error ](readme-materials/bug_screenshots/bug_13(a).png)
- To solve this I added a hidden form into the modal.
```
<div class="modal fade" id="deleteModal" data-backdrop="static" data-keyboard="false" tabindex="-1"
    aria-labelledby="deleteModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content text-black">
            <div class="modal-header">
                <h5 class="modal-title" id="deleteModalLabel">Are you sure you want to delete?</h5>
            </div>
                <div class="modal-footer">
                    <form id="delete-form" method="POST" action="{% url 'confirm_delete' %}">
        {% csrf_token %}
        <input type="hidden" name="id-selected" id="id-selected">
        <input type="hidden" name="redirect_url" value="{{ request.path }}">
        <input type="submit" value="Confirm Delete" class="btn btn-danger">
       <button type="button" class="btn-success btn" data-dismiss="modal" aria-label="Close"> No
                </button>
    </form>
                </div>
        </div>
    </div>
</div>
```
- Made a new view with a corresponding URL 
```
def confirm_delete(request):
    """
   confirm delete
    """
    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        product = get_object_or_404(Product, pk=selected)
        product.delete()
        messages.success(request, f' {product.name} has been deleted')
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
```
- Finally, used Jquery to complete the action and direct the functionality 
```
    <!-- delete modal -->
    <script type="text/javascript">
    $(".js-delete").click(function () {
        var productId = $(this).attr("data-value");
        $("#id-selected").val(productId)
    });
    </script>
```
- It has become clear throughout this project, that whilst Django is a very helpful framework, its limitations lie within the difficulty to apply specific actions to more than one item, hence why its easier to have detail pages for each item/ blog. I could have decided to simply have the delete functionality on the product detail only, however I truly beleiev it is better UX for the delete to be accessible in all items. Moving forward, I would spend more time learning AJAX, which i know would have come in handy here. 
## Validators and Linters

### WW3 HTML validation 
As expected, each of my pages flagged errors due to my use of jinja code, I also had some warnings about the misuse of the `aria-label` attribute, however since I had added these after taking the accessibility of my site into account, I thought that the wave tool was likely to be a better judge of the use of this particular attribute and felt comfortable with my choice. 

Other than the jinja code-related errors, I had no other HTML validation errors. 

### WW3 CSS validation 
- My CSS had no errors.
![CSS Validator](/testing/usability/CSS-Validator.png)

### PEP8 validation 
- My python code had no errors.
![PEP8](/testing/usability/PEP8.png)


### Javascript validation 
- My javascript code had no errors but did have 3 warnings. The warnings were about the use of keywords such as `let` and `const`, to avoid any issues with this, in the future I would ensure that all of my JS functions had an `error` response, if anything I was using, was not supported in the users' browser. Similar to the error function I used for the creation of my copy to clipboard function. 
```
clipboard.on('error', function(e) {
alert("Oops, it looks like this function isn't supported on your browser! Don't worry, Just copy this: https://self-isolation-watch.herokuapp.com/"); 
```

![JS-Hint](/testing/usability/JS-Hint.png)


> [To return to the previous document please click here](https://github.com/mayasaffron/self-isolation-watch/blob/master/README.md) 








