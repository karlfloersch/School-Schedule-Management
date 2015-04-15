
$( document ).ready(function() { 
    console.log( "ready!" );
})
function deleteListRow(obj, list) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    list.deleteRow(index);
}
function acceptAll(){
  var table = document.getElementById("manageAccountReq");
  var rowCount = table.rows.length;

  for(var i = 0; i < rowCount - 1; i++){
    table.deleteRow(1);
  }
}
function createAcctReqList() {  
  var table = document.getElementById("manageAccountReq");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Name</b>";
  row.insertCell(1).innerHTML= "<b>ID</b>";
  row.insertCell(2).innerHTML= "<b>School</b>";
  row.insertCell(3).innerHTML= '<b>Accept</b>';
  row.insertCell(4).innerHTML= '<b>Deny</b>';


  rowCount = rowCount + 1;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Joe Poodle";
  row.insertCell(1).innerHTML= "0000007";
  row.insertCell(2).innerHTML= "MSC";
  row.insertCell(3).innerHTML= '<input type="button" class="btn" value = "Accept" \
  onClick="Javacsript:deleteListRow(this, manageAccountReq)"></button>';
  row.insertCell(4).innerHTML= '<input type="button" class="btn" value = "Delete" \
  onClick="Javacsript:deleteListRow(this, manageAccountReq)">';
  for(var i = 0; i < 5; i++){
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "Bob";
    row.insertCell(1).innerHTML= "DICK";
    row.insertCell(2).innerHTML= "I3";
    row.insertCell(3).innerHTML= '<input type="button" class="btn" value = "Accept" \
    onClick="Javacsript:deleteListRow(this, manageAccountReq)"></button>';
    row.insertCell(4).innerHTML= '<input type="button" class="btn" value = "Delete" \
    onClick="Javacsript:deleteListRow(this, manageAccountReq)">';
  }
}
function createManageSchool() {  
  var table = document.getElementById("manageSchool");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Name</b>";
  row.insertCell(1).innerHTML= "<b>Year</b>";
  row.insertCell(2).innerHTML= "<b>#Semester</b>";
  row.insertCell(3).innerHTML= '<b>Range of Periods</b>';
  row.insertCell(4).innerHTML= '<b>View/Edit</b>';
  row.insertCell(5).innerHTML= '<b>Delete</b>';

  rowCount = rowCount + 1;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "SBU";
  row.insertCell(1).innerHTML= "30040";
  row.insertCell(2).innerHTML= "2";
  row.insertCell(3).innerHTML= "4";
  row.insertCell(4).innerHTML= '<input type="button" class="btn" value = "Edit" \
  onClick=""></button>';
  row.insertCell(5).innerHTML= '<input type="button" class="btn" value = "Delete" \
  onClick="Javacsript:deleteListRow(this, manageSchool)">';
  for(var i = 0; i < 5; i++){
    rowCount = rowCount + 1;
    var row = table.insertRow(rowCount);    
    row.insertCell(0).innerHTML= "NYU";
    row.insertCell(1).innerHTML= "20231";
    row.insertCell(2).innerHTML= "2";
    row.insertCell(3).innerHTML= "4";
    row.insertCell(4).innerHTML= '<input type="button" class="btn" value = "Edit" \
    onClick=""></button>';
    row.insertCell(5).innerHTML= '<input type="button" class="btn" value = "Delete" \
    onClick="Javacsript:deleteListRow(this, manageSchool)">';
  }
}
function createManageStudent() {  
  var table = document.getElementById("manageStudents");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Name</b>";
  row.insertCell(1).innerHTML= "<b>ID</b>";
  row.insertCell(2).innerHTML= "<b>School</b>";
  row.insertCell(3).innerHTML= '<b>Delete</b>';

  rowCount = rowCount + 1;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "Joe Poodle";
  row.insertCell(1).innerHTML= "0000007";
  row.insertCell(2).innerHTML= "MSC";
  row.insertCell(3).innerHTML= '<input type="button" class="btn" value = "Delete" \
  onClick="Javacsript:deleteListRow(this, manageStudents)">';
  for(var i = 0; i < 5; i++){
    rowCount = rowCount+1;
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= "Bob";
    row.insertCell(1).innerHTML= "DICK";
    row.insertCell(2).innerHTML= "I3";
    row.insertCell(3).innerHTML= '<input type="button" class="btn" value = "Delete" \
    onClick="Javacsript:deleteListRow(this, manageStudents)">';
  }
}
function start(){
  createAcctReqList();
  createManageSchool();
  createManageStudent();
}