# EJERCICIO 13.4 - making HTML with filter and map
all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]
# Your code here
def generate_li(color):
	return "<li>" + color["label"] +"</li>"

def filter_colors(adjective):
	if adjective["sexy"] == True:
		return True
	else:
		return False 
sexy_colors = list(filter(filter_colors, all_colors))

result = list(map(generate_li, sexy_colors))

print(result)
