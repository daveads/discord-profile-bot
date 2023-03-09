from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

# Define a route that accepts image filenames in the URL
@app.get('/image/{filename}')
async def get_image(filename: str):
    # Set the path to the directory containing the images
    image_dir = '/path/to/image/directory'

    # Check if the filename is valid
    if not filename.endswith('.jpg'):
        raise HTTPException(status_code=400, detail='Invalid filename')

    # Try to send the image file
    try:
        return FileResponse(image_dir + '/' + filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail='File not found')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

