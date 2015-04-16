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
  if(start.value < end.value){
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
  row.insertCell(2).innerHTML= '<input type="text" id="daysActive">';
  row.insertCell(3).innerHTML= '';  
}
function addToLegalBlocks(){
  var s = document.getElementById("st");
  var e = document.getElementById("en");
  var days = document.getElementById("daysActive");

  var table = document.getElementById("legalBlocks");

  var rowCount = table.rows.length - 1;
  if(s.value < e.value){
    var row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= s.value;
    row.insertCell(1).innerHTML= e.value;
    row.insertCell(2).innerHTML= days.value;
    row.insertCell(3).innerHTML= '<input type="button" value = "Delete"\
    onClick="Javacsript:deleteListRow(this, legalBlocks)">';

    rowCount = rowCount + 1;
    s.value = '';
    e.value = '';
    days.value = '';

    table.deleteRow(rowCount);
    row = table.insertRow(rowCount);
    row.insertCell(0).innerHTML= '<input type="text" id="st">';
    row.insertCell(1).innerHTML= '<input type="text" id="en">';
    row.insertCell(2).innerHTML= '<input type="text" id="daysActive">';
    row.insertCell(3).innerHTML= '';
  }
}
function start(){
  periodLunchList();
  legalBlocksList();
}