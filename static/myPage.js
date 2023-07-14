function updateTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var timeString = hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0');
    document.getElementById('time').textContent = timeString;
}

updateTime();
setInterval(updateTime, 1000);
