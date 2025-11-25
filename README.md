# 🛡️ Honeypot Security Project
**Author:** Swapnil Katuwal  
**Purpose:** Multi-layer cybersecurity honeypot for detection, analysis, and attacker behavior study.

---

## 📌 Overview
This project is a **multi-stage honeypot environment** designed to attract, detect, and log malicious activity.  
It includes:

- **Low-interaction honeypot** (simulated vulnerable service) ✅ Implemented: logs TCP connections with SOC-style timestamps  
- **SSH honeypot** (fake shell login)  
- **Web honeypot** (fake login portal)  
- **Centralized log pipeline** for analysis  
- **Dashboard integrations** (ELK, Grafana) planned  
- **Network hardening configs** (iptables, fail2ban)  

---

## 📂 Project Structure

```text
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
│   │   └── .gitkeep
│   ├── enriched/
│   │   └── .gitkeep
│   └── reports/
│       └── .gitkeep
│
├── dashboards/
│   ├── elk/
│   │   └── .gitkeep
│   └── grafana/
│       └── .gitkeep
│
└── scripts/
    ├── start_all.sh
    ├── stop_all.sh
    └── rotate_logs.sh
````

---

## ⚠️ Disclaimer

This honeypot is for **educational and research purposes only**.
Running honeypots on public networks can expose you to malicious traffic — **deploy responsibly**.


