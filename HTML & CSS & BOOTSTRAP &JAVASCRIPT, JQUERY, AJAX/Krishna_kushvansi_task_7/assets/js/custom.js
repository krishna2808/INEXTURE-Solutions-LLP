var loadFile = function (event) {
    var imgOut = document.getElementById("outputImage").src = URL.createObjectURL(event.target.files[0]);;
}

function clearFeild(){
    document.getElementById("sucess").innerHTML =  "successful Submited"; 
    first_name = document.getElementById("firstName").value ="";  
    last_name = document.getElementById("lastName").value = '';


    email = document.getElementById("email").value = '';
    url = document.getElementById("url").value = '';
    let password = document.getElementById("password").value = '';
    let con_password =document.getElementById("conformPassword").value = '';
     // radio input from form
    gen_male = document.getElementById("male").checked = false;
    gen_female = document.getElementById("female").checked = false;

    address = document.getElementById("address").value = '';
    phone_number = document.getElementById("phoneNumber").value = '';

    // radio input from form
    let hobby_read = document.getElementById("read").checked = false;
    let hobby_cricket = document.getElementById("cricket").checked = false;
    let hobby_watch = document.getElementById("watch").checked = false;
    document.getElementById("outputImage").remove()

}

function formValidation(){
    let first_name = document.getElementById("firstName").value.split("");
    let last_name = document.getElementById("lastName").value.split("");
    let email = document.getElementById("email").value;
    let url = document.getElementById("url").value;
    let password = document.getElementById("password").value.split("");
    let con_password =document.getElementById("conformPassword").value;
     // radio input from form
    let gen_male = document.getElementById("male").checked;
    let gen_female = document.getElementById("female").checked;

    let address = document.getElementById("address").value;
    let phone_number = document.getElementById("phoneNumber").value;

    // radio input from form
    let hobby_read = document.getElementById("read").checked;
    let hobby_cricket = document.getElementById("cricket").checked;
    let hobby_watch = document.getElementById("watch").checked;
        
    let  image_upload = document.getElementById("imageUpload").value;
    

    // console.log(first_name);
    // console.log(phone_number);
    // console.log(image_upload);
    // document.getElementById("hobbyError").innerHTML =  "";
    // document.getElementById("genderError").innerHTML =  "";
  
   
    

    if(phone_number != '' && image_upload.length != 0 && first_name.length !=0 && last_name.length != 0 && email != '' && password.length != 0 && address != '' && gen_male == true || gen_female == true && hobby_read == true  || hobby_cricket ==true || hobby_watch == true ){
            
            var right_first_name = false;
            var right_last_name = false;
            var right_email = false;
            var right_url = false;
            var right_password = false;
            var right_address = false;
            var right_image = false;
            var right_number = false;
            var right_con_password = false;
            var right_gen = true;
            var right_hobby = true;

         

            for(i=0;i<first_name.length;i++){
                 if( 65 <= first_name[i].codePointAt(0) && 90 >= first_name[i].codePointAt(0) || 97 <= first_name[i].codePointAt(0)  &&  first_name[i].codePointAt(0) <= 122){
                    right_first_name = true;   
                    document.getElementById("firstNameError").innerHTML = "";
                    // console.log("value -------")
                    // console.log(first_name[i])

                 }
                 else{
                     right_first_name = false;
                     document.getElementById("firstNameError").innerHTML = "Enter only Alphabets";

                     break;
                 }
            }
            // ---------------last name ----------------------
            for(i=0;i<last_name.length;i++){
                if( 65 <= last_name[i].codePointAt(0) && 90 >= last_name[i].codePointAt(0) || 97 <= last_name[i].codePointAt(0)  &&  last_name[i].codePointAt(0) <= 122){
                   right_last_name = true;   
                   document.getElementById("lastNameError").innerHTML = "";

                }
                else{
                    right_last_name = false;
                    document.getElementById("lastNameError").innerHTML = "Enter only Alphabets";
                    break;
                   
                }
           }
           // ----------------------------------for email  -----------------------

    //        for(i=0;i< 5 ;i++){
    //         if(  >= url[i].codePointAt(0)){
    //            right_last_name = true;   

    //         }
    //         else{
    //             right_last_name = false;
    //             document.getElementById("lastNameError").innerHTML = "Enter only Alphabets";
    //             break;
               
    //         }
    //    }
            try{


                split_email = email.split("@");
                split_dot = split_email[1].split(".");
                console.log("------ea=mail")
                console.log(split_email[0].length);
                console.log(split_email[1]);
                console.log(split_dot[1].length);
                console.log(split_dot[0].length);
    
                if(split_email[0].length >=3 && split_dot[1].length>=3 && split_dot[0].length>=2){
                    var dot=0;
                    for(i=0;i<email.length;i++){
                        if(email[i] == '.'){
                            dot += 1;
                        }
                        
                    }
                    console.log("in----------for");
                    console.log(dot);
                        if(dot==1){
                            right_email = true
                            document.getElementById("emailError").innerHTML =  "";
    
    
                            
                        }
    
                }
                else{
                    document.getElementById("emailError").innerHTML =  "Enter valid email";
    
                }
            }catch(err){
                document.getElementById("emailError").innerHTML =  "Enter valid email";

            }
           
                  // ----------------------------------for url  -----------------------
              
                 if(url.match('http:') && url.indexOf('p') == 3 ||  url.match('https:') && url.indexOf('s') == 4 ){
                    right_url = true;
                    document.getElementById("urlError").innerHTML =  "";
    
                }  
                else{
                    document.getElementById("urlError").innerHTML =  "Enter valid URL";
                }

         
        //------------------------------------Phone number--------------

          console.log(phone_number)
          console.log(isNaN(phone_number))
          console.log(typeof phone_number)
          console.log("-----------------")
          console.log(phone_number[0])
          if(!isNaN(phone_number)){
              if(phone_number[0] == '9' ||phone_number[0] == '8' || phone_number[0] == '7'){
                 if(phone_number.length == 10){
                    right_number = true
                    document.getElementById("phoneNumberError").innerHTML =  "";

                 }else{
                    document.getElementById("phoneNumberError").innerHTML =  "Only 10 Digit Number";
                 }
              

              }
              else{
                document.getElementById("phoneNumberError").innerHTML =  "The number should be starting 7 , 8 , 9";

              }

          }else{ 

                for(var i; i< phone_number.length ; i++){
                    if(65 <= phone_number[i].codePointAt(0) && 90 >= phone_number[i].codePointAt(0)){
                        document.getElementById("phoneNumberError").innerHTML =  "Enter only number Not alphabet";
                    
                        break;
                    }
                    if(97 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 122){
                        document.getElementById("phoneNumberError").innerHTML =  "Enter only number Not alphabet";
                        break;    
                    }
                    if(48 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 57){
                        document.getElementById("phoneNumberError").innerHTML =  "Enter only number Not Special-Character";
                        break;
                }
                    if(33 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 47  || 58 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 64 || 91 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 96 || 123 <= phone_number[i].codePointAt(0)  &&  phone_number[i].codePointAt(0) <= 126   ){
                        document.getElementById("phoneNumberError").innerHTML =  "Enter only number Not Special-Character";
                        break;
    
                }
    
                } 
              

          }


         //---------------------------------password --------------
          var digit=0; 
          var alph =0;
          var alphUp =0;
          var speChar =0;
          console.log("pass");
          console.log(password)
          for(var i=0; i< password.length ; i++){
              if(65 <= password[i].codePointAt(0) && 90 >= password[i].codePointAt(0)){
                 
                   alphUp =alphUp +  1 ;
                   console.log("alphaUp")
                   console.log(alphUp);

              }
              if(97 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 122){
                    alph = alph +  1;   
                    console.log("alph") 
                    console.log(alph) ;     
              }
              if(48 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 57){
                 digit = digit+ 1;  
                 console.log("digit")   
                 console.log(digit) ;    
             }
               if(33 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 47  || 58 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 64 || 91 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 96 || 123 <= password[i].codePointAt(0)  &&  password[i].codePointAt(0) <= 126   ){
                speChar = speChar +  1  ; 
                console.log("spe")
                console.log(speChar)

             }

          } 
          total_password = speChar +digit +alph + alphUp;
          console.log("jjjjjjjjjjjjjjjjjjjjjjjjjj")
          console.log(total_password)
          if(speChar>=1 && digit >=1 && alphUp >= 1 && alph >=1 && total_password >= 6 && total_password <= 14 ){
              right_password = true
              document.getElementById("passwordError").innerHTML =  "";
                  
          }else{
            document.getElementById("passwordError").innerHTML =  "Enter valid Password";
          }
          //------------------------con-password-------------------------------
                if(con_password.length == password.length){
                    for(var i =0; i<password.length; i++){
                        if(password[i] == con_password[i]){
                            right_con_password = true;
                            document.getElementById("conformPasswordError").innerHTML =  "";

                        }
                        else{
                            document.getElementById("conformPasswordError").innerHTML =  "Password is not match";

                        }
                      
                    }


                }
                else{
                    document.getElementById("conformPasswordError").innerHTML =  "Password is not match";

                }


          //-----------------------------Addresss ----------------------------------  

          if(address.length <= 125){
              right_address = true;
              document.getElementById("addressError").innerHTML =  "";
          }
          else{
            document.getElementById("addressError").innerHTML =  "Enter only 125 character";
          }

          //--------------------image formate-------------
          if( image_upload.endsWith('.jpeg') ||  image_upload.endsWith('.JPEG')||  image_upload.endsWith('.png') ||  image_upload.endsWith('.PNG')){
            right_image = true;
            document.getElementById("imageError").innerHTML =  "";
            // image_upload
            // document.getElementById("demo").innerHTML = image_upload;

        }
        else{
            document.getElementById("imageError").innerHTML =  "Enter valid formate image ";

        } 
        //---------------------------------everything successfully

        if(right_first_name && right_last_name && right_number && right_address && right_password && right_image && right_con_password && right_url&& right_email && right_gen && right_hobby){
           
            clearFeild();
            
            


        }

           
            
    }
    else{
        console.log("Errorooooooooooooooooooooooooooooooooooooor");
        // image_upload.length != 0 &&first_name.length !=0 && last_name.length != 0 && email != '' && password.length != 0 && address != ''
        if(first_name.length ==0 ){

            document.getElementById("firstNameError").innerHTML = "Enter First Name ";

        }
        if(last_name.length ==0 ){

            document.getElementById("lastNameError").innerHTML =  "Enter Last Name";

        }
        if(image_upload.length == '' ){

            document.getElementById("imageError").innerHTML =  "Upload  Image   ";

        }
        if(email.length == '' ){

            document.getElementById("emailError").innerHTML =  "Enter  Email";

        }
        if(password.length == 0 ){

            document.getElementById("passwordError").innerHTML =  "Enter Password ";

        }
        if(url.length == '' ){

            document.getElementById("urlError").innerHTML =  "Enter URL   ";

        }
        // gen_male == true || gen_female == true && hobby_read == true  || hobby_cricket ==true || hobby_watch == true
        if(gen_male != true || gen_female != true){
            document.getElementById("genderError").innerHTML =  "Select Gender";

        }
        if( hobby_read != true  || hobby_cricket !=true || hobby_watch != true){
            document.getElementById("hobbyError").innerHTML =  "Select Hobby ";

        }
        if(phone_number == '' ){

            document.getElementById("phoneNumberError").innerHTML =  "Enter number   ";

        }

    }


}

