# 🛡️ **Honeypot Security Project**

**Author:** Swapnil Katuwal
**Purpose:** Multi-layer cybersecurity honeypot for detection, analysis, and attacker behavior study.

---

## 📌 **Overview**

This project is a **multi-stage honeypot environment** designed to attract, detect, and analyze malicious activity.

It includes:

* **Low-interaction honeypot** (TCP trap)
  ✔️ Implemented: Logs connection attempts/payloads
* **SSH honeypot** (credential harvesting)
  ✔️ Implemented: Fake SSH banner + credential logger
* **Web honeypot** (fake login portal)
  ⏳ In development
* **Centralized log pipeline** (SIEM-style analysis)
  ⏳ Planned
* **Dashboard integrations** (ELK, Grafana)
  ⏳ Planned
* **Network hardening configs**
  ⏳ Planned

A full environment for studying attacker behavior, scanning patterns, password spraying, brute force attempts, and general threat activity.

---

# 📂 **Project Structure**

```
honeypot-project/
│
├── README.md
├── .gitignore
│
├── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── low_interaction/
│   ├── server.py
│   └── logs/
│       └── .gitkeep
│
├── ssh_honeypot/
│   ├── ssh_fake.py
│   └── logs/
│       └── .gitkeep
│
├── web_honeypot/
│   ├── app.py
│   ├── templates/
│   │   └── login.html
│   └── logs/
│       └── .gitkeep
│
├── network/
│   ├── iptables_rules.txt
│   └── fail2ban/
│       └── jail.local
│
├── analysis/
│   ├── raw/
│   └── enriched/
│   └── reports/
│
├── dashboards/
│   ├── elk/
│   └── grafana/
│
└── scripts/
    ├── start_all.sh
    ├── stop_all.sh
    └── rotate_logs.sh
```

---

# 🔥 **Modules Documentation**

---

# 📡 **1. Low-Interaction Honeypot (`low_interaction/`)**

### 🧠 Purpose

A lightweight TCP-based trap to capture probes, scans, bot traffic, and attacker fingerprints without exposing any real service.
It listens, accepts connections, and logs EVERYTHING.

---

### ⚙️ Features

* Opens a configurable TCP port
* Logs:

  * Attacker IP
  * Attacker port
  * Timestamp
  * Payload (if sent)
* Multi-threaded — handles large scan bursts
* Silent responses to confuse scanners
* Perfect for early detection

---

### 📄 Log Example

```
[2025-11-26 14:42:01] Connection from 103.54.12.22:51893
[2025-11-26 14:42:01] Payload: "GET /malware HTTP/1.1"
```

Logs stored in:

```
low_interaction/logs/low_interaction.log
```

---

### ▶️ Run it

```bash
python3 server.py --port 2222
```

Background mode:

```bash
nohup python3 server.py --port 2222 &
```

---

### ⚠️ Notes / Warnings

* This is intentionally minimal
* Use inside a VM or controlled environment
* Pair with ELK for analytics

---

# 🔑 **2. SSH Honeypot (`ssh_honeypot/`)**

### 🧠 Purpose

A fake SSH service built to attract brute-force bots, automated scripts, and attackers looking for weak credentials.

It **never gives real access** — only logs credentials and interaction attempts.

---

### ⚙️ Features

* Custom fake SSH banner
* Logs:

  * Username
  * Password
  * Attacker IP
  * Timestamp
* Simulates authentication failure
* Simple to deploy
* Safe “illusion” of SSH access

---

### 📄 Log Example

```
[2025-11-26 15:30:14] IP: 185.244.25.10 USER: root PASS: admin123
```

Stored in:

```
ssh_honeypot/logs/ssh.log
```

---

### ▶️ Run it

```bash
python3 ssh_fake.py --port 2222
```

or background mode:

```bash
nohup python3 ssh_fake.py --port 2222 &
```

You can also bind it to port 22 (⚠️ with sudo):

```bash
sudo python3 ssh_fake.py --port 22
```

---

### 🛑 Notes

* This is a credential harvester ONLY
* Does not emulate a real SSH shell
* Do NOT run alongside your actual SSH server on same port

---

# 🌐 **3. Web Honeypot (In Development)**

Simulated login page to capture:

* Username
* Password
* IP address
* User-agent
* Timestamp

You will implement this in a Flask app.

---

# ⚠️ Disclaimer

This project is for **educational and research purposes ONLY**.
Running honeypots on public networks can expose you to malicious threats.

Deploy responsibly.

