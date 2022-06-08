const url = "http://api.open-notify.org/iss-now.json";
var map = L.map('map').setView([45.797394,15.952180], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

function locationISS(){
    fetch(url).then(res => res.json())
    .then(data => {
        console.log(data);
        createCoords(data.iss_position.latitude, data.iss_position.longitude);
    })
}
function createCoords(x,y){
    console.log(x,y)
    var circle = L.circle([x, y], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: 200000
    }).addTo(map);
}

setInterval( _ => locationISS(),1000); 
