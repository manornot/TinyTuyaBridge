from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tinytuya
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
dev_id = os.getenv('DEVICEID')
dev_ip = os.getenv('DEVICEIP')
dev_key = os.getenv('DEVICEKEY')

# Initialize TinyTuya device


# FastAPI app instance
app = FastAPI()

# Request model for controlling the plug
class PlugControlRequest(BaseModel):
    action: str  # "on" or "off"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tuya Bridge API"}

@app.post("/plug/control")
def control_plug(request: PlugControlRequest):
    """Control the smart plug by turning it on or off based on the action."""
    d = tinytuya.OutletDevice(dev_id=dev_id, address=dev_ip, local_key=dev_key, version=3.5)
    try:
        if request.action.lower() == "on":
            d.turn_on()
            return {"status": "Plug turned on"}
        elif request.action.lower() == "off":
            d.turn_off()
            return {"status": "Plug turned off"}
        else:
            raise HTTPException(status_code=400, detail="Invalid action. Use 'on' or 'off'.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plug/status")
def get_plug_status():
    d = tinytuya.OutletDevice(dev_id=dev_id, address=dev_ip, local_key=dev_key, version=3.5)
    """Retrieve the current status of the smart plug."""
    try:
        status = d.status()
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
