# Testing
The project was tested through Postman an HTTP client.   
![PostmanUI](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman1.png?raw=true)  
There are 3 requests which test each endpoint making sure the correct response or error is returned.  
The API will always repond with JSON with a "successful" boolean attribute, unless there is a 5xx error.

## Example Test
![PostmanTest1](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman2.png?raw=true)  
In this test we send a request to book the seat A20 for John Smith.  
As seen in the image, we get the successful response and a passenger ID that John must keep if he wishes to unbook his ticket.  

![PostmanTest2](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman3.png?raw=true)  
Now, we see Jane Smith wanting to book the same seat that John just booked. We can see that the API returns a false successful with a message that her seat has already been booked.  

![PostmanTest3](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman4.png?raw=true)  
Jane tries to book at seat but it is not actally a valid seat on the aircraft, so the API returns 404 with a message "That is not a valid seat number."  

![PostmanTest4](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman5.png?raw=true)  
Now someone tries to unbook John's seat but the API returns with a 403 Forbidden with a message that they are not authorized to do so.  

![PostmanTest5](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman6.png?raw=true)  
John now deletes his seat with his correct Passenger ID and someone else is free to book it.  

![PostmanTest6](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/postman7.png?raw=true)   
John now sees what seats are left on the plane and he seat has been correctly identified as not taken. 