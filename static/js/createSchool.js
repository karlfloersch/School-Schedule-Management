function deleteListRow(obj, list) {
      
    var index = obj.parentNode.parentNode.rowIndex;
    list.deleteRow(index);
}
function periodLunchList() {  
  var table = document.getElementById("periodLunch");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Period Start</b>";
  row.insertCell(1).innerHTML= "<b>Period End</b>";
  row.insertCell(2).innerHTML= "<b>Remove</b>";

  rowCount = rowCount + 1;
  row = table.insertRow(rowCount);
  row.insertCell(0).innerHTML= '<input type="text" id="periodStart">';
  row.insertCell(1).innerHTML= '<input type="text" id="periodEnd">';
  row.insertCell(2).innerHTML= "";
}
function addToPeriodLunch(){
  var start = document.getElementById("periodStart");
  var end = document.getElementById("periodEnd");

  var table = document.getElementById("periodLunch");
  var rowCount = table.rows.length - 1;

  var numPeriod = document.getElementById("periodInADay");

  if(Number(end.value) > Number(numPeriod.value)){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(numPeriod.value == ""){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }

  else if(Number(start.value) < Number(end.value) && start.value != '' && end.value != ''){
    var row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= start.value;
    row.insertCell(1).innerHTML= end.value;
    row.insertCell(2).innerHTML= '<input type="button" value = "Delete"\
    onClick="Javacsript:deleteListRow(this, periodLunch)">';

    rowCount = rowCount + 1;
    start.value = '';
    end.value = '';
    table.deleteRow(rowCount);
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= '<input type="text" id="periodStart">';
    row.insertCell(1).innerHTML= '<input type="text" id="periodEnd">';
    row.insertCell(2).innerHTML= '';
  }
}
function legalBlocksList() {  
  var table = document.getElementById("legalBlocks");

  var rowCount = table.rows.length;
  var row = table.insertRow(rowCount);

  row.insertCell(0).innerHTML= "<b>Period Start</b>";
  row.insertCell(1).innerHTML= "<b>Period End</b>";
  row.insertCell(2).innerHTML= "<b>Days Active</b>";
  row.insertCell(3).innerHTML= "<b>Remove</b>";

  rowCount = rowCount + 1;
  row = table.insertRow(rowCount);
  row.insertCell(0).innerHTML= '<input type="text" id="st">';
  row.insertCell(1).innerHTML= '<input type="text" id="en">';
  row.insertCell(2).innerHTML= 'Monday <input type="checkbox" id="monday">\
  Tuesday <input type="checkbox" id="tuesday">\
  Wednesday<input type="checkbox" id="wednes">\
  Thursday <input type="checkbox" id="thursday">\
  Friday <input type="checkbox" id="friday">';
  row.insertCell(3).innerHTML= '';
}
function addToLegalBlocks(){
  var s = document.getElementById("st");
  var e = document.getElementById("en");

  var table = document.getElementById("legalBlocks");
  var rowCount = table.rows.length - 1;

  var numPeriod = document.getElementById("periodInADay");

  var mon = document.getElementById("monday");
  var tues = document.getElementById("tuesday");
  var wed = document.getElementById("wednes");
  var thur = document.getElementById("thursday");
  var fri = document.getElementById("friday");
  
  var days = "";

  if(mon.checked == 1){
    days += "M "
  }
  if(tues.checked == 1){
    days += "Tu "
  }
  if(wed.checked == 1){
    days += "W "
  }
  if(thur.checked == 1){
    days += "Th "
  }
  if(fri.checked == 1){
    days += "F"
  }
  

  if(Number(e.value) > Number(numPeriod.value)){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }
  else if(numPeriod.value == ""){
      $( "#dialog-error-number-period" ).dialog( "open" );
  }

  else if(Number(s.value) < Number(e.value) && s.value != '' && e.value != ''){
    var row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= s.value;
    row.insertCell(1).innerHTML= e.value;
    row.insertCell(2).innerHTML= days;
    row.insertCell(3).innerHTML= '<input type="button" value = "Delete"\
    onClick="Javacsript:deleteListRow(this, legalBlocks)">';

    days = "";

    rowCount = rowCount + 1;
    s.value = '';
    e.value = '';
    days.value = '';

    table.deleteRow(rowCount);
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= '<input type="text" id="st">';
    row.insertCell(1).innerHTML= '<input type="text" id="en">';
    row.insertCell(2).innerHTML= 'Monday <input type="checkbox" value = "M" id="monday"> \
    Tuesday <input type="checkbox" value = "Tues" id="tuesday"> \
    Wednesday<input type="checkbox" id="wednes"> \
    Thursday <input type="checkbox" id="thursday"> \
    Friday <input type="checkbox" id="friday">';
    row.insertCell(3).innerHTML= '';
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
  });