VALUE_ON = '1'
VALUE_OFF = '0'

DIRECTION_IN = 'in'
DIRECTION_OUT = 'out'

_EXPORT_PIN_STREAM = '/sys/class/gpio/export'
_UNEXPORT_PIN_STREAM = '/sys/class/gpio/unexport'

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

