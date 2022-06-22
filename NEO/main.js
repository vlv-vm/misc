const url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-05-13&end_date=2022-05-15&api_key=LdhrmPNpdy2dEYhPUuZEv4WAQKHstlx3IzsCEnqe";

const submitBtn = document.querySelector("button");

submitBtn.addEventListener("click", queryAPI);

document.body.addEventListener("click", function(event){
    if(event.target.classList.value === "expand"){
    console.log(event)
    event.target.childNodes[1].classList.toggle("hidden");
    }
})

function queryAPI(){
    const startDate = document.querySelector("input").value;
    const url = `https://api.nasa.gov/neo/rest/v1/feed?start_date=${startDate}&end_date=${startDate}&api_key=LdhrmPNpdy2dEYhPUuZEv4WAQKHstlx3IzsCEnqe`;
    
    document.querySelector("ul").innerHTML = null;

    fetch(url).then(res => res.json())
    .then(data => {
        getRelevantData(data);
    })
}

function getRelevantData(data){
    const neoDates = data.near_earth_objects;
    const objKey = Object.keys(neoDates)[0];
    const numberOfObjects = neoDates[objKey].length;

    for(let i = 0; i < numberOfObjects; i++){
        console.log(neoDates[objKey][i])
        populate(neoDates[objKey][i]);
    }
}

function populate(neo){
    const li = document.createElement("li");
    const div = document.createElement("div");
    const p = document.createElement("p");
    const hiddenP = document.createElement("p");

    hiddenP.classList.add("hidden");
    hiddenP.classList.add("help");
    
    p.innerHTML = "Name: " + neo.name + " <br> " + "ID: " + neo.id + " <br> " + "Potentially hazardous: " + neo.is_potentially_hazardous_asteroid ;
    hiddenP.innerHTML = `Approach date: ${neo.close_approach_data[0].close_approach_date_full} <br>Miss distance: ${neo.close_approach_data[0].miss_distance.kilometers}km <br>Relative velocity: ${neo.close_approach_data[0].relative_velocity.kilometers_per_second} kilometers per second <br>Estimated diameter: ${neo.estimated_diameter.kilometers.estimated_diameter_min}km - ${neo.estimated_diameter.kilometers.estimated_diameter_max}km`;

    div.appendChild(p);
    div.appendChild(hiddenP);

    div.classList.add("expand");

    li.classList.add("dynamicLi");

    li.appendChild(div);

    document.querySelector("ul").appendChild(li);   
}