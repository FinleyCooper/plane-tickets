# Analysis
## The Problem
A major problem prevelent in many systems and businesses is the managment of data between users.  
It is extremely important, espically in senstive areas, such as the airline business that the user is correctly informed to what seats are avaible are what are not  
This solution aims to provid a backend API that will make it trivial for a front end developer to intergrate the database into the page throught the web API.
A robust solution such as this is very important. We can she this importance when the US airliner United Airlines' booking website went down.  
Just this booking website going down made news around the country and it was even reported by some UK based news outlets.  
Objectives to be made throughout the project:
 - Allow the API to book a seat stored on the datebase
 - Made it so this seat cannot be booked by another user  
 - Allow to user to unbook their seat
 - Made it the seat can only be unbooked if the user has their passenger ID stored with the seat on the databse  
 - All the API to get the states of all seats on an aircraft without reveling personal information  

Due to the 8 hour limit on this project, there will be no third party and instead the project is aimed to provide an open source solution for the problem  

## The Solution 
The project will be coded in Python with the Flask framework which is very popular. This means it will be able to be easily integrated into many systems which may also use Flask, or Django a similar python alternative.

![Diagram](https://github.com/FinleyCooper/plane-tickets/blob/main/docs/images/diagram1.png?raw=true)