from functools import partial
import os
import threading
from tkinter import *
from tkinter.ttk import Treeview
import cv2
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util
import numpy as np
import constValues
from functions import addItem, getTotalPrice

tf.config.experimental.set_visible_devices([], 'GPU')

# Odtworzenie etykiet
category_index = label_map_util.create_category_index_from_labelmap(constValues.files['LABELMAP'])

# Plik konfiguracyjny do ponownego załadowania
configs = config_util.get_configs_from_pipeline_file(constValues.files['PIPELINE_CONFIG'])
detection_model = model_builder.build(model_config=configs['model'], is_training=False)

# Odtwórz najbardziej zaawansowany checkpoint modelu
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(constValues.paths['CHECKPOINT_PATH'], 'ckpt-5')).expect_partial()

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections

def open_camera(tree: Treeview, sumText: Label):
  vid = cv2.VideoCapture(0)

  width, height = 800, 600
  vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  while vid.isOpened():
    ret, frame = vid.read()
    image_np = np.array(frame)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections = detect_fn(input_tensor)

    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
                image_np_with_detections,
                detections['detection_boxes'],
                detections['detection_classes']+label_id_offset,
                detections['detection_scores'],
                category_index,
                use_normalized_coordinates=True,
                max_boxes_to_draw=5,
                min_score_thresh=.5,
                agnostic_mode=False)
    

    # Print detected elements to the screen (test mode)
    my_classes = detections['detection_classes'][0] + label_id_offset
    my_scores = detections['detection_scores'][0]

    min_score = 0.15

    if hasattr(my_classes, "__len__"):
      print([category_index[value]['name']
        for index,value in enumerate(my_classes) 
        if my_scores[index] > min_score
      ])
      #TODO: Test if viable case
    elif my_scores > min_score:
      addItem(tree, category_index[my_classes]['name'])
      sumText.config(text=getTotalPrice(tree))
      print([category_index[my_classes]['name']])

    cv2.imshow('AI cash register camera', cv2.resize(image_np_with_detections, (800, 600)))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        vid.release()
        cv2.destroyAllWindows()
        break

def run_camera(tree, sumText):
  threading.Thread(target=partial(open_camera, tree, sumText)).start()