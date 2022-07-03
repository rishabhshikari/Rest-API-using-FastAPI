The User.json files contains the data which is used in API. Loaded it with the help of Json Libray and declared the function named "User"

@app.get('/') Function returns the message To the user. 

1.To get the Particular user with the help of His/her ID the condition is implemented as below:
a. The provided ID should be an integer.
b.The Provided ID should exist in the DB
If the given information is correct BioData of the user will pop up as output.

2.To search the User with the letter of its name or Gender The following conditions were used:
a.The Gender and name to be provided in String form(Optional)
b.if the given gender is available in the set of data the Users with the same Gender will appear
c.if the given letters are available in the name of User. Every Username Containing that letter will appear(Scrrenshot Provided)

3.To Fetch the complete List of Users in terms of viewing the database:
* Defined a function named fetch_users():
*Returned The converted Json file "User"


****It was my First Experience with FastAPI. I tried my best to met all conditions******


 