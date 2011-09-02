
    	$(function() {
    		$("#search").append("<input id='partial' name='partial' value='true' type='hidden' />");
    		$("#search").ajaxForm({
        		target:        '#chars',
    		});
    		console.log("HERE", $("#chars"))
    	});