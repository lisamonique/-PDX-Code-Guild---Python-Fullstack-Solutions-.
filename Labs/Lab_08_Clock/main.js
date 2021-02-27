// Clock Elements
let hours = document.querySelector('.hours')
let minutes = document.querySelector('.minutes')
let seconds = document.querySelector('.seconds')

// Stopwatch Elements
let stopwatch = document.querySelector('.stopwatch')
let stopHours = stopwatch.querySelector('.hours')
let stopMinutes = stopwatch.querySelector('.minutes')
let stopSeconds = stopwatch.querySelector('.seconds')

// Clock Logic
setInterval(function () {
    currentTime = new Date()
    hours.innerText = currentTime.getHours().toString().padStart(2, 0)
    minutes.innerText = ":" + currentTime.getMinutes().toString().padStart(2, 0)
    seconds.innerText = ":" + currentTime.getSeconds().toString().padStart(2, 0)
}, 1000)

// Stopwatch Setup
let stopwatchTimer = new Date()
function stopwatchSetup(){
    stopwatchTimer.setHours(0,0,0,0)
    stopHours.innerText = stopwatchTimer.getHours().toString().padStart(2, 0)
    stopMinutes.innerText = stopwatchTimer.getMinutes().toString().padStart(2, 0)
    stopSeconds.innerText = stopwatchTimer.getSeconds().toString().padStart(2, 0)   
}

stopwatchSetup()
let stopwatchInterval = undefined

startBtn.addEventListener('click', function() {
    if(stopwatchInterval) {
        return
    }
    else {
      stopwatchInterval = setInterval(function(){
        let seconds = stopwatchTimer.getSeconds(seconds + 1)
        stopHours.innerText = stopwatchTimer.getHours().toString().padStart(2, 0)
        stopMinutes.innerText = stopwatchTimer.getMinutes().toString().padStart(2, 0)
        stopSeconds.innerText = stopwatchTimer.getSeconds().toString().padStart(2, 0)
    }, 1000)  
    }
})

stopBtn.addEventListener('click', function (){
    clearInterval(stopwatchInterval)
})

lapBtn.addEventListener('click', function () {
    let li = document.createElement('li')
    let hours = stopwatchTimer.getHours()
    let minutes = stopwatchTimer.getMinutes()
    let seconds = stopwatchTimer.getSeconds()
    li.innerText = 'Lap ${lapTimes.children.length + 1}${hours.'
    lapTimes.append(li)
})