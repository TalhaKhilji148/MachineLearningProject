function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getGarageValue() {
    var uiGarage = document.getElementsByName("uiGarage");
     console.log(`This is garage ${uiGarage}This is type ${typeof(uiGarage)} `);
    for(var i in uiGarage) {
      if(uiGarage[i].checked) {
          return parseInt(i);
          console.log(`This is garage ${uiGarage}This is type ${typeof(uiGarage)} `);
      }
    }
    return -1; // Invalid Value
  }
//The parseInt function converts its first argument to a string, parses that string, then returns an integer or NaN
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var portion=  document.getElementById("uiPortion").value;
    var garage=getGarageValue();
    var House_location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");
    
   
    
  
    var url = "http://127.0.0.1:5000/predict_rent_a_house_price"; 
    var squarefeet=parseFloat(sqft)

   
    if(squarefeet>0){
        if(squarefeet<4500){
            $.post(url, {
                total_sqft: sqft,
                beds: bhk,
                baths: bathrooms,
                House_location: House_location,
                portion:portion,
                garage:garage
            },
            function(data, status) {
                console.log(data.estimated_price);
                estPrice.innerHTML = "<h2>" + (data.estimated_price/553772).toString() + "Eth. </h2>";
                console.log(status);
            });

        }else{
            estPrice.innerHTML = "<h2>" + 0 + " Eth.</h2>";
            alert("Sorry! Can't Estimate the Price, The value for Squarefeet should be less then 45000.")
            
        }

    }
    else{
        estPrice.innerHTML = "<h2>" + 0 + " Eth.</h2>";
        setTimeout(() => {  console.log("World!"); }, 2000);
        alert("Sorry! Can't Estimate the Price, The value for Squarefeet should be greater then 0.")
        
    }
       


    
  }

function onPageLoad() {
    console.log( "document loaded" );
    //using Jquery $ to get the request 
     var url = "http://127.0.0.1:5000/get_location_names_for_rent_a_house"; 
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var House_location = data.House_location;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in House_location) {
                var opt = new Option(House_location[i]);
                $('#uiLocations').append(opt);
                //jQuery append option in select dropdown from json 
            }
        }
    });
  }
  
  window.onload = onPageLoad;