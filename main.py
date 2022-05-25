import requests
from bs4 import BeautifulSoup
import smtplib

def send_email(title,price,link):
    my_email="your-gmail-id"
    my_password = "your-gmail-password"

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Amazon Price Alert!\n\n{title} is now avilable at {price}.\n{link}")

# You can see your browser headers by going to this website:
# http://myhttpheader.com/

headers={
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}
product_link="https://www.amazon.com/Ninja-OL501-Pressure-SmartLid-Capacity/dp/B0995HLCQ8/ref=sr_1_6?crid=3MT6B4MJ51Z8B&keywords=pressure%2Bcooker&qid=1653198784&sprefix=pressure%2Bcooke%2Caps%2C318&sr=8-6&th=1"
response=requests.get(url=product_link,headers=headers)
# print(response.text)
amazon_web=BeautifulSoup(response.text,"html.parser")
title=amazon_web.find(name="h1",id="title").text
price=amazon_web.find(name="span",class_="priceToPay").find(name="span",class_="a-offscreen").text


if float(price.split("$")[1]) < 100:
    send_email(title.replace("\t",""),price,product_link)
