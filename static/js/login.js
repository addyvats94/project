$(document).ready(function() {



 $("#login").click(function(){
        var data={
                 'username': $('#email').val(),
                 'password': $('#password').val()
        };

    $.ajax({
       url: "/login/",
       method : "POST",

       dataType: 'json',
       data: (data),
       
       
       success: function(results) {
            $.cookie('access_token', (results.message.access_token));
            $.cookie('first_name', (results.message.first_name));
            $.cookie('last_name', (results.message.last_name));
            $.cookie('email', (results.message.email));
            alert('login successfully');
            window.location.replace('/hostel/room/');

           //getBookmarkStatus($('#article_slug').val());    // this is required because only 'favourite/get/' api returns the
                                                           // id of the bookmark (which is needed when deleting it)
       },
       error: function(results) {
           // debugger;
           alert('error OCCURED,email should be valid and password should be strong');
           console.log('GET_ERROR' + JSON.stringify(results));
        }
  });
 });

 $("#logout").click(function(){
        var data={
        };

    $.ajax({
       url: "/logout/",
       method : "POST",
       headers: {
            'Authorization': 'Bearer ' + $.cookie('access_token')
          },
       dataType: 'json',
       data: (data),
       success: function(results) {
            alert("logout successfully");
            window.location.replace('/');


           //getBookmarkStatus($('#article_slug').val());    // this is required because only 'favourite/get/' api returns the
                                                           // id of the bookmark (which is needed when deleting it)
       },
       error: function(results) {
           // debugger;
           alert("ERROR OCCURED");
           console.log('GET_ERROR' + JSON.stringify(results));
        }
	});
 });

});