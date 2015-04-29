function deleteListRow(list) {
    $(list).closest('tr').remove();
}
function acceptAll(){
  var table = $('#manageAccountReq').children();

  $('#manageAccountReq tr').each(function (i, row) { 
    if(i != '0'){
      row.remove();
    }
  })
}
function createAcctReqList() { 
  $('#manageAccountReq').append('<table></table>');
  var table = $('#manageAccountReq').children();
  
  table.append('<tr><td><b>Name</b></td>\
    <td><b>ID</b></td>\
    <td><b>School</b></td>\
    <td><b>Accept</b></td>\
    <td><b>Deny</b></td></tr>');

  table.append('<tr><td>Joe Poodle</td>\
    <td>0000007</td>\
    <td>MSC</td>\
    <td><input type="button" class="btn" value = "Accept" \
    onClick="Javacsript:deleteListRow(this)"></button></td>\
    <td><input type="button" class="btn" value = "Deny" \
    onClick="Javacsript:deleteListRow(this)"></td></tr>');
}
function createManageSchool() {  
//  $('#manageSchool').append('<table></table>');
//  var table = $('#manageSchool').children();
//  
//  table.append('<tr><td><b>Name</b></td>\
//    <td><b>School Address</b></td>\
//    <td><b>View/Edit</b></td>\
//    <td><b>Delete</b></td>');
//
//  for(var i = 0; i < 1; i++){
//    table.append('<tr><td class="schoolName">SBU</td>\
//      <td class = "schoolAddress">Stony Brook, NY 11794</td>\
//      <td><input type="button" class="btn" value = "Edit" \
//        onClick=""></button></td>\
//      <td><input type="button" class="btn" value = "Delete" \
//        onClick="Javacsript:deleteListRow(this)"></td>');
//  }
}
function createManageStudent() {  
  $('#manageStudents').append('<table></table>');
  var table = $('#manageStudents').children();
  
  table.append('<tr><td><b>Name</b></td>\
    <td><b>ID</b></td>\
    <td><b>School</b></td>\
    <td><b>Delete</b></td></tr>');

  table.append('<tr><td>Joe Poodle</td>\
    <td>0000007</td>\
    <td>MSC</td>\
    <td><input type="button" class="btn" value = "Delete" \
      onClick="Javacsript:deleteListRow(this)"></td></tr>');
}
$( document ).ready(function() {
  createAcctReqList();
  //createManageSchool();
  createManageStudent();
});
