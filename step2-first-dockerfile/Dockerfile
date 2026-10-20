# 1. Start from the official Python 3.13 image, in its lightweight (slim) version
_____ python:3.13-slim

# 2. Set /app as the working directory in the image
_____ /app

# 3. Copy the list of dependencies into the working directory
_____ requirements.txt .

# 4. Install the dependencies
_____ pip install --no-cache-dir -r requirements.txt

# 5. Copy the Python script
_____ hello.py .

# 6. Set the command to run when the container starts
_____ ["python", "hello.py"]
