var drawing = false;
var canvas, ctx;

window.onload = function() {
	canvas = document.getElementById("canvas");
	ctx = canvas.getContext("2d");
	ctx.beginPath();

	canvas.addEventListener("mousedown", listener);
	canvas.addEventListener("mousemove", listener);
	canvas.addEventListener("mouseup", listener);
	canvas.addEventListener("mouseout", listener);
}

function listener(event) {
	var x = event.pageX - canvas.offsetLeft;
	var y = event.pageY - canvas.offsetTop;
	switch(event.type) {
	case "mousedown":
		drawing = true;
		ctx.moveTo(x, y);
		break;
	case "mousemove":
		if (drawing) {
			ctx.lineTo(x, y);
			ctx.stroke();
		}
		break;
	case "mouseup":
		drawing = false;
		break;
	case "mouseout":
		drawing = false;
		break;
	}
}

function get_image_data() {
    var image_data = ctx.getImageData(canvas.x, canvas.y, canvas.width, canvas.height);
    var data = image_data.data;
    var str = "";
    var temp;

    for (var i = 0; i < data.length; i += 4) {
        temp = parseInt(0.34 * data[i] + 0.5 * data[i + 1] + 0.16 * data[i + 2]);
        str = str + temp.toString() + " ";
    }
    return str;
}