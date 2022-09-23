# DRF-Pizza-Menu-API

Pizza Menu API with:
- Backend and authentication: ***Django Rest Framework***

### How to Use the API

Make a fetch request to [nathan34.pythonanywhere.com](http://nathan34.pythonanywhere.com/).

> This returns the following json response.
```json wrap
[
   {
      "id":1,
      "name":"Italian Pizza",
      "price":13.0,
      "topping_1":1,
      "topping_2":3,
      "topping_3":6,
      "size":2,
      "average_rating":0.0,
      "number_of_ratings":0
   },
   {
      "id":2,
      "name":"Garlic Pizza",
      "price":10.0,
      "topping_1":1,
      "topping_2":3,
      "topping_3":7,
      "size":2,
      "average_rating":0.0,
      "number_of_ratings":0
   }
]
```

You can choose a response using the menu ID.
For example: [nathan34.pythonanywhere.com/1/](http://nathan34.pythonanywhere.com/1/).

>This return the following json response
```json wrap
{
   "id":1,
   "name":"Italian Pizza",
   "price":13.0,
   "topping_1":1,
   "topping_2":3,
   "topping_3":6,
   "size":2,
   "average_rating":0.0,
   "number_of_ratings":0
}
```

### Topping
1. Pepperoni
2. Mushroom
3. Extra cheese
4. Sausage
5. Onion
6. Black olives
7. Green pepper
8. Fresh garlic
9. Tomato
10. Fresh basil

### Size
1. Small
2. Medium
3. Large

