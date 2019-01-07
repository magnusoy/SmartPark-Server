function initMap() {

    var options = {
        zoom: 15,
        center: {
            lat: 62.7372,
            lng: 7.1607
        }
    };
    var map = new google.maps.Map(document.getElementById("map"), options);
    const Url = 'http://localhost:5000/parkinglots'
    var nearbyButtons = new Array();
    var nearbyCoords = new Array();
    fetch(Url)
        .then(data => {
            return data.json()
        })
        .then(function (data) {
            let size = 0;
            let empty = 0;
            let coords = '';
            for (let index = 0; index < data.length; index++) {
                size = data[index]['size'];
                empty = data[index]['empty'];
                coords = data[index]['location'];
                let lat = parseFloat(coords.split(',')[0]);
                let lng = parseFloat(coords.split(',')[1]);
                let content = empty + "/" + size;
                // Parkinglist
                var parkinglotButton = document.createElement("button");
                parkinglotButton.Name = "button-" + index + 1;
                parkinglotButton.className = "btn btn-secondary";
                var text = document.createTextNode(data[index]['name'] + ' : ' + content);
                parkinglotButton.appendChild(text);
                document.getElementById("parkingList").appendChild(parkinglotButton);
                nearbyButtons.push(parkinglotButton);
                nearbyCoords.push(coords);
                addMarker({
                    coords: {
                        lat: lat,
                        lng: lng
                    },
                    iconImage: "https://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png",
                    content: content
                });
            }
            for (let index = 0; index < nearbyButtons.length; index++) {
                const button = nearbyButtons[index];
                const nearbyCoord = nearbyCoords[index];
                button.addEventListener("click", function () {
                    setCenterMap(nearbyCoord);
                });
            }
        });
    var infoWindow = new google.maps.InfoWindow;
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            addMarker({
                coords: {
                    lat: pos.lat,
                    lng: pos.lng
                },
                iconImage: "",
                content: "My location"
            });

            map.setCenter(pos);
        }, function () {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }


    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
            'Error: The Geolocation service failed.' :
            'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
    }


    function addMarker(props) {
        var marker = new google.maps.Marker({
            position: props.coords,
            map: map
        });

        if (props.iconImage) {
            marker.setIcon(props.iconImage);
        }

        if (props.content) {
            var infoWindow = new google.maps.InfoWindow({
                content: props.content
            });

            marker.addListener("click", function () {
                infoWindow.open(map, marker);
            });
        }
    }

    function setCenterMap(position) {
        let lat = parseFloat(position.split(',')[0]);
        let lng = parseFloat(position.split(',')[1]);
        var pos = {
            lat: lat,
            lng: lng
        };
        map.setCenter(pos);
        map.setZoom(15);
    }
}