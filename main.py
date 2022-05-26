import uvicorn
from routes.app import App

app = App()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")