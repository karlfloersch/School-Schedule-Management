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
        table.append('<tr><td><input type="text" name="semester_' + i + '"></td>');
    }
  }
  else{
    $('#err_number_semester').html("Semesters must range from 1-4");
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
       table.append('<tr><td>Period '+ i +'<input type="checkbox" name="lunch_'+ i +'"></td>');
    }
  }
  else{
    $('#err_periods').html("Periods must range from 6-12");
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
      days += "M,";
  }
  if($('#tuesday').is(':checked')) {
      days += "Tu,";
  }
  if($('#wednes').is(':checked')) {
      days += "W,";
  }
  if($('#thursday').is(':checked')) {
      days += "Th,";
  }
  if($('#friday').is(':checked')) {
      days += "F,";
  }

  if(Number(e) > Number(numPeriod)){
    $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(numPeriod == ""){
    $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(days == ""){
    $( "#dialog-error-days" ).dialog( "open" );
  }
  else if(Number(s) <= Number(e) && s != '' && e != ''){
    $("#legalBlocks tr:last").remove();

    table.append('<tr><td class="period_start">' + s + '</td>\
    <td class="period_end">' + e + '</td>\
    <td class="days_active">' + days.substring(0, days.length - 1) + '</td>\
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
function start() {
    legalBlocksList();
}
$( document ).ready(function() {
  //legalBlocksList();
  $('#numberOfSem').keyup(semesterTable);
  $('#periodInADay').keyup(periodLunchList);
  $('#daysInAcademicYear').keyup(function (){
    var days = $('#daysInAcademicYear').val();
    if(days < 15){
      $('#err_day_acad').html("Days much exceed 15");
    }
    else{
      $('#err_day_acad').html("");
    }
  });
    start();
    console.log("Am i working?");
    $("#save_btn").click(function(){
        var start_periods = "";
        var end_periods = "";
        var days_active = "";
        $(".period_start").each(function(i) {
            start_periods += $(this).text() + " ";
        });
        $(".period_end").each(function(i) {
            end_periods += $(this).text() + " ";
        });
        $(".days_active").each(function(i) {
            days_active += $(this).text() + " ";
        });
        $('<input />').attr('type', 'hidden')
            .attr('name', "start_periods")
            .attr('value', start_periods)
            .appendTo('#create_school_form');

        $('<input />').attr('type', 'hidden')
            .attr('name', "end_periods")
            .attr('value', end_periods)
            .appendTo('#create_school_form');

        $('<input />').attr('type', 'hidden')
            .attr('name', "days_active")
            .attr('value', days_active)
            .appendTo('#create_school_form');
    });
});
