
  var numOfFriends = 0;
$( document ).ready(function() { 
    console.log( "ready!" );
})
function deleteListRow(obj, list) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    if(list == friendList){
      numOfFriends = numOfFriends - 1;
    }
    list.deleteRow(index);
}
function acceptFriendReq(obj){
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("friendReqList");
    table.deleteRow(index);
}

function createFriendList() {  
  populFriend();
  populFriendReq();
  document.getElementById("friendReqList").style.display = "none";
}

function displayFriendList(){
  document.getElementById("friendReqList").style.display = "none";
  document.getElementById("friendList").style.display = "table";
}
function displayFriendReq(){
  document.getElementById("friendReqList").style.display = "table";
  document.getElementById("friendList").style.display = "none";
}

function addFriend(){
  var studName = document.getElementById("studentName");
  var table = document.getElementById("friendList");
  numOfFriends = numOfFriends+1;

  var rowCount = table.rows.length;
  var row = table.insertRow(numOfFriends);

  row.insertCell(0).innerHTML= studName.value;
  row.insertCell(1).innerHTML= "BBM@SBU.com";
  row.insertCell(2).innerHTML= "SBU";
  row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>';  
  row.insertCell(4).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteListRow(this, friendList)">';
  studName.value = '';
}

function populFriend(){
  var table = document.getElementById("friendList");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Name</b>";
  row.insertCell(1).innerHTML= "<b>Email</b>";
  row.insertCell(2).innerHTML= "<b>School</b>";
  row.insertCell(3).innerHTML= '<b>View Schedule</b>';
  row.insertCell(4).innerHTML= '<b>Delete</b>';


  rowCount = rowCount + 1;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Joe Poodle";
  row.insertCell(1).innerHTML= "BBM@SBU.com";
  row.insertCell(2).innerHTML= "SBU";
  row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>';
  row.insertCell(4).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteListRow(this, friendList)">';
    numOfFriends = numOfFriends+1;
  for(var i = 0; i < 1; i++){
    numOfFriends = numOfFriends+1;
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "Boba Poodle";
    row.insertCell(1).innerHTML= "BBM@SBU.com";
    row.insertCell(2).innerHTML= "SBU";
    row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>'; 
    row.insertCell(4).innerHTML= '<input type="button" value = "Delete" onClick="Javacsript:deleteListRow(this, friendList)">';
  }
}

function populFriendReq(){
  var table = document.getElementById("friendReqList");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Name</b>";
  row.insertCell(1).innerHTML= "<b>Email</b>";
  row.insertCell(2).innerHTML= "<b>School</b>";
  row.insertCell(3).innerHTML= '<b>Accept</b>';
  row.insertCell(4).innerHTML= '<b>Deny</b>';


  rowCount = rowCount + 1;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Lonely Poodle";
  row.insertCell(1).innerHTML= "BBM@SBU.com";
  row.insertCell(2).innerHTML= "SBU";
  row.insertCell(3).innerHTML= '<input type="button" value = "Accept" onClick = "Javacsript:acceptFriendReq(this)">';
  row.insertCell(4).innerHTML= '<input type="button" value = "Deny" onClick="Javacsript:deleteListRow(this, friendReqList)">';

  for(var i = 0; i < 3; i++){
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "----";
    row.insertCell(1).innerHTML= "----";
    row.insertCell(2).innerHTML= "----";
    row.insertCell(3).innerHTML= '<input type="button" value = "Accept" onClick = "Javacsript:acceptFriendReq(this)">';
    row.insertCell(4).innerHTML= '<input type="button" value = "Deny" onClick="Javacsript:deleteListRow(this, friendReqList)">';
  }
}

function createCourseList() {
    createAssignSche();
    createGenSche();
    createLunSche();
    document.getElementById("genSch").style.display = "none";
    document.getElementById("lunSch").style.display = "none";
}
function createAssignSche(){
  var t = document.getElementById("assignSch");

  var rC = t.rows.length;
  var r = t.insertRow(rC);

  r.insertCell(0).innerHTML= '<b>' + 'Course ID' + '</b>';
  r.insertCell(1).innerHTML= "<b>Course Name</b>";
  r.insertCell(2).innerHTML= "<b>Instructor</b>";
  r.insertCell(3).innerHTML= "<b>School</b>";
  r.insertCell(4).innerHTML= "<b>Days</b>";
  r.insertCell(5).innerHTML= "<b>Period</b>";
  r.insertCell(6).innerHTML= "<b>Remove</b>";

  rC = rC + 1;
  var r = t.insertRow(rC);
  r.insertCell(0).innerHTML= "blahblahblah";
  r.insertCell(1).innerHTML= "CSE 308";
  r.insertCell(2).innerHTML= "monkey";
  r.insertCell(3).innerHTML= "BoB";
  r.insertCell(4).innerHTML= "M W";
  r.insertCell(5).innerHTML= "1";
  r.insertCell(6).innerHTML= '<input type="button" value = "Remove" onClick="Javacsript:deleteListRow(this, assignSch)">';

  var n = 5;
  for(var j = 0; j < 3; j++){
    rC = rC+1;
    r = t.insertRow(rC);
    r.insertCell(0).innerHTML= "----";
    r.insertCell(1).innerHTML= "----";
    r.insertCell(2).innerHTML= "----";
    r.insertCell(3).innerHTML= "----";
    r.insertCell(4).innerHTML= "----";
    r.insertCell(5).innerHTML= "----";
    r.insertCell(6).innerHTML= '<input type="button" value = "Remove" onClick="Javacsript:deleteListRow(this, assignSch)">';
  }
}
function createGenSche(){
  var t = document.getElementById("genSch");

  var rC = t.rows.length;
  var r = t.insertRow(rC);

  r.insertCell(0).innerHTML= ' ';
  r.insertCell(1).innerHTML= "<b>Course</b>";
  r.insertCell(2).innerHTML= "<b>Section To Exclude(optional)</b>";
  r.insertCell(3).innerHTML= "<b>Instructor(optional)</b>";
  r.insertCell(4).innerHTML= "<b>Add</b>";
  r.insertCell(5).innerHTML= "<b>Remove</b>";

  var qNum = rC - 1;
  rC = rC + 1;
  r = t.insertRow(rC);
  r.insertCell(0).innerHTML= 'Criteria ' + qNum;
  r.insertCell(1).innerHTML= '<input type="text" id="course">';
  r.insertCell(2).innerHTML= '<input type="text" id="sections">';
  r.insertCell(3).innerHTML= '<input type="text" id="instructor">';
  r.insertCell(4).innerHTML= '<input type="button" value = "Add" onClick="">';
  r.insertCell(5).innerHTML= "";
}
function createLunSche(){
  var table = document.getElementById("lunSch");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= '';
  row.insertCell(1).innerHTML= 'Monday';
  row.insertCell(2).innerHTML= 'Tuesday';
  row.insertCell(3).innerHTML= 'Wednesday';
  row.insertCell(4).innerHTML= 'Thursday';
  row.insertCell(5).innerHTML= 'Friday';

  rowCount = rowCount + 1;
  row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= 'Lunch: ';
  row.insertCell(1).innerHTML= '<input type="checkbox" id="monday">';
  row.insertCell(2).innerHTML= '<input type="checkbox" id="tuesday">';
  row.insertCell(3).innerHTML= '<input type="checkbox" id="wednes">';
  row.insertCell(4).innerHTML= '<input type="checkbox" id="thursday">';
  row.insertCell(5).innerHTML= '<input type="checkbox" id="friday">';
}
function displayGen(){
  document.getElementById("assignSch").style.display = "none";
  document.getElementById("genSch").style.display = "table";
  document.getElementById("lunSch").style.display = "table";
}
function displayAssign(){
  document.getElementById("assignSch").style.display = "table";
  document.getElementById("genSch").style.display = "none";
  document.getElementById("lunSch").style.display = "none";
}
function start(){
  createFriendList();
  createCourseList();
}