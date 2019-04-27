import requests
import bs4

base_url = "https://www.gsmarena.com/"
request = requests.get("https://www.gsmarena.com/makers.php3")
soup = bs4.BeautifulSoup(request.content, "html.parser")

soup_trs = soup.find("div",{"class":"st-text"}).find_all("tr")
No_of_trs = len(soup_trs)
links_list = []

for i in range(No_of_trs):
    
    No_of_tds = len(soup_trs[i])
    for k in range(No_of_tds-1):
        
        link = soup_trs[i].find_all("td")[k].find("a")['href']
        links_list.append(link)

if __name__ == "__main__":
	print(links_list)
