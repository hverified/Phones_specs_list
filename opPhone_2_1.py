import opPhone_1
import opPhone_2_0
import requests
import bs4

for i in range(len(opPhone_2_0.final_url_list)):
    request1 = requests.get(f"{opPhone_1.base_url}{opPhone_2_0.final_url_list[i]}")

    soup1 = bs4.BeautifulSoup(request1.content,"lxml")

    soup_li = soup1.find("div",class_="makers").find_all("li")

    No_of_phones = len(soup1.find("div",class_="makers").find_all("li"))
    phones_list = []
    
    for i in range(No_of_phones):
        if 'Android' in (soup_li[i].find("img")['title']):
            link = soup_li[i].find("a")['href']
            phones_list.append(link)
        elif 'iOS' in (soup_li[i].find("img")['title']):
            link = soup_li[i].find("a")['href']
            phones_list.append(link)
        elif 'Windows' in (soup_li[i].find("img")['title']):
            link = soup_li[i].find("a")['href']
            phones_list.append(link)
    
if __name__ == "__main__":
    print(phones_list)
