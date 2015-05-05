   function exportGeneratedSchedule(){
  // var getUrl = window.location;
  // var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  // var urlSubmit = baseUrl + "/export-course-schedule";
  // var data ={

  // };
  // $.ajax({  
  //   type: "POST",
  //   url: urlSubmit,
  //   dataType: "json",
  //   data      : data,
  //   success: function(response){

  //     }
  // });
  
}
function deleteFriendRequest(obj) {
  var info = $(obj).closest('tr').text();
  var res= info.split(" ");
  res = res.filter(Boolean);
      var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/delete-friend-request";
       var data ={
          'email_of_requester' : res[2]
       };
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             $(obj).closest('tr').remove();
          }
     });
}
function deleteFriend(obj) {
  var info = $(obj).closest('tr').text();
  var res= info.split(" ");
  res = res.filter(Boolean);
      var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/delete-friend";
       var data ={
          'first_name' : res[0],
          'last_name' : res[1],
          'friend_email' : res[2]
       };
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             $(obj).closest('tr').remove();
          }
     });
}
function removeAssignedCourse(obj) {
  var info = $(obj).closest('tr').children();
      var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/remove-assigned-course";
       // TODO: Add the course start and end times
       var block = info[3].textContent;
       block = block.split(/-|:|,/);
       var block_start = block[0];
       var block_end = block[1];
       var i;
       var days = "";
       for(i = 2; i < block.length; i++){
          days += block[i] + " ";
       }
       var data ={
          'course_name' : info[1].textContent,
          'course_id' : info[0].textContent,
          'instructor' : info[2].textContent,
          'start_period' : block_start,
          'end_period' : block_end,
          'days_array' : days
       };
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
          }
     });
       $(obj).closest('tr').remove();
}
function acceptFriendReq(obj){
  var info = $(obj).closest('tr').text();
  var res= info.split(" ");
  res = res.filter(Boolean);
      var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/accept-friend-request";
       var data ={
          'email_of_requester' : res[2]
       };
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             $(obj).closest('tr').remove();
             populFriend();
          }
     });
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
function displayCourseOffering(){
  $("#course_offerings").show();
  $("#offeringShow").hide();
  $("#offeringHide").show(); 
}
function hideCourseOffering(){
  $("#course_offerings").hide();
  $("#offeringShow").show();
  $("#offeringHide").hide(); 
}
function createCourseOfferingList(){
  $('#course_offerings').empty();
  $('#course_offerings').append('<table></table>');
  var table = $('#course_offerings').children();

  table.append('<tr><td><b>Course ID</b></td>\
    <td><b>Course Name</b></td>\
    <td><b>Instructor</b></td>\
    <td><b>Semester</b></td></tr>');

  var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-course-offerings";
        
        //need to check if information is missing
       var data ={

       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             var i;
            for(i = 0; i < response.length; i++){
              table.append('<tr><td>' + response[i].course_id +'</td>\
                <td>' + response[i].course_name + '</td>\
                <td>' + response[i].instructor + '</td>\
                <td>' + response[i].semester_name + '</td></tr>');
            }
          }
     });
}
function addFriend(){
  // var table = $('#friendList').children();
  
  // var studName = $('#studentName').val();
  
  // table.append('<tr><td>'+ studName +'</td>\
  //   <td>BBM@SBU.com</td>\
  //   <td>SBU</td>\
  //   <td><input type="button" class="btn" value = "View"></button></td>\
  //   <td><input type="button" class="btn" value = "Delete" \
  //     onClick="Javacsript:deleteListRow(this)"></td></tr>');

  // $('#studentName').val('');
        $("#sendFriendRequest").click(function(){
        $("sendFriendRequest").prop( "disabled", true );
        var textValue = $("#studentName").val();
        // if(textValue.slice(-1) != " "){
        //     return;
        // }
        // var firstName = textValue.trim();

       var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/send-friend-request";
        
       var requestInfo = textValue.split(/ - | /);
        var i;
        for(i = 0; i < requestInfo.length; i++){
        }
        //need to check if information is missing
       var data ={
           'first_name_emailee': requestInfo[0],
           'last_name_emailee' : requestInfo[1],
           'email_of_sendee' : requestInfo[2]
       }; 
      $('#studentName').val('');
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             populFriendReq();
          }
     });
  });
  $("sendFriendRequest").prop( "disabled", false );
}
function populFriend(){
  $('#friendList').empty();
  $('#friendList').append('<table></table>');
  var table = $('#friendList').children();

  table.append('<tr><td><b>Name</b></td>\
    <td><b>Email</b></td>\
    <td><b>View Schedule</b></td>\
    <td><b>Delete</b></td></tr>');

  // table.append('<tr><td>Joe Poodle</td>\
  //   <td>BBM@SBU.com</td>\
  //   <td><input type="button" class="btn" value = "View"></button></td>\
  //   <td><input type="button" class="btn" value = "Delete" \
  //     onClick="Javacsript:deleteListRow(this)"></td></tr>');
var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-friend-list";
        
        //need to check if information is missing
       var data ={

       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
             var i;
            for(i = 0; i < response.length; i++){
              table.append('<tr><td>' + response[i].first_name + " " + response[i].last_name + '</td>\
                <td>' + response[i].email + '</td>\
                <td><input type="button" class="btn" value = "View"></button></td>\
                <td><input type="button" class="btn" value = "Delete" \
                  onClick="Javacsript:deleteFriend(this)"></td></tr>');
            }
          }
     });
}
function populFriendReq(){
  $('#friendReqList').empty();
  $('#friendReqList').append('<table></table>');
  var table = $('#friendReqList').children();
  
  table.append('<tr><td><b>Name</b></td>\
    <td><b>Email</b></td>\
    <td><b>Accept</b></td>\
    <td><b>Delete</b></td></tr>');

  // table.append('<tr><td>Joe Poodle</td>\
  //   <td>BBM@SBU.com</td>\
  //   <td><input type="button" class="btn" value = "Accept"\
  //     onClick = "Javacsript:acceptFriendReq(this)"></td>\
  //   <td><input type="button" class="btn" value = "Delete" \
  //     onClick="Javacsript:deleteListRow(this)"></td></tr>');

var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-friends-request";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete
            var i;
            for(i = 0; i < response.length; i++){
              table.append('<tr><td>' + response[i].first_name_of_requester + " " + response[i].last_name_of_requester + '</td>\
                <td>' + response[i].email_of_requester + '</td>\
                <td><input type="button" class="btn" value = "Accept"\
                  onClick = "Javacsript:acceptFriendReq(this)"></td>\
                <td><input type="button" class="btn" value = "Delete" \
                  onClick="Javacsript:deleteFriendRequest(this)"></td></tr>');
            }
          }
     });
}
function createCourseList() {
    createAssignSche();
    createGenSche();
    createLunSche();
    $("#genSch").hide();
    $("#lunSch").hide();
    $("#genButtons").hide();
    $("#exportButton").hide();
}
function createAssignSche(){
  $('#assignSch').empty();
  $('#assignSch').append('<table></table>');
  var table = $('#assignSch').children();
  
  table.append('<tr><td><b>Course ID</b></td>\
    <td><b>Course Name</b></td>\
    <td><b>Instructor</b></td>\
    <td><b>Block</b></td>\
    <td><b>Add</b></td>\
    <td><b>Remove</b></td></tr>');

  var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-assigned-schedule";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // TODO: Add the block in human readable format
             if(response != "null"){
                var i;
                var j;
                var block_start;
                var block_end;
                var block_days = "";
                var block;
                for(i = 0; i < response.length; i++){
                  block_days = "";
                  block_start = response[i].blocks.start_period;
                  block_end = response[i].blocks.end_period;
                  for(j = 0; j < response[i].blocks.days.length; j++){
                    block_days += response[i].blocks.days[j];
                    block_days += ","
                  }
                  block_days = block_days.slice(0, -1);
                  table.append('<tr><td>' + response[i].course_id + '</td>\
                    <td>' + response[i].course_name + '</td>\
                    <td>' + response[i].instructor + '</td>\
                    <td>' + block_start + "-" + block_end + ":" + block_days + '</td>\
                    <td></td>\
                    <td><input type="button" class="btn" value = "Remove" \
                      onClick="Javacsript:removeAssignedCourse(this)"></td></tr>');
                }
              }
              table.append('<tr>\
                <td><input type="text" id="courseID"></td>\
                <td><input type="text" id="courseName"></td>\
                <td><input type="text" id="instructor"></td>\
                <td><select type="text" id="block"></select></td>\
                <td><input type="button" class="btn" value = "Add"\
                  onClick="Javacsript:addAssignCourse()"></td>\
                <td></td></tr>');
                addYear();
                $('#academicYears').on('click', function() {
                    getBlocks($('#academicYears').val());
                });

          }
     });
}
function addAssignCourse(){
  var table = $('#assignSch').children();
  var select = $('#semester').val();
        //need to check if information is missing
       
      if($('#courseID').val() != ""){

       var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/add-assigned-class";
       var data ={
           'course_id': $('#courseID').val(),
           'course_name' : $('#courseName').val(),
           'instructor' : $('#instructor').val(),
           'block': $('#block').val(),
           'year': $('#academicYears').val(),
           'semester' : select
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
           // set the autocomplete

             createGenSche();
             createAssignSche();
             createCourseOfferingList();
           }
     });
     
  }
}
// function deleteAssignedCourse(obj) {
//   var info = $(obj).closest('tr').text();
//   var res= info.split(" ");
//   res = res.filter(Boolean);
//       var getUrl = window.location;
//        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
//        var urlSubmit = baseUrl + "/delete-friend-request";
//        var data ={
//           'email_of_requester' : res[2]
//        };
//        $.ajax({  
//            type: "POST",
//            url: urlSubmit,
//            dataType: "json",
//            data      : data,
//            success: function(response){
//            // set the autocomplete
//              $(obj).closest('tr').remove();
//           }
//      });
// }

function addYear(){
  var getUrl = window.location;
  var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  var urlSubmit = baseUrl + "/get-school-info";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "JSON",
           data      : data,
           success: function(response){
             selectValues = response.year;
             $.each(selectValues, function(key, value) {
                $('#academicYears')
                    .append($("<option></option>")
                    .attr("value",value.year_name)
                    .text(value.year_name)); 
             });
            getBlocks($('#academicYears').val());
            }
      });
}
function addSemester(){
  var getUrl = window.location;
  var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  var urlSubmit = baseUrl + "/get-school-info";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "JSON",
           data      : data,
           success: function(response){
             selectValues = response.name_of_semesters;
             $.each(selectValues, function(key, value) {
                $('#semester')
                    .append($("<option></option>")
                    .attr("value",value)
                    .text(value)); 
             });
            }
      });
}
function getBlocks(year){
  var getUrl = window.location;
  var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  var urlSubmit = baseUrl + "/get-school-info";
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "JSON",
           data      : data,
           success: function(response){
             var years = response.year;
             var i;
             $('#block').empty()
             for(i = 0; i < years.length; i++){
                 if(String(year) == years[i].year_name){
                    $('block').html('');
                    var blocks = years[i].blocks;
                    var ii;
                    for(ii = 0; ii < years[i].blocks.length; ii++){
                        var block = years[i].blocks[ii];
                        var block_text = block.start + '-' + block.end + ':'; 
                        var days = block.days_active;
                        var iii;
                        for(iii = 0; iii < block.days_active.length; iii++){
                            block_text += block.days_active[iii] + ',';
                        }
                        block_text = block_text.substring(0, block_text.length - 1);
                        $('#block').append($("<option></option>")
                            .attr("value",block_text)
                            .text(block_text));
                    }
                 }
             }
            }
      });
}
function createGenSche(){
  $('#course_offerings').empty();
  $('#course_offerings').append('<table></table>');
  var table = $('#genSch').children();

  // table.append('<tr><td><b>Course ID</b></td>\
  //   <td><b>Course Name</b></td>\
  //   <td><b>Instructor</b></td>\
  //   <td><b>Semester</b></td></tr>');

  var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-course-offerings";
        
        //need to check if information is missing
       var data ={

       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
               console.log(response);
           // set the autocomplete
             var i;
                var j;
                var block_start;
                var block_end;
                var block_days = "";
                var block;
            for(i = 0; i < response.length; i++){
               block_days = "";
                  block_start = response[i].blocks.start_period;
                  block_end = response[i].blocks.end_period;
                  for(j = 0; j < response[i].blocks.days.length; j++){
                    block_days += response[i].blocks.days[j];
                    block_days += ","
                  }
                  block_days = block_days.slice(0, -1);
              table.append('<tr><td>' + response[i].course_id +'</td>\
                <td>' + response[i].course_name + '</td>\
                <td>' + response[i].instructor + '<input type="checkbox" class="preferred"/>' + '</td>\
                <td>' + block_start + "-" + block_end + ":" + block_days + '</td>\
                <td>' + response[i].semester_name + '</td>\
                <td><input type="checkbox" class="include"' + '"></td></tr>');
            }
          }
     });
  $('#genSch').empty();
  $('#genSch').append('<table></table>');
  var table = $('#genSch').children();
  
  table.append('<tr><td><b>Course</b></td>\
    <td><b>Course Name</b></td>\
    <td><b>Instructor(optional)</b></td>\
    <td><b>Block Schedule</b></td>\
    <td><b>Semester</b></td>\
    <td><b>Include</b></td></tr>');
}
function getBlockText(year_info){
}
function addGenCourse(){
//  var courseName = $('#course').val();
//  var sectEx = $('#sections').val();
//  var instr = $('#professor').val();
//  var table = $('#genSch').children();
//
//  if(courseName != ""){
//    $("#genSch tr:last").remove();
//    table.append('<tr>\
//    <td>'+ courseName +'</td>\
//    <td>'+ sectEx +'</td>\
//    <td>'+ instr +'</td>\
//    <td></td>\
//    <td><input type="button" class="btn" value = "Delete"\
//      onClick="Javacsript:deleteListRow(this)"></td></tr>');
//
//    table.append('<tr>\
//    <td><input type="text" id="course"></td>\
//    <td><input type="text" id="sections"></td>\
//    <td><input type="text" id="professor"></td>\
//    <td><input type="button" class="btn" value = "Add"\
//      onClick="Javacsript:addGenCourse()"></td>\
//    <td></td></tr>');
//  }
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
    <td><b>Friday</b></td></tr>');

  table.append('<tr>\
    <td>Lunch: </td>\
    <td><input type="checkbox" id="monday"></td>\
    <td><input type="checkbox" id="tuesday"></td>\
    <td><input type="checkbox" id="wednes"></td>\
    <td><input type="checkbox" id="thursday"></td>\
    <td><input type="checkbox" id="friday"></td></tr>');
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
  $("#exportButton").show();
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
  $("#exportButton").hide();
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
               var students = [];//JSON.parse(response);
               var i = 0;
               for(i = 0; i < response.length; i++){
                   students.push(response[i].first_name + " " + 
                           response[i].last_name + " - " + response[i].email);
               }
               addAutoComplete($("#studentName"), students);
           }
       });
    });
}
$( document ).ready(function() {
    // add auto complete to our text boxes
   addFriendAutoComplete();
  addAutoComplete($("#studentName"), []);
  addFriend();
  addSemester();
  createFriendList();
  createCourseList();
  hideCourseOffering();
  createCourseOfferingList();
  setupViewSchedule0();
  $("#export").click(function(){ 
    exportGeneratedSchedule();
  });
  $("#generate").click(function(){ 
    generateDesiredSchedule();
  });
});



function setupViewSchedule0() {
    $('#view-assigned-schedule').click(function (){
        setupViewSchedule1();
    });
}

function setupViewSchedule1() {
  var getUrl = window.location;
  var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  var urlSubmit = baseUrl + "/get-school-info";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "JSON",
           data      : data,
           success: function(response){
               var years = response.year;
               var i;
               for(i = 0; i < years.length; i++){
                   if($('#academicYears').val().localeCompare(years[i].year_name) == 0){
                       setupViewSchedule2(years[i].num_periods_in_a_day);
                   }
               }
            }
      });
}

function setupViewSchedule2(periods) {
  var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/get-assigned-schedule";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){

$('#schedule-popup').remove();
$('#close-schedule-popup').remove();
$('#toggle-schedule-popup').remove();
$('body').prepend('<div id="close-schedule-popup"></div><div id="toggle-schedule-popup"></div> <div id="schedule-popup"> <table id="schedule" style="width:100%"></table> </div>');
$('#close-schedule-popup').click(function() {
    $('#schedule-popup').remove();
    $('#close-schedule-popup').remove();
    $('#toggle-schedule-popup').remove();
});
$('#toggle-schedule-popup').click(function() {
    $('.friends-courses').toggle();
});

// add periods to table
$('#schedule').append('<tr id="period-days"> <td>Periods</td> </tr>');
var i = 0;
for (i = 0; i < periods; i++) {
    $('#schedule').append('<tr id="period-' + i + '"><td>Periods ' + String(i + 1) + '</td></tr>');
}
$('#period-days').append('<td>M</td>');
$('#period-days').append('<td>Tu</td>');
$('#period-days').append('<td>W</td>');
$('#period-days').append('<td>Th</td>');
$('#period-days').append('<td>F</td>');
var ii;
var iii;
for (ii = 0; ii < 5; ii++) {
    for (iii = 0; iii < periods; iii++) {
        $('#period-' + iii).append('<td id="' + ii + '-' + iii + '"></td>');
    }
}

addFriendOverlay();





// TODO: Add the block in human readable format
if (response != "null") {
    var t;
    var j;
    var block_start;
    var block_end;
    var block_days = "";
    var block;
    var table = $('#schedule');
    for (t = 0; t < response.length; t++) {
    var schedule = {
        'M': [],
        'Tu': [],
        'W': [],
        'Th': [],
        'F': []
    };
        block_start = response[t].blocks.start_period;
        block_end = response[t].blocks.end_period;
        var p = []
        for (j = block_start; j <= block_end; j++) {
            p.push(j-1);
        }
        for (j = 0; j < response[t].blocks.days.length; j++) {
            schedule[response[t].blocks.days[j]].push({
                'periods': p,
                'class': response[t].course_id
            });
        }
        console.log(response[t]);

        if (schedule['M'].length > 0) {
            var i;
            for (i = 0; i < schedule.M.length; i++) {
                for (j = 0; j < schedule.M[i].periods.length; j++) {
                    $('#0-' + schedule['M'][i].periods[j]).append(schedule['M'][i].class);
                    $('#0-' + schedule['M'][i].periods[j]).addClass(schedule['M'][i].class);
                }
            }
        }
        if (schedule['Tu'].length > 0) {
            var i;
            for (i = 0; i < schedule.Tu.length; i++) {
                for (j = 0; j < schedule.Tu[i].periods.length; j++) {
                    $('#1-' + schedule['Tu'][i].periods[j]).append(schedule['Tu'][i].class);
                    $('#1-' + schedule['Tu'][i].periods[j]).addClass(schedule['Tu'][i].class);
                }
            }
        }
        if (schedule['W'].length > 0) {
            var i;
            for (i = 0; i < schedule.W.length; i++) {
                for (j = 0; j < schedule.W[i].periods.length; j++) {
                    $('#2-' + schedule['W'][i].periods[j]).append(schedule['W'][i].class);
                    $('#2-' + schedule['W'][i].periods[j]).addClass(schedule['W'][i].class);
                }
            }
        }
        if (schedule['Th'].length > 0) {
            var i;
            for (i = 0; i < schedule.Th.length; i++) {
                for (j = 0; j < schedule.Th[i].periods.length; j++) {
                    $('#3-' + schedule['Th'][i].periods[j]).append(schedule['Th'][i].class);
                    $('#3-' + schedule['Th'][i].periods[j]).addClass(schedule['Th'][i].class);
                }
            }
        }
        if (schedule['F'].length > 0) {
            var i;
            for (i = 0; i < schedule.F.length; i++) {
                for (j = 0; j < schedule.F[i].periods.length; j++) {
                    $('#4-' + schedule['F'][i].periods[j]).append(schedule['F'][i].class);
                    $('#4-' + schedule['F'][i].periods[j]).addClass(schedule['F'][i].class);
                }
            }
        }

    }
}

}

     });

}

function addFriendOverlay(){
    console.log("poo");
  var getUrl = window.location;
  var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
  var urlSubmit = baseUrl + "/get-friends-schedules";
        
        //need to check if information is missing
       var data ={
       }; 
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "JSON",
           data      : data,
           success: function(response){
               console.log(response);
               var friends = response.courses;
               var i;
               for(i = 0; i < friends.length; i++){
                   var j;
                   for(j = 0; j < friends[i].courses.length; j++){
                       $('.' + friends[i].courses[j]).append('<br><span class="friends-courses">'+friends[i].friend + '</span>');
                   }
               }
            }
      });
}
function generateDesiredSchedule() {
   // 'course_id' : "cse220",
   //          'blocks' : {
   //              'start_period' : "1",
   //              'days' : [
   //                  "M",
   //                  "W"
   //              ],
   //              'end_period' : "2"
   //          },
   //          'instructor' : "wong",
   //          'course_name' : "systems",
   //          'preferred': False
     data = [];
     var course_id;
     var course_name;
     var instructor;
     var preferred;
     var block;

     var periods;
     var days;
     var start_period;
     var end_period;
     var include;
      var table = $('#genSch').children().children();
      table.find('tr').each(function (i, row) {
        if(i!=0){
            var $tds = $(this).find('td'),
            course_id = $tds.eq(0).text(),
            course_name = $tds.eq(1).text(),
            instructor = $tds.eq(2).text(),

            block = $tds.eq(3).text();
            
            block = block.split(":");
            periods = block[0];
            days = block[1].split(',');
            start_period = periods.split('-')[0];
            end_period = periods.split('-')[1];

            if($(row).find('input.preferred[type="checkbox"]').is(':checked')){
              preferred = true;
            }
            else{
              preferred = false;
            }
            
            if($(row).find('input.include[type="checkbox"]').is(':checked')){
              include = true;
            }
            else{
              include = false;
            }
            if(include){
              data.push({'course_id':course_id, 'blocks':{'start_period':start_period,
              'end_period': end_period, 'days': days}, 'instructor': instructor,
              'course_name': course_name, 'preferred': preferred});
            }
          }
        });
      console.log(data)
      var getUrl = window.location;
       var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
       var urlSubmit = baseUrl + "/generate-course-schedule";
       var data ={
          'data[]' : JSON.stringify(data)
       };
       $.ajax({  
           type: "POST",
           url: urlSubmit,
           dataType: "json",
           data      : data,
           success: function(response){
            console.log(response);
          }
     });
     }
