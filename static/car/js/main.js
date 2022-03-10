let search_bar = document.getElementById("car-search-bar");

search_bar.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        search();
    }
});

function search() {
    window.location = `?car_name=${search_bar.value}`
}

function put(pk) {
    let name = document.getElementById(`car-${pk}-name`).innerText
    let price = document.getElementById(`car-${pk}-price`).innerText
    let max_speed = document.getElementById(`car-${pk}-max_speed`).innerText

    fetch('/car/put/', {
        method: 'PUT',
        headers: {'X-CSRFToken': csrf},
        body: JSON.stringify({pk, name, price, max_speed})
    })
}

function del(pk) {
    fetch('/car/delete/' + pk, {method: 'GET'})
    document.getElementById("car-" + pk).remove();
}

let modal = document.getElementById("addCarModal");
let btn = document.getElementById("addCar");
let span = document.getElementsByClassName("close")[0];

btn.onclick = () => modal.style.display = "block";
span.onclick = () => modal.style.display = "none";