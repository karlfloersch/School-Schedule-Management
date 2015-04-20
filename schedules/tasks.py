from __future__ import absolute_import
from celery import task
from celery import Celery
from celery import app
import pymongo
import json
from bson import json_util
from pymongo import MongoClient
from bson.dbref import DBRef
from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.read_preferences import ReadPreference

#client = MongoClient()
client = MongoReplicaSetClient('localhost:27017,localhost:27018,localhost:27019', replicaSet='socsDBset')
client.readPreference = 'primaryPreferred'


@task(bind=True)
def add_students_to_database_two(self, data):
	db = client.students
	students_temp = db.students
	friends_list = db.friends_list

	first_name_var = data['first_name']
	last_name_var = data['last_name']
	email_stuff = data['email']
	school_name= data['school']
	friend_info_dict = {'first_name': first_name_var, 'last_name': last_name_var, 'list':[]}
	id_1 = friends_list.insert_one(friend_info_dict)

	student_dict = {'first_name': first_name_var,'last_name': last_name_var, 'email': email_stuff, 'school': school_name, 'friendslist': DBRef('friends_list', friend_info_dict[ "_id"])}
	print (student_dict)
	id_2 = students_temp.insert_one(student_dict)

	return str(student_dict)


@task(bind=True)
def search_for_student(self, username, first_name, last_name):
	# """ render the create school view. """
    # Display the create school view if the admin is logged in
    print(first_name + " " + last_name + " " + username)
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    db = client.students
    students_temp = db.students
    friend_requests = db.friend_requests
    friends_list = db.friends_list
    #Display all possible people we can add by searching a name
    #username = name
    # Search this person
    #first_name = first_name
    #last_name = last_name
    print(first_name + " " + last_name + " " + username)
    # find out who i am
    myself = students_temp.find_one({'email':username})
    print(myself)
    # cool i go to this cool
    school_i_go_to= myself['school']
    # lets get all the people with this name and go to the same school as i do
    people = []
    # students_list =
    for person in students_temp.find({'$and':[{'first_name': first_name},{'last_name': last_name},{'school':school_i_go_to}]}):
	    #people_dict = {'first_name': first_name_var,'last_name': last_name_var, 'email': email_stuff, 'school': school_name, 'friendslist': DBRef('friends_list', friend_info_dict[ "_id"])}
        person['friendslist'] = json.dumps(str(person['friendslist']))
        person['_id'] = str(person['_id'])
        print(person)
        people.append(person)
    # go to this place
    # print people
    all_my_friends_complete = friends_list.find_one(myself['friendslist'])
    #all_my_friends_complete = DBRef('friends_list', friend_info_dict["_id"])
    # get the list itself
    all_my_friends = None
    if all_my_friends_complete:
        all_my_friends = all_my_friends_complete['list']
    # get all the requests assocaited with this person. Both sender or reciever
    all_my_requests = []
    for req in friend_requests.find({'$or':[{'email_of_requester':username},{'email_of_emailee':username}]}):
        all_my_requests.append(req)

    if (not all_my_friends):
        # this checks if the word non is on the list remove it
        # this means you have no friends
        # now we know that we have no friends
        # this means that we cannot remove it from the list
        # lets check if we can remove from ppl already requested
        #my_friendslist_id = all_my_friends_complete['_id']
        # print my_friendslist_id
        # db.friends_list.update( { "_id": my_friendslist_id }, { "$pop": { "list": -1 } } ))
        # print all_my_requests
        if (not all_my_requests or len(all_my_requests)==0):
            # well shit there are no requests either
            # nothing we can do show everything
            x = ""
        else:
            x = ""
            # we must people - all_my_requests
            for pe in people:
                # print str(pe) + "\n"
                for rq in all_my_friends:
                    # print str(rq)+"\n"
                    if (pe['email'] == rq['email_of_requester'] or pe['email'] == rq['email_of_emailee']):
                        people.remove(pe)

            # requests were made and need to be removed
    else:
        # you have friends do something about it
        # remove all your friends
        # print all_my_friends
        # we must people - all_my_requests
        for pe in people:
            # print str(pe) + "\n"
            for af in all_my_friends:
                # print str(af)+"\n"
                if (pe['email'] == af['email']):
                    people.remove(pe)


        if (not all_my_requests or len(all_my_requests)==0):
            # we found no current requests
            x = ""
        else:
            # we must people - all_my_requests
            for pe in people:
                # print str(pe) + "\n"
                for rq in all_my_requests:
                    # print str(rq)+"\n"
                    if (pe['email'] == rq['email_of_requester'] or pe['email'] == rq['email_of_emailee']):
                        people.remove(pe)

    # print people
    # print "success"
    #html = "<html><body> string: "+"success"+"</body></html>"
    return_dict = {'success': 'success'}
    print(people)
    return people


@task
def mul(x, y):
	# html = "<html><body> string: "+""+"</body></html>"
	# return x + y
	return x * y


@task
def xsum(numbers):
    return sum(numbers)
