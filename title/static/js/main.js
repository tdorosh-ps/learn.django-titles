function initDone() {
	$('input[type="checkbox"]').click(function(event) {
		var box = $(this);
		$.ajax(box.data('url'), {
			'type': 'GET',
			'async': true,
			'dataType': 'json',
			'data': {
				'done': box.is(':checked') ? 'on': ''
			}
		})
	});
}

$(document).ready(function() {
	initDone();
});