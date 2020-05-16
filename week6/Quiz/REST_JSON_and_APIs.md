> I've provided all possible questions, mark the ones that appear


#### Q1 Who is credited with the REST approach to web services?

Ans : Roy Fielding

#### Q1b Who is credited with getting the JSON movement started?

Ans : Douglas Crockford

#### Q2. Which of the following is true about an API?

Ans: An API is a contract that defines how to use a software library

#### Q3. Which of the following is a web services approach used by the Twitter API?

Ans: REST

#### Q4. What kind of variable will you get in Python when the following JSON is parsed:

    { 
        "id" : "001", 
        "x" : "2", 
        "name" : "Chuck" 
    }

Ans: A dictionary with three key / value pairs

#### Q5. Which of the following is not true about the service-oriented approach?

Ans: An application runs together all in one place

#### Q6. If the following JSON were parsed and put into the variable x,

    { "users": [ 
        { "status": 
            { 
                "text": "@jazzychad I just bought one .__.", }, "location": "San Francisco, California", "screen_name": "leahculver",
                "name": "Leah Culver", 
            }, ...

#### what Python code would extract "Leah Culver" from the JSON?

Ans: x["users"][0]["name"]

#### Q6b. Which of these two web service approaches is preferred in most modern service-oriented applications?

Ans : REST -Representational State Transfer

#### Q7. What library call do you make to append properly encoded parameters to the end of a URL like the following:

> http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI

Ans: urllib.parse.urlencode()

#### Q8. What happens when you exceed the Google geocoding API rate limit?

Ans: You cannot use the API for 24 hours

#### Q9. What protocol does Twitter use to protect its API?

Ans: OAuth

#### Q10. What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?

Ans: x-rate-limit-remaining