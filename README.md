API endpoints
Note: use token authentication for all API

1) Login API
	POST	http://127.0.0.1:8000/api/auth/login
	post_data = {"username": "admin", "password": "123"}


2) Registration API
	POST	http://127.0.0.1:8000/api/auth/register
	post_data = {"username": "test", "email": "test@gmail.com", "password": "123", "password2": "123"}

3) Chat send to another user API
	0<=__pk__<=max user id
	POST	http://127.0.0.1:8000/api/chat/send/__pk__
	post_data = {"content": "hi how are you!"}

4) View chat of single user API
	0<=__pk__<=max user id
	GET	http://127.0.0.1:8000/api/chat/view/__pk__

5) View chat of all users API
	GET	http://127.0.0.1:8000/api/chat/users