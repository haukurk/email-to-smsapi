# EMAIL to SMS API service

This project is a proposal for an email-to-SMSAPI service.
It works as an email server that listens for emails that contains the recipient msidsn number as the sender address and
email body as the text message. The service then translates the message to a SMS HTTP API and sends out the email that way.

# Install

Install requirements 
```
pip install -r requirements.txt
```

Run the service
```
python run.py
```

# Features

This bridge features:
* Email server component that listens for requests in form of:
  - msisdn@[computerip], using email body as the text message.
* SMS Interpreter component that communicates with REST APIs like CM.nl.
 - Examples
* Activity Monitor
 - Logging to /logs
 - HTTP Server with logging tail [TODO]

# Prerequisites

This is very basic solution that only needs one non built in package:
* urllib3

# Other

Pull requests are gladly accepted.

# License

The MIT License (MIT)

Copyright (c) 2014 Haukur Kristinsson

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.