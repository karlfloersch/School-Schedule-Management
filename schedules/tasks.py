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
from operator import itemgetter
from random import randint
import bisect
import collections
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
# {u'course_id': u'cse220', u'blocks': {u'start_period': u'1', u'days': [u'M', u'W'], u'end_period': u'2'}, u'instructor': u'wong', u'course_name': u'systems', u'block_key_value': u'13'}
class DayItemSort(object):
    def __init__(self, course_id,blocks,instructor,course_name,block_key_value):
        self.course_id = course_id
        self.blocks = blocks
        self.instructor = instructor
        self.course_name= course_name
        self.block_key_value = block_key_value

    def __repr__(self):
        return '{}: {} '' {} {} {} {}'.format(self.__class__.__name__,
                                  self.course_id,
                                  self.blocks,
                                  self.instructor,
                                  self.course_name,
                                  self.block_key_value)

    def __cmp__(self, other):
        if hasattr(other, 'getKey'):
            return self.getKey().__cmp__(other.getKey())

    def getKey(self):
        return self.block_key_value

    def __getitem__(self, key):
        return self.block_key_value[key]


@task(bind = True, queue = 'read_tasks')
def create_desired_schedule(self, data):
    data = [    {
            'course_id' : "cse220",
            'blocks' : {
                'start_period' : "1",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "2"
            },
            'instructor' : "wong",
            'course_name' : "systems",
            'preferred': False
        },
        {
            'course_id' : "cse114",
            'blocks' : {
                'start_period' : "5",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "6"
            },
            'instructor' : "skiena",
            'course_name' : "intro",
            'preferred': True
        },
        {
            'course_id' : "cse110",
            'blocks' : {
                'start_period' : "5",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "6"
            },
            'instructor' : "bach",
            'course_name' : "android",
            'preferred': False
        }
    ]

    # data.append()

    db = client.students
    student_collection = db.students
    assigned_schedule = db.assigned_schedule
    email = 'peter@gmail.com'
    who_i_am =student_collection.find_one({'email':email})
    friends_loc = str(who_i_am['friendslist'])
    friends_loc = friends_loc.split(",",1)
    friends_loc = friends_loc[1]
    friends_loc = friends_loc.split("'",2)
    friends_loc = friends_loc[1]
    list_of_stuff= db.friends_list.find_one({'_id':ObjectId(friends_loc)})
    list_of_stuff= list_of_stuff['list']
    day_map= {'M':"1",'Tu':"2",'W':"3",'Th':"4",'F':"5",'S':"6",'Su':"7"}
    # num_friends_in_classes_hash = {}
    friends_overlap = []
    course_hash_map={}
    current_blocks =[]
    sort_day_value = ""

    for courses_in_data in data:
        # course_hash_map[courses_in_data['course_name']] = 0
        courses_in_data['count'] = 0

    for fr in list_of_stuff:
        assigned_schedule_friends =assigned_schedule.find_one({'email':fr['email']})
        friends_class_array = assigned_schedule_friends['classes']
        for classes in data:
            for fclasses in friends_class_array:
                if  fclasses['course_name']==classes['course_name'] and fclasses['instructor']== classes['instructor'] and fclasses['course_id']==classes['course_id']:
                    classes['count']=classes['count']+1

    for classes in data:
        current_blocks = classes['blocks']
        for day in current_blocks['days']:
            sort_day_value = sort_day_value + day_map[day]
        classes['block_key_value'] = sort_day_value
        classes['dif'] = int(current_blocks['end_period'])- int(current_blocks['start_period'])
        sort_day_value = ""

    for da in data:
        da['weight'] = 0.01
        if da['preferred']== True:
            da['weight'] = da['weight']+.6
        da['weight'] =  (da['count'] *.1) + da['weight']

    new_list = sorted(data, key=itemgetter('block_key_value', 'dif'))

    start = []
    finish = []
    for datas in new_list:
        this_block = datas['blocks']
        start.append(this_block['start_period'])
        finish.append(this_block['end_period'])

    p = []
    for j in xrange(len(new_list)):
        i = bisect.bisect_right(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        p.append(i)

    OPT = collections.defaultdict(int)
    OPT[-1] = 0
    OPT[0] = 0
    for j in xrange(1, len(new_list)):
        dats = new_list[j]
        print(dats)
        OPT[j] = max(dats['weight'] + OPT[p[j]], OPT[j - 1])

    # given OPT and p, find actual solution intervals in O(n)
    O = []
    def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            dats = new_list[j]
            if dats['weight'] + OPT[p[j]] > OPT[j - 1]:
                O.append(new_list[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(new_list) - 1)

    return O

@task(bind=True, queue='read_tasks')
def find_school_two(self, data):
    db = client.students
    school_collection = db.school_list
    student_collection = db.students
    student =student_collection.find_one({'email':data['email']})
    student_school = student['school']
    student_school_address = student['address']
    print("PPOOOOOOOOOOOOOOOOOOOOOODLE")
    print(student_school)
    print(student_school_address)
    target = school_collection.find_one( { '$and': [ { 'name': student_school }, { 'address': student_school_address } ] })
    del target['_id']
    return json_util.dumps(target)


@task(bind=True, queue='read_tasks')
def get_overlapping_friends_by_specific_course_two(self, data):
    db = client.students
    assigned_schedule = db.assigned_schedule
    email = data['email']
    target = data['target']
    # name = data['course_name']
    # start_period = data['start_period']
    # end_period = data['end_period']
    # course_id = data['course_id']
    # instructor = data['instructor']
    # print(email)
    assigned_schedule_return =assigned_schedule.find_one({'email':email})
    assigned_schedule_friends =assigned_schedule.find_one({'email':target})
        # "classes" : [
        # {
        #     "course_name" : "wongs time",
        #     "start_period" : "1",
        #     "days" : [
        #         "tu"
        #     ],
        #     "end_period" : "2",
        #     "course_id" : "cse220",
        #     "instructor" : "wong"
        # },
    return_list={}
    course_list=[]
    class_array = assigned_schedule_return['classes']
    friends_class_array = assigned_schedule_friends['classes']
    return_list['friend']=target

    for classes in class_array:
        for fclasses in friends_class_array:
            if  fclasses['course_name']==classes['course_name'] and fclasses['instructor']== classes['instructor'] and fclasses['course_id']==classes['course_id']:
                course_list.append(fclasses['course_id'])
    return_list['courses']=course_list
    return return_list


@task(bind=True, queue='write_tasks')
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

@task(bind=True, queue='write_tasks')
def remove_school(self, data):
    db = client.students
    school_collection = db.school_list
    name = data['school_name']
    address = data['school_address']
    target = school_collection.find_one_and_delete( { '$and': [ { 'name': name }, { 'address': address } ] })
    #school_collection.remove(target.id)
    return str(target)

@task(bind = True, queue = 'read_tasks')
def create_desired_schedule(self, data):
    data = [    {
            'course_id' : "cse220",
            'blocks' : {
                'start_period' : "1",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "2"
            },
            'instructor' : "wong",
            'course_name' : "systems",
            'preferred': False
        },
        {
            'course_id' : "cse114",
            'blocks' : {
                'start_period' : "5",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "6"
            },
            'instructor' : "skiena",
            'course_name' : "intro",
            'preferred': True
        },
        {
            'course_id' : "cse110",
            'blocks' : {
                'start_period' : "5",
                'days' : [
                    "M",
                    "W"
                ],
                'end_period' : "6"
            },
            'instructor' : "bach",
            'course_name' : "android",
            'preferred': False
        }
    ]

    # data.append()

    db = client.students
    student_collection = db.students
    assigned_schedule = db.assigned_schedule
    email = 'peter@gmail.com'
    who_i_am =student_collection.find_one({'email':email})
    friends_loc = str(who_i_am['friendslist'])
    friends_loc = friends_loc.split(",",1)
    friends_loc = friends_loc[1]
    friends_loc = friends_loc.split("'",2)
    friends_loc = friends_loc[1]
    list_of_stuff= db.friends_list.find_one({'_id':ObjectId(friends_loc)})
    list_of_stuff= list_of_stuff['list']
    day_map= {'M':"1",'Tu':"2",'W':"3",'Th':"4",'F':"5",'S':"6",'Su':"7"}
    # num_friends_in_classes_hash = {}
    friends_overlap = []
    course_hash_map={}
    current_blocks =[]
    sort_day_value = ""

    for courses_in_data in data:
        # course_hash_map[courses_in_data['course_name']] = 0
        courses_in_data['count'] = 0

    for fr in list_of_stuff:
        assigned_schedule_friends =assigned_schedule.find_one({'email':fr['email']})
        friends_class_array = assigned_schedule_friends['classes']
        for classes in data:
            for fclasses in friends_class_array:
                if  fclasses['course_name']==classes['course_name'] and fclasses['instructor']== classes['instructor'] and fclasses['course_id']==classes['course_id']:
                    classes['count']=classes['count']+1

    for classes in data:
        current_blocks = classes['blocks']
        for day in current_blocks['days']:
            sort_day_value = sort_day_value + day_map[day]
        classes['block_key_value'] = sort_day_value
        classes['dif'] = int(current_blocks['end_period'])- int(current_blocks['start_period'])
        sort_day_value = ""

    for da in data:
        da['weight'] = 0.01
        if da['preferred']== True:
            da['weight'] = da['weight']+.6
        da['weight'] =  (da['count'] *.1) + da['weight']

    new_list = sorted(data, key=itemgetter('block_key_value', 'dif'))

    start = []
    finish = []
    for datas in new_list:
        this_block = datas['blocks']
        start.append(this_block['start_period'])
        finish.append(this_block['end_period'])

    p = []
    for j in xrange(len(new_list)):
        i = bisect.bisect_right(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        p.append(i)

    OPT = collections.defaultdict(int)
    OPT[-1] = 0
    OPT[0] = 0
    for j in xrange(1, len(new_list)):
        dats = new_list[j]
        print(dats)
        OPT[j] = max(dats['weight'] + OPT[p[j]], OPT[j - 1])

    # given OPT and p, find actual solution intervals in O(n)
    O = []
    def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            dats = new_list[j]
            if dats['weight'] + OPT[p[j]] > OPT[j - 1]:
                O.append(new_list[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(new_list) - 1)

    return O


@task(bind=True, queue='write_tasks')
def remove_a_class_from_assigned_two(self, data,days_array):
    db = client.students
    assigned_schedule = db.assigned_schedule
    email = data['email']
    name = data['course_name']
    start_period = data['start_period']
    end_period = data['end_period']
    course_id = data['course_id']
    instructor = data['instructor']
    print(data)
    print(days_array)
    blocks = {}
    blocks['start_period'] = start_period
    blocks['end_period'] = end_period
    blocks['days'] = days_array
    print(" ")
    print(blocks)
    val =assigned_schedule.find_one_and_update( {'email': email, 'classes.course_name': name, 'classes.course_id':course_id,'classes.instructor':instructor},
                                                {'$pull': { 'classes': { 'course_name': name, 'course_id':course_id,'instructor':instructor}}})
    print(val)
    return json_util.dumps(val)


@task(bind = True,queue='read_tasks')
def get_course_offerings_two(self,email,year):
    db = client.students
    student_collection = db.students
    school_collection = db.school_list
    course_offerings =db.semester_courses_ref
    course_list = db.course_list
    # print(email)
    who_i_am =student_collection.find_one({'email':email})
    school_i_go_to = who_i_am['school']
    school_address = who_i_am['address']
    # print(school_i_go_to)
    my_school =school_collection.find_one({'$and': [{'address': school_address}, {'name': school_i_go_to}]})

    # year is missing
    output = []
    for yr in my_school['year']:
        if yr['year_name']== year:
            all_semesters = yr['semesters']
            for als in all_semesters:
                semester_ref = als['semester_courses_ref']
                semester_name = als['semester_name']
                course_ref_list = course_offerings.find_one({'_id':ObjectId(semester_ref)})
                courses_held = course_ref_list['courses_held']
                for cor in courses_held:
                    # prepare to trim the stuff we dont need
                    setup_course = {}
                    id_of_this_course = str(cor['course_id'])
                    print(id_of_this_course)
                    found_course = course_list.find_one({'_id':ObjectId(id_of_this_course)})
                    print(found_course)
                    setup_course['course_id'] = found_course['course_id']
                    setup_course['instructor'] = found_course['instructor']
                    setup_course['course_name']= found_course['course_name']
                    setup_course['blocks'] = found_course['blocks']
                    setup_course['semester_name']=semester_name
                    output.append(setup_course)

    return output


@task(bind = True,queue='read_tasks')
def get_course_offerings_by_semester_two(self,email,year,semester):
    db = client.students
    student_collection = db.students
    school_collection = db.school_list
    course_offerings =db.semester_courses_ref
    course_list = db.course_list
    # print(email)
    who_i_am =student_collection.find_one({'email':email})
    school_i_go_to = who_i_am['school']
    school_address = who_i_am['address']
    # print(school_i_go_to)
    my_school =school_collection.find_one({'$and': [{'address': school_address}, {'name': school_i_go_to}]})

    # year is missing
    output = []
    for yr in my_school['year']:
        if yr['year_name']== year:
            all_semesters = yr['semesters']
            for als in all_semesters:
                if als['semester_name'] == semester:
                    semester_ref = als['semester_courses_ref']
                    semester_name = als['semester_name']
                    course_ref_list = course_offerings.find_one({'_id':ObjectId(semester_ref)})
                    courses_held = course_ref_list['courses_held']
                    for cor in courses_held:
                        # prepare to trim the stuff we dont need
                        setup_course = {}
                        id_of_this_course = str(cor['course_id'])
                        print(id_of_this_course)
                        found_course = course_list.find_one({'_id':ObjectId(id_of_this_course)})
                        print(found_course)
                        setup_course['course_id'] = found_course['course_id']
                        setup_course['instructor'] = found_course['instructor']
                        setup_course['course_name']= found_course['course_name']
                        setup_course['semester_name']=semester_name
                        output.append(setup_course)

    return output



@task(bind = True, queue='write_tasks')
def get_normal_schedule_two(self,data):
    db = client.students
    assigned = db.assigned_schedule
    email = data['email']
    # print(email)
    val =assigned.find_one({'email':email})
    # print(val)
    if val is None:
        return "null"
    else:
        return val['classes']


@task(bind=True, queue='read_tasks')
def add_classes_to_database_two(self, data):
    db = client.students
    students_collection = db.students
    school_collection = db.school_list
    course_list = db.course_list
    course_offerings =db.semester_courses_ref
    assigned = db.assigned_schedule

    # {'username': 't1@t1.com',
    # 'year': '2015', 'course_id': 'CSE 201',
    # 'days': ['M', 'Tu', 'W'], 'course_name': 'Comp Sci',
    # 'semester': 'Fall', 'new_year_flag': False,
    # 'instructor': 'Poodle', 'start_period': '0', 'end_period': '3'}

    username= data['username']
    course_id=data['course_id']
    course_name=data['course_name']
    instructor=data['instructor']
    # data['school'] = ''
    blocks={}
    blocks['days']=data['days']
    blocks['start_period']= data['start_period']
    blocks['end_period']= data['end_period']
    # days=data['days'] #= ['','']
    #start_period=data['start_period']
    #end_period=data['end_period']

    year=data['year']
    semester=data['semester']
    myself = students_collection.find_one({'email': username})
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

    temp_school = school_collection.find_one({'name':school_name, 'address': address_of_school})
    year_sem = None
    current_semester = None

    # print(temp_school['year'])
    for y in temp_school['year']:
        if year == y['year_name']:
            year_sem = y
            break
    # print("*******************")
    # print(year_sem)

    for s in year_sem['semesters']:
        print("*******************")
        print(semester +"=="+ s['semester_name'])
        if semester.lower() == s['semester_name'].lower():
            current_semester = s

    ref_number = current_semester['semester_courses_ref']
    # print(ref_number)


    course_data = {'course_id':course_id,'course_name':course_name,'instructor':instructor,'blocks':blocks}
    # deference(s['semester_courses_ref'])course_id=data['course_id']
    course_name=data['course_name']
    instructor=data['instructor']
    # update({}, course_data, {upsert:true})
    # id_of_course = course_list.insert_one(course_data).inserted_id
    course_list.update(course_data, course_data, True)
    id_of_inserted_course = course_list.find_one(course_data)
    # print(id_of_inserted_course)
    id_of_inserted_course = id_of_inserted_course['_id']
    # print(id_of_inserted_course)
    id_to_insert= {'course_id':ObjectId(id_of_inserted_course)}
    course_offerings.update({'_id':ObjectId(ref_number)},{ '$addToSet':  {'courses_held': id_to_insert} },True)

    # add it the schedule now
    # assigned
    # insert_into_schedule

    course_id=data['course_id']
    course_name=data['course_name']
    instructor=data['instructor']
    # data['school'] = ''
    days=data['days'] #= ['','']
    #start_period=data['start_period']
    #end_period=data['end_period']
    ##PUT BLOCK INFORMATION HERE
    set_add = {'course_id':course_id, 'course_name': course_name, 'instructor': instructor,'blocks':blocks}
    assigned.update({'email':username},{'$addToSet':{'classes':set_add}},True)

    # .inserted_id



    return

@task(bind=True, queue='write_tasks')
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

@task(bind=True, queue='read_tasks')
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
    # print(friends_loc)
    list_of_stuff= db.friends_list.find_one({'_id':ObjectId(friends_loc)})
    # print(list_of_stuff)
    list_of_stuff= list_of_stuff['list']
    print(list_of_stuff)
    # html = "<html><body> string: "+""+"</body></html>"
    # print(list_of_stuff)
    return list_of_stuff

@task(bind=True, queue='write_tasks')
def delete_a_student_from_database_two(self,email):
    db = client.students
    student_collection = db.students
    db.students.find_one_and_delete({'email':email})



@task(bind=True, queue='write_tasks')
def delete_friend_from_friends_list_two(self,data):
    db = client.students
    # self
    email_stuff = data['email']
    first_name = data['first_name']
    last_name =data['last_name']
    f_email= data['friend_email']

    value = db.students.find_one({'email':email_stuff})
    # value_two = db.students.find_one({'email':f_stuff})

    friends_loc = str(value['friendslist'])

    friends_loc = friends_loc.split(",",1)
    friends_loc = friends_loc[1]
    friends_loc = friends_loc.split("'",2)
    friends_loc = friends_loc[1]
    first_name_two=value['first_name']
    last_name_two=value['last_name']

    friend_ob = db.students.find_one({'email':f_email})

    friends_loc_two = str(friend_ob['friendslist'])
    # strip the info we dont need
    friends_loc_two = friends_loc_two.split(",",1)
    friends_loc_two = friends_loc_two[1]
    friends_loc_two = friends_loc_two.split("'",2)
    friends_loc_two = friends_loc_two[1]

    # first_name_two=friend_ob['first_name']
    # last_name_two=friend_ob['last_name']
    print(first_name_two)
    print(last_name_two)

    value_two = {'first_name':first_name,'last_name':last_name,'email':f_email}
    print(value)
    value = {'first_name':first_name_two,'last_name':last_name_two,'email':email_stuff}
    print(value_two)
    # {'$addToSet': {'year': year_obj}}
    list_of_stuff= db.friends_list.find_one_and_update({'_id':ObjectId(friends_loc_two)},{ '$pull':  {'list': value} })

    list_of_stuff= db.friends_list.find_one_and_update({'_id':ObjectId(friends_loc)},{ '$pull':  {'list': value_two} })
    # return list_of_stuff

#dont use this yet
@task(bind=True, queue='read_tasks')
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
@task(bind=True, queue='write_tasks')
def delete_school_from_database_two(self, data):
    # not done
    db = client.students
    school_collection = db.school_list
    return str(student_dict)


@task(bind=True, queue='read_tasks')
def search_all_students_two(self):
    db = client.students
    student_collection = db.students
    students = student_collection.find({})
    array_of_students=[]
    for stud in students:
        array_of_students.append(stud)

    return json_util.dumps(array_of_students)


@task(bind=True, queue='read_tasks')
def search_school_from_database_two(self, data=None):
    db = client.students
    school_collection = db.school_list
    schools = None
    if data:
        name_of_school = data['school_name']
        schools = school_collection.find({'name':name_of_school})
    else:
        schools = school_collection.find()
    array_of_schools=[]
    for cus in schools:
        # my_values['name'] = cus['name']
        # cus['_id']= JSONEncoder().encode(cus['_id'])
        array_of_schools.append(cus)


    # return_bundle = {'result': array_of_schools}
    return json_util.dumps(array_of_schools)
    # return array_of_schools


@task(bind=True, queue='write_tasks')
def edit_school_to_database_two(self, data,address_of_edit):
    db = client.students
    school_collection = db.school_list
    semester_courses_ref = db.semester_courses_ref
    #data= {'name':name_of_school, 'num_days':days_in_a_year, 'num_sem':number_of_sem, 'address':address, 'num_days_in_schedule':num_days_in_a_schedule, 'year_obj':year}
    name_of_school = data['name']
    days_in_a_year = data['num_days']
    address = data['address']
    semesters_in_year= data['num_sem']
    num_days_in_a_schedule=data['num_days_in_schedule']
    name_of_semesters=data['semester_names']
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
    school_collection.find_one_and_replace({'address':address_of_edit},data_input)

    return



@task(bind=True, queue='write_tasks')
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
    name_of_semesters=data['semester_names']
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

@task(bind = True, queue='write_tasks')
def copy_and_modify_school_two(self, data):
    pass


@task(bind = True, queue='write_tasks')
def accept_friend_request_two(self, data):
    db = client.students
    friend_requests = db.friend_requests
    student_collection = db.students
    friends_collection = db.friends_list
    emailee = data['email_of_sendee']
    emailer = data['email_of_requester']

    value=friend_requests.find_one_and_delete({'email_of_emailee':emailee, 'email_of_requester':emailer})
    sendee_first_name=value['first_of_emailee']
    sendee_last_name=value['last_name_emailee']
    sender_first_name=value['first_name_of_requester']
    sender_last_name=value['last_name_of_requester']

    sender_info = student_collection.find_one({'email':emailer})

    friends_loc = str(sender_info['friendslist'])
    # strip the info we dont need
    friends_loc = friends_loc.split(",",1)
    friends_loc = friends_loc[1]
    friends_loc = friends_loc.split("'",2)
    friends_loc = friends_loc[1]

    sendee_info = student_collection.find_one({'email':emailee})

    friends_loc_two = str(sendee_info['friendslist'])
    # strip the info we dont need
    friends_loc_two = friends_loc_two.split(",",1)
    friends_loc_two = friends_loc_two[1]
    friends_loc_two = friends_loc_two.split("'",2)
    friends_loc_two = friends_loc_two[1]

    send_to_sender_friends= {'first_name': sendee_first_name, 'last_name':sendee_last_name, 'email':emailee}
    send_to_sendee_friends= {'first_name': sender_first_name, 'last_name':sender_last_name, 'email':emailer}

    # sender
    friends_collection.find_one_and_update({'_id':ObjectId(friends_loc)},{ '$addToSet': { 'list': send_to_sender_friends} })
    # sendee
    friends_collection.find_one_and_update({'_id':ObjectId(friends_loc_two)},{ '$addToSet': { 'list': send_to_sendee_friends} })

    # db.friends_list.find_one({'_id':ObjectId(friends_loc)})




@task(bind = True, queue='write_tasks')
def deny_friend_request_two(self, data):
    db = client.students
    friend_requests = db.friend_requests
    emailee = data['email_of_sendee']
    emailer = data['email_of_requester']

    print(emailee)
    print(emailer)

    friend_requests.find_one_and_delete({'email_of_emailee':emailee, 'email_of_requester':emailer})




@task(bind = True, queue='read_tasks')
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



@task(bind=True, queue='read_tasks')
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
    print(username)
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
                for rq in all_my_requests:
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

@task(bind=True, queue='read_tasks')
def get_a_person_two(self, data):
    email = data['email']
    db = client.students
    students_temp = db.students
    value = students_temp.find_one({'email':email})
    return json_util.dumps(value)


@task
def mul(x, y):
        # html = "<html><body> string: "+""+"</body></html>"
        # return x + y
    return x * y


@task
def xsum(numbers):
    return sum(numbers)
