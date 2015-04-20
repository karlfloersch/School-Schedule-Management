function deleteListRow(obj, list) {
    $(list).closest('tr').remove();
}
var semesterTable = function (){
  $('#semester').empty();
  $('#semester').append('<table></table>');
  var table = $('#semester').children();

  var numSemester = $('#numberOfSem').val();

  if(Number(numSemester)>=1 && Number(numSemester)<=4){
    $('#err_number_semester').html("");
    table.append('<tr><td><b>Name of Semester In Order</b></td>');

    for(var i = 0; i < numSemester; i++){
        table.append('<tr><td><input type="text" id="semester + i"></td>');
    }
  }
  else{
    $('#err_periods').html("Invalid");
  }
}
var periodLunchList = function () {  
  $('#periodLunch').empty();
  $('#periodLunch').append('<table></table>');
  var table = $('#periodLunch').children();
  var numPeriod = $('#periodInADay').val();

  if(Number(numPeriod)>=6 && Number(numPeriod)<=12){
    $('#err_periods').html("");
    table.append('<tr><td><b>Valid Lunch Periods</b></td>');

    for(var i = 1; i <= numPeriod; i++){
       table.append('<tr><td>Period '+ i +'<input type="checkbox" id="i" value = "i"></td>');
    }
  }
  else{
    $('#err_periods').html("Invalid");
  }
}
function legalBlocksList() {  
  $('#legalBlocks').append('<table></table>');
  var table = $('#legalBlocks').children();
  

  table.append('<tr><td><b>Period Start</b></td>\
    <td><b>Period End</b></td>\
    <td><b>Days Active</b></td>\
    <td><b>Remove</b></td>');

  table.append('<tr><td><input type="text" id="st"></td>\
    <td><input type="text" id="en"></td>\
    <td>Monday <input type="checkbox" id="monday">\
        Tuesday <input type="checkbox" id="tuesday">\
        Wednesday<input type="checkbox" id="wednes">\
        Thursday <input type="checkbox" id="thursday">\
        Friday <input type="checkbox" id="friday"<td>\
    <td></td>');
}
function addToLegalBlocks(){
  var table = $('#legalBlocks').children();

  var s = $('#st').val();
  var e = $('#en').val();
  var numPeriod = $('#periodInADay').val();

  var days = "";
  if($('#monday').is(':checked')) {
    days += "M "
  }
  if($('#tuesday').is(':checked')) {
    days += "Tu "
  }
  if($('#wednes').is(':checked')) {
    days += "W "
  }
  if($('#thursday').is(':checked')) {
    days += "Th "
  }
  if($('#friday').is(':checked')) {
    days += "F"
  }

  if(Number(e) > Number(numPeriod)){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(numPeriod == ""){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(Number(s) < Number(e) && s != '' && e != ''){
    $("#legalBlocks tr:last").remove();

    table.append('<tr><td>' + s + '</td>\
    <td>' + e + '</td>\
    <td>' + days + '</td>\
    <td><input type="button" class="btn" value = "Delete"\
    onClick="Javacsript:deleteListRow(this, this)"></td>');

    table.append('<tr><td><input type="text" id="st"></td>\
      <td><input type="text" id="en"></td>\
      <td>Monday <input type="checkbox" id="monday">\
      Tuesday <input type="checkbox" id="tuesday">\
      Wednesday<input type="checkbox" id="wednes">\
      Thursday <input type="checkbox" id="thursday">\
      Friday <input type="checkbox" id="friday"<td>\
      <td></td>');
  }
}
function start(){
  legalBlocksList();
}
 $(function() {
    $( "#dialog-error-number-period" ).dialog({
      autoOpen: false,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
      effect: "fade",
        duration: 1000
      }
    });
     $( "#dialog-error-number-semesters" ).dialog({
      autoOpen: false,
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
      effect: "fade",
        duration: 1000
      }
    });
  });
$( document ).ready(function() {
  $('#numberOfSem').keyup(semesterTable);
  $('#periodInADay').keyup(periodLunchList);
  $('#daysInAcademicYear').keyup(function (){
    var days = $('#daysInAcademicYear').val();
    if(days < 1 || days > 7){
      $('#err_day_acad').html("Invalid");
    }
    else{
      $('#err_day_acad').html("");
    }
  })
});