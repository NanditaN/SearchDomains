from google import search

#This method gets the list of the URLs obtained from the search results of Google
def search_for_domain(company_name, no_of_results):
    search_results =[]
    for url in search_google(company_name, no_of_results):
        search_results.append(strip_url(url));
    return search_results

#This method uses the BeautifulSoup library behind the scenes to extract the data related to a particular search query
def search_google(company_name, no_of_results):
    return search(company_name, stop = no_of_results);

#This method takes the search query as an input from the user and sends it for further processing to the method search_for_domain
def get_input():
    company_name = input("Enter company name: ")
    return search_for_domain(company_name, 10);

#This method is used to modify the URL and bringing it to the form www.abc.xyz
def strip_url(url):
    l = len(url)
    for b in range(0, l):
        if url[b] == '/' and url[b + 1] == '/':
            url_1 = url[b + 2:]
            break;

    l1 = len(url_1)
    for c in range(0, l1):
        if url_1[c] == "/":
            url_final = url_1[:c]
            return url_final

#This method is used to remove duplicates from a list
def remove_duplicates(list):
    return list(set(list))

#prints the top n most relevant results
print(remove_duplicates(get_input()));
