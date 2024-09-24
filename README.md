# NULL AI Server API

This project is a simple Flask server to handle API requests (primarily created to serve my [ChatFXT](https://github.com/NULLCommand1/ChatFXT) project). It includes 3 main API endpoints to handle user requests: the first is to provide a brief response, the second is to provide a more detailed response using generative text models like GPT, Gemini 1.5 Pro, etc., and the last is to provide image responses from Bing Image Creator. It is based on the core support library [gpt4free](https://github.com/xtekky/).

## Project Structure

```
.gitignore
api/
    module.py
    server.py
    static/
        helloworld.txt
.env.example
Pipfile 
README.md
requirements.txt
vercel.json
```

## API Endpoints

### `/api/v2/simple_response`

- **Method:** POST
- **Description:** Handles simple messages and responds briefly, adding icons to make the response more lively.
- **Request Example:**
  ```json
  {
    "message": "Hello!"
  }
  ```
- **Response Example:**
  ```json
  {
    "text": "(Powered by OpenFXT): Hello! 😊"
  }
  ```

### `/api/v2/detail_response`

- **Method:** POST
- **Description:** Handles detailed messages and responds more comprehensively, adding icons to make the response more lively.
- **Request Example:**
  ```json
  {
    "message": "Tell me more about your service."
  }
  ```
- **Response Example:**
  ```json
  {
    "text": "(Powered by OpenFXT): Our service is fantastic, try it today! 😊"
  }
  ```

### `/api/v2/image_response`

- **Method:** POST
- **Description:** Handles text prompt requests for image creation ideas and responds with images using Bing Image Creator.
- **Request Example:**
  ```json
  {
    "message": "Find images of cats."
  }
  ```
- **Response Example:**
  ```json
  {
    "text": "(Powered by OpenFXT): image_url"
  }
  ```

## Installation and Running the Project

1. **Clone the repository:**
   ```sh
   git clone https://github.com/NULLCommand1/NULLAIServerAPI.git
   cd NULLAIServerAPI
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file from the `.env.example` file and provide the values:**
   ```sh
   cp .env.example .env
   ```

4. **Run the server:**
   ```sh
   python api/server.py
   ```
Note: Running the server on localhost has some differences compared to running on Vercel. Please see the `server.py` file and adjust the imports accordingly to run the server on localhost.

## Contribution

We welcome contributions from the community! If you would like to contribute to the **NULL AI Server API** project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of the repository page to create a copy of the repository in your GitHub account.

2. **Clone Your Fork**: Clone the forked repository to your local machine using the following command:

 ```bash
   git clone https://github.com/NULLCommand1/NULLAIServerAPI.git
   cd NULLAIServerAPI
   ```

3. **Create a Branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b your-feature-branch
   ```

4. **Make Changes**: Implement your changes in the new branch. Ensure your code follows the project's coding standards and includes appropriate tests.

5. **Commit Changes**: Commit your changes with a descriptive commit message:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. **Push to GitHub**: Push your changes to your forked repository:
   ```bash
   git push origin your-feature-branch
   ```

7. **Submit a Pull Request**: Go to the original repository and click the "New Pull Request" button. Select your branch and submit the pull request. Provide a clear description of your changes and any related issues.

8. **Review Process**: Your pull request will be reviewed by the maintainers. They may request changes or ask for additional information. Please be responsive and address any feedback promptly.

Thank you for your contributions! Together, we can make **NULL AI Server API** even better.

## Contact

If you have any questions or feedback, please contact via email: nguyenhuutaistd1@gmail.com.