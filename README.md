# Wheater API

## INITIAL CONFIGS:

### 1 - Virtual Environment(venv):
1.1 - Creating venv

On terminal, in Weather_API folder, type:

```bash
python -m venv venv
```

1.2 - Entering venv

still on terminal, in Weather_API folder, type:

```bash
source venv/bin/activate
```

(if everything works correctly, a (venv) word should
 appear before the current path on terminal.)
____________________________________________________

### 2 - Installing requirements:
(You should have the venv activated, otherwise it won't work correctly)

To install all the packages that is needed to this repo, type on terminal:

```bash
pip install -r requirements.txt
```
_______________________________

### 3 - Start server:

To run flask server, on terminal, type: 

```bash
flask run
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