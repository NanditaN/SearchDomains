from google import search

#This method gets the list of the URLs obtained from the search results of Google
def search_for_domain(company_name, no_of_results):
    search_results =[]
    for url in search_google(company_name, no_of_results):
        search_results.append(strip_url(url));
    short_list=[]
    for url in search_results:
        if match_me(company_name.lower(),url):
            short_list.append(url)
    return short_list

#This method uses the BeautifulSoup library behind the scenes to extract the data related to a particular search query
def search_google(company_name, no_of_results):
    return search(company_name, stop = no_of_results);
    """test_list = ['http://www.gurutechnologies.co.in/',
    'http://www.guru-technology.co.in/',
    'http://www.gurutechindia.com/',
    'http://www.gurutechindia.com/contact.htm',
    'http://www.gurutechnologies.net/',
    'http://www.justdial.com/Delhi-NCR/Guru-Technologies-India-Pvt-Ltd-%3Cnear%3E-Sec64-Distt-Gautam-Budh-Ngr/011P1741167_BZDET',
    'http://www.indiamart.com/maaguru-technology/',
    'https://www.getguru.com/',
    'http://brainguru.in/',
    'http://brainguru.in/career.html',
    'http://www.gurutech.ca/',
    'http://www.naukri.com/guru-technologies-recruiters',
    'http://www.yelp.com/biz/guru-technologies-brenham-6',
    'http://www.innogurutechnologies.com/',
    'http://www.innogurutechnologies.com/about-us.html',
    'https://www.facebook.com/public/Guru-Technologies-Inc',
    'https://www.facebook.com/hitechguru/',
    'http://www.tradeindia.com/Seller-351539-GURU-TECHNOLOGY-SERVICES/',
    'http://www.indeed.co.in/Guru-Technologies-jobs',
    'https://local.yahoo.com/info-89202226-guru-technologies-brenham']"""
    
    #print(test_list)
    #return test_list;
    

#This method takes the search query as an input from the user and sends it for further processing to the method search_for_domain
def get_input(no_of_results):
    company_name = input("Enter company name: ")
    return search_for_domain(company_name, no_of_results);
    

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
def remove_duplicates(list_r):
    return list(set(list_r))


#This method narrows down to the least number of possible matched in the list
def match_me(company_name,url):
    #extract host name from url
    host=extract_host_name(url)
    name_list = company_name.split()
    for i in name_list:
        if i in host:
            return True
    return False
#This method will only extract the host name from the URL        
def extract_host_name(url):
    #www.abc.com -> abc.com
    if url.startswith('www'):
        for i in range(0,len(url)):
            if url[i]==".":
                url_1=url[i+1:]
                break
    else:
        url_1=url
        
    #abc.com -> abc
    for j in range(0,len(url_1)):
        if url_1[j]==".":
            url_host = url_1[:j]
            return url_host

#prints the top n most relevant results
no_of_results = 20
print(remove_duplicates(get_input(no_of_results)));

#print(get_input());
