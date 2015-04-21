function deleteListRow(obj) {
    $(obj).closest('tr').remove();
}
function acceptFriendReq(obj){
     $(obj).closest('tr').remove();
}
function createFriendList() {  
  populFriend();
  populFriendReq();
  $("#friendReqList").hide();
}
function displayFriendList(){
  $("#friendReqList").hide();
  $("#friendList").show();
}
function displayFriendReq(){
  $("#friendReqList").show();
  $("#friendList").hide();
}
function addFriend(){
  var table = $('#friendList').children();
  
  var studName = $('#studentName').val();
  
  table.append('<tr><td>'+ studName +'</td>\
    <td>BBM@SBU.com</td>\
    <td>SBU</td>\
    <td><input type="button" class="btn" value = "View"></button></td>\
    <td><input type="button" class="btn" value = "Delete" \
      onClick="Javacsript:deleteListRow(this)"></td>');

  $('#studentName').val('');
}
function populFriend(){
  $('#friendList').append('<table></table>');
  var table = $('#friendList').children();

  table.append('<tr><td><b>Name</b></td>\
    <td><b>Email</b></td>\
    <td><b>School</b></td>\
    <td><b>View Schedule</b></td>\
    <td><b>Delete</b></td>');

  table.append('<tr><td>Joe Poodle</td>\
    <td>BBM@SBU.com</td>\
    <td>SBU</td>\
    <td><input type="button" class="btn" value = "View"></button></td>\
    <td><input type="button" class="btn" value = "Delete" \
      onClick="Javacsript:deleteListRow(this)"></td>');
}
function populFriendReq(){
  $('#friendReqList').append('<table></table>');
  var table = $('#friendReqList').children();
  
  table.append('<tr><td><b>Name</b></td>\
    <td><b>Email</b></td>\
    <td><b>School</b></td>\
    <td><b>Accept</b></td>\
    <td><b>Delete</b></td>');

  table.append('<tr><td>Joe Poodle</td>\
    <td>BBM@SBU.com</td>\
    <td>SBU</td>\
    <td><input type="button" class="btn" value = "Accept"\
      onClick = "Javacsript:acceptFriendReq(this)"></td>\
    <td><input type="button" class="btn" value = "Delete" \
      onClick="Javacsript:deleteListRow(this)"></td>');
}
function createCourseList() {
    createAssignSche();
    createGenSche();
    createLunSche();
    $("#genSch").hide();
    $("#lunSch").hide();
    $("#genButtons").hide();
}
function createAssignSche(){
  $('#assignSch').append('<table></table>');
  var table = $('#assignSch').children();
  
  table.append('<tr><td><b>Course ID</b></td>\
    <td><b>Course Name</b></td>\
    <td><b>Instructor</b></td>\
    <td><b>School</b></td>\
    <td><b>Days</b></td>\
    <td><b>Periods</b></td>\
    <td><b>Add</b></td>\
    <td><b>Remove</b></td>');

  table.append('<tr><td>Technical Writing</td>\
    <td>CSE300</td>\
    <td>Liu</td>\
    <td>SBU</td>\
    <td>M W</td>\
    <td>1</td>\
    <td></td>\
    <td><input type="button" class="btn" value = "Remove" \
      onClick="Javacsript:deleteListRow(this)"></td>');

  table.append('<tr>\
    <td><input type="text" id="courseID"></td>\
    <td><input type="text" id="courseName"></td>\
    <td><input type="text" id="instructor"></td>\
    <td><input type="text" id="School"></td>\
    <td><input type="text" id="days"></td>\
    <td><input type="text" id="Period"></td>\
    <td><input type="button" class="btn" value = "Add"\
      onClick="Javacsript:addAssignCourse()"></td>\
    <td></td>');
}
function addAssignCourse(){
  var courseName = $('#courseID').val();
  var sectEx = $('#courseName').val();
  var instr = $('#instructor').val();
  var sch = $('#School').val();
  var days = $('#days').val();
  var period = $('#Period').val();

  var table = $('#assignSch').children();

  if(courseName != ""){
    $("#assignSch tr:last").remove();
    table.append('<tr>\
    <td>'+ courseName +'</td>\
    <td>'+ sectEx +'</td>\
    <td>'+ instr +'</td>\
    <td>'+ sch +'</td>\
    <td>'+ days +'</td>\
    <td>'+ period +'</td>\
    <td></td>\
    <td><input type="button" class="btn" value = "Remove"\
      onClick="Javacsript:deleteListRow(this)"></td>');

    table.append('<tr>\
      <td><input type="text" id="courseID"></td>\
      <td><input type="text" id="courseName"></td>\
      <td><input type="text" id="instructor"></td>\
      <td><input type="text" id="School"></td>\
      <td><input type="text" id="days"></td>\
      <td><input type="text" id="Period"></td>\
      <td><input type="button" class="btn" value = "Add"\
        onClick="Javacsript:addAssignCourse()"></td>\
      <td></td>');
  }
}
function createGenSche(){
  $('#genSch').append('<table></table>');
  var table = $('#genSch').children();
  
  table.append('<tr><td><b>Course</b></td>\
    <td><b>Section To Exclude(optional)</b></td>\
    <td><b>Instructor(optional)</b></td>\
    <td><b>Add</b></td>\
    <td><b>Remove</b></td>');

  table.append('<tr>\
    <td><input type="text" id="course"></td>\
    <td><input type="text" id="sections"></td>\
    <td><input type="text" id="professor"></td>\
    <td><input type="button" class="btn" value = "Add"\
      onClick="Javacsript:addGenCourse()"></td>\
    <td></td>');
}
function addGenCourse(){
  var courseName = $('#course').val();
  var sectEx = $('#sections').val();
  var instr = $('#professor').val();
  var table = $('#genSch').children();

  if(courseName != ""){
    $("#genSch tr:last").remove();
    table.append('<tr>\
    <td>'+ courseName +'</td>\
    <td>'+ sectEx +'</td>\
    <td>'+ instr +'</td>\
    <td></td>\
    <td><input type="button" class="btn" value = "Delete"\
      onClick="Javacsript:deleteListRow(this)"></td>');

    table.append('<tr>\
    <td><input type="text" id="course"></td>\
    <td><input type="text" id="sections"></td>\
    <td><input type="text" id="professor"></td>\
    <td><input type="button" class="btn" value = "Add"\
      onClick="Javacsript:addGenCourse()"></td>\
    <td></td>');
  }
}
function createLunSche(){
  $('#lunSch').append('<table></table>');
  var table = $('#lunSch').children();
  
  table.append('<tr>\
    <td></td>\
    <td><b>Monday</b></td>\
    <td><b>Tuesday</b></td>\
    <td><b>Wednesday</b></td>\
    <td><b>Thursday</b></td>\
    <td><b>Friday</b></td>');

  table.append('<tr>\
    <td>Lunch: </td>\
    <td><input type="checkbox" id="monday"></td>\
    <td><input type="checkbox" id="tuesday"></td>\
    <td><input type="checkbox" id="wednes"></td>\
    <td><input type="checkbox" id="thursday"></td>\
    <td><input type="checkbox" id="friday"></td>');
}
// Setup stuff for the CSRF Token/post requests
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
// End CSRF stuff
function displayGen(){
  $("#assignSch").hide();
  $("#assignButtons").hide();
  $("#genSch").show();
  $("#genButtons").show();
  $("#lunSch").show();
  
  // Add autocomplete for generated schedule
  var courses = [
       "CSE300",
       "CSE310",
       "CSE308",
       "CSE214",
       "CSE114",
       "CSE219",
       ];
  addAutoComplete($("#course"), courses);
  var professors = [
       "McKenna",
       "Smolka",
       "Osama",
       "Obama",
       "Stoller",
       "Poodle",
       ];
  addAutoComplete($("#instructor"), professors);
  var sections = [
       "1",
       "2",
       "3",
       "4",
       "5",
       "6",
       ];
  addAutoComplete($("#sections"), sections);
}
function displayAssign(){
  $("#assignSch").show();
  $("#assignButtons").show();
  $("#genSch").hide();
  $("#genButtons").hide();
  $("#lunSch").hide();
}
function addAutoComplete(element, values) {  
  element.autocomplete({
    source: values
  });
}
function addFriendAutoComplete() {
    $("#studentName").keyup(function(){
        var textValue = $("#studentName").val();
        if(textValue.slice(-1) != " "){
            return;
        }
        var firstName = textValue.trim();

       var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-friends";
     
       var data ={
           "first_name": firstName
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
               // set the autocomplete
               console.log("working?");
               console.log(response);
               var students = [];//JSON.parse(response);
               var i = 0;
               for(i = 0; i < response.length; i++){
                   students.push(response[i].first_name + " " + 
                           response[i].last_name + " - " + response[i].email);
               }
               console.log(students);
               addAutoComplete($("#studentName"), students);
           }
       });
    });
}
$( document ).ready(function() {
    // add auto complete to our text boxes
  addFriendAutoComplete();
  addAutoComplete($("#studentName"), []);
  createFriendList();
  createCourseList();
});
