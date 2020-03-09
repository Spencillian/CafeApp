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

- `GET /food`

**Response**

 - `200 OK`
 
```json
{
    "message": "(schedule exists) ? Schedule Exists : No Schedule Exists ",
    "data": 
    {
        "time_type": "Breakfast/Lunch/Dinner",
        "session_type": "Adviser/Sit Down/Business/Buffet",
        "time_day": "Monday/Tuesday/Wednesday/./././...",
        "time_clock": "{hour}:{minute} of lunch start time",
        "food": ["Foods"]
    }
}
```

###### Might have to change the Foods array into a dictionary due to list ids in react native

