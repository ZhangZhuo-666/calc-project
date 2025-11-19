1. Sprint Goal
Sprint Goal: Set up a basic server and verify that the backend can respond to a simple API request.
2. Mini-ADR
Decision: Use Node.js with Express for the backend.
Reason: Fast setup and ideal for small iterative development.
Consequence: Enables quick prototyping but may require extra modules for scalability.
3. Mini-API Description
Endpoint: GET /health
Request: None
Success: 200 OK
Fail: 500 Server Error
Description: Checks if the server is running and returns a basic status message.
