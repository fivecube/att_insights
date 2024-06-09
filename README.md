## Attendance Analytics

#### Requirements
- Python 3.9
- Django 4.2.13
- djangorestframework==3.14.0

##### Steps to Check Solution
1. Run `python manage.py runserver`
2. Call the API `{{baseUrl}}attendance_insight/attendance_selector/?academic_days=10`
Here baseUrl will be `http://localhost:8000`

#### Extra Capabilities:-
There is a postman collection named **attendance_analytics.postman_collection.json**
with which you can call directly the api's of the project deployed on render at https://mysite-atis.onrender.com/

1. You can save the attendance of a person with name and it 
will be save in the db at this POST API:- `{{baseUrl}}attendance_insight/attendance_selector/`
with payload data like
`{
    "name": "Mohit Chouhan",
    "selected_way_to_attend_class": ["P", "P", "P", "P", "P"]
}`
2. The above will give you a roll_no which you can use in this 
GET API:- `{{baseUrl}}/attendance_insight/attendance_tracker/?roll_no=2`



