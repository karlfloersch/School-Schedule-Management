from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pymongo
import json
from pymongo import MongoClient
from bson.dbref import DBRef
client = MongoClient()

@login_required(redirect_field_name='/login')
def search_for_person_view(request):
	# """ render the create school view. TODO: add validation """
    # Display the create school view if the admin is logged in
    db = client.students
    #Display all possible people we can add by searching a name
    username = request.user.username
    # username = "punk@gmail.com"
    # Search this person
    first_name = "punk"
    last_name = "bitch"
    # find out who i am
    myself = db.students.find_one({"email":username})
    # cool i go to this cool
    school_i_go_to= myself["school"]
    # lets get all the people with this name and go to the same school as i do
    people = []
    # students_list = 
    for person in db.students.find({"$and":[{"first_name": first_name},{"last_name": last_name},{"school":school_i_go_to}]}):
        people.append(person)
    # go to this place
    # print people
    all_my_friends_complete = db.dereference(myself["friendslist"])
    # get the list itself
    all_my_friends = all_my_friends_complete["list"]
    # get all the requests assocaited with this person. Both sender or reciever 
    all_my_requests = []
    for req in db.friend_requests.find({"$or":[{"email_of_requester":username},{"email_of_emailee":username}]}):
        all_my_requests.append(req)

    if (not all_my_friends):
        # this checks if the word non is on the list remove it
        # this means you have no friends
        # now we know that we have no friends
        # this means that we cannot remove it from the list
        # lets check if we can remove from ppl already requested
        my_friendslist_id = all_my_friends_complete["_id"]
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
                    if (pe["email"] == rq["email_of_requester"] or pe["email"] == rq["email_of_emailee"]):
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
                if (pe["email"] == af["email"]):
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
                    if (pe["email"] == rq["email_of_requester"] or pe["email"] == rq["email_of_emailee"]):
                        people.remove(pe)

    # print people
    # print "success"
    html = "<html><body> string: "+"success"+"</body></html>"
    return HttpResponse(html)
@login_required(redirect_field_name='/login')
def add_a_student_to_friendslist_view(request):
	db = client.students
	username = request.user.username
	myself = db.students.find_one({"email":username})
	original_id = myself["_id"]
	first_name_to_be_inserted = "punk"
	last_name_to_be_inserted = "bitch"
	email_to_be_inserted = "punk@gmail.com"
	db.friends_list.update({"_id":original_id},{ "$push": { "list": { "first_name": first_name_to_be_inserted, "last_name": last_name_to_be_inserted, "email": email_to_be_inserted } } })
	html = "<html><body> string: "+"success"+"</body></html>"
	return HttpResponse(html)

def send_a_friend_request_view(request):
	db = client.students
	email_of_requester="billy@gmail.com"
	first_name_of_requester="billy"
	last_name_of_requester="bob"
	email_of_emailee="charles@gmail.com"
	name_of_emailee="charles"
	friend_request_info = {"email_of_requester":email_of_requester,
	"first_name_of_requester":first_name_of_requester,
	"last_name_of_requester":last_name_of_requester,
	"email_of_emailee":email_of_emailee,
	"name_of_emailee":name_of_emailee}
	db.friend_requests.insert_one(friend_request_info)


	html = "<html><body> string: "+"success"+"</body></html>"
	return HttpResponse(html)

def get_friendslist_view(request):
	db = client.students
	dat_base_var = "students"
	first_name_var = "billy"
	last_name_var = "bob"
	email_stuff = "billy@gmail.com"
	school_name= "magic school bus"
	info ={"first_name" : first_name_var,"last_name" : last_name_var, "list":[]}
	original_id =db.friends_list.insert(info)
	info2 = {"first_name" : first_name_var,"last_name" : last_name_var,"email" : email_stuff, "school" : school_name, "friendslist": DBRef(collection = "friends_list", id = original_id)}
	original_id_2=db.students.insert(info2)
	html = "<html><body> string: "+""+"</body></html>"
	return HttpResponse(html)

def add_students_to_database(request):
	db = client.students
	dat_base_var = "students"
	first_name_var = "billy"
	last_name_var = "bob"
	email_stuff = "billy@gmail.com"
	school_name= "magic school bus"
	info ={"first_name" : first_name_var,"last_name" : last_name_var, "list":[]}
	original_id =db.friends_list.insert(info)
	info2 = {"first_name" : first_name_var,"last_name" : last_name_var,"email" : email_stuff, "school" : school_name, "friendslist": DBRef(collection = "friends_list", id = original_id)}
	original_id_2=db.students.insert(info2)
	html = "<html><body> string: "+""+"</body></html>"
	return HttpResponse(html)