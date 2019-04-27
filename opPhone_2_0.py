import bs4
import opPhone_1
import requests

inner_url_list = []

for k in range(len(opPhone_1.links_list)):
    inner_page = requests.get(f"{opPhone_1.base_url}{opPhone_1.links_list[k]}")
    new_soup = bs4.BeautifulSoup(inner_page.content, "html.parser")
    try:
        pages = new_soup.find("div", class_="nav-pages").find_all("a")
    except:
        pass
    for i in range(len(pages)):
        inner_url_list.append(pages[i]['href'])

final_url_list = opPhone_1.links_list+inner_url_list

if __name__ = "__main__":
    print(len(final_url_list))
