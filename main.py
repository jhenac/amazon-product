###############Web Scraping###############################################
from amazon_details import Amazon

amazon_url = "https://www.amazon.com/TCL-Class-720p-Smart-Roku/dp/B09YWT3P5Q/ref=sr_1_4?crid=1W3HPYTLCO930&keywords=tv&qid=1667902931&sprefix=tv%2Caps%2C348&sr=8-4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-PH,en-US;q=0.9,en;q=0.8",
}

amazon_scraper = Amazon(url=amazon_url, headers=headers)
price = amazon_scraper.get_amazon_price()
product_title = amazon_scraper.get_product_title()

#######################Automated Email################################
import os
from email_manager import Email

my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]
outlook_host = "smtp.office365.com"
port = "587"
receiver_email = os.environ["RECEIVER_EMAIL"]
cutt_api_key = os.environ["CUTT_API_KEY"]
long_link = "https://www.amazon.com/TCL-Class-720p-Smart-Roku/dp/B09YWT3P5Q/ref=sr_1_4?crid=1W3HPYTLCO930&keywords=tv&qid=1667902931&sprefix=tv%2Caps%2C348&sr=8-4"

email_notif = Email(my_email=my_email, my_password=my_password,host=outlook_host,port=port,r_email=receiver_email)

if price < 150:
    link = email_notif.url_shortener(link=long_link, key=cutt_api_key)
    message = f"Subject:Amazon Price Alert!\n\n{product_title} now ${price} only.\n{link}"
    email_notif.send_email(message=message)