from csv import reader
from csv import writer
import requests
from bs4 import BeautifulSoup
import re

with open('D:\Excel-Work\links.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)

    for row in csv_reader:

        try:
            final_list = []

            url = row[0]
            res = requests.get(url).content
            soup = BeautifulSoup(res, "html.parser")
            try:

                name = soup.find('h1', attrs={'class': 'MedicineOverviewSection_medicineName__3D2tG'})
                medicinename = (name.text)
                final_list.append(medicinename)

            except Exception as e:
                print(e)
                final_list.append("None")

            try:

                manu = soup.find('div', attrs={'class': 'MedicineOverviewSection_brandName__YOB67'})
                manufatcure = (manu.text[3:])
                final_list.append(manufatcure)


            except Exception as e:
                print(e)
                final_list.append("None")

            try:

                size = soup.find('div', attrs={'class': 'MedicineOverviewSection_measurementUnit__RUDyf'})
                size1 = (size.text)
                final_list.append(size1)

            except Exception as e:
                print(e)
                final_list.append("None")

            try:

                price = soup.find('div', attrs={'class': 'PriceInfo_ourPrice__P1VR1'})
                price1 = (price.text[1:])
                final_list.append(price1)

            except Exception as e:
                print(e)
                final_list.append("None")

            try:

                therapy = soup.find('div', attrs={'class': 'Text_text__2lWwP'})
                therapy1 = (therapy.text)
                final_list.append(therapy1)

            except Exception as e:
                print(e)
                final_list.append("None")

            print(final_list)

            with open('D:\Excel-Work\Data.csv', 'a', encoding="utf-8", newline='') as f_obj:
                writer_obj = writer(f_obj)
                writer_obj.writerow(final_list)
                f_obj.close()

        except Exception as e:
            print(e)
