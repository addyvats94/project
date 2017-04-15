$(document).ready(function() {

 

 $("#register").click(function(){
        var data={ 
	        	'firstname': $('#fname').val(),
	        	'lastname': $('#lname').val(),
    				'email': $('#cname').val(), 
    				'username': $('#uname').val(),
    				// 'password' $('#fname').val(),
    				'mobile_no': $('#mobile_no').val(),
    				'college': $('#college').val(),
    				'roll_no': $('#roll_no').val(),
            'password': $('#password').val(),       
    				'room_size': $("#room_size input[type='radio']:checked").val(),
    				'room_type': $("#room_type input[type='radio']:checked").val(),    
        }
       
    $.ajax({
       url: "/register/create/",
       method : "POST",
       
       dataType: 'json',
       data: (data),
       success: function(results) {
            alert("Register Successfully ");
            window.open('/login/','self');
           // debugger;
           //getBookmarkStatus($('#article_slug').val());    // this is required because only 'favourite/get/' api returns the
                                                           // id of the bookmark (which is needed when deleting it)
       },
       error: function(results) {
           // debugger;
           console.log('GET_ERROR' + JSON.stringify(results));
           alert("ERROR OCCURED");
        }
	});
 });

});	