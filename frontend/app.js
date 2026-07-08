// ================================
// BakeMe Frontend Script
// Version 1.0
// ================================

// HTML Elements
const hoursInput = document.getElementById("hours");
const minutesInput = document.getElementById("minutes");

const hoursPlus = document.getElementById("hoursPlus");
const hoursMinus = document.getElementById("hoursMinus");

const minutesPlus = document.getElementById("minutesPlus");
const minutesMinus = document.getElementById("minutesMinus");

const finishTime = document.getElementById("finishTime");
const currentDateTime = document.getElementById("currentDateTime");

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");

// -------------------------------
// Live Date & Time
// -------------------------------

function updateClock() {

    const now = new Date();

    currentDateTime.textContent =
        now.toLocaleDateString() +
        " " +
        now.toLocaleTimeString();

}

setInterval(updateClock,1000);

updateClock();


// -------------------------------
// Hours
// -------------------------------

hoursPlus.onclick = () => {

    if(hoursInput.value < 24)
        hoursInput.value++;

    calculateFinish();

};

hoursMinus.onclick = () => {

    if(hoursInput.value > 0)
        hoursInput.value--;

    calculateFinish();

};

// -------------------------------
// Minutes
// -------------------------------

minutesPlus.onclick = () => {

    if(minutesInput.value < 59)
        minutesInput.value++;

    calculateFinish();

};

minutesMinus.onclick = () => {

    if(minutesInput.value > 0)
        minutesInput.value--;

    calculateFinish();

};

// -------------------------------
// Finish Time
// -------------------------------

function calculateFinish(){

    let now = new Date();

    let totalMinutes =
        parseInt(hoursInput.value)*60 +
        parseInt(minutesInput.value);

    now.setMinutes(now.getMinutes()+totalMinutes);

    finishTime.textContent =
        now.toLocaleTimeString([],{
            hour:'2-digit',
            minute:'2-digit'
        });

}

calculateFinish();

// -------------------------------
// Start Button
// -------------------------------

startBtn.onclick = () => {

    alert("Backend connection will be added next.");

};

// -------------------------------
// Stop Button
// -------------------------------

stopBtn.onclick = () => {

    alert("Backend connection will be added next.");

};
