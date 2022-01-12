from src.constants_and_functions.constants import wine_links
from src.constants_and_functions.functions import scraping_links, creating_csv_file, creating_soup_object, scraping_all_characteristics, saving_to_csv

# Scraping all wine links
def files():
    links = scraping_links()
    creating_csv_file()
    print('Start scraping data!')
    print()

# Scraping wine characteristics from every single web page
def scaping():
    i = 1
    for page in wine_links:
        try:
            soup = creating_soup_object(page)
            try:
                characteristics = scraping_all_characteristics(soup)
                wine_data = saving_to_csv(characteristics)
                print('Data scraped and saved successfully!')
                print()
                print()

            except:
                print('SOMETHING WENT WRONG!')
                print()
                print()
                pass
        except:
            pass
        i = + 1

def main():
    files()
    scaping()


if __name__ == "__main__":
    main()








