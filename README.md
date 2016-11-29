# Fake user data server

### A fake user data server to practice with angular2 small project.

1. Django base server.
2. db.sqlite3 already have 12 users' physiological data.
3. 1 user have Heat Beat, Breath, Blood pressure, Body temperature info. every physiological info with 20 data.

### REST API

#### POST:
1. api/userlist/  => get user id list

    - success:
    ```
    {
        "list": [
            1,
            2,
            3,
            4,
            5,
            6
        ]
    }
    ```
    代表有6個病患資料

2. api/profile/ with { 'id': _number_ } => get id=_number_ patient's info
    - success:
    ```
    {
      "name": "Elizabeth Pitts",
      "weight": "52",
      "age": "39",
      "number": "1",
      "sex": "M",
      "contact": "553-039-1072",
      "result": "success",
      "address": "0142 King Meadow Suite 646\nWilliamsfurt, TN 18039-1802",
      "message": "Success",
      "height": "171",
      "id": 1,
      "room": "天龍房"
    }
    ```

    - failed:
    ```
    }
        "message": "Can not find user.",
        "result": "error"
    }
    ```

3. api/physiological/ with {'id': _number_ } => get id=_number_ patient's physiological info

    - success:
    ```
    {
        "blood_pressure": 102,
        "uric_acid": "6.8",
        "body_temperature": "37.2",
        "walk_steps": 1308,
        "leave": false,
        "count_call": 0,
        "count_leave": 25,
        "blood_oxygen": "93",
        "breath": 15,
        "call": false,
        "result": "success",
        "glycemia": "99",
        "wristband_power": true,
        "heartbeat": 104,
        "message": "Success",
        "mattress_power": true
    }
    ```

    - failed:
    ```
    {
        "message": "Can not find user.",
        "result": "error"
    }
    ```
