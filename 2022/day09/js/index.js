const SIZE = 10;

var content = document.getElementById('content');

for (var y=SIZE; y>-SIZE-1; y--) {
    var row = document.createElement("div");
    row.className = "row";

    for (var x=-SIZE; x<SIZE+1; x++) {
        var el = document.createElement("div");
        el.className = "cell";
        el.id = btoa(`${x},${y}`);
        row.appendChild(el);
    }

    content.appendChild(row);
}

function render(knots) {
    for (var y=SIZE; y>-SIZE-1; y--) {
        for (var x=-SIZE; x<SIZE+1; x++) {
            var label = ".";
            var idx = knots.findIndex(el => el[0] == x && el[1] == y);

            if (idx != -1) {
                label = idx;
            }

            if (label == 0) {
                label = "H";
            }

            var el = document.getElementById(btoa(`${x},${y}`));
            el.innerHTML = label;
        }
    }

}

function chase(head, tail) {
    var [hx, hy] = head;
    var [tx, ty] = tail;

    if (hx > tx) {
        tx++;
    } else if (hx < tx) {
        tx--;
    }

    if (hy > ty) {
        ty++;
    } else if (hy < ty) {
        ty--;
    }

    return [tx, ty];
}


var knots = Array.apply(null, Array(10)).map(() => [0,0]);

render(knots);

document.addEventListener('keydown', (event) => {
    var name = event.key;
    var code = event.code;

    var previousPosition = knots[0];
    switch(code) {
        case 'ArrowLeft':
            knots[0][0] = knots[0][0] - 1;
            break;
        case 'ArrowUp':
            knots[0][1] = knots[0][1] + 1;
            break;
        case 'ArrowRight':
            knots[0][0] = knots[0][0] + 1;
            break;
        case 'ArrowDown':
            knots[0][1] = knots[0][1] - 1;
            break;
    }

    for (var i=1; i<knots.length; i++) {
        // stop if touching
        if (Math.abs(knots[i][0] - knots[i-1][0]) <= 1 && Math.abs(knots[i][1] - knots[i-1][1]) <= 1) {
            break;
        }
        knots[i] = chase(knots[i-1], knots[i]);
    }

    render(knots);
}, false);
