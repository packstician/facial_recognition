from deepface import DeepFace

DeepFace.stream(db_path = 'dataset/Faces', model_name = 'VGG-Face', distance_metric = 'euclidean', source = "rtsp://packstician:Shiny680@10.0.0.182:8554/stream1", time_threshold = 10, frame_threshold = 5)
