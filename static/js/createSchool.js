function deleteListRow(obj, list) {
    $(list).closest('tr').remove();
}
function createSemesterTable(){
  $('#semester').empty();
  $('#semester').append('<table></table>');
  var table = $('#semester').children();

  var numSemester = $('#numberOfSem').val();

  if(Number(numSemester)>=1 && Number(numSemester)<=4){
    table.append('<tr><td><b>Name of Semester In Order</b></td>');

    for(var i = 0; i < numSemester; i++){
        table.append('<tr><td><input type = "text" id="semesterName"></td>');
    }
  }
  else{
    $( "#dialog-error-number-semesters" ).dialog( "open" );
  }
}
function periodLunchList() {  
  $('#periodLunch').append('<table></table>');
  var table = $('#periodLunch').children();
  

  table.append('<tr><td><b>Period Start</b></td>\
    <td><b>Period End</b></td>\
    <td><b>Remove</b></td>');

  table.append('<tr><td><input type="text" id="periodStart"></td>\
    <td><input type="text" id="periodEnd"></td>\
    <td></td>');
}
function addToPeriodLunch(){
  var table = $('#periodLunch').children();

  var start = $('#periodStart').val();
  var end = $('#periodEnd').val();
  var numPeriod = $('#periodInADay').val();

  if(Number(end) > Number(numPeriod)){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(numPeriod == ""){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }

  else if(Number(start) < Number(end) && start != '' && end != ''){
    $("#periodLunch tr:last").remove();

    table.append('<tr><td>' + start + '</td>\
    <td>' + end + '</td>\
    <td><input type="button" class="btn" value = "Delete"\
    onClick="Javacsript:deleteListRow(this, this)"></td>');

    table.append('<tr><td><input type="text" id="periodStart"></td>\
      <td><input type="text" id="periodEnd"></td>\
      <td></td>');
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
  periodLunchList();
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