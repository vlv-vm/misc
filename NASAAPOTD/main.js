populate();
function populate(url = "https://api.nasa.gov/planetary/apod?api_key=LdhrmPNpdy2dEYhPUuZEv4WAQKHstlx3IzsCEnqe"){
    fetch(url).then(res => res.json())
    .then(data => {
        console.log(data);
        let title = data.title;
        let date = data.date;
        let copyright = data.copyright;
        let image = data.hdurl;
        let explanation = data.explanation;
        let mediaType = data.media_type;
        console.log(title, date, copyright, image, mediaType, explanation);
        if(mediaType !== "image"){
            let link = data.url;
            document.querySelector("iframe").src = link;
            document.querySelector("iframe").classList.remove("hidden");
            document.querySelector("img").classList.add("hidden");
        }
        else{
            document.querySelector("img").src = image;
            document.querySelector("img").classList.remove("hidden");
            document.querySelector("iframe").classList.add("hidden");
        }
        
        document.querySelector(".title").innerHTML = title;
        document.querySelector(".explanation").innerHTML = explanation;
        document.querySelector(".date").innerHTML = date;
        document.querySelector(".copyright").innerHTML = "Copyright: " + copyright;
    })
    .catch(err => {
        console.log(`error ${err}`);
    })
}


document.querySelector("button").addEventListener("click", () => {
    let inputDate = document.querySelector("input").value;
    let url = `https://api.nasa.gov/planetary/apod?api_key=LdhrmPNpdy2dEYhPUuZEv4WAQKHstlx3IzsCEnqe&date=${inputDate}`;
    populate(url);
})



