import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
res = requests.get(url=url)

soup = BeautifulSoup(res.text, "html.parser")
product_price = soup.select_one(".a-offscreen").get_text().split("$")[1]
