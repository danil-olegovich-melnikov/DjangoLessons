let start_day = document.getElementById("start_day_filter");
let end_day = document.getElementById("end_day_filter");

function search() {
    window.location = `?start_day=${start_day.value}&end_day=${end_day.value}`
}


function del(pk) {
    fetch('delete/' + pk, {method: 'GET'})
    document.getElementById("trip-" + pk).remove();
}

let modal = document.getElementById("addTripModal");
let btn = document.getElementById("addTrip");
let span = document.getElementsByClassName("close")[0];

btn.onclick = () => modal.style.display = "block";
span.onclick = () => modal.style.display = "none";