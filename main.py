import requests
import smtplib
from bs4 import BeautifulSoup

my_email = 'YOUR_EMAIL'
my_password = 'YOUR_PASSWORD'

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
res = requests.get(url=url)

soup = BeautifulSoup(res.text, "html.parser")
product_name = soup.select_one(
    ".product-title-word-break").get_text().split(",")[0].lstrip(" ")
product_price = soup.select_one(".a-offscreen").get_text().split("$")[1]

print(product_name)
print(float(product_price))


if float(product_price) < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Price for {product_name}\n\nThe current price for {product_name} is only {product_price}$")
