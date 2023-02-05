hour = 2;
min = 00;
sec = 00;

function secFun() {
  sec--;
  if (sec < 0) {
    min--;
    sec = 59;
  }
  if (min < 0) {
    hour--;
    min = 59;
  }
  if (hour == 24) {
    hour = 0;
  }

  if (sec < 10) {
    sec = "0" + sec;
  }
  if (min < 10) {
    min = "0" + min;
  }
  //   if (hour < 10) {
  //     hour = "0" + hour;
  //   }

  document.getElementById("sec").innerHTML = sec;
  document.getElementById("min").innerHTML = min;
  document.getElementById("hour").innerHTML = hour;
  // document.getElementById("_date").innerHTML = _date;
}

setInterval(secFun, 1000);
