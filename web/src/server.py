from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

import mysql.connector as mysql
import os
import datetime
import json

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def post_form(request):

  fname = request.POST['fname']
  lname = request.POST['lname']
  email = request.POST['email']
  comment = request.POST['comment']
  created_at = datetime.datetime.now()

  try:
    db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
    cursor = db.cursor()

    query = "insert into Users (first_name, last_name, email, comment, created_at) value (%s, %s, %s, %s, %s)"
    value =  (fname,lname, email, comment, created_at)
    cursor.execute(query,value)
    db.commit()
    db.close()
    
  except:
    print("Not successful insertion")
  
  return get_welcome(request)

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from Classmembers;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html',{'users': records}, request=req)

def get_personal(req):

  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Personal;")
  records = cursor.fetchall()
  db.close()

  record = records[0]
  print (record)

  resArray = {'Firstname': record[0], 'Lastname': record[1], 'Email': record[2]}
  response = Response(body=json.dumps(resArray))
  response.headers.update({'Access-Control-Allow-Origin': '*'})

  return  response

def get_welcome(req):
  # Connect to the database and retrieve the users
    # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email, comment from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/welcome.html', {'users': records}, request=req)

def get_cv(req):
  return render_to_response('templates/cv.html',[],request=req)

def about(req):
  return render_to_response('templates/about.html',[],request=req)

def get_avatar(req):

  resArray = { "Avatar": "/public/myo.jpg"}
  response = Response(body=json.dumps(resArray))
  response.headers.update({'Access-Control-Allow-Origin': '*'})
  return  response

def get_education(req):
  
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from Education;")
  records = cursor.fetchall()
  db.close()

  record = records[0]
  resArray = {'Education': record[1], 'Degree': record[2], 'Major': record[3], 'Date': record[4]}
  response = Response(body=json.dumps(resArray))
  response.headers.update({'Access-Control-Allow-Origin': '*'})
  return  response

def get_project(req):
  
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from Link;")
  links = cursor.fetchall()
  db.commit()

  cursor.execute("select * from Project;")
  records = cursor.fetchall()
  db.close()

  record = records[0]
  Tan = links[0]
  Hector = links[1]
  Adib = links[2]
  resArray = {'Title': record[1], 'Description': record[2], 'Link': record[3], 'Image_src': record[4] , 'Teamlinks': [Tan[1],Hector[1], Adib[1]]}
  response = Response(body=json.dumps(resArray))
  response.headers.update({'Access-Control-Allow-Origin': '*'})
  return  response

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_welcome', '/welcome')
  config.add_view(get_welcome, route_name='get_welcome')

  config.add_route('post_form', '/post')
  config.add_view(post_form, route_name='post_form')

  config.add_route('get_cv', '/cv')
  config.add_view(get_cv, route_name='get_cv')

  config.add_route('get_avatar', '/avatar')
  config.add_view(get_avatar, route_name='get_avatar',renderer='json')

  config.add_route('get_personal', '/personal')
  config.add_view(get_personal, route_name='get_personal',renderer='json')

  config.add_route('get_education', '/education')
  config.add_view(get_education, route_name='get_education',renderer='json')

  config.add_route('get_project', '/project')
  config.add_view(get_project, route_name='get_project', renderer='json')

  config.add_route('about', '/about')
  config.add_view(about, route_name='about')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)


  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()