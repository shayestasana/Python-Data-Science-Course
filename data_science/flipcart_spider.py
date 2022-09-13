from dputils import scrape

#step 1.  get the data as soup obj
#step 2.  create the setup dictionaries  (most important)
#step 3.  pass the dictionaries into the extract_many() function
#step 4.  repeat step 1 to step 3 until data keep coming
#step 5.  check and save data into a file.

# understanding the url:  after the question mark--> url parameters
#url = 'https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=a3ccb2e9-70ce-4887-babe-e25f7474a665&page=7'
#print(url.split('?')[-1].split('&'))




from dputils import scrape
import pandas as pd

# step 1. get the data as soup obj
# step 2. create the setup dictionaries (most important)
# step 3. pass the dictionaries into the extract_many() function
# step 4. repeat step 1 to step 3 until data keep coming
# step 5. check and save data into a file.

def getdata(q):
    
    t = {'tag':'div', 'attrs':{'class':'_1YokD2 _3Mn1Gg'}}
    rep_items = {'tag':'div', 'attrs':{'class':'_1AtVbE col-12-12'}}
    title = {'tag':'div', 'attrs':{'class':'_4rR01T'}}
    price = {'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
    link = {'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}
    
    pos = 1
    all_data = []
    while True:
        url = f'https://www.flipkart.com/search?q={q}&page={pos}'
        print(url)
        soup = scrape.get_webpage_data(url)    #bewaqoof banane ke liye dusri website ko that u r using a browser not a code
        data = scrape.extract_many( soup, target=t, items=rep_items,title=title,price=price, link=link )
        if isinstance(data, list):
            if len(data) > 0:
                pos += 1
                all_data.extend(data)
            else:
                break
        else:
            break
    return all_data


# use
laptops = getdata('laptops')
pd.DataFrame(laptops).to_csv('laptop_data.csv')