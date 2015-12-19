$(document).ready(function(){
  $('.song').click(function(){
    $(this).addClass('active');

    $.ajax({
      url: 'http://localhost:5000/change',
      type: 'POST',
      data: JSON.stringify({
        'song': $(this).children('.title').text()
      }),
      contentType: 'application/json; charset=UTF-8',
    })
  })
});
