import gpio

from bottle import route
from bottle import run
from bottle import static_file

# Configure to listen on any hostname, port 80.
_HOSTNAME = '0.0.0.0'
_PORT = 80
_ACTIVE_PINS = [25]

@route('/')
def Index():
  return static_file('static/html/index.html', root='.')

@route('/static/<path:path>')
def StaticFiles(path):
  return static_file(path, './static')

@route('/api/pin/get/<pin>')
def GetPinValue(pin=None):
  if pin is None:
    return ''
  return gpio.GetValue(pin)

@route('/api/pin/on/<pin>')
def SetPinOn(pin=None):
  if pin is None:
    return
  gpio.SetValue(pin, gpio.VALUE_ON)

@route('/api/pin/off/<pin>')
def SetPinOff(pin=None):
  if pin is None:
    return
  gpio.SetValue(pin, gpio.VALUE_OFF)

def setup():
  for pin in _ACTIVE_PINS:
    gpio.ExportPin(pin)
    gpio.SetDirection(pin, gpio.DIRECTION_OUT)
  
def exit():
  for pin in _ACTIVE_PINS:
    gpio.UnexportPin(pin)

try:
  setup()
  run(host=_HOSTNAME, port=_PORT)
finally:
  exit()

