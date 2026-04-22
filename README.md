# 🔐 Real-Time Intrusion Detection System (IDS)

## 📌 Overview

This project implements a real-time Intrusion Detection System (IDS) to detect brute-force SSH attacks by monitoring Linux authentication logs.

---

## 🎯 Objective

* Detect unauthorized login attempts
* Identify brute-force attack patterns
* Trigger alerts and simulate response actions
* Demonstrate real-world cybersecurity workflow

---

## 🧠 How It Works

* Monitors `/var/log/auth.log`
* Detects repeated failed login attempts
* Identifies attacker IP
* Triggers alert and response

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[Attacker] --> B[SSH Service]
    B --> C[auth.log]
    C --> D[IDS Script - Python]
    D --> E[Log Parsing]
    E --> F[Threshold Detection]
    F --> G[Alert Trigger]
    G --> H[IP Blocking Simulated]
```

---

## ⚙️ Tech Stack

* Python
* Linux (WSL / Ubuntu)
* SSH
* rsyslog

---

## 🚀 Features

* Real-time log monitoring
* Brute-force attack detection
* IP tracking and counting
* Threshold-based alert system
* Automated response simulation

---

## 📂 Project Structure

```
ids-project/
│── ids.py
│── README.md
```

---

## 🧪 Setup & Installation

```bash
sudo apt update
sudo apt install python3 rsyslog openssh-server -y
```

### Start services

```bash
sudo service rsyslog start
sudo service ssh start
```

---

## ▶️ Usage

### Run IDS

```bash
python3 ids.py
```

### Simulate attack

```bash
ssh fakeuser@localhost
```

---

## 📊 Sample Output

```
[INFO] Failed attempt from 127.0.0.1 (1)
[INFO] Failed attempt from 127.0.0.1 (2)
[INFO] Failed attempt from 127.0.0.1 (3)

[ALERT] Brute-force attack detected from 127.0.0.1
[ACTION] Blocking IP: 127.0.0.1
```

---

## 🧠 Key Concepts Demonstrated

* Log analysis and parsing
* Pattern detection using regular expressions
* Real-time monitoring
* Basic security automation

---

## ⚠️ Limitations

* IP blocking is simulated (WSL limitation)
* Uses local logs instead of distributed systems

---

## 🚀 Future Enhancements

* Real firewall integration (UFW / iptables)
* Email / Telegram alert system
* Cloud integration (AWS logs)

---

## 💼 Resume Description

Developed a real-time intrusion detection system to monitor SSH logs and detect brute-force attacks using Python with automated response simulation.


