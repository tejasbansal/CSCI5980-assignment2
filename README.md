## This is a Flask app that provides PUT, GET, and DELETE  
The GET returns the value associated with the given key in the kv_store dictionary  
The PUT adds a new key-value pair to the dictionary. It accepts two query parameters, key, and value, and adds the key-value pair to the dictionary. If either of the parameters is missing, the endpoint returns an error message  
The DELETE deletes a key from the dictionary and will return an error if the key is not present  
The app also logs all requests to a file named dataLog.json  

To test the Flask application, you can use the following curl commands:

### GET Request  
curl -X GET "http://localhost:5000/get/my_key"  
This will send a GET request to the Flask server with the key parameter set to my_key.  

### PUT Request  
curl -X PUT "http://127.0.0.1:5000/put?key=my_key&value=my_value"  

### DELETE Request
curl -X DELETE "http://localhost:5000/delete/my_key"  

This will send a PUT request to the Flask server with the key parameter set to my_key and the value parameter set to my_value.

