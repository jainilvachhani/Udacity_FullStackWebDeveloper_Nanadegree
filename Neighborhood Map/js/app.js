var infowindow;
var viewModel;
var map;
var markerList = [];

$(function() {
	var locations = [{
		name: "Mount Everest",
		lat:  27.986065,
		lng: 86.922623,
		show: ko.observable(true),
		
	}, {
		name: "Taj Mahal",
		lat: 27.173891,
		lng: 78.042068,
		show: ko.observable(true),
		
	}, {
		name: "Godavari River",
		lat: 16.708548,
		lng: 82.118683,
		show: ko.observable(true),
		
	},  {
		name: "Banaras Hindu University",
		lat: 25.267878,
		lng: 82.990494,
		show: ko.observable(true),
		
	},  {
		name: "University of Mumbai",
		lat: 19.073212,
		lng: 72.854195,
		show: ko.observable(true),
		
	}, ];

	var MyViewModel = function() {
		var self = this;
		self.locations = [];
		for (var x in locations) {
			self.locations.push(locations[x]);
		}
		self.filteredlocations = ko.observableArray(locations);
		self.query = ko.observable('');
		self.search = function(value) {
		self.filteredlocations.removeAll();
			for (var x in self.locations) {
				if (self.locations[x].name.toLowerCase().indexOf(value.toLowerCase()) >= 0) {
					locations[x].setVisible(true);
					//self.filteredlocations.push(self.locations[x]);
				}
				
				
				
			}
			var searchPlaces = self.filteredlocations();
			clearMarkers();
			setMarkers(map, searchPlaces);
		};
		self.locationClicked = function(value) {
			for (var markerIndex in markerList) {
				if (value.name == markerList[markerIndex].title) {
					google.maps.event.trigger(markerList[markerIndex], 'click');
				}
			}
		};
		self.query.subscribe(self.search);

	};
	viewModel = new MyViewModel();

	ko.applyBindings(viewModel);
});


function initmap() {
	var currCenter = new google.maps.LatLng(27.897551, 77.384117);
	var mapOptions = {
		zoom: 5,
		center: currCenter
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	setMarkers(map, viewModel.filteredlocations());
	infowindow = new google.maps.InfoWindow();
	google.maps.event.trigger(map, 'resize');
	map.setCenter(currCenter);
}

function Error() {
	alert("Error");
}

function setMapOnAll(map) {
	for (var i = 0; i < markerList.length; i++) {
		markerList[i].setMap(map);
	}
	markerList.length = 0;
}

function clearMarkers() {
	setMapOnAll(null);
}

function setMarkers(map, places) {
	places.forEach(function(places, index) {
		if (places.show()) {
			var contents = '';
			var target = "https://en.wikipedia.org/api/rest_v1/page/summary/" 
	+ places.name+ 
	"?redirect=false";
	$.getJSON(target, function(data)
	{
		contents   = contents + data.extract;	
	}).fail(function() {
    alert("error");
  });
			var latlong = new google.maps.LatLng(places.lat, places.lng);
			var venues = "";
			
			var marker = new google.maps.Marker({
				position: latlong,
				animation: google.maps.Animation.DROP,
				map: map,
				title: places.name,
				url: viewModel.filteredlocations.url,
			});


			google.maps.event.addListener(marker, 'click', toggleBounce);

			function toggleBounce() {
				if (marker.getAnimation() !== null) {
					marker.setAnimation(null);
				} else {
					marker.setAnimation(google.maps.Animation.BOUNCE);
					setTimeout(function() {
						marker.setAnimation(null);
					}, 2100);
				}
			}

			google.maps.event.addListener(marker, 'click', (function(marker) {
				return function() {
					infowindow.setContent(contents);
					infowindow.open(map, this);
				};
			})(marker));

			markerList.push(marker);
		}
	});
}