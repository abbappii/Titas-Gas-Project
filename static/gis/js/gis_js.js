//define variables
//map add
const map = new L.Map('map', {
    zoomControl: true,
    keyboard: true,
    center: [23.794974851869533, 90.41417595064569],
    zoom: 13,
    minZoom: 10,
    attributionControl: true
});
//=================Open street map view=================
map.attributionControl.addAttribution('&copy; <a href="#">Project Research & Consultancy(IIC)</a>');
$('.leaflet-control-attribution a').first().css('display', 'none');
$('.leaflet-control-attribution span').first().css('display', 'none');


openStreetMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {});

transparentMap = L.tileLayer('', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">PRC</a> contributors',
    opacity: 0,
    background: 'red'
});


//=================google street map view=================
googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});
//=================Google satellite map view=================
googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
}).addTo(map);
// googleSat.addTo(map)

// marker = L.marker([23.794974851869533, 90.41417595064569]).addTo(map)
//     .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
//     .openPopup();


var controlValIcon = L.icon({

    iconUrl: '../../static/gis/img/valvepit.png',
    // shadowUrl: '../static/img/conval.png',

    iconSize: [20, 20], // size of the icon
    shadowSize: [1, 1], // size of the shadow
    iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
});

var EndCapIcon = L.icon({

    iconUrl: '../../static/gis/img/endcap.png',
    // shadowUrl: '../static/img/conval.png',

    iconSize: [20, 20], // size of the icon
    shadowSize: [1, 1], // size of the shadow
    iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
});

var ReducerIcon = L.icon({

    iconUrl: '../../static/gis/img/reducer.png',
    // shadowUrl: '../static/img/conval.png',

    iconSize: [20, 20], // size of the icon
    shadowSize: [1, 1], // size of the shadow
    iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
});

var RiserIcon = L.icon({

    iconUrl: '../../static/gis/img/riser.png',
    // shadowUrl: '../static/img/conval.png',

    iconSize: [20, 20], // size of the icon
    shadowSize: [1, 1], // size of the shadow
    iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
});


// casing icon create 
var CasingIcon = L.icon({

    iconUrl: '../../static/gis/img/casing.png',
    // shadowUrl: '../static/img/conval.png',

    iconSize: [20, 20], // size of the icon
    shadowSize: [1, 1], // size of the shadow
    iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
});


//marker while click and press ctrl + click
var control = false;
$(document).on('keyup keydown', function (e) {
    control = e.ctrlKey;
});
let marker;
map.on('click', function (e) {
    if (control) {
        try {
            if (map.hasLayer(marker)) {
                marker.remove();

            }
        } catch (e) {
            console.log(e)
        }

        var latLng = e.latlng
        marker = L.marker([latLng.lat, latLng.lng]);
        marker.addTo(map).bindPopup(`${latLng}`).openPopup()
    }


    // L.popup().setLatLng(e.latlng)
    //     .setContent(`Lat: ${latLng.lat}, Lng: ${latLng.lng}`)
    //     .openOn(map);
})


$('#point-center').on('click', function () {
    map.flyTo([23.794974851869533, 90.41417595064569], 15);
})


//Set Current location

L.Control.geocoder().addTo(map);


var getGps = false;
let gpsMap;
let fitTrack = false;

$('#current-location').on('click', function (e) {
    getGps = getGps ? false : true;
    fitTrack = true;
    if (getGps) {
        GpsSupportCheck()
        $(this).css({'color': 'blue'});
    } else {
        clearInterval(gpsMap);
        $(this).css({'color': 'white'});
        if (mark) {
            map.removeLayer(mark)
        }

        if (circle) {
            map.removeLayer(circle)
        }
        map.flyTo([23.794974851869533, 90.41417595064569], 13);

    }
});


// const options = {
//   enableHighAccuracy: true,
//   timeout: 5000,
//   maximumAge: 0
// };
//
// function success(pos) {
//   const crd = pos.coords;
//
//   console.log('Your current position is:');
//   console.log(`Latitude : ${crd.latitude}`);
//   console.log(`Longitude: ${crd.longitude}`);
//   console.log(`More or less ${crd.accuracy} meters.`);
// }
//
// function error(err) {
//   console.warn(`ERROR(${err.code}): ${err.message}`);
// }
//
// navigator.geolocation.getCurrentPosition(success, error, options);


function GpsSupportCheck() {
    if (!navigator.geolocation) {
        console.log("Your browser doesn't support geolocation feature!")
    } else {
        navigator.geolocation.getCurrentPosition(getPosition)
        gpsMap = setInterval(() => {
            navigator.geolocation.getCurrentPosition(getPosition)
        }, 5000);
    }
}

var mark, circle, lat, long, accuracy;

function getPosition(position) {
    // console.log(position)
    lat = position.coords.latitude
    long = position.coords.longitude
    accuracy = position.coords.accuracy

    if (mark) {
        map.removeLayer(mark)
    }

    if (circle) {
        map.removeLayer(circle)
    }

    mark = L.marker([lat, long])
    circle = L.circle([lat, long], {radius: 10})

    var featureGroup = L.featureGroup([mark, circle]).addTo(map);
    if (fitTrack) {
        map.flyToBounds(featureGroup.getBounds(),{duration: 3});
        fitTrack = false;
    }
    console.log("Your coordinate is: Lat: " + lat + " Long: " + long + " Accuracy: " + accuracy)
}