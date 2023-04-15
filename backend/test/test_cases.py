import requests
import json

def test_login():
    url = "http://localhost:5000/api/auth/login"

    payload = json.dumps({
      "username": "premium@gmail.com",
      "password": "Premium@24"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200

#------------ use apis ---------------
def test_get_expense_for_categoryId():
    url = "http://localhost:5000/api/expense/getByCategoryId?cat_id=2"

    payload = json.dumps({
        "cat_id": 2
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxNzczMCwianRpIjoiMTJmZGRkZjYtNDgyNy00NmY5LTg0NTgtZTc1NzEyN2RlMTQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByZW1pdW1AZ21haWwuY29tIiwibmJmIjoxNjgxNTE3NzMwLCJleHAiOjE2ODE2MDQxMzB9.OL-x2lOG2LPsIO-5hnaXxqIAZfn69oZET_dQoTuH2aI'
    }
    #need to replace bearer token

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.json()["data"][0]["CAT_ID"] == 2 #change this value if passing another cat_id

def test_add_expense():
    url = "http://localhost:5000/api/expense/addExpense"

    payload = json.dumps({
        "cat_id": 5,
        "amount": 400,
        "description": "toronto trip",
        "expense_date": "2023-04-06"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxNzc2NCwianRpIjoiM2U2NTk5NWUtNTBkOC00MDQxLThlN2YtMzhlNThhYzAzZTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByZW1pdW1AZ21haWwuY29tIiwibmJmIjoxNjgxNTE3NzY0LCJleHAiOjE2ODE2MDQxNjR9.3BSJD_5Im3nBw-Twwyz2E_KGH8Crhr1M89eU2WZhrX4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.json()['status'] == 'Success'

def test_edit_expense():
    url = "http://localhost:5000/api/expense/editExpense"

    payload = json.dumps({
        "ID": 7,
        "cat_id": 2,
        "amount": 199,
        "description": "dineout in cafe",
        "expense_date": "2023-04-03"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxNzc2NCwianRpIjoiM2U2NTk5NWUtNTBkOC00MDQxLThlN2YtMzhlNThhYzAzZTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByZW1pdW1AZ21haWwuY29tIiwibmJmIjoxNjgxNTE3NzY0LCJleHAiOjE2ODE2MDQxNjR9.3BSJD_5Im3nBw-Twwyz2E_KGH8Crhr1M89eU2WZhrX4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.json()['status'] == 'Success'

def test_delete_expense():
    url = "http://localhost:5000/api/expense/deleteExpense"

    payload = json.dumps({
        "id": 11
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxNzc2NCwianRpIjoiM2U2NTk5NWUtNTBkOC00MDQxLThlN2YtMzhlNThhYzAzZTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByZW1pdW1AZ21haWwuY29tIiwibmJmIjoxNjgxNTE3NzY0LCJleHAiOjE2ODE2MDQxNjR9.3BSJD_5Im3nBw-Twwyz2E_KGH8Crhr1M89eU2WZhrX4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.json()['status'] == 'Success'

def test_get_all_category_for_user():
    url = "http://localhost:5000/api/category/getAllForCurrentUser"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxNzc2NCwianRpIjoiM2U2NTk5NWUtNTBkOC00MDQxLThlN2YtMzhlNThhYzAzZTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InByZW1pdW1AZ21haWwuY29tIiwibmJmIjoxNjgxNTE3NzY0LCJleHAiOjE2ODE2MDQxNjR9.3BSJD_5Im3nBw-Twwyz2E_KGH8Crhr1M89eU2WZhrX4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.json()['data'][1]["NAME"] == "Education"

#-----------admin apis------------
def test_get_all_category_for_admin():
    url = "http://localhost:5000/api/category/getAllForAdmin"

    payload = {}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxOTQ1OSwianRpIjoiNjVkYmVmYmQtMTBiZC00ZTE0LTk1YTYtY2M0MzQwZDlmM2QwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluQGdtYWlsLmNvbSIsIm5iZiI6MTY4MTUxOTQ1OSwiZXhwIjoxNjgxNjA1ODU5fQ.a5jBKgWLsOrK12CBAl0IdLBhEblfOftioZYEVhV5kOA'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.json()['data'][0]["NAME"] == "Education"

def test_add_category():
    url = "http://localhost:5000/api/category/addCategory"

    payload = json.dumps({
        "NAME": "Housing",
        "REMARKS": "created by admin"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxOTQ1OSwianRpIjoiNjVkYmVmYmQtMTBiZC00ZTE0LTk1YTYtY2M0MzQwZDlmM2QwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluQGdtYWlsLmNvbSIsIm5iZiI6MTY4MTUxOTQ1OSwiZXhwIjoxNjgxNjA1ODU5fQ.a5jBKgWLsOrK12CBAl0IdLBhEblfOftioZYEVhV5kOA'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.json()['status'] == 'Success'

def test_edit_category():
    url = "http://localhost:5000/api/category/editCategory"

    payload = json.dumps({
        "ID": 7,
        "NAME": "Housing Expense",
        "REMARKS": "updated by admin"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTUxOTQ1OSwianRpIjoiNjVkYmVmYmQtMTBiZC00ZTE0LTk1YTYtY2M0MzQwZDlmM2QwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluQGdtYWlsLmNvbSIsIm5iZiI6MTY4MTUxOTQ1OSwiZXhwIjoxNjgxNjA1ODU5fQ.a5jBKgWLsOrK12CBAl0IdLBhEblfOftioZYEVhV5kOA'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.json()['status'] == 'Success'