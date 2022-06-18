import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# list
endpoints = []

# range()
for i in range(0, 130):
    url = "https://pharmeasy.in/online-medicine-order/browse?alphabet=e&page=" + str(i)
    res = requests.get(url).content
    soup = BeautifulSoup(res, "html.parser")

    for link in soup.find_all('a', href=True, attrs={'class': 'heILj'}):
        result = (link.get('href'))

        endpoints.append(result)
print(endpoints)
append_str = "http://pharmeasy.in"
final_link = [append_str + sub for sub in endpoints]
print(final_link)
df = pd.DataFrame(final_link)
print(df)
df.to_csv(r'D:\Excel-Work\links.csv')

# D:\Excel Work
