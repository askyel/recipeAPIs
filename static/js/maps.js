(function initialize() {
    if (latlng==="") 
	return;
    //Settings for the map
    var mapSetting = {
	center: latlng,
	zoom: 9,
	mapTypeId: google.maps.MapTypeId.HYBRID
    };
    var map = new google.maps.Map(document.getElementById("map"), mapSetting);
    var marker = new google.maps.Marker({
	position: latlng;
    });
    //puts it on the map
    marker.setMap(map);
})();
