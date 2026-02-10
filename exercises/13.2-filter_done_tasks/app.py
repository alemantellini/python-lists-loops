# EJERCICIO 13.2 - filter done tasks
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]
# Your code here
def filter_task(element):
    if element["done"] == True:
        return True
    else:
        return False
done_tasks = list(filter(filter_task, tasks))
print(done_tasks)
