import requests
import smtplib
import pandas
from bs4 import BeautifulSoup

my_email = 'YOUR_EMAIL'
my_password = 'YOUR_PASSWORD'

data = pandas.read_csv("products.csv").to_dict()

for key, value in data["amazon_links"].items():
    url = value
    price_to_buy = data["price_to_buy"][key]
    res = requests.get(url=url)

    soup = BeautifulSoup(res.text, "html.parser")
    product_price = soup.select_one(".a-offscreen").get_text().split("$")[1]

    if float(product_price) <= price_to_buy:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject:Price for {data['product_name'][key]}\n\nThe current price for {data['product_name'][key]} is only {product_price}$")
