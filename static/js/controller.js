

function PinCtrl($http) {
  this.http_ = $http;
  this.pins = {25: null};
}

PinCtrl.prototype.init = function() {
  for (var pin in this.pins) {
    this.getPinValue(pin);
  }
};


PinCtrl.prototype.getPinValue = function(pin) {
  var self = this;
  this.http_({method: 'GET', url: '/api/pin/get/' + pin.toString()}).
    success(function(data) {
      self.pins[pin] = data.trim() === '1';
    }).
    error(function() {
      alert('an error occurred getting the pin value...')
    });
};


PinCtrl.prototype.turnPinOn = function(pin) {
  var self = this;
  this.http_({method: 'GET', url: '/api/pin/on/' + pin.toString()}).
    success(function(data) {
      self.getPinValue(pin);
    }).
    error(function() {
      alert('an error occurred turning the pin on...');
    });
};


PinCtrl.prototype.turnPinOff = function(pin) {
  var self = this;
  this.http_({method: 'GET', url: '/api/pin/off/' + pin.toString()}).
    success(function(data) {
      self.getPinValue(pin);
    }).
    error(function() {
      alert('an error occurred turning the pin off...');
    });
};



