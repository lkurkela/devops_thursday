var tid = setInterval(timerApiCall, 5000);

function timerApiCall() {
	$.ajax({
		url: '/api/status',
		success: updateStatus,
		timeout: 3000
	});
}

function updateStatus(data) {
	console.log(data);
	var newHost = true;
	
	var table = $('#apitable').DataTable();
	table.rows().every( function () {
		var d = this.data();
		if (d.server == data.host) {
			newHost = false;
			d.count++;
			d.version = data.version;
		}
		this.invalidate(); 
	} );
	
	if (newHost) {
		table.rows.add([{"server": data.host, "count": 1, "version": data.version} ]);
	}
	
	table.draw();	
}

$(document).ready(function() {
	$('#apitable').DataTable( {
		"info": false,
		"paging": false,
		"processing": true,
		"searching": false,
        "data": [],
	    "columns": [
	       { "title": "Server", "data": "server" },
	       { "title": "Count", "data": "count" },
		   { "title": "Version", "data": "version"}
	    ],
		"order": [[1, "desc"]]
	} );

	$('#requestrate').change(function() {
	   var rate = $('#requestrate').val();
	   console.log("changed to " + rate);
	   clearInterval(tid);
	   tid = setInterval(timerApiCall, rate);
	} );
} );

