# CafeApp API

## Usage

### Format

```json
{
    "message": "Extra description of what is going on",
    "data": "Mixed typed content of the response"
}
```

### Requests

- `GET /food?day=<int:day>`

###### `Future` - Other data might be needed

**Response**

 - `200 OK`
 
```json
{
    "message": "There is or isn't a menu today",
    "data": 
    {
        "breakfast": ["List of foods in breakfast menu"],
        "lunch": ["List of foods in lunch menu"],
        "dinner": ["List of foods in dinner menu"]
    }
}
```
###### `Future` - Might have to change the breakfast/lunch/dinner arrays into a dictionary due to list ids in react native

