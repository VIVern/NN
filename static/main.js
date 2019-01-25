let singleW = singleH = 10;
let w = h = 500 / singleW;
let color = ['green', 'red', 'blue', 'yellow', 'purple', 'black'];
let imageVector = [];

let field = document.querySelector('#field');
let clearButton = document.querySelector('#clear');
let sendButton = document.querySelector('#send');

function randomInteger(min, max) {
    var rand = min - 0.5 + Math.random() * (max - min + 1);
    rand = Math.round(rand);
    return rand;
}

for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
        let randColor = randomInteger(0, 5);
        let p = document.createElement('div');
        p.setAttribute('data-active', '0');
        p.setAttribute('class', 'pixel');
        p.setAttribute('style', `width:${singleW}px; height:${singleW}px; float:left;`);
        field.appendChild(p);
    }
}

function draw(event) {
    let p = event.target;
    p.setAttribute('style', `width:${singleW}px; height:${singleW}px; float:left; background-color:red;`);
    p.setAttribute('data-active', '1');
}


field.onmousedown = function (event) {
    imageVector.length = 0;
    field.addEventListener("mouseover", draw);
};

field.onmouseup = function (event) {
    field.removeEventListener("mouseover", draw);

    let pixels = document.querySelectorAll('.pixel');

    for (let i = 0; i < pixels.length; i++) {
        imageVector.push(+pixels[i].getAttribute('data-active'))
    }

    console.log(imageVector);
};

clearButton.onclick = function (event) {
    event.preventDefault();
    let pixels = document.querySelectorAll('div[data-active="1"]');

    for (let i = 0; i < pixels.length; i++) {
        pixels[i].setAttribute('data-active', '0');
        pixels[i].setAttribute('style', `width:${singleW}px; height:${singleW}px; float:left;`);
    }
};

sendButton.onclick = function (event) {
    event.preventDefault();
    let xhr = new XMLHttpRequest();

    xhr.open('POST', '/send_image');
    xhr.send("hi");
    console.log(xhr.response);
};
