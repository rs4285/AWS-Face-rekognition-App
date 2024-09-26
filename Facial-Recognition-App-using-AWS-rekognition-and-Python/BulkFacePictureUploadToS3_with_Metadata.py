import boto3
import os

s3 = boto3.resource('s3')

# Define the base path where the images are stored
base_path = 'D:/faceapp/Facial-Recognition-App-using-AWS-rekognition-and-Python/FaceBook/'

# Get list of objects for indexing with updated paths
images = [
    (os.path.join(base_path, '1.jpg'), 'APJ Kalam'),
    (os.path.join(base_path, '2.jpg'), 'CV Raman'),
    (os.path.join(base_path, '3.jpg'), 'David Bekhm'),
    (os.path.join(base_path, '4.png'), 'Albert Einstein'),
    (os.path.join(base_path, '5.jpg'), 'Isaac Newton'),
    (os.path.join(base_path, '6.png'), 'Lionel Messi'),
    (os.path.join(base_path, '7.jpeg'), 'Nikola Tesla'),
    (os.path.join(base_path, '8.jpeg'), 'Mahendra Singh Dhoni'),
    (os.path.join(base_path, '9.jpeg'), 'Mithali Raj'),
    (os.path.join(base_path, '10.jpeg'), 'Smriti Mandhana'),
    (os.path.join(base_path, '11.jpeg'), 'Hardik Pandya'),
    (os.path.join(base_path, '12.jpeg'), 'Yuvraj Singh'),
    (os.path.join(base_path, '13.jpg'), 'Sachin Tendulkar'),
    (os.path.join(base_path, '14.jpeg'), 'Yuzvendra Chahal'),
    (os.path.join(base_path, '15.jpeg'), 'Virat Kohli'),
    (os.path.join(base_path, '16.jpg'), 'Sunil Gavaskar'),
    (os.path.join(base_path, '17.jpg'), 'Kapil Dev'),
    (os.path.join(base_path, '18.jpeg'), 'Ruturaj Gaikwad'),
    (os.path.join(base_path, '19.jpeg'), 'Kiran Kumar Malik'),
    (os.path.join(base_path, '20.jpeg'), 'Sagar Kumar Ojha'),
    (os.path.join(base_path, '21.jpeg'), 'Sarukh Khan'),
    (os.path.join(base_path, '22.jpg'), 'Harleen Deol'),
    (os.path.join(base_path, '23.png'), 'Chandan Kumar Sahu')
]

# Iterate through the list to upload objects to S3   
for image in images:
    try:
        with open(image[0], 'rb') as file:
            print(f"Uploading {image[1]} from {image[0]} to S3...")
            object = s3.Object('facialimagescollections', 'index/' + os.path.basename(image[0]))
            object.put(Body=file, Metadata={'FullName': image[1]})
    except FileNotFoundError:
        print(f"File not found: {image[0]}")
