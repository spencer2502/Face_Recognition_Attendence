import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://faceattendance-27f7c-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "9713":
        {
        "name": "Aman Nirmalkar",
        "major": "CSE CORE",
        "starting_year": 2022,
        "total_attendance": 6,
        "standing": "A",
        "year" : 2,
        "last_attendance_time": "2023-11-3 02:00:00"

        },

    "6734":
        {
            "name": "Elon Musk",
            "major": "Money Making",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "c",
            "year": 4,
            "last_attendance_time": "2023-11-3 02:00:00"

        },

    "4562":
        {
            "name": "Will Smith",
            "major": "Slap",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing": "E",
            "year": 2,
            "last_attendance_time": "2023-11-3 02:00:00"

        },

"5287":
        {
            "name": "Rudra Tiwari",
            "major": "Chutiyape",
            "starting_year": 2025,
            "total_attendance": 1,
            "standing": "F",
            "year": 1,
            "last_attendance_time": "2023-11-3 02:00:00"

        },


}

for key, value in data.items():
    ref.child(key).set(value)