Here's a `README.md` draft for your project:

---

# Tuya Smart Plug Control API

This project provides a simple API to control a Tuya smart plug via a FastAPI server, allowing integration with automation tools like IFTTT or Automate. The server forwards commands to turn the plug on or off, or to retrieve its status, by leveraging the `TinyTuya` library.

## Features
- Turn the Tuya smart plug on or off through API endpoints
- Check the current status of the plug
- Built on top of [TinyTuya](https://github.com/jasonacox/tinytuya)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A Tuya-compatible smart plug
- Credentials for your Tuya device (obtained using TinyTuya Wizard)

### Setup

1. Clone this repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Install dependencies:

   ```bash
   pip install fastapi tinytuya python-dotenv uvicorn
   ```

3. Configure environment variables:
   - Create a `.env` file in the project directory with the following variables:

     ```plaintext
     DEVICEID=<Your_Device_ID>
     DEVICEIP=<Your_Device_IP>
     DEVICEKEY=<Your_Device_Key>
     ```

4. Run the FastAPI server with Uvicorn:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   This will start the server, listening for requests on the specified port.

### Usage

- **Control the plug:** Send a `POST` request to `/plug/control` with a JSON payload specifying the action (`"on"` or `"off"`):

  ```json
  {
    "action": "on"
  }
  ```

- **Get plug status:** Send a `GET` request to `/plug/status` to retrieve the current state of the plug.

## TinyTuya Wizard for Device Setup

To obtain the required credentials (`Device ID`, `Device IP`, and `Local Key`), use the [TinyTuya Wizard](https://github.com/jasonacox/tinytuya) provided by TinyTuya.

### Important Note

If you encounter the following error:

```json
{
  "code": 28841107,
  "msg": "No permission. The data center is suspended.Please go to the cloud development platform to enable the data center.",
  "success": false
}
```

This issue might be related to using the Smart Life app in conjunction with the Tuya Developer Portal. Switching to the Tuya app (instead of Smart Life) resolved this issue during testing.

## References

- [TinyTuya Library](https://github.com/jasonacox/tinytuya)

---

This guide should help users understand and set up your Tuya Smart Plug Control API project. Let me know if you'd like to include additional details!