from bottle import route
from bottle import run
from bottle import static_file

_EXPORT_PIN_STREAM = '/sys/class/gpio/export'
_UNEXPORT_PIN_STREAM = '/sys/class/gpio/unexport'

_VALUE_ON = '1'
_VALUE_OFF = '0'

_DIRECTION_IN = 'in'
_DIRECTION_OUT = 'out'

def ExportPin(pin):
  with open(_EXPORT_PIN_STREAM, 'w') as f:
    f.write(str(pin))

def UnexportPin(pin):
  with open(_UNEXPORT_PIN_STREAM, 'w') as f:
    f.write(str(pin))

def GetPinPath(pin):
  return '/sys/class/gpio/gpio%s' % pin

def GetDirectionFile(pin):
  return '%s/direction' % GetPinPath(pin)

def GetValueFile(pin):
  return '%s/value' % GetPinPath(pin)

def SetDirection(pin, direction):
  file_name = GetDirectionFile(pin)
  with open(file_name, 'w') as f:
    f.write(direction)

def SetValue(pin, value):
  file_name = GetValueFile(pin)
  with open(file_name, 'w') as f:
    f.write(value)

def GetValue(pin):
  file_name = GetValueFile(pin)
  with open(file_name, 'r') as f:
    return f.read()



@route('/')
def index():
  return static_file('static/html/index.html', root='.')

@route('/static/<path:path>')
def static_files(path):
  return static_file(path, './static')

@route('/api/pin/get/<pin>')
def GetPinValue(pin=None):
  if pin is None:
    return ''
  return GetValue(pin)

@route('/api/pin/on/<pin>')
def SetPinOn(pin=None):
  if pin is None:
    return
  SetValue(pin, _VALUE_ON)

@route('/api/pin/off/<pin>')
def SetPinOff(pin=None):
  if pin is None:
    return
  SetValue(pin, _VALUE_OFF)

def setup():
  ExportPin(25)
  SetDirection(25, _DIRECTION_OUT)
  
def exit():
  UnexportPin(25)

try:
  setup()
  run(host='192.168.1.177', port=80)
finally:
  exit()

