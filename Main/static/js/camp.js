function show(x, y) {
    document.getElementById(x).style.display = "grid";
    document.getElementById(y).style.gridColumnStart = "1";
}

function hide(x, y) {
    document.getElementById(x).style.display = "none";
    document.getElementById(y).style.gridColumnStart = "";
}