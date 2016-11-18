# Fake user data server

### A fake user data server to practice with angular2 small project.

1. Django base server.
2. db.sqlite3 already have 12 users' physiological data.
3. 1 user have Heat Beat, Breath, Blood pressure, Body temperature info. every physiological info with 20 data.

### REST API

#### POST:
1. http://localhost:8000/api/userlist/  => get user id list
2. http://localhost:8000/api/profile/ with { 'id': _number_ } => get id=1 user name, breath, heartbeat, bloodpressure, bodytemperature. Every physiological info data will random choice.
    - success:
    ```
    {
        "bloodpressure": 104,
        "name": "Justin Morgan",
        "bodytemperature": "36.9",
        "breath": 15,
        "result": "success",
        "heartbeat": 84,
        "message": "Success"
    }
    ```

    - failed:
    ```
    }
        "message": "Can not find user.",
        "result": "error"
    }
    ```
