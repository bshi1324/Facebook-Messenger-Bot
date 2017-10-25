from fbchat import Client
from fbchat.models import *
from getpass import getpass
import facebook


def send_message():
	people = get_member_list()
	
	username = raw_input("Username: ")
	client = Client(username, getpass())
	
	message = raw_input('Type your message: ')
	
	for person in people:
		users = client.searchForUsers(person)
		user = users[0]
		
		client.send(Message(text=message), thread_id=user.uid, thread_type=ThreadType.USER)
		print 'Message to {} sent!'.format(person)

		
def get_member_list():
	gid = group_checker

	result = graph.get_object(id=gid,fields='members')
	members_data = result['members']['data']
	members = [info['name'] for info in members_data]
	
	return members

	
def group_checker():
	index = int(raw_input('Enter the number of the correct group: '))
	try:
		id = relevant_groups[index]['id']
	except:
		print 'Enter a valid number.'
		group_checker()
	
	return id

	
token = raw_input('Token: ')
group = raw_input('Group: ')
print '\n'

graph = facebook.GraphAPI(access_token=token,version='2.10')


results = graph.search(type='group',q=group)
relevant_groups = results['data']


lst_group = [group['name'] for group in relevant_groups]
x = 0
for group_name in lst_group:
	print str(x) + ' ' +  group_name
	x += 1
	
print '\n'

group_checker()
	

