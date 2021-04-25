# Sending Emails(Gmail) With Python

## **Steps to follow:**
  * Allow google to log in via smtplib
    * In a nutshell, google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to         this link while you're logged in to your google account, and allow the access:
      [https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps)
  * Create virtual environment
      ```javascript
    python3 -m venv venv
    ```
  * Activate virtualenv
    ```javascript
    source venv/bin/activate
    ```
  * Install requirements
    ```javascript
    pip3 install > r.txt
    ```
  * Change your account credentials and other details in Constants Class
    ```javascript
    self._from_address = "youremail@gmail.com"
    self._email_subject = "Automated email with Python"
    self._email_body = "Hi, This is an automated mail. Please do ot reply."
    self._email_password = "yourpassword"
    self._to_address = ["youremail2@gmail.com","youremail3@gmail.com"]
    ```
  * Email scheduling:
    ```javascript
    def schedule(self,sch):
    project = self._project
    while True:
      try:
        now = datetime.now()
        if now.hour==int(sch.split(':')[0]) and now.minute==int(sch.split(':')[1]):
          time.sleep(3)
          self.runServer()
        time.sleep(30)
      except Exception as e:
        print(e)
        time.sleep(100)
    ```
    * Above method can be used for email scheduling.
  * Execute the code
    ```javascript
    python3 send_email.py 19:34
    ```
    * Here 19:34 is the time when you want to schedule your mail
    
