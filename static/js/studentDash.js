
  var numOfFriends = 0;
$( document ).ready(function() { 
    console.log( "ready!" );
})
function deleteFriendRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("friendList");
    table.deleteRow(index);
}
function acceptFriendReq(obj){
    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("friendList");
    table.deleteRow(index);
}

function deleteCourseRow(obj) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    var t = document.getElementById("courseList");
    t.deleteRow(index);
}

function createFriendList() {
  var table = document.getElementById("friendList");
  
  populFriend();
  populFriendReq();
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
  row.insertCell(4).innerHTML= '';
  row.insertCell(5).innerHTML= '';
  studName.value = '';
}
function populFriend(){
  var table = document.getElementById("friendList");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Joe Poodle";
  row.insertCell(1).innerHTML= "BBM@SBU.com";
  row.insertCell(2).innerHTML= "SBU";
  row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>';
  row.insertCell(4).innerHTML= '';
  row.insertCell(5).innerHTML= '';
  numOfFriends = numOfFriends+1;
  for(var i = 0; i < 1; i++){
    numOfFriends = numOfFriends+1;
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "Boba Poodle";
    row.insertCell(1).innerHTML= "BBM@SBU.com";
    row.insertCell(2).innerHTML= "SBU";
    row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>'; 
    row.insertCell(4).innerHTML= '';
    row.insertCell(5).innerHTML= '';
  }
}

function populFriendReq(){
  var table = document.getElementById("friendList");
  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Lonely Poodle";
  row.insertCell(1).innerHTML= "BBM@SBU.com";
  row.insertCell(2).innerHTML= "SBU";
  row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>';
  row.insertCell(4).innerHTML= '<input type="button" value = "Accept" onClick = "Javacsript:acceptFriendReq(this)">';
  row.insertCell(5).innerHTML= '<input type="button" value = "Deny" onClick="Javacsript:deleteFriendRow(this)">';

  for(var i = 0; i < 3; i++){
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "----";
    row.insertCell(1).innerHTML= "----";
    row.insertCell(2).innerHTML= "----";
    row.insertCell(3).innerHTML= '<input type="button" value = "View"></button>';
    row.insertCell(4).innerHTML= '<input type="button" value = "Accept" onClick = "Javacsript:acceptFriendReq(this)">';
    row.insertCell(5).innerHTML= '<input type="button" value = "Deny" onClick="Javacsript:deleteFriendRow(this)">';
  }
}

function createCourseList() {
    createAssignSche();
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
  r.insertCell(6).innerHTML= '<input type="button" value = "Remove" onClick="Javacsript:deleteCourseRow(this)">';

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
    r.insertCell(6).innerHTML= '<input type="button" value = "Remove" onClick="Javacsript:deleteCourseRow(this)">';
  }
}

function displayGen(){
  document.getElementById("assignSch").style.display = "none";
  document.getElementById("genSch").style.display = "table";
}
function displayAssign(){
  document.getElementById("assignSch").style.display = "table";
  document.getElementById("genSch").style.display = "none";
}
function start(){
  createFriendList();
  createCourseList();
}