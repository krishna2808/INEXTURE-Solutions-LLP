var images = [
    "assets/images/11.jpeg",
    "assets/images/12.jpeg",
    "assets/images/13.jpeg",
    "assets/images/14.jpeg",
    "assets/images/15.jpeg",
    "assets/images/16.jpeg",
    "assets/images/17.jpeg",
    "assets/images/18.jpeg"

];
var index = 0;

function slider(){
    document.getElementById("image").src = images[index];
    if(index < (images.length-1)){
        index += 1;
    }
    else{
        index = 0;
    }

}
setInterval(slider, 2000);


function knowMe(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
            if(this.readyState == 4 && this.status == 200){
                console.log(this.responseText);
                document.getElementById("id1").innerHTML = this.responseText
            }
    };


    xhttp.open('GET', "assets/files/ajax.txt", true);
    xhttp.send();

}




$(document).ready(function(){
//   ---------------------------Show Data -----------------------------------------------------
        $("#show-data").click(function(){
            document.getElementById("id2").innerHTML = "";
            document.getElementById("id3").innerHTML = "";
            document.getElementById("table").style.display = "inline";
            $.getJSON("assets/files/ajax.json", 
                function (data) {
            var employees = '';

          
            $.each(data, function (key, value) {
            //    console.log("---------show data-------");
            //    console.log(data[0]);
            //    console.log([key].User_Name);

            //    console.log(value);
              

            
                employees += '<tr>';
                employees += '<td>' + 
                    value.User_Name + '</td>';

                employees += '<td>' + 
                    value.Email_Id+ '</td>';

                employees += '<td>' + 
                    value.Experience + '</td>';

                employees += '<td>' + 
                    value.Number + '</td>';

                employees += '</tr>';
            });
              
            //INSERTING ROWS INTO TABLE 
            $('#table').append(employees);
            
            
        });
        


        });
        // -------------------------------Hide Data------------------------------------------
        $("#hide-data").click(function(){
            document.getElementById("id2").innerHTML = "";
            document.getElementById("id3").innerHTML = "";
            document.getElementById("table").style.display = "none";
        });

          //   ------------------------Delete Data ---------------------------------------

        $("#delete-user-btn").click(function(){
            document.getElementById("id2").innerHTML = "";
            // document.getElementById("id3").innerHTML = "";
            document.getElementById("table").style.display = "none";
            var UpdateEmployees = '';
            username = document.getElementById("delete-username").value;

            $.getJSON("assets/files/ajax.json", 
                function (data) {
          
            var updateData;
          
            $.each(data, function (key, value) {
               console.log("----------------");
            //    console.log(data);
            //    console.log([key].User_Name);
            //    console.log(value);
            //    console.log("username" + username);
            
               if(username == value.User_Name){
                   delete data[key];
                   console.log("successfully deleted data ")
                   updateData = data;

                   for(i in updateData){

                    console.log(i)
                    console.log(updateData[i].User_Name); 
                    UpdateEmployees += '<tr>';
                    UpdateEmployees += '<td>' + 
                        updateData[i].User_Name + '</td>';
    
                        UpdateEmployees += '<td>' + 
                        updateData[i].Email_Id+ '</td>';
    
                        UpdateEmployees += '<td>' + 
                        updateData[i].Experience + '</td>';
    
                        UpdateEmployees += '<td>' + 
                        updateData[i].Number + '</td>';
    
                        UpdateEmployees += '</tr>';
    
                    }
                    $('#table2').append(UpdateEmployees);
                    document.getElementById("table").style.display = "inline";
                    document.getElementById("table2").style.display = "inline";
                   
                    document.getElementById("id4").innerHTML = 'NEW RECORD';

                    document.getElementById("id2").innerHTML = username +"'s record has been deleted.";
                    // document.getElementById("id3").innerHTML = " ";
               
               }
               else{
                   var a;
                //   document.getElementById("id3").innerHTML = "USER NAME IS NOT FOUND";
               

               }
               
            //    console.log(updateData)
               
             
            
            });
        
           
        });
        // document.getElementById("table").style.display = "inline";


        });

  
         
});
// console.log(assets/ajax.json);
// const fs = require('fs');

// function loadJson(filename = ''){
//      return JSON.parse(fs.existsSync(filename) 
//         ? fs.readFileSync(filename).toString(): '""'
//      )
     
// }

// function saveJSON(filename='', json='""'){
//     return fs.writeFileSync(filename, JSON.stringify(json))
// }
// const data = loadJson("assets/ajax.json");

// saveJSON("assets/ajax.json", data)
// console.log(assets/ajax.json);