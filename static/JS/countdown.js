// COUNTDOWN
function secondsToDhms(seconds) {
  if (seconds < 0) {
      document.getElementById("counter").style.display = "None";
  }
  seconds = Number(seconds);
  var d = Math.floor(seconds / (3600*24));
  var h = Math.floor(seconds % (3600*24) / 3600);
  var m = Math.floor(seconds % 3600 / 60);
  var s = Math.floor(seconds % 60);
  if (d == 0) {
      document.getElementById("days").parentElement.classList.add("hidden");
      document.getElementById("seconds").parentElement.classList.remove("hidden");
  }
  document.getElementById("days").innerText = d ;
  document.getElementById("hours").innerText = h ;
  document.getElementById("mins").innerText = m ;
  document.getElementById("seconds").innerText = s ;

}

function startTimer() {
  setInterval(countdown,1000)
}

function countdown() {
  let seconds = document.getElementById('time_diff').innerHTML;
  document.getElementById('time_diff').innerHTML = seconds - 1;
  // let seconds = 100;
  // console.log(document.getElementById('time_diff').innerHTML);
  console.log(seconds)
  secondsToDhms(seconds)
}

document.addEventListener('DOMContentLoaded', startTimer());



//OLD
var target_date = new Date().getTime() + 1000 * 3600 * 48; // set the countdown date
var days, hours, minutes, seconds; // variables for time units

var countdown = document.getElementById("tiles"); // get tag element

getCountdown();

setInterval(function () {
  getCountdown();
}, 1000);

function getCountdown() {
  // find the amount of "seconds" between now and target
  var current_date = new Date().getTime();
  var seconds_left = (target_date - current_date) / 1000;

  days = pad(parseInt(seconds_left / 86400));
  seconds_left = seconds_left % 86400;

  hours = pad(parseInt(seconds_left / 3600));
  seconds_left = seconds_left % 3600;

  minutes = pad(parseInt(seconds_left / 60));
  seconds = pad(parseInt(seconds_left % 60));

  // format countdown string + set tag value
  countdown.innerHTML =
    "<span>" +
    days +
    "</span><span>" +
    hours +
    "</span><span>" +
    minutes +
    "</span><span>" +
    seconds +
    "</span>";
}

function pad(n) {
  return (n < 10 ? "0" : "") + n;
}





