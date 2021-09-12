## Query: Create a python code that will get the user details as input, store them in the table and perform the eligibility and give response in JSON if the user is eligible or not eligible
1. Following are the input in user details  :
   1. First Name 
   2. Middle Name - Optional 
   3. Last Name 
   4. DOB – YYYY-MM-DD 
   5. Gender 
   6. Nationality 
   7. Current City 
   8. State 
   9. Pin-code 
   10. Qualification 
   11. Salary 
   12. PAN Number
2. Create Two Mysql table :
   1. Request_Info :
      1. Should contain above set of fields with appropriate data type 
      2. Should have id field as auto increment. 
      3. Should have Request received datetime field. 
   2. Response_Info 
      1. Should have id field as auto increment. 
      2. Should have request_id as a foreign key reference to the Request_Info id column. 
      3. Should have response field to store the response generated for the request.
3. Eligibility Criteria :
   1. Age should be greater than 21 Yrs for Male as of current day. 
   2. Age should be greater than 18 Yrs for Female as of current day. 
   3. No Request should have received in last 5 days from the same user (use PAN as the identifier). 
   4. Nationality should be “Indian” or “American”. 
   5. State should be only from Andhra Pradesh, Arunachal Pradesh, Assam, Bihar,  Chhattisgarh,  Karnataka,  Madhya Pradesh,  Odisha,  Tamil Nadu,  Telangana, West Bengal. 
   6. Salary should not be less than 10,000. 
   7. Salary Should not be greater than 90,000.
4. Response should be formed as a JSON. 
   1. Sample success response :
      1. {‘Request_id’: 1, ‘Response’:’Success’}
   2. Sample Validation Failure response :
      1. Here assuming the DOB input was not in expected format, below will be the response. 
      2. {‘Response’:’Validation Failure’, ‘Reason’:’Invalid Input for DOB’} 
   3. Sample Eligibility Failure  response :
      1. Response example1: Here assuming the DOB input was ‘2015-06-01’, below will be the response. 
         1. {‘Request_id’: 2, ‘Response’:Failed’, ’Reason’:’Age is less than expected.’}
      2. Response example2: Here assuming other request received with same pan number within last 5 days, below will be the response. 
         1. {‘Request_id’: 3, ‘Response’:Failed’, ’Reason’:’Recently request received in last 5 days.’
