import cv2
import re
import os
import csv
from csv import writer
import glob
import face_recognition
import re
import pandas as pd
import numpy as np
import glob
import face_recognition
import streamlit as st
def facial_search(image_to_test):
    name = None
    status = False
    image_dir = "C:\\Users\\User\\OneDrive\\Desktop\\data\\"
    test_image = face_recognition.load_image_file(image_to_test)
    known_face_encodings = []
    known_face_names = []
    if os.path.exists(image_dir):
        for filename in glob.iglob(os.path.join(image_dir, '*png'), recursive=True):
            print(filename)
            image = face_recognition.load_image_file(filename)
            image_face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(image_face_encoding)
            child_id = filename.split("/")[-1].split(".")[0]
            known_face_names.append(child_id)

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)

        name = None
        status = False

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            status = True
    return name, status 