****Face Recognition Application****
A Python-based face recognition application leveraging AWS services for efficient and scalable image processing and identification.

****Key Features****
Face Detection & Recognition: Utilizes Amazon Rekognition to identify and analyze faces in images stored in Amazon S3.
Automated Processes: Implements an AWS Lambda function for automatic face indexing and recognition.
Metadata Management: Stores face metadata, including unique IDs and names, in a DynamoDB table for quick retrieval.
Image Preprocessing: Enhances recognition accuracy using the Pillow library for image processing.

****Technologies Used****
Programming Language: Python
Libraries: boto3, Pillow
AWS Services: Rekognition, S3, Lambda, DynamoDB

Setup and Usage
1. Clone the repository:
git clone https://github.com/yourusername/face-recognition-app.git
cd face-recognition-app

2. Install dependencies:
pip install -r requirements.txt

3. Add AWS credentials and configure Rekognition, S3, and DynamoDB services.
Run the application and upload images for face recognition.

4. Add AWS credentials and configure Rekognition, S3, and DynamoDB services.
Run the application and upload images for face recognition.

This project demonstrates seamless integration with AWS for real-time face recognition and metadata management, offering scalability and automation.
