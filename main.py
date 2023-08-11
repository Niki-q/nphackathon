from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import os
from datetime import datetime

app = FastAPI()


@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        # Create a directory if it doesn't exist
        if not os.path.exists("./data/questions"):
            os.makedirs("./data/questions")

        for file in files:
            # Add a timestamp to the filename
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename, file_extension = os.path.splitext(file.filename)
            new_filename = f"{filename}_{timestamp}{file_extension}"
            file_path = os.path.join("./data/questions", new_filename)

            with open(file_path, "wb") as f:
                f.write(file.file.read())

        # Process the files (you can replace this with your own processing logic)
        # For now, just return a success message
        return JSONResponse(content={"message": "Files uploaded successfully"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
