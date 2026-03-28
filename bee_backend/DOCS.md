# 🐝 Bee Backend for Home Assistant

This add-on connects your **Bee wearable data** to Home Assistant by providing a local backend API.

It acts as the bridge between the Bee CLI and a Home Assistant integration, making your data available for automations, dashboards, and notifications.

---

## ✨ Features

- 📡 Local API (no cloud dependency required)
- 🧠 Access Bee data:
  - Conversations
  - Daily summaries
  - Facts (memory)
  - Todos
- ⚡ Fast and lightweight backend (FastAPI)
- 🔌 Designed for seamless Home Assistant integration

---

## 🚀 Getting Started

### 1. Install the add-on

- Add this repository to Home Assistant
- Install **Bee Backend**
- Start the add-on

---

### 2. Verify it is running

Once started, the backend will be available at:

- http://homeassistant.local:8130
     or
- http://<your-home-assistant-ip>:8130


Test it:

```bash

curl http://<your-home-assistant-ip>:8130/health

```
You should receive:
~~~
{
  "ok": true,
  "service": "bee_backend"
}
~~~
⚙️ Configuration
~~~
bee_binary_path: "/usr/local/bin/bee"
webhook_url: ""
~~~


| Option            | Description                                 |
| ----------------- | ------------------------------------------- |
| `bee_binary_path` | Path to the Bee CLI binary                  |
| `webhook_url`     | Optional webhook for realtime event pushing |

| Endpoint  | Description               |
| --------- | ------------------------- |
| `/health` | Check backend status      |
| `/status` | Bee authentication status |
| `/me`     | User profile              |
| `/today`  | Daily summary             |
| `/now`    | Recent conversations      |
| `/facts`  | Stored facts              |
| `/todos`  | Task list                 |

🧩 Integration

This add-on is designed to work with the Bee Home Assistant Integration (HACS).

The integration will:

- Automatically connect to this backend
- Create sensors and entities
- Enable automations based on Bee data

🛠️ Troubleshooting
Add-on starts but API not responding
Check logs for errors
Ensure port 8130 is accessible
Restart the add-on

Bee commands failing

If Bee-related endpoints fail:

- Ensure Bee CLI is installed in the container
- Verify bee_binary_path is correct

⚠️ Notes
- This project is under active development
- Some features may be incomplete or evolving


🧑‍💻 Author

Built for Home Assistant users who want deeper insight into their daily life through Bee.

⚠️ Disclaimer

This project is not affiliated with Bee.
It is an independent integration for Home Assistant.
