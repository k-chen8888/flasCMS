# Utility functions for other apps to use index
# from index import [items]
def import_index(items):
	return __import__('index', globals(), locals(), items, -1)

# from index.models import [items]
def import_index_models(items):
	return __import__('index.models', globals(), locals(), items, -1)
