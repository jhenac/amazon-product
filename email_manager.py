import smtplib
import urllib.parse
import requests

class Email():
    def __init__(self, my_email, my_password, host, port, r_email):
        self.email = my_email
        self.password = my_password
        self.host = host
        self.port = port
        self.receiver = r_email

    def send_email(self, message):
        with smtplib.SMTP(self.host, self.port) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.receiver,
                                msg=message
                                )

    def url_shortener(self, link, key):
        key = key
        url = urllib.parse.quote(link)
        response = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(key, url))
        short_url = response.json()["url"]["shortLink"]
        return short_url