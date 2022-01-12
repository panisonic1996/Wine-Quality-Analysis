from bs4 import BeautifulSoup
import requests
import re
from csv import DictWriter
from PIL import Image, ImageEnhance
import easyocr
import pandas as pd
import os
from src.constants_and_functions.constants import headers, wine_page, page_number, image_folder, data_raw_folder, data_additional_folder, wine_links

def scraping_links():
   for x in range(1, page_number):
      r = requests.get(f'{wine_page}page/{x}/', headers)
      soup = BeautifulSoup(r.content, 'html.parser')
      #Scraping links of every single wine page
      wine_list = soup.find_all('h1', {'class': 'entry-title'})
      for i in wine_list:
         for link in i.find_all('a', href=True):
            wine_links.append(link['href'])
   print(f"{len(wine_links)} links are found!")
   os.chdir(data_additional_folder)
   links_file = pd.DataFrame(wine_links)
   links_file.to_csv("Links list.csv", index=False)
   print('File created!')


def creating_csv_file():
    os.chdir(data_raw_folder)
    wine_file = [
        'Name',
        'Rating',
        'Color',
        'Intensity',
        'Aroma',
        'Sweetness',
        'Acidity',
        'Alcohol',
        'Tannin',
        'Balance',
        'Finish',
        'Aftertaste'
    ]
    statistics = pd.DataFrame(columns=wine_file)
    statistics.to_csv("Wine statistics (raw data)1.csv", index=False)
    print('File created!')


def creating_soup_object(page):
      r = requests.get(page, headers)
      soup = BeautifulSoup(r.content, 'html.parser')
      return soup


def scraping_name(soup):
      name = soup.find('strong').text.strip()
      return name


def scraing_rating(soup):
      paragraphs_list = []
      paragraphs = soup.find_all('p')
      for i in paragraphs:
            paragraphs_list.append(i.text.strip())
      paragraphs_text = '\n'.join(paragraphs_list)
      pattern = re.compile(r'[0-9]+[.][0-9]+')
      matches = pattern.findall(paragraphs_text)
      rating = matches[0]
      return rating


def image_downloader(soup):
    os.chdir(image_folder)
    # Opening image
    regex = re.compile('.*wp-image.*')
    images = soup.find_all('img', {"class": regex})
    image = (list(images)[1])
    link = image['src']
    image_name = image['alt']
    print(link)
    print(image_name)
    with open(image_name + '.png', 'wb') as file:
        img = requests.get(link)
        file.write(img.content)
    print('Image found and downloaded!')
    return image_name


def enhancing_image(image_name):
    filename = f'{image_folder}\\{image_name}.png'
    img_open = Image.open(filename)
    img_grayscale = img_open.convert('L')
    img_grayscale.show()
    img_1 = ImageEnhance.Contrast(img_grayscale).enhance(5)
    # Cropping Image
    x_1 = 0
    y_1 = 40
    x_2 = 650
    y_2 = 130
    crop_image = img_1.crop((x_1, y_1, x_2, y_2))
    # Resizing Image
    image_resize = crop_image.resize((2600, 450))
    # Enhancing Image
    img_contrast = ImageEnhance.Contrast(image_resize).enhance(5)
    img_sharpness = ImageEnhance.Sharpness(img_contrast).enhance(5)
    greyscale_image = img_sharpness.convert('L')
    enhanced_image = greyscale_image.save('new_image.png')
    # Text Recognition from Image
    IMAGE_PATH = 'new_image.png'
    reader = easyocr.Reader(['en'])
    results = reader.readtext(IMAGE_PATH, detail=0)
    return results


def scraping_all_characteristics(soup):
    image_name = image_downloader(soup)
    results = enhancing_image(image_name)
    characteristics = {
            'Name': scraping_name(soup),
            'Rating': scraing_rating(soup),
            'Color': results[0],
            'Intensity': results[1],
            'Aroma': results[2],
            'Sweetness': results[3],
            'Acidity': results[4],
            'Alcohol': results[5],
            'Tannin': results[6],
            'Balance': results[7],
            'Finish': results[8],
            'Aftertaste': results[9]
      }
    print(characteristics)
    return characteristics


def saving_to_csv(characteristics):
    os.chdir(data_raw_folder)
    columns = ['Name', 'Rating', 'Color', 'Intensity', 'Aroma', 'Sweetness', 'Acidity', 'Alcohol', 'Tannin', 'Balance',
               'Finish', 'Aftertaste']
    with open('Wine statistics(raw data)1.csv', 'a', encoding='utf-8') as file:
        w = DictWriter(file, fieldnames=columns)
        w.writerow(characteristics)
    return









