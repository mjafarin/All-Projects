var Gpio = require('onoff').Gpio; 
var LED = new Gpio(4, 'out');
var intervalBlinking = setInterval(ledBlink, 250);

function ledBlink(){
  if (LED.readSync() === 0){
    LED.writeSync(1);
  } else {
    LED.writeSync(0);
  }
}

function endBlink(){
  clearInterval(blinkInterval);
  LED.writeSync(0);
  LED.unexport();
}

setTimeout(endBlink, 5000);

