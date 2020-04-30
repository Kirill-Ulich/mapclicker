let map;
let popup = L.popup();

function init() {
    map = new L.Map('map').setView([51.505, -0.09], 7);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 18
    }).addTo(map);

    map.on('click', onMapClick);
}

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(map);

    $.ajax({
        type: 'POST',
        url: '/add_point/',
        data: {
            'lat': e.latlng.lat,
            'lng': e.latlng.lng},
        dataType: 'json',
        headers: {'X-CSRFToken': '{{ csrf_token }}'}
    });
}
