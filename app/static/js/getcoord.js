var mymap = L.map('map').locate({setView: true, maxZoom: 16});

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png?lang=it', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);



function getCoord(e){
    var coord = e.latlng;
    var lat = coord.lat;
    var lng = coord.lng;
    var newMarker = L.marker(e.latlng, {draggable:'true'})
	.addTo(mymap)
	.bindPopup('<input class="offscreen" value='+lat+','+lng+' id="coordIN" aria-hidden="true"><button onclick="copyCoord()">Copy coordinates<br>to clipboard</button>')
	.openPopup();
}	

function copyCoord(){
    var coord = document.getElementById("coordIN");

    coord.select();
    coord.setSelectionRange(0, 99999);
    document.execCommand('copy');
    //alert(coord+' are being copied!');
}

mymap.on('click', getCoord);