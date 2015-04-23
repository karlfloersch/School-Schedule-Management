from __future__ import absolute_import
from celery import task
from celery import Celery
from celery import app
import pymongo
import json
from bson import json_util,ObjectId
from pymongo import MongoClient
# from pymongo import find_many
from bson.dbref import DBRef
from pymongo.mongo_replica_set_client import MongoReplicaSetClient
from pymongo.read_preferences import ReadPreference
# from pymongo.objectid import ObjectId  

#client = MongoClient()
client = MongoReplicaSetClient(
    'localhost:27017,localhost:27018,localhost:27019',
    replicaSet='socsDBset')
client.readPreference = 'primaryPreferred'


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@task(bind=True)
def add_students_to_database_two(self, data):
    db = client.students
    students_temp = db.students
    friends_list = db.friends_list

    first_name_var = data['first_name']
    last_name_var = data['last_name']
    email_stuff = data['email']
    school_name = data['school']
    school_address = data['address']
    friend_info_dict = {
        'first_name': first_name_var,
        'last_name': last_name_var,
        'list': []}
    id_1 = friends_list.insert_one(friend_info_dict)

    student_dict = {
        'first_name': first_name_var,
        'last_name': last_name_var,
        'email': email_stuff,
        'school': school_name,
        'address':school_address,
        'friendslist': DBRef(
            'friends_list',
            friend_info_dict["_id"])}
    print (student_dict)
    id_2 = students_temp.insert_one(student_dict)

    return str(student_dict)


# unfinshed
@task(bind=True)
def add_classes_to_database_two(self, data):
    db = client.students
    students_collection = db.students
    school_collection = db.school_list

    name= data['username']
    course_id=data['course_id']
    course_name=data['course_name']
    instructor=data['instructor']
    # data['school'] = ''
    days=data['days'] #= ['','']
    start_period=data['start_period']
    end_period=data['end_period']
    year=data['year']
    semester=data['semester']
    myself = students_temp.find_one({'email': username})
    address_of_school = myself['address']
    school_name = myself['school']
    is_new_year=data['new_year_flag']

    #the_school_info = school_collection.find_one({'name':school_name, 'address': address_of_school})
    # info doesnt exist in the schools
    # create info
    # if newyear and not already in the database
    if(is_new_year):
        # create year object

        course_list= []
        courses = []
        course_obj_ids=[]
        semester = []


    #for x in range len(name_of_semesters)
        #course_listing_and_semster += {None, name_of_semesters[x]} 

        year_obj = {'year_name':year,'num_periods_in_a_day': 0,'blocks':[],'semesters':[]}
        #school_collection.update_one({'$addToSet': {'year': year_obj}})
        


        course_list.append({'year':year, 'sem_name':semester, 'courses_held':courses})

        course_obj_ids.append(semester_courses_ref.insert_one(semester_temp).inserted_id)
        #semester.append({'semester_name': semester,'semester_courses_ref': DBRef('semester_courses_ref':ObjectId(course_obj_ids[0])}))
        semester.append({'semester_name': semester,'semester_courses_ref': str(course_obj_ids[0])})
        year_obj['semester']=semester
        # return str(course_obj_ids)
        #for index, g in enumerate(name_of_semesters):
        # for i in range(len(name_of_semesters)):
        #     semester+={'semester_name': i,'course_listing': DBRef('course_offerings',course_obj_ids[i])}
        school_collection.find_one_and_update({'name':school_name, 'address': address_of_school}, {'$addToSet': {'year': year_obj}})

    else:
        pass

    temp_school = school_collection.find_one({{'name':school_name, 'address': address_of_school}})
    year_sem = None
    current_semester = None

    for y in temp_school['year']:
        if year == y['year_name']:
            year_sem = y
            break

    for s in year_sem['semesters']:
        if semester == s['semester_name']:
            current_semester = s

    deference(s['semester_courses_ref'])



    return

@task(bind=True)
def send_a_friend_request_two(self,data):
    db = client.students
    email_of_requester = data['email_of_sender']
    first_name_of_requester = data['first_name_emailer']
    last_name_of_requester = data['last_name']
    email_of_emailee = data['email_of_sendee']
    first_name_of_emailee = data['first_name_emailee']
    last_name_of_emailee = data['last_name_emailee']

    friend_request_info = {"email_of_requester": email_of_requester,
                           "first_name_of_requester": first_name_of_requester,
                           "last_name_of_requester": last_name_of_requester,
                           "email_of_emailee": email_of_emailee,
                           "first_of_emailee": first_name_of_emailee,
                           'last_name_emailee':last_name_of_emailee}
    db.friend_requests.insert_one(friend_request_info)

@task(bind=True)
def get_friends_list_two(self,data):
    db = client.students
    # dat_base_var = "students"
    # first_name_var = data['first_name']
    # last_name_var = data['last_name']
    email_stuff = data['email']
    
    # original_id_2=db.students.insert(info2)
    value = db.students.find_one({'email':email_stuff})
    friends_loc = str(value['friendslist'])

    friends_loc = friends_loc.split(",",1)
    friends_loc = friends_loc[1]
    friends_loc = friends_loc.split("'",2)
    friends_loc = friends_loc[1]
    # friends_loc = friends_loc.split("'",1)
    # friends_loc = friends_loc[:-1]
    # friends_loc = friends_loc[1:]
    print(friends_loc)
    list_of_stuff= db.friends_list.find_one({'_id':ObjectId(friends_loc)})
    print(list_of_stuff)
    list_of_stuff= list_of_stuff['list']
    print(list_of_stuff)
    # html = "<html><body> string: "+""+"</body></html>"
    # print(list_of_stuff)
    return list_of_stuff




#dont use this yet
@task(bind=True)
def get_schools_address_two(self):

    db = client.students
    school_collection = db.school_list
    name_of_school = data['school_name']
    address_of_school = data['address']
    schools = school_collection.find_one({'name':name_of_school, 'address': address_of_school})
    # schools = school_collection.find({'name':name_of_school, 'address': address_of_school})
    array_of_schools=[]
    for cus in schools:
        # my_values['name'] = cus['name']
        # cus['_id']= JSONEncoder().encode(cus['_id'])
        array_of_schools.append(cus)


    # return_bundle = {'result': array_of_schools}
    return json_util.dumps(array_of_schools)


   



#unfinished
@task(bind=True)
def delete_school_from_database_two(self, data):
    # not done
    db = client.students
    school_collection = db.school_list
    return str(student_dict)


@task(bind=True)
def search_all_students_two(self):
    db = client.students
    student_collection = db.students
    students = student_collection.find({})
    array_of_students=[]
    for stud in students:
        array_of_students.append(stud)

    return json_util.dumps(array_of_students)


@task(bind=True)
def search_school_from_database_two(self, data):
    db = client.students
    school_collection = db.school_list
    name_of_school = data['school_name']
    schools = school_collection.find({'name':name_of_school})
    array_of_schools=[]
    for cus in schools:
        # my_values['name'] = cus['name']
        # cus['_id']= JSONEncoder().encode(cus['_id'])
        array_of_schools.append(cus)


    # return_bundle = {'result': array_of_schools}
    return json_util.dumps(array_of_schools)
    # return array_of_schools


@task(bind=True)
def add_school_to_database_two(self, data):
    db = client.students
    school_collection = db.school_list
    semester_courses_ref = db.semester_courses_ref
    #data= {'name':name_of_school, 'num_days':days_in_a_year, 'num_sem':number_of_sem, 'address':address, 'num_days_in_schedule':num_days_in_a_schedule, 'year_obj':year}
    name_of_school = data['name']
    days_in_a_year = data['num_days']
    address = data['address']
    semesters_in_year= data['num_sem']
    num_days_in_a_schedule=data['num_days_in_schedule'] 
    #num_periods_in_a_day=data['periodInADay']
    #dictionary {nameofsemester}
    name_of_semesters=data['semester_names']
    #must be bundled with year
    #dictionary
    # lunch_periods = data['luch_periods']
    # legal_blocks = data['legal_blocks']
    year = data['year_obj']
    year_container = []


    semester = []
    courses = []
    course_list =[]
    course_obj_ids=[]
    course_name_id_tuple=[]
    for current_sem_name in name_of_semesters:
        course_list.append({'year':year['year_name'], 'sem_name':current_sem_name, 'courses_held':courses})

    for semester_temp in course_list:
        course_obj_ids.append(semester_courses_ref.insert_one(semester_temp).inserted_id)

    # print (type(course_obj_ids[0]))
    # print(str(course_obj_ids[0]))
    
    # return str(course_obj_ids)

    #for index, g in enumerate(name_of_semesters):
    # for i in range(len(name_of_semesters)):
    #     semester+={'semester_name': i,'course_listing': DBRef('course_offerings',course_obj_ids[i])}
    for index ,g in enumerate(name_of_semesters):
        semester.append({'semester_name': g,'semester_courses_ref': str(course_obj_ids[index])})
        #some_val = db.dereference(semester[index])

    year['semesters'] = semester
    year_container.append(year)

    data_input = {'name':name_of_school, 'days_in_a_year': days_in_a_year,
     'address':address, 'semesters_in_year':semesters_in_year,
     'num_days_in_a_schedule':num_days_in_a_schedule,'name_of_semesters':name_of_semesters,
     'year':year_container
     }
    id_1 = school_collection.insert_one(data_input)

    return



@task(bind = True)
def accept_friend_request_two(self, data):
    db = client.students




@task(bind = True)
def get_friend_request_two(self, data):
    db = client.students
    email = data['email_of_sendee']
    first_name= data['first_name_emailee']
    last_name = data['last_name_emailee']

    # "email_of_emailee" : "cheap@gmail.com",
    # "last_name_emailee" : "will",
    # "first_of_emailee" : "cheap",


    friend_requests = db.friend_requests
    result = friend_requests.find({'email_of_emailee':email})
    # print(result['email_of_requester'])
    allRequests= []

    for req in result:
        # print(result)
        allRequests.append(req)

        # print("returned")

    return json_util.dumps(allRequests)



@task(bind=True)
def possible_friends(self, username, first_name):
    # """ render the create school view. """
    # Display the create school view if the admin is logged in
    db = client.students
    students_temp = db.students
    friend_requests = db.friend_requests
    friends_list = db.friends_list
    # Display all possible people we can add by searching a name
    #username = name
    # Search this person
    #first_name = first_name
    #last_name = last_name
    # find out who i am
    myself = students_temp.find_one({'email': username})
    print(myself)
    # cool i go to this cool
    school_i_go_to = myself['school']
    # lets get all the people with this name and go to the same school as i do
    people = []
    # students_list =
    for person in students_temp.find({'$and': [{'first_name': first_name}, {'school': school_i_go_to}]}):
            #people_dict = {'first_name': first_name_var,'last_name': last_name_var, 'email': email_stuff, 'school': school_name, 'friendslist': DBRef('friends_list', friend_info_dict[ "_id"])}
        # person['friendslist'] = json.dumps(str(person['friendslist']))
        # person['_id'] = str(person['_id'])
        del person['friendslist']
        del person['_id']
        del person['school']
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
    for req in friend_requests.find({'$or': [{'email_of_requester': username}, {'email_of_emailee': username}]}):
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
        if (not all_my_requests or len(all_my_requests) == 0):
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

        if (not all_my_requests or len(all_my_requests) == 0):
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
    # html = "<html><body> string: "+"success"+"</body></html>"
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
