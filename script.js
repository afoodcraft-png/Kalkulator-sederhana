function add(value) {
    document.getElementById("display").value += value;
}

function calc() {
    let hasil =
    eval(document.getElementById("display").value);
    document.getElementById("display").value = hasil;
}