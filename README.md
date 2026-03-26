# bee-homeassistant-addon
A backend service that connects Bee wearable data to Home Assistant, providing real-time insights, summaries, and automation-ready endpoints.


# 🐝 Bee Home Assistant Backend

Bring your **Bee wearable data** into Home Assistant with a clean, local, and automation-ready backend.

This add-on provides a bridge between the Bee CLI and Home Assistant, exposing your data through a simple HTTP API that can be used by a custom HACS integration.

---

## ✨ Features

- 📡 Local API for Bee data (no cloud required)
- 🧠 Access conversations, daily summaries, facts, and todos
- 📊 Designed for dashboards, automations, and notifications
- ⚡ Fast and lightweight backend powered by Python + FastAPI
- 🔌 Built specifically for Home Assistant integration

---

## 🧱 What This Add-on Does

This add-on runs a backend service that:

- Communicates with the Bee CLI
- Converts Bee data into structured JSON
- Exposes a local API for Home Assistant to consume

Example endpoints:

| Endpoint     | Description                          |
|-------------|--------------------------------------|
| `/health`   | Check if backend is running          |
| `/status`   | Bee authentication status            |
| `/me`       | Your Bee profile                     |
| `/today`    | Daily summary (calendar + email)     |
| `/now`      | Recent conversations                 |
| `/facts`    | Stored memory/facts                  |
| `/todos`    | Task list                            |

---

## 🚀 Installation

1. Add this repository to Home Assistant:
   - **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
   - Paste your repo URL

2. Install **Bee Backend**

3. Start the add-on

4. (Optional) Configure Bee CLI path if needed

---

## ⚙️ Configuration

```yaml
bee_binary_path: "/usr/local/bin/bee"
webhook_url: ""
