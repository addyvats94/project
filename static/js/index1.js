
  $(document).ready(function() {
  
// 	var nice = $("html").niceScroll();  // The document page (body)
	
// 	$("#div1").html($("#div1").html()+' '+nice.version);
    
//     $("#boxscroll").niceScroll({cursorborder:"",cursorcolor:"#00F",boxzoom:true}); // First scrollable DIV

//     $("#boxscroll2").niceScroll("#contentscroll2",{cursorcolor:"#F00",cursoropacitymax:0.7,boxzoom:true,touchbehavior:true});  // Second scrollable DIV
//     $("#boxframe").niceScroll("#boxscroll3",{cursorcolor:"#0F0",cursoropacitymax:0.7,boxzoom:true,touchbehavior:true});  // This is an IFrame (iPad compatible)
	
//     $("#boxscroll4").niceScroll("#boxscroll4 .wrapper",{boxzoom:true});  // hw acceleration enabled when using wrapper
    
 

//  $('#registerform').submit(function() {
//     $('.se-pre-con').css('visibility', 'visible');
//     return true;
// });
 
 
 
 
 function checkpass()
 {
 var a = document.getElementById("pass1").value;
 var b = document.getElementById("pass2").value;
 if(a!=b)
 {
 
$(".checkpass").addClass("has-error");
 
 $("#passerror").show("slide",{direction:'up'},100);
 

 }
 else
 {
 $(".checkpass").removeClass("has-error");
 $(".checkpass").addClass("has-success");
 $("#passerror").hide("slide",{direction:'up'},100);

 }
  if(a=="0"||a==null|| b=="0"||b==null)
 {
 
 $(".checkpass").removeClass("has-error");
 $(".checkpass").removeClass("has-success");
 
 
 }
 
 
 }

 $(".imag").delay(1000).show("fade",1000);
 $("#image1").delay(1000).show("fade",1000);
 $("#image2").delay(1000).show("fade",1000);
 $("#image3").delay(1000).show("fade",1000);
 $("#image4").delay(1000).show("fade",1000);
 $("#image5").delay(1000).show("fade",1000);

   $(".se-pre-con").fadeOut("slow");

 
 function validatemail() {
 $(".se-pre-con").show("fade",100);
 var x = document.getElementById("cname").value;
 
    $.ajax({
         data: {mailer:x} ,
         url: "/register/create/",
         type: 'post',
         // url: 'checkuser.php',
       success: function sub(data){
       var $response=$(data);
  var tot = $response.filter('#one').text();
$(".se-pre-con").hide("fade",100);

if(tot>0){
 $("#already").show("slide",{direction:'up'},100);

}
else{

 $("#already").hide("slide",{direction:'up'},100);

}
     }
   
});



}





function validateuser() {
$(".se-pre-con").show("fade",100);
 var y = document.getElementById("uname").value;
 
    $.ajax({
         data: {username:y} ,
         url: "/register/create/",
         type: 'post',
         // url: 'checkuser.php',
       success: function(data){
       var $response=$(data);
  var pot = $response.filter('#two').text();
$(".se-pre-con").hide("fade",100);

if(pot>0){
 $("#alreadyuser").show("slide",{direction:'up'},100);

}
else{

 $("#alreadyuser").hide("slide",{direction:'up'},100);

}
     }
   
});



}


   $('[data-toggle="tooltip"]').tooltip();

       var showwidth=1;
       if(showwidth==1)
       {

          $(window).resize(function()
          {
            var width=$(window).width();
            document.getElementById("output_width").innerHTML="Window Width:"+width.toString();

          });



  }
});


   
 
 
 
 


