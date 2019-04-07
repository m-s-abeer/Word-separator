let printConsole = (msg) =>{
  $("#console_output").html($("#console_output").html() + msg + '\n');
  $("#console_output").animate({ scrollTop: $('#console_output').prop("scrollHeight")}, 1000);
}

let printDataList = (data) => {
  console.log('printing data');
  console.log(data);
  $('#fetchedData').html('');
  var cnt=20;
  data.forEach(element => {
    if(cnt===0) return;
    $('#fetchedData').append('<li>'+element[1]+'[Score:'+element[0]+']'+'</li>');
    cnt--;
  });
}

let printBestResults = (data) => {
  console.log('printing data');
  console.log(data);
  $('#best_results').html('');
  data.forEach(element => {
    if(element[0]!==data[0][0]) return;
    $('#best_results').append('<li>'+element[1]+'</li>');
  });
}

let submitNlq = () =>{
  $.ajax({
    url: '/query',
    method: 'POST',
    dataType: 'JSON',
    data: {'query': $("#nlq").val()},
    success: (msg) => {
      console.log('Query Returned!');
      printConsole('Query: '+msg.query);
      $("#best-result").val(msg.data[0][1]);
      console.log('Query: ' + msg.data)
      printDataList(msg.data);
      printBestResults(msg.data);
    }
  });
}


document.getElementById("nlq").addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("qSubmit").click();
  }
});

let startup = () => {

}

window.onload = startup;
