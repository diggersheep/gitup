import re


def colorize ( codes ) :
	if type(codes) == type([]) or type(codes) == type(()) :
		if len(codes) :
			return '\033[{codes}m'.format(codes=';'.join([str(code) for code in codes]))
		else :
			return ''

	elif type(codes) == type(0) :
		return '\033[{code}m'.format(code=codes)
	else :
		return ''

def uncolor ( str_color ) :
	r = r'(\033)\[[0-9 ]+(;[0-9]+)*m'
	str_color = re.sub(r, '', str_color)

	return str_color

COLOR_CODE = {
	'black':30,
	'red': 31,
	'green': 32,
	'yellow': 33,
	'blue': 34,
	'magenta': 35,
	'cyan': 36,

	'dark gray':90,
	'light red':91,
	'light green':92,
	'light yellow':93,
	'light blue':94,
	'light magenta':95,
	'light cyan':96,
	'white' : 97,

	'default': 39,

	'back black':40,
	'back red': 41,
	'back green': 42,
	'back yellow': 43,
	'back blue': 44,
	'back magenta': 45,
	'back cyan': 46,

	'back dark gray':100,
	'back light red':101,
	'back light green':102,
	'back light yellow':103,
	'back light blue':104,
	'back light magenta':105,
	'back light cyan':106,
	'back white' : 107,

	'back default': 49,

	'bold':1,
	'dim':2,
	'underline':4,
	'blink':5,
	'reverse':7,
	'hidden':8,

	'reset':0,
	'reset bold': 21,
	'reset dim':22,
	'reset underline':24,
	'reset blink':25,
	'reset reverse':27,
	'reset hidden':28,
}


COLOR = {}
for key in COLOR_CODE : 
	COLOR[key] = colorize(COLOR_CODE[key])
