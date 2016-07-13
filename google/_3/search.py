from google import search
import urllib.request
from bs4 import BeautifulSoup

#This method will strip http://www.abc.com/contact us to http://www.abc.com/ to hit the URL and get title
def strip_to_homepage(url):
    url_homepage=url
    l=len(url)
    for i in range (l-2,1,-1):
        if url[i] == "/" and url[i-1]!="/" and url[i+1]!="/":
            url_homepage = url[0:i]
    return strip_to_website(url_homepage)

#To print the websites
def strip_to_homepage2(url):
    url_homepage=url
    l=len(url)
    for i in range (l-2,1,-1):
        if url[i] == "/" and url[i-1]!="/" and url[i+1]!="/":
            url_homepage = url[0:i]
    return url_homepage


#This method will strip http://www.abc.com/ to www.abc.com for dispay purpose
def strip_to_website(url_homepage):
    for i in range(0,len(url_homepage)-1):
            if url_homepage[i]=="/" and url_homepage[i+1]=="/":
                website=url_homepage[i+2:]
                return(strip_to_host(website))
            
#This method will strip website to hostname for comparison purpose: www.abc.com to abc
def strip_to_host(website):
    if website.startswith('www'):
        for i in range(0,len(website)):
            if website[i]==".":
                hostname_1=website[i+1:]
                break
            
    else:
        hostname_1=website
    #abc.com -> abc
    hostname_r = hostname_1[::-1]
    for j in range(0,len(hostname_r)):
        if hostname_r[j]==".":
            url_host_r = hostname_r[j+1:]
            url_host=url_host_r[::-1]
            return url_host
        
#This method is used to remove duplicates from a list
def remove_duplicates(list_x):
    return list(set(list_x))

#This method will return the title of the webpage
def get_title(url):
    try:
        page = urllib.request.urlopen(url)
        page_data = page.read()
        soup = BeautifulSoup(page_data, "html.parser")
        if not soup:
            return "dummy"
        return soup.title.string.lower();
    except:
        return "Unable to get the title"
   

#This method will match the company name and host name and give appropriate URLs as result
def host_name_match(list_1,company_name):
    final_list=[]
    name_list = company_name.split()
    for url in list_1:
        for i in name_list:
            if i.lower() in strip_to_homepage(url):
                #if company_name.lower() in get_title(strip_to_homepage2(url)):
                final_list.append(strip_to_homepage2(url))
    print(remove_duplicates(final_list))


#This method uses the BeautifulSoup library behind the scenes to extract the data related to a particular search query
def search_google(company_name, no_of_results):
    list_1=[]
    for url in search(company_name, stop = no_of_results):
    #for url in list_ip:
        list_1.append(url)
    return host_name_match(list_1,company_name)

#This method takes the search query as an input from the user and sends it for further processing to the method search_for_domain
def get_input(no_of_results):
    company_name = input("Enter company name: ")
    return search_google(company_name, no_of_results);

no_of_results = 10
get_input(no_of_results)
