/*marker = new L.marker([{{ r['coordinates']['latitude'] }}, {{ r['coordinates']['longitude'] }}]).addTo(mymap)
    .bindPopup('{{ r['title'] }}')
    .openPopup();;*/

marker = new L.marker([lat, lng]).addTo(mymap)
    .bindPopup(title)
    .openPopup();
