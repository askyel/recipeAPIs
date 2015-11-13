
//This is the main function called to make the map
function initialize() {
    var geocoder = new google.maps.Geocoder;
    latitude = 90;
    longitude = 180;
    var latlng = {lat:latitude,lng:longitude}
    var infowindow = new google.maps.InfoWindow; //An info window is what pops up when you click a marker
    //we are going to use this to set up the map
    var mapSettings = {
	zoom: 11,
	center: latlng
    }
    //I think this makes the map not sure, got to look at it
    var map = new google.maps.Map(document.getElementById("map"), mapSettings);
    //actually draws the map
    makeMap(geocoder, map, infowindow, latlng)
}

/*
function codeAddress() {
    var address = document.getElementById("address").value;
    geocoder.geocode({"address":address}, function(results, status) {
	if (status === google.maps.GeocoderStatus.OK) {
	    map.setCenter(results[0].geometry.location);
	    //Makes the marker for the map
	    var marker = new google.map.Marker({
		map: map,
		position: results[0].geometry.location
	    });
	}
	//if something goes wrong
	else {
	    alert("Failed because: " + status);
	}
    });
}
*/

//This is a helper to actually generate the map
function makeMap(geocoder, map, infowindow, latlng) {
    geocoder.geocode({'location':latlng}, function(results, status) {
	if (status === google.maps.GeocoderStatus.OK) {
	    if (results[1]) {
		map.setZoom(11);
		var marker = new google.maps.Marker({
		    position: latlng,
		    map: map
		});
		infowindow.setContent(results[1].formatted_address);
		infowindow.open(map, marker);
	    } else {
		window.alert('No results found');
	    }
	} else {
	    window.alert('Geocoder failed due to: ' + status);
	}
    });
}
