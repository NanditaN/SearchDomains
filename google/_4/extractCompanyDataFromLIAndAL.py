import urllib.request;
from bs4 import BeautifulSoup;

# extracting the source code of a webpage
def get_company_information(url):
    try:
        page = urllib.request.urlopen(url)

        page_data = page.read()
        soup = BeautifulSoup(page_data, "html.parser")

        if not soup:
            return "Nothing could be extracted"
        
        return soup.prettify()

        """
        all_links = soup.find_all('a')

        for link in all_links:
            link_individual = link.get('href', None)
            if link_individual is not None:
                print(link)
        """
        
        #return "something"
        
    except:
        return "Some exception occured"

url_list = ["https://en.wikipedia.org/wiki/P.E.S._Institute_of_Technology,_Bangalore_South_Campus"
            , "https://www.linkedin.com/company/siftery"
            , "https://angel.co/siftery"];

for url in url_list:
    print(get_company_information(url))
    print("+++++++++++++++++++++++++++++++");
