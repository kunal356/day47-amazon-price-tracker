import requests
from bs4 import BeautifulSoup
import smtplib
from config import MY_PASSWORD, MY_EMAIL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9,en-GB;q=0.8',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br, zstd'
}
amazon_url = "https://www.amazon.com/Instant-Pot-Electric-Multi-Cooker-Pressure/dp/B0B4PQDFCL/ref=sr_1_1_sspa?crid=2YPCTK2W1NLQA&dib=eyJ2IjoiMSJ9.g1Lrz7oNcd8sVDvjEfcK43hdjIMppvRQyEWPpo05tT_k-YZ_pifVShNGsxsQK47WIVE57dn92fpxJ2JdGtXOKb4dnhBYMKPNHLRyjuF9tZQ-RyGcANZNana2UFSxIn4dG7-Rt1VUCxfaqTgaTm7QW6SOY-V84uoC5zmL0kZAaWRZZbZA7imAxeE5PnuHOLR7sCUKVG9o2xZSs5Jh0l09V1BJxkV5dxUzlpOgCOaGxrE.FfNUUFeFTZGOhDqzdqugNH1YyzyGcO_0tq4bC3Brf8E&dib_tag=se&keywords=instant+pot&qid=1714839750&sprefix=insta%2Caps%2C1015&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
resp = requests.get(url=amazon_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
item_name = soup.find(name="span", id="productTitle").getText()
item_name = item_name.strip().encode('utf-8')
if price < "90":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Price drop Alert!!!! \n\n{item_name} is now {price} \n{amazon_url}"
        )
