user story testing 

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
