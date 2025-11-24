Honeypot Security Project

Author: Swapnil Katuwal
Purpose: Multi‑layer cybersecurity honeypot for detection, analysis, and attacker behavior study.

📌 Overview

This project is a multi‑stage honeypot environment designed to attract, detect, and log malicious activity.
It includes:

Low‑interaction honeypot (simulated vulnerable service)

SSH honeypot (fake shell login)

Web honeypot (fake login portal for credential harvesting)

Log pipeline + analysis folders

Future dashboard integrations (ELK, Grafana)

Network hardening configs (iptables, fail2ban)

This project demonstrates your skills in Python, network security, log analysis, incident detection, and SOC tooling.

📂 Project Structure
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

🚀 Current Features

✔ Low‑interaction honeypot
✔ SSH credential harvesting honeypot
✔ Web login decoy
✔ Centralized log directories
✔ Organized project structure
✔ Ready for Dockerization

📅 Roadmap (Coming Soon)

Docker deployment

ELK dashboard

Grafana visualization

Threat enrichment (GeoIP, ASN lookup)

Automated log rotation

Log correlation scripts

⚠️ Disclaimer

This honeypot is for educational and research purposes only.
Running honeypots on a public network can expose you to malicious traffic — deploy responsibly.