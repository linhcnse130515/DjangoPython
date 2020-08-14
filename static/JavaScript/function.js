var x1,y1,x2,y2;
var rect1, rect2;



function getPositionXY1(element) 
{ 
	rect1 = element.getBoundingClientRect();
}

function getPositionXY2(element) 
{ 
	rect2 = element.getBoundingClientRect();
	drawLineXY(rect1,rect2)
}


// store our global state here

var lineElem;
function drawLineXY(fromXY, toXY) {
    //if(!lineElem) {
        can = document.getElementById('myCanvas');
        //lineElem.style.position = "absolute";
        can.style.zIndex = -100;
        
    var ctx = can.getContext('2d');
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.lineWidth = 4;
    ctx.strokeStyle = '#09f';
    //ctx.beginPath();
    ctx.moveTo(fromXY.x + 9, 0);
    ctx.lineTo(toXY.x + 9, 150);
    ctx.stroke();
}



