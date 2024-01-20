# Email OTP verification sample using Django

## Here We are going to see how we can send Email OTP using django.
  - ### Requirements - You need to setup your email in settings.py file.
      - EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
      - EMAIL_HOST = 'smtp.gmail.com'
      - EMAIL_USE_TLS = True
      - EMAIL_PORT = 587
      - EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
      - EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
  - Here I've used python-dotenv librrary to keep my secret in codebase. You can use any other one as per your requirements. You just need to follow their documentation to integrate it in your codebase.
  - How to run the code?
      - Download the code in zip format. Unzip it at specified location.
      - Create and activate the virutal environment using**py -m venv venv**, **py venv\scripts\activate**
      - install the required dependencies using pip such as *django, djangorestframework etc. python-dotenv*
      - test using Postman or browser at localhhost.
      - That's it.
  - Note - I did not create any requirements.txt file for handlinng depedencies.
