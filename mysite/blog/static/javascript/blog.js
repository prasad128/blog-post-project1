console.log("Hello");
const bodyVar = document.getElementsByName("body");

function random() {
  let num = Math.floor(Math.random() * 256);
  return num;
}
function changeColor() {
  body.style.color =
    "rgb" + "(" + random() + "," + random() + "," + random() + ")";
}
setInterval("changeColor()", 500);
