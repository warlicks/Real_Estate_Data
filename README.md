## Intro  
The project is project is designed to analyze housing prices (rentals & purchases) in the Seattle area.  It utilizes the Truila API.  The project utilizes Python to call the API and parse the returned XML.  

## Using the Functions
To utilize the functions in **api_function.py** the user needs a Truila API key.  It can be obtained from [Truila](http://developer.trulia.com/page) by signing up for a user account and requesting an API Key.  The functions are currently set up to import the key in a variable *\_apiKey* from a module **api.py**  

## Files  
* **api_function.py:** Contains two functions one to access Truila's `LocationInfo` library and one to access the `TruilaStats` library.   

* **xml_parsers.py:** Contains two functions, one to retreive data from the XML returned by Truila's `LocationInfo` library and one to to retreive data from the XML returned by the `TruilaStats` library.  

## License
The MIT License (MIT)

Copyright (c) 2016 Sean Warlick

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*Last Updated: July 27, 2016*