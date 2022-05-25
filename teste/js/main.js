var x = document.getElementById("get");
var city = document.getElementById("city")
function getPlaylists() {
    fetch("http://localhost:5000/playlist?city="+city.value)
        .then( response => {
            console.log(response.json())
        }).catch( error => console.log(error));
}
