# 🐳 Dockerized Machine-to-Machine Communication

This project demonstrates how to set up **two Docker containers (Machine A & Machine B)** and establish communication between them.  
It is designed as a beginner-friendly guide to understand **Docker networking, container communication, and interactive debugging**.

---

## 📌 Features
- Two separate machines (`Machine A` and `Machine B`) built with **individual Dockerfiles**.
- Containers are connected on the **same Docker network** to enable communication.
- Interactive shell access to each container.
- Example of how containers can **exchange messages**.
- Beginner-friendly setup with clear steps.

---

## 🛠️ Project Structure
.

├── Dockerfile.D # Build instructions for Machine A 

├── Dockerfile.B # Build instructions for Machine B

├── docker-compose.yml # Compose file to start both machines together

├── client.py      # clinet program 

├── server.py      # server program 

└── README.md # Project documentation
