const url = "http://api.open-notify.org/iss-now.json"

const locationISS = () => {
    fetch(url).then(res => res.json())
    .then(data => {
        console.log(data);
        document.querySelector("h3").innerHTML=`ISS Location | x: ${data.iss_position.longitude} | y: ${data.iss_position.latitude}`;

    })
};

locationISS()
setInterval( _ => locationISS(),1000); 

var container = document.getElementById( "globalArea" );
var controller = new GIO.Controller( container );
//controller.addData( data );
//controller.setTransparentBackground(true);
controller.init();