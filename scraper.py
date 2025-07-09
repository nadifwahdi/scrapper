from bs4 import BeautifulSoup
import argparse 
import requests
import re

# link = "https://quotes.toscrape.com/page/1/"
# r = requests.get(link)
# html_text = r.text 

# soup = BeautifulSoup(html_text, 'html.parser')
# quotes_div = soup.find_all("div", class_="quote")

# for quote_html in quotes_div:
#     quote_text_html = quote_html.find("span", class_="text")
#     quote_text = quote_text_html.get_text(separator="", strip=False)
#     quote_by_html = quote_html.find("small", class_="author")
#     print(quote_text, "\n", quote_by_html)

    

LINK = "https://quotes.toscrape.com/page/"
def scraper(from_page: str, to_page: str):
    for page in range(from_page, to_page+1):
        link = LINK + f"{page}/"
        r = requests.get(link)
        html_text = r.text 
        soup = BeautifulSoup(html_text, 'html.parser')
        quotes_div = soup.find_all("div", class_="quote")

        
        for quote_html in quotes_div:
            quote_text = quote_html.find("span", class_="text").get_text(separator="", strip=False)
            quote_by = quote_html.find("small", class_="author").get_text(separator="", strip=False)
            
            with open("quotes.txt", "a") as file:
                file.write(f"{quote_text} \n - by {quote_by} \n")
    
def main():
    parser = argparse.ArgumentParser(description="scraping website from a page to certain page")
    parser.add_argument("from_page", type=int, help="from page")
    parser.add_argument("to_page", type=int, help="to page")  
    
    args = parser.parse_args()
    
    scraper(args.from_page, args.to_page)

if __name__ == "__main__":
    main()