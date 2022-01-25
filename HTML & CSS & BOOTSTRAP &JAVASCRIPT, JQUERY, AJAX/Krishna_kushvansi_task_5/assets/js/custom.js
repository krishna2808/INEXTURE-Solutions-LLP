

function calculator(){
    let Field_1, Field_2; 
    let value_1 = document.getElementById("value-1").value;
    let value_2 = document.getElementById("value-2").value;
    let operation = document.getElementById("operation").value;
    document.getElementById("first_feild").innerHTML = ""
    document.getElementById("second_feild").innerHTML = ""
    if(value_1.length>0 && value_2.length> 0){
        value_1 = parseInt(value_1);
        value_2 = parseInt(value_2);
        // console.log(isNaN(operation));
        // console.log(value_2);
        console.log(operation)
        let result;
        if(!isNaN(value_1) && !isNaN(value_2)){
            switch(operation){
                case "add": 
                         result = value_1 + value_2;
                         document.getElementById("result").innerHTML = value_1  + " + " +  value_2 +" = "+ result;
                        break;
                case "sub": 
                           result = value_1 - value_2;
                           document.getElementById("result").innerHTML = value_1  + " - " +  value_2 +" = "+ result;
    
                         break;
                case "multi": 
                          result = value_1 * value_2;
                          document.getElementById("result").innerHTML = value_1  + " * " +  value_2 +" = "+ result;
    
    
                        break;
                case "div": 
                          result = value_1 / value_2;
                          document.getElementById("result").innerHTML = value_1  + " / " +  value_2 +" = "+ result;
    
                        break;
                case "mod": 
                          result = value_1%value_2;
                          document.getElementById("result").innerHTML = value_1  + " % " +  value_2 +" = "+ result;
    
                        break;    
                default:
                       
                        result  = "invaild";
        
            }
            // document.getElementById("result").innerHTML = result;
          
    
           
         
    
        }
        else{
            if(isNaN(value_1) == true){
                document.getElementById("first_feild").innerHTML = "Please Enter Number NOT String  "
    
            }
            if(isNaN(value_2) ==true){
                document.getElementById("second_feild").innerHTML = "Please Enter Number NOT String "
    
            }
            // if(isNaN(operation)==true){
            //     document.getElementById("third_feild").innerHTML = "Select operation"
    
            // }
        }
    
    }
    else{
        if(value_1.length==0){
            document.getElementById("first_feild").innerHTML = "Please Enter Number "

        }
        if(value_2.length == 0){
            document.getElementById("second_feild").innerHTML = "Please Enter Number "

        }
    }
    // console.log(typeof(value_1));
    // console.log(operation);
   
        
    

}