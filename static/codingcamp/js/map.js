jQuery(function($) {
    // Asynchronously Load the map API 
    var script = document.createElement('script');
    script.src = "http://maps.googleapis.com/maps/api/js?sensor=false&callback=initialize";
    document.body.appendChild(script);
});

function initialize() {
    var map;
    var bounds = new google.maps.LatLngBounds();
    var mapOptions = {
        mapTypeId: 'roadmap'
    };
                    
    // Display a map on the page
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
    map.setTilt(45);
        
    // Multiple Markers
    var markers = [
        ['cipete', -6.273876, 106.801841],
        ['kemang' , -6.269996, 106.815098],
        ['bintaro' , -6.257967, 106.736984],
        ['sekolah cikal', -6.293181, 106.803639],
        ['sekolah highscope', -6.293018, 106.804211],
        ['sekolah nizamia', -6.307024, 106.898264],
        ['sekolah stella maris', -6.241419, 106.618013],
        ['sekolah santa ursula', -6.167755, 106.833127],
        
    ];
                        
    // Info Window Content
    var infoWindowContent = [
        ['<div class="info_content">' +
        '<h3>Satoe Residence Cipete</h3>' +
        '<p>Jl. Ros 1 e, masuk dari Jl. Haji Junaidi, Cipete Selatan</p> <img src="/static/codingcamp/img/map/cipete.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>Plaza 88 Kemang</h3>' +
        '<p>Jl. Kemang Raya kav. 88, Jakarta Selatan (lantai 2)</p> <img src="/static/codingcamp/img/map/kemang.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>Bintaro</h3>' +
        '<p>Ruko Multiguna sektor 3A, Blok O-8</p> <img src="/static/codingcamp/img/map/bintaro.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>SD Cikal</h3>' +
        '<p> Jalan Tb. Simatupang Kav.18, Cilandak, Daerah Khusus Ibukota Jakarta 12430</p> <img src="/static/codingcamp/img/map/sekolah cikal.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>SD. High Scope International</h3>' +
        '<p>JI TB Simatupang No. 8. Cilandak Barat, Jakarta 12430</p> <img src="/static/codingcamp/img/map/sekolah highscope.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>SD Nizamia</h3>' +
        '<p>Jl. Mabes Hankam No. 15-16, Bambu Apus, Cipayung, Daerah Khusus Ibukota Jakarta 13890</p> <img src="/static/codingcamp/img/map/sekolah nizamia.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>Stella Maris International Gading Serpong</h3>' +
        '<p>Jl. Vatican Cluster Sektor 8A, Gading Serpong, Tangerang, Banten</p> <img src="/static/codingcamp/img/map/sekolah stella maris.jpg">' +        '</div>'],
        ['<div class="info_content">' +
        '<h3>SD Santa Ursula, Jakarta Pusat</h3>' +
        '<p>Jl. Pos no.2 , Pasar Baru, Sawah Besar, Daerah Khusus Ibukota Jakarta 10110</p> <img src="/static/codingcamp/img/map/sekolah santa ursula.jpg">' +        '</div>'],
    ];
        
    // Display multiple markers on a map
    var infoWindow = new google.maps.InfoWindow(), marker, i;
    
    // Loop through our array of markers & place each one on the map  
    for( i = 0; i < markers.length; i++ ) {
        var position = new google.maps.LatLng(markers[i][1], markers[i][2]);
        bounds.extend(position);
        marker = new google.maps.Marker({
            position: position,
            map: map,
            title: markers[i][0]
        });
        
        // Allow each marker to have an info window    
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.setContent(infoWindowContent[i][0]);
                infoWindow.open(map, marker);
            }
        })(marker, i));

        // Automatically center the map fitting all markers on the screen
        map.fitBounds(bounds);
    }

    // Override our map zoom level once our fitBounds function runs (Make sure it only runs once)
    var boundsListener = google.maps.event.addListener((map), 'bounds_changed', function(event) {
        this.setZoom(12);
        google.maps.event.removeListener(boundsListener);
    });
    
}
