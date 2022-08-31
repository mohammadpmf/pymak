from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="color: red;">Welcome to my shop</h1>
    <p>Have a nice day</p>
</body>
</html>
""")
