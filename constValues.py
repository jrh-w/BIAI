import os

CUSTOM_MODEL_NAME = 'resnet'
LABEL_MAP_FILE = 'label_map.pbtxt'

paths = {
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
 }

files = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_FILE)
}

columns = ('product', 'count', 'price')

# prices = {
#   "produkt 1": 1,
#   "produkt 2": 2,
#   "produkt 3": 3,
#   "produkt 4": 4,
#   "produkt 5": 5,
#   "dzik": 3.99,
#   "kasztelan": 2.99,
#   "kozel": 4.99,
#   "lech-active": 3.49,
#   "monster": 5.99,
#   "red-bull": 4.49,
# }

products = {
  "produkt 4": {
    "name": "Test",
    "price": 4,
  },
  "dzik": {
    "name": "Dzik",
    "price": 3.99,
  },
  "kasztelan": {
    "name": "Kasztelan",
    "price": 2.99,
  },
  "kozel": {
    "name": "Kozel",
    "price": 4.99,
  },
  "lech-active": {
    "name": "Lech Active",
    "price": 3.49,
  },
  "monster": {
    "name": "Monster",
    "price": 5.99,
  },
  "red-bull": {
    "name": "Red Bull",
    "price": 4.49,
  }
}