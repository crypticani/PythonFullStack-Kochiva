let weather_icon = document.getElementById('weather-icon');
let temperature = document.querySelector("#temperature span");
let input = document.getElementById("input");
let btn = document.querySelector(".btn");
let inner1 = document.querySelector(".inner-1");
let inner2 = document.querySelector(".inner-2");
let inner3 = document.querySelector(".inner-3");
let inner4 = document.querySelector(".inner-4");
let inner5 = document.querySelector(".inner-5");
let inner6 = document.querySelector(".inner-6");

const cities = document.getElementById("cities")

let api_key = "0fd7f7019c5c42a49fa104303221507"

function handleOnChange(e) {
    let url = `http://api.weatherapi.com/v1/search.json?key=${api_key}&q=${e.value}`;
    fetch(url)
        .then(response => response.json())
        .then((data) => {
            for(let i=0; i<data.length; i++){
                city = data[i].name
                console.log(city)
                cities.innerHTML+=`<option value="${city}">${city}</option>`
            }
        })
}

btn.addEventListener("click", () => {
    temperature.innerText = "Data Fetching....";
    temperature.style.fontSize = "10px";

    let cityname = input.value;

    let url = `http://api.weatherapi.com/v1/current.json?key=${api_key}&q=${cityname}`;
    fetch(url)
        .then(response => response.json())
        .then((data) => {
            // console.log(data);
            let temp = data.current.temp_c;
            temperature.innerText = temp;
            temperature.style.color = "black";
            temperature.style.fontSize = "32px";
            weather_icon.src = data.current.condition.icon

            inner1.innerText = 'Cityname: ' + data.location.name;
            inner2.innerText = 'Country: ' + data.location.country;
            inner3.innerText = 'Feels like: ' + data.current.feelslike_c + ' C';
            inner4.innerText = 'Humidity: ' + data.current.humidity + "";
            inner5.innerText = 'Wind: ' + data.current.wind_kph + " KPH";
            inner6.innerText = 'Condition: ' + data.current.condition.text;
        })
})
