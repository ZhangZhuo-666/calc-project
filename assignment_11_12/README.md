## 1. Sprint Goal
Sprint Goal: Establish the initial backend foundation by creating a simple server endpoint, ensuring the project environment is correctly set up and ready for future feature development.

## 2. Mini-ADR
- **Decision:** Use Node.js with Express as the backend framework.
- **Reason:** It provides a clean structure for defining routes and supports rapid iteration during early development.
- **Consequence:** The system becomes easy to extend, but long-term scalability may require additional design considerations.

## 3. Mini-API Description
- **Endpoint:** GET /health
- **Request:** No request body required
- **Success:** 200 OK with a JSON status message
- **Fail:** 500 Internal Server Error if the server cannot respond
- **Description:** A basic health-check endpoint used to verify that the backend server is running properly.
