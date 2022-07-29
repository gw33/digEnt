#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable(display=0, logdir="/home/gw33/public_html/cgi-bin/logdir")
 
 
print("""

<html>
 
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Report 5</title>
  </head>
 
  <body>
    <h2> Report 5 - Web Services Application </h2>
    <h4> This site allows for entry of a city and displays the weather conditions using the <i><a href='https://openweathermap.org/api'>OpenWeather API</a></i>.</h4>
 
    <h2> Enter a City: </h2>
    <input type="text" id="wordEntry">
    <button type="submit" onclick="getWeather()"> Submit </button>
 
    <div id="city" style="background-color:#E0E0E0;"> City: </div>
    <div id="high" style="background-color:#E0E0E0;"> High: </div>
    <div id="low" style="background-color:#E0E0E0;"> Low: </div>
    
    <hr>
    
    <script>
    
        function getWeather(){
 
          var input = document.getElementById('wordEntry').value;
          var url = 'https://api.openweathermap.org/data/2.5/weather?q=' + input + '&APPID=19641fa3f7ed52db67852c519cb363cc';
          var city = document.getElementById('city');
          var tempHigh = document.getElementById('high');
          
          fetch(url)
          .then((resp) => resp.json())
          .then(json => console.log(json))
          .then(function(data) {
            let weatherInfo = data[0];
            
            let cityName = document.createElement('cityName');
            cityName.innerHTML = `${weatherInfo.name}`
            city.appendChild(cityName);
            
            let highTemp = document.createElement('highTemp');
            highTemp.innerHTML = `${weatherInfo.main[0].temp_max}`
            tempHigh.appendChild(highTemp);
          })
          .catch(function(error){
            alert(error);
          });
        }
    </script>
 
  </body>
 
</html>
 
            """)
