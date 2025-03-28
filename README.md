# DRF-Pizza-Menu-API

Pizza Menu API with:

- Backend and authentication: **_Django Rest Framework_**

To get more information about the API check the documentation at the `/docs` end point.

### Authentication

The API uses JWT (JSON Web Tokens) authentication. Refresh tokens are issued at regular intervals. When a user logs out, the token is added to a blacklist to prevent further usage.

### How to Use the Current API

Make a fetch request to the end points.

### Example Response

```json
[
  {
    "id": 1,
    "name": "Italian Pizza",
    "price": 13.0,
    "topping_1": 1,
    "topping_2": 3,
    "topping_3": 6,
    "size": 2,
    "average_rating": 0.0,
    "number_of_ratings": 0
  },
  {
    "id": 2,
    "name": "Garlic Pizza",
    "price": 10.0,
    "topping_1": 1,
    "topping_2": 3,
    "topping_3": 7,
    "size": 2,
    "average_rating": 0.0,
    "number_of_ratings": 0
  }
]
```

You can choose a response using the menu ID.
For example: [nathan34.pythonanywhere.com/1/](http://nathan34.pythonanywhere.com/1/).

> This returns a json response that have the following structure.

```json
{
  "id": 1,
  "name": "Italian Pizza",
  "price": 13.0,
  "topping_1": 1,
  "topping_2": 3,
  "topping_3": 6,
  "size": 2,
  "average_rating": 0.0,
  "number_of_ratings": 0
}
```

### Topping Options

| Number | Topping Type |
| :----- | -----------: |
| 1      |    Pepperoni |
| 2      |     Mushroom |
| 3      | Extra cheese |
| 4      |      Sausage |
| 5      |        Onion |
| 6      | Black olives |
| 7      | Green pepper |
| 8      | Fresh garlic |
| 9      |       Tomato |
| 10     |  Fresh basil |

### Size Options

| Number | Size Type |
| :----- | --------: |
| 1      |     Small |
| 2      |    Medium |
| 3      |     Large |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
