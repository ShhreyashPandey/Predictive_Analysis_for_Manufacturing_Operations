# Machine Downtime Prediction API
This API provides endpoints for uploading data, training a ML model, and making predictions about machine downtime based on input features. The model uses Decision Tree for classification.
## Setup Instructions
1. Install Python 3.7 or higher along with pip package manager.
2. Clone Repository or Download
3. Install required packages:
   ```pip install flask pandas scikit-learn```
4. Run the Flask app:
   ```python main.py```
   
   If successful, you should see output similar to:
   > Running on http://127.0.0.1:5007
   
   ![image](https://github.com/user-attachments/assets/64601dee-9814-4d94-bba9-d74758d56746)
   I have used PyCharm to run the program

6.  Now to test the API we will use cURL in Command Prompt
  
   a. Upload a CSV file(with columns Temperature, Run_Time, and Downtime_Flag) containing the data for training.

   ```curl -X POST -F "file=@data.csv" http://127.0.0.1:5007/upload```

  ![image](https://github.com/user-attachments/assets/ab77e404-6127-4a5e-aff0-8ac026d1a396)
  
  b. Train a Decision Tree model using the uploaded data.
  
  ```curl -X POST http://127.0.0.1:5007/train```
  
  ![image](https://github.com/user-attachments/assets/9bdfd672-2017-4a82-baf9-1a9cae465821)

  c. Predict whether a machine will experience downtime based on input features.
  
  ```curl -X POST -H "Content-Type: application/json" -d "{\"Temperature\": 80, \"Run_Time\": 100}" http://127.0.0.1:5007/predict```
  
  ![image](https://github.com/user-attachments/assets/1a1e2e3f-9ca8-4330-a5c4-8396ca8ab8b8)

  ![image](https://github.com/user-attachments/assets/2f3eb6ae-4e9d-41ce-ac1c-d88f8b59a7a4)


