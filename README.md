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


---

## ⚙️ How We Created It
1. **Built two Dockerfiles** (`Dockerfile.D` & `Dockerfile.B`) with minimal Linux + tools installed.
2. **Wrote a `docker-compose.yml`** file that defines both machines and exposes ports.
3. build server and client programs 
4. Used `docker-compose up` to start both containers together.
5. Verified that both machines could communicate through the internal Docker network.
6. Used `docker exec -it` to open interactive shells and test message exchange between machines.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/docker-machines-communication.git
cd docker-machines-communication
```-
