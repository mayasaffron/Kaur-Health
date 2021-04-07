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




## User stories testing

## Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Read all content clearly | Enjoy using the site. |


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Access the website on both larger and smaller screened devices | Access the website on my phone and PC |


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Be able to easily access information about Juspreet and the services she offers | Trust the validity of her and her services. |

- The about page is breif and informative, not only do users have access to inforamtion regarding Juspreet and her work, they can also find testimonies from clients too. 
- I feel the about page, fully satisfies this user story. 


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily navigate to the Products and services available | Find the product or service I want to purchase |

- There is a searchbar on the main nav bar which says `Search Products & Services`
![ All products and services ](readme_materials/testing_screenshots/user_stories_products(2)).png)
- Products and services tab is clear and obvoius on the nav bar.


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | See a shopping cart icon on nav bar | Always check the current order and checkout when I want |

- The shopping cart icon is black when bag is empty, when bag has items; the bag becomes illuminated and reads the current total in bag. 

<br/>

## Online shopping 

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User| Filter by a specific category | Easily find products in a specific category |

- When a user clicks on ` Product and services` dropdown nav bar option, you are given a dropdown to the different categories of the products and services. I thought that the dropdown would provide better user experience than a direct link, which takes you to a page where you then have to sift through the categores that you are interested in. The nature of this site, is such that, as a user you are prpbably well aware of what you are looking and therefore which category to find it. Or, if you are new to the sites content, i felt it would be less overwhelming if you have some filtering control and could navigate to the category you were most interested in. 
By doing this I satisfy the ease of navihation in my user stories and adhere to my wireframes. 
![ The dropdown distinguishes the products and services by category ](readme_materials/logic_screenshots/navbar_dropdown(products).png)
- After clicking on your chosen category, all of the products and services under this category, will be displayed. The category name will appear just beneath the consistent title of 'products and services' and there is a banner just above the title, with the free delivery minimum spend. 
In the top left corner the user will see a link to `Products and services home` which when clicked will take them to the `all products and services`, here all of the categories will be clickable links beneath the title, so that a user can navigate to the other categories from here as well/ instead of the navbar dropdown.
Beside the `Products and services home` there is a product and service count, outlining how many products and how many services belong to this category. 
![ All products and services ](readme_materials/testing_screenshots/user_stories_products(1)).png)

Originally I toyed with the idea of having the product and service count clickable links and sectioning the page so that the user would be taken to a products section if they clicked the product count link to 'products' and the same for services. However, this proved to be bad UI, as when and if the user chose to sort the products, the sections would make things very messy and hard to contain. 
- It was through this boolean field, that i was als able to filter down to just the services. I simply added some code to my views and template so that just the services would be displayed when a user clicks on the services. 
I opted to distinguish services from products in a few ways;
1) Adding a consistent banner in each of the services' descriptions # picture
2) When a service is added to the users bag, the success message will clearly state that the user has just added a service and should read the terms and conditions carefully. 
3) On the order receipt, I have again stated, which of the items are services and that the user should therefore read the terms and conditions. 

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | View individual product pages that have prices and descriptions | Get detailed information about the product before purchasing |

- The product detail page satisfies this user story. 
- For servicess in particular, it was important that the user could access all necessary information. 

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Leave/View product reviews with scores | Understand which products are popular with other customers |

- Site users can view ratings of each product, however as noted in the `features left to implement` section of the readme; in production i quickly understood that he nature of this site is such that there needed to be a balance between business and community. The use of testimonies on the about page served as a review and in the future as the site grows I would consider adding a product review section and functionality.  

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily update and remove a product | Make sure the online site has the latest catalogue |

- If the user is logged in as a superuser, Update / Delete option is also shown on each card.
![ product management ](readme_materials/testing_screenshots/user_stories_product_management(1)).png)
![ updating product ](readme_materials/testing_screenshots/user_stories_product_management(5)).png)
![ updating product ](readme_materials/testing_screenshots/user_stories_product_management(6)).png)
![ updating product ](readme_materials/testing_screenshots/user_stories_product_management(7)).png)
![ updating product ](readme_materials/testing_screenshots/user_stories_product_management(8)).png)
![ deleting product ](readme_materials/testing_screenshots/user_stories_product_management(11)).png)
![ deleting product ](readme_materials/testing_screenshots/user_stories_product_management(9)).png)
- It was also necessary to add some defensive programming, to inform none admin users that they are not permitted to make any changes to the products, should a none admin user attempt it.
![ alert message for none admin user ](readme_materials/testing_screenshots/user_stories_product_management(10)).png)

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily add a new product | Make sure the online site has the latest catalogue |

- As explained in readme, when superuser is logged on, product management is accessible as dropdown link from `account` in nav bar. 
- this link will take admin straight to a new product form. 
![ adding product ](readme_materials/testing_screenshots/user_stories_product_management(2)).png)
![ adding product ](readme_materials/testing_screenshots/user_stories_product_management(4)).png)
![ product management ](readme_materials/testing_screenshots/user_stories_product_management(3)).png)

<br/>

## Cart, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily select the quantity (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity |

- The quantity is set to a defualt of 1 and can be easily adjustable both in and out side of the bag. 
![ updating bag items outside ](readme_materials/testing_screenshots/user_stories_cart(1)).png)
![ updating bag items ](readme_materials/testing_screenshots/user_stories_cart(2)).png)
- Users are also given feedback messages when adjusting any of the items in their bags. 
- Items can be easily removed from the bag. 
![ updating bag items ](readme_materials/testing_screenshots/user_stories_cart(3)).png)


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Have my delivery information is prefilled if logged in | Smoothly proceed with my purchase |

- If users are authenticated, after their first order, their delivery information can be saved to their profiles. Users can update their details on their profile, this means the details will be updated for when the user carries out their next order.
![ delivery info on profile ](readme_materials/testing_screenshots/user_stories_checkout(2)).png)
![ delivery info prefilled ](readme_materials/testing_screenshots/user_stories_checkout(3)).png) 



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Be reminded to log in if I did not log in | Smoothly proceed with my purchase and prefilled form | 

- Beneath the order form there are links to either register for an account or log in. 
- I considered adding more reminders to log in for this functionality, throughout the site, howver decided against it, as I thought this could attribute to bad UX. If a user feels that it is impossible to carry out the desired action, without being authenticated, this may disuade them from visiting or more importantly, purchasing thorough the site again. 

<br/>

## Registration, User Accounts and User Community


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information and access blog articles |

- users with a profile can edit their delivery information. 
- Initially, I had intended to make blog articles accessible for users only. However, during production I decided against this as i felt this would negatively impact Juspreets exposure to brands and other potential clients (brand goals). 
- Blogs are accessible to all, however, only authenticated users can make a post or comment on a post. 
- To acknowledge this user story, if a user has written blog posts, when they log on and click on the blog tab in the nav bar they will see a dropdown link ` my blog posts `. Here they will find all of the posts that they have written. 
- Whilst my original idea hasnt been executed, I feel that what exists now is a better alternative and will reuslt in a better UX. The users perosonal blogs being accessed via the nav bar is another way of satisfying the idea behind this user story. 
![ my blog posts ](readme_materials/testing_screenshots/user_stories_blog(1)).png) 
![ my blog posts ](readme_materials/testing_screenshots/user_stories_blog(2)).png)


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | View my order history | Purchase the same product again in the next order |

- This is achieved on the users profile page. 
![ my blog posts ](readme_materials/testing_screenshots/user_stories_profile(1)).png)


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily recover my password in case I forget it | Recover access to my account |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |



| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Post a blog about any of my areas of expertise | Provide site visitors interesting information and hopefully make a sale as a result |

- As aforementioned, I thought it would be a good way to encourage more users and build an online community if users were only permitted to write blogs, if they were authenticated. 
- I convey this clearly throughout the site.
![ authenticated users can add blogs ](readme_materials/testing_screenshots/user_stories_blog(3)).png)
- Adding a post is easy to do. 
![ adding blog ](readme_materials/testing_screenshots/user_stories_blog(4)).png)
![ posted blog ](readme_materials/testing_screenshots/user_stories_blog(5)).png)


| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Add comments to the blog posts | Write down my thoughts on the post |

- Comments of a post can be viewed by all users, however, only authenticated users can add a comment. 
- If a user is authenticated they will see links to comment, if the user is not they will see links to `login and comment` which will direct them to the login. 
- Initially, instead of links i had an alert message which was triggered if a none authenticated user attempted to comment. However I chnaged this, as the natire of 'topical comments' are such that, the user will want to quickly express whatever feeling/ response, the post have evoked in them. I felt an alert message was a little vague and would contribute to bad UX. the user could likely be confused as to what to do next? Whereas a link will direct them to the login page, where they are on a mission to comment. 

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Have the ability to remove unsavoury comments | Protect my brand and the site visitors' experince |

- I did not have time to add this in, however in the future i will. 
<br/>




# Manual testing



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



# Bugs discovered

## Solved Bugs
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

## Bug 14 deployed heroku site error
- I was repeatedly getting this error after pushing to heroku master, to see the changes made to my site. 
![ pre-receive hook declined heroku ](readme-materials/bug_screenshots/bug_15.png)
- I came across [this](https://stackoverflow.com/questions/63639673/heroku-deploy-error-remote-rejected-master-master-pre-receive-hook-dec) rticle on slack overflow and tried it 


## Unsolved Bugs

### Bug 1 aws email 
- Despite wanting to use aws for my email functionality, I was denied my request to leave the sandbox.
- I continued to dipute this, howevere gave up in the interest of time. 
![ AWS correspondance ](readme-materials/bug_screenshots/bug_14(a).png)
![ AWS correspondance ](readme-materials/bug_screenshots/bug_14(b).png)
![ AWS correspondance ](readme-materials/bug_screenshots/bug_14(c).png)
![ AWS correspondance ](readme-materials/bug_screenshots/bug_14(d).png)

# Further testing 
Used peer code review in channel in slack

Kaur Health viewed on all devices and orientations available in Chrome DevTools.

## Accessibility
* I used [wave](https://wave.webaim.org/) to achieve better accessibility on my site. 

> [To return to the previous document please click here](https://github.com/mayasaffron/self-isolation-watch/blob/master/README.md) 