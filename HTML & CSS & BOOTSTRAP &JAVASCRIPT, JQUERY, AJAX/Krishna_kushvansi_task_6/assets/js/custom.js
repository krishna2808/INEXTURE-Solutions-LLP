$(document).ready(function(){

    // <!-- --------   For Browser  Event of Scroll Function ...........  -->  
    
    content =    document.getElementById("temp");
    

    $( "#target" ).scroll(function() {
        $( "#log" ).append( "<div>Handler for .scroll() called.</div>" );
        console.log("hey you are scrolling of div Element...");
        document.getElementById("temp1").innerHTML = "You are scrolling... ";

      });
  
      

    // <!-- --------   keyboard   Events of Changing body background ...........  -->           

     $("body").keypress(function(){
        //   $("body").css('background-color', 'orange');
        //   content.innerHTML = "You are press any-key so body-background color is Orange ";

     });
     $("body").keyup(function(){
        // $("body").css('background-color', 'white');
        // content.innerHTML = "You are press Up-arrow so body-background color is white "
        document.getElementById("image").src = "assets/images/keyboard_key_up.png";


        // content.innerHTML = "";
     
         });
        
     $("body").keydown(function(){
        // $("body").css('background-color', 'blue');
        // content.innerHTML = "You are press Down-arrow so body-background color is blue ";
        document.getElementById("image").src = "assets/images/keyboard_key_down.png";

      
   });

   //--------------------------Manipulation------------------
     $("#removeListElement").click(function(){
         $("ul").remove();
     });
     $("#green-color").click(function(){
         $("#div-color").css("background-color", "green");

     });
     $("#yellow-color").click(function(){
        $("#div-color").css("background-color", "yellow");

    });
    $("#pink-color").click(function(){
        $("#div-color").css("background-color", "pink");

    });
    $("#red-color").click(function(){
        $("#div-color").css("background-color", "red");

    });

     //---------------------form set data using jquery-----------

     $('#sname').val("prince");
     $("#semail").val("prince@gmail.com");

   
   // ---------------------mouse event -----------------------
   $("#mouse-event").click(function(){
       $("#mouse-event").css("background-color", "green");
   });
   $("#mouse-event").dblclick(function(){
       $("#mouse-event").css("background-color", "orange");
   });
   $("#mouse-event").contextmenu(function(){
    $("#mouse-event").css("background-color", "red");
   });
   $("#mouse-event").mouseenter(function(){
    $("#mouse-event").css("background-color", "blue");
   });
   $("#mouse-event").mouseleave(function(){
    $("#mouse-event").css("background-color", "white");
    });

    //----------------------------------Empty-boxes--------------------------------------
    $("#emptyBox").click(function(){
        $("#manipulation , #mouse-event, #keyboard-event, #target"  ).empty();
    });
   

    //--------------------------Delete-form--------------------------------
    $("#delete-form").click(function(){
        $("#student-form").remove();

    });

    $("#delete-form").click(function(){
        $("#student-form").remove();
    });

    $("#delete-box").click(function(){
        $("#student-form,  #manipulation , #mouse-event, #keyboard-event, #target, #delete-box, #emptyBox, #temp1").remove();
    });

    
//----------------------Hide and Show images---------------------------------

    $("#hide").click(function(){
        $(".owl-carousel, .grid").hide();
    });
    $("#show").click(function(){
        $(".owl-carousel, .grid").show();
    });
  
  

// -------------------------- owlcarousel --------------------------------------------------------------------------
    
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });

/* <!----------------------Mansonry ---------------> */
            var grid = document.querySelector('.grid');

            var msnry = new Masonry( grid, {
            itemSelector: '.grid-item',
            columnWidth: '.grid-sizer',
            percentPosition: true
            });

            imagesLoaded( grid ).on( 'progress', function() {
            // layout Masonry after each image loads
            msnry.layout();
            });

     


 


});



