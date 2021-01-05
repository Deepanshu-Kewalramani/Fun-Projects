import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=india'
page = requests.get(url)									#Gets the HTML code
soup = bs(page.content , 'html.parser')							#Beutifies the HTML code
results = soup.find(id='ResultsContainer')					#Extract the HTML code that has id ResultContainer as when we see the page jobs listing are present here
#print(results.prettify())
job_elems = results.find_all('section' , class_ = 'card-content')				#Every Job posting is wrapped in a tag named 'section' and class 'card-content'
specific_jobs = results.find_all('h2' , string = lambda text: 'backend' in text.lower())     #Finds specific jobs change the keyword in lambda function

#Get every jobs from here
for i in job_elems:
	#print(i , end = '\n'*2)
	title_elem = i.find('h2' , class_ = 'title')
	company_elem = i.find('div' , class_ = 'company')
	location_elem = i.find('div' , class_ = 'location')
	if None in (title_elem , company_elem , location_elem):
		continue
	print(title_elem.text.strip())
	print(company_elem.text.strip())
	print(location_elem.text.strip())
	print()

'''
#Get Specific jobs from here
for i in specific_jobs:
	link = i.find('a')['href']
	print(i.text.strip())
	print('Apply Here: {}\n'.format(link))'''
