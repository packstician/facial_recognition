from deepface import DeepFace

DeepFace.stream(db_path = '/Users/benjaminsewell/Documents/Python/FacialRecognition/facial_recognition/dataset/Faces/', model_name = 'GhostFaceNet',detector_backend="retinaface" ,distance_metric = 'cosine',source="rtsp://packstician:Shiny680@10.0.0.182:8554/stream1", enable_face_analysis = True)
