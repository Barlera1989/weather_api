# Wheater API

## INITIAL CONFIGS:

### 1 - Start server:

To start the server, on terminal, type: 

```bash
docker-compose up
```

Now the API is ready to interact with the endPoints listed below!
__________________________________________________________________________



## ENDPOINTS

Base URL:

```url
localhost:5000/
```

### GET /weather/<city_name>/  -> Get specified city.
### notes:
This route pushes city data to a list.
A new request will push another city data 
to the beginning of that list.
____________________________________________________


example: "Base URL/weather/london"

response:

```json
{
  "City_name": "London",
  "City_temp": 11,
  "City_condition": "Clouds"
}
```

### GET /weather/weather?max=<max>  -> Get a list of cities.
### notes:
The max parameter defines how much items will have in the response list.
If the parameter is higher existing items, the response will be
the existing items.

____________________________________________________

example: 
1° Fill Api List
"Base URL/weather/london"
"Base URL/weather/paris"
"Base URL/weather/porto"

2° Request examples
"Base URL/weather?max=3"

response:

```json
[
  {
    "City_name": "Porto",
    "City_temp": 13,
    "City_condition": "Clouds"
  },
  {
    "City_name": "Paris",
    "City_temp": 12,
    "City_condition": "Clouds"
  },
  {
    "City_name": "London",
    "City_temp": 11,
    "City_condition": "Clouds"
  }
]
```

"Base URL/weather?max=5"

response:

```json
[
  {
    "City_name": "Porto",
    "City_temp": 13,
    "City_condition": "Clouds"
  },
  {
    "City_name": "Paris",
    "City_temp": 12,
    "City_condition": "Clouds"
  },
  {
    "City_name": "London",
    "City_temp": 11,
    "City_condition": "Clouds"
  }
]
```

"Base URL/weather?max=2"

response:

```json
[
  {
    "City_name": "Porto",
    "City_temp": 13,
    "City_condition": "Clouds"
  },
  {
    "City_name": "Paris",
    "City_temp": 12,
    "City_condition": "Clouds"
  }
]
```