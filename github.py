import urllib
from xml.dom import minidom                                          

#USER = "ShadOoW"
#REPOSITORY = "Python-Antispam-CAPTCHA"
#URL = "http://github.com/api/v2/xml/commits/list/" + USER + "/" + REPOSITORY + "/master"

def getCommits(user="ShadOoW", repository="Python-Antispam-CAPTCHA"):
	
	url = "http://github.com/api/v2/xml/commits/list/" + user + "/" + repository + "/master"
	dom = minidom.parse(urllib.urlopen(url))  
	commitsNode = dom.firstChild
	i = 0
	node = 1
	commit =  dict()
	commits = list() 
	while i < 5:
		
		name = commitsNode.childNodes[node].childNodes[3].childNodes[1].firstChild.data
		email = commitsNode.childNodes[node].childNodes[3].childNodes[5].firstChild.data
		date = commitsNode.childNodes[node].childNodes[9].firstChild.data
		message = commitsNode.childNodes[node].childNodes[13].firstChild.data
		formated_date = datetime.strptime(date[:-6], '%Y-%m-%dT%H:%M:%S')
		i += 1
		node += 2
		
		commit = ({"name": name, "email": email, "date": formated_date, "message": message})
		commits.append(commit)

	return commits
	
def getRepInfo(repository="Python-Antispam-CAPTCHA"):
	
	url = "http://github.com/api/v2/xml/repos/search/" + repository
	dom = minidom.parse(urllib.urlopen(url))  
	repositoryNode = dom.firstChild

	name = repositoryNode.childNodes[1].childNodes[1].firstChild.data
	watchers = repositoryNode.childNodes[1].childNodes[5].firstChild.data
	language = repositoryNode.childNodes[1].childNodes[7].firstChild.data
	author = repositoryNode.childNodes[1].childNodes[9].firstChild.data
	date = repositoryNode.childNodes[1].childNodes[27].childNodes[1].firstChild.data
	description = repositoryNode.childNodes[1].childNodes[27].childNodes[7].firstChild.data
	
	formated_date = datetime.strptime(date[:-6], '%Y-%m-%dT%H:%M:%S')
	
	repInfo = ({"name": name, "watchers": watchers, "language": language, "author": author, "date": formated_date, "description": description})

	return repInfo
