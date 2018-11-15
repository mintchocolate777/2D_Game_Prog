objects = [[],[],[],[]]
layer_bg = 0
layer_hurdle = 1
layer_guide = 2
layer_horse = 3

def add_object(o, layer):
	objects[layer].append(o)
def remove_object(o):
	for i in range(len(objects)):
		if o in objects[i]:
			print('deleting', o)
			objects[i].remove(o)
			del o

def clear():
	for o in all_objects():
		del o
	objects.clear()

def clear_layer(layer):
	for o in objects_at_layer(layer):
		del o
	objects[layer].clear()

def all_objects():
	for i in range(len(objects)):
		for o in objects[i]:
			yield o
def objects_at_layer(layer):
	for o in objects[layer]:
		yield o
def update():
	for o in all_objects():
		o.update()
def draw():
	for o in all_objects():
		o.draw()


