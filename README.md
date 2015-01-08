Simple API for retrieving data from a Federal Reserve web site

=Usage

The basic URL prefix for all queries is: <server>/fed/fomc
Calling this prefix without any other paramters will return the version info for the
service.

For example...

{"status": "ok", "version": "1.0", "data": "{\"last revised\": \"January 7, 2015\", \"source repository\": \"https://github.com/JimHagan/flyberry_task.git\", \"description\": \"Federal Reserve Information API\", \"author\": \"Jim Hagan\"}"}


RESPONSE FORMAT


SUCCESS


If a query is successful, an "ok" response will be returned with HTTP response code 200:

{
 "status": "ok",
 "version": "version_num",
 "data": "<the returned query data>"
}

The "data" field should return a string value. It can be a JSON string, a CSV string, or any
other type of string, but it should be a string.

FAILURE

If a query is unsuccessful, an "error" response will be returned:

{
 "status": "error",
 "code": "short_code",
 "message": "A longer description of the error"
}                                                                                                                                                                                                               

For example, entering an unknown URL will return the fact that a 404 error occcured in our custom JSON format.

Example...

{"status": "error", "message": "404 Error", "code": "404"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  