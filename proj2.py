#proj2.py
import requests
from bs4 import BeautifulSoup

# #### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

# ### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

title_lst = []
for story_heading in soup.find_all(class_="story-heading"): 
	if story_heading.a: 
		title_lst.append((story_heading.a.text.replace("\n", " ").strip()))
	else: 
		title_lst.append((story_heading.contents[0].strip()))
for t in title_lst[:10]:
	print(t)

# for tag in soup.find_all(class_="story-heading"):
# 	print(tag.get_text().replace("\n"," ").strip())


# #### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url2 =  'https://www.michigandaily.com/'
r2 = requests.get(base_url2)
soup2 = BeautifulSoup(r2.text, 'html.parser')

for mostread in soup2.find_all(class_="view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266"):
	print(mostread.get_text())


# #### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url3 =  'http://newmantaylor.com/gallery.html'
r3 = requests.get(base_url3)
soup3 = BeautifulSoup(r3.text, 'html.parser')

for img in soup3.find_all("img"):
	if img.get('alt') != None:
		print (img.get('alt'))
	else:
		print("No alternative text provided!")


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here

# staff_list = []
# for div in soup4.find_all('div', attrs={'class':'field field-name-title field-type-ds field-label-hidden'}):
# 	staff_list.append(div.find('h2').text)
# print(staff_list)
	
# lst = [list(x) for x in zip(staff_list, email_list)]
# for tup in lst:
# 	counter +=1
# 	print(counter, tup[0], tup[1]) 

base = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
email_list=[]
counter = 0
def get_email(base, page):
	base_url = base + page
	request = requests.get(base_url, headers={'User-Agent':'SI_CLASS'})
	soup = BeautifulSoup(request.text, 'html.parser')
	node_list =[]
	for div in soup.find_all('div', attrs={'class':'field field-name-contact-details field-type-ds field-label-hidden'}):
		node_list.append(div.find('a')['href'])
	
	for node in node_list:
		u = "https://www.si.umich.edu" + str(node)
		r = requests.get(u, headers={'User-Agent': 'SI_CLASS'})
		s = BeautifulSoup(r.text, 'html.parser')
		for link in s.find_all('a'):
			link = link.get('href')
			if '@' in link:
				email_list.append(link[7:])	

page_lst = ['', '&page=1', '&page=2', '&page=3', '&page=4', '&page=5']

for page in page_lst:
	get_email(base,page)
for email in email_list:
	counter +=1
	print(counter, email)












