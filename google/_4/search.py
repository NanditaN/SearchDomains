from google import search
import urllib.request
from bs4 import BeautifulSoup

#Read the web pageand return the information asked for: title or the string that follows copyright
def get_information(src_code,info):
    if info == "title":
        if src_code.title is not None:
            if src_code.title.string is not None:
                return src_code.title.string.lower()
            else:
                return "title_unavailable";
        return "title_unavailable";
    else:
        str_1 = get_company_name_from_copyright_string(str(src_code).find(info),str(src_code)) 

        if str_1 is not None:
            return str_1

        return "no copyright information availables"
    
#Get company information that follows the copyright symbol/keyword    
def get_company_name_from_copyright_string(index_copyright,src_code_string):
    for i in range(index_copyright,len(src_code_string)):
        if src_code_string[i]=="<":
            return src_code_string[index_copyright:i]
            
#This method will strip http://www.abc.com/contact us to http://www.abc.com/ to hit the URL and get title
def strip_to_homepage(url):
    url_homepage=url
    l=len(url)
    for i in range (l-2,1,-1):
        if url[i] == "/" and url[i-1]!="/" and url[i+1]!="/":
            url_homepage = url[0:i]
    return strip_to_website(url_homepage)

#This method will strip http://www.abc.com/contact us to http://www.abc.com/ to hit the URL and get title
def strip_to_homepage_with_protocol(url):
    url_homepage=url
    url_homepage_unique=''
    l=len(url)
    for i in range (l-2,1,-1):
        if url[i] == "/" and url[i-1]!="/" and url[i+1]!="/":
            url_homepage = url[0:i]

    l1 = len(url_homepage);

    if url_homepage.endswith('/'):
        url_homepage_unique = url_homepage[0:l1-1]
    else:
        url_homepage_unique=url_homepage
    return url_homepage_unique
    #return strip_to_website(url_homepage)

#This method will strip http://www.abc.com/ to www.abc.com for dispay purpose
def strip_to_website(url_homepage):
    for i in range(0,len(url_homepage)-1):
            if url_homepage[i]=="/" and url_homepage[i+1]=="/":
                if url_homepage[len(url_homepage)-1] != "/":
                    website=url_homepage[i+2:]
                elif url_homepage[len(url_homepage)-1] == "/":
                    website=url_homepage[i+2:len(url_homepage)-1]
                #return strip_to_host(website)
                return website
            
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

#This method will match the company name and host name and give appropriate URLs as result
def host_name_match(list_1,company_name):
    final_list=[]
    second_source=[]
    name_list = company_name.split()
    for url in list_1:
        for i in name_list:
            #if "linkedin" in url or "wikipedia" in url:
            #   second_source.append(url)
            if i.lower() in strip_to_homepage(url):
                #if company_name.lower() in get_title(strip_to_homepage2(url)):
                #final_list.append(strip_to_homepage(url))
                final_list.append(strip_to_homepage_with_protocol(url))
    return remove_duplicates(final_list)

#This method uses the BeautifulSoup library behind the scenes to extract the data related to a particular search query
def search_google(company_name, no_of_results):
    list_1=[]
    for url in search(company_name, stop = no_of_results):
        list_1.append(url)
    return host_name_match(list_1,company_name)

#This method takes the search query as an input from the user and sends it for further processing to the method search_for_domain
def get_input(company_name, no_of_results):
    return search_google(company_name, no_of_results);

#This method will check if any word in the company name is present in the target_string - title or string after copyright
def check(company_name, target_string):
    company_name_list = company_name.lower().split()
    for each_name in company_name_list:
        if each_name in target_string:
            return True;

    return False;

#This method will check if the source code is encoded. If it is, then it decodes it.
def decode_page(page):
    encoding = page.info().get("Content-Encoding")    
    if encoding in ('gzip', 'x-gzip', 'deflate'):
        content = page.read()
        if encoding == 'deflate':
            data = StringIO.StringIO(zlib.decompress(content))
        else:
            try:
                data = zlib.decompress(content, 16+zlib.MAX_WBITS)
                return data;
                #data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(content))
            except:
                return None
        page = data.read()

    return page

#This method opens a URL
def get_page(url):
    try:
        return urllib.request.urlopen(url)
    except:
        return None

#This method invokes the decoder method and parses the output as HTML
def get_soup(url):
    try:
        page = get_page(url)

        page_data = decode_page(page)
        #page_data = page.read()

        soup = BeautifulSoup(page_data, "html.parser")

        if not soup:
            return None;

        return soup
    except:
        return None
    
no_of_results = 10
company_name = input("Enter company name: ")
list_1 = get_input(company_name, no_of_results)

#print(list_1);

final_list_f = [];

for url in list_1:
    src_code = get_soup(url)
    #if website doesn't return any source code, just append the URL
    if src_code is None:
        final_list_f.append(strip_to_website(url))
        continue

    title = get_information(src_code,"title")
    copyright_1 = get_information(str(src_code),"©");
    copyright_2 = get_information(str(src_code), "Copyright")
    
    #append URL to list only if the company name is present in URL or is present next to copyright.
    if check(company_name, title.lower()) and (check(company_name, copyright_1.lower()) or check(company_name, copyright_2.lower())):
        final_list_f.append(strip_to_website(url))

print(final_list_f)
