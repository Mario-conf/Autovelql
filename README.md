# Autovelql - Laravel & MySQL Environment Builder

![Version](https://img.shields.io/badge/version-3.0-blue.svg) ![License](https://img.shields.io/badge/license-Proprietary_Freeware-red.svg) ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Autovelql** is a professional-grade automation tool designed to streamline the initialization of Laravel development environments. It eliminates the complex, error-prone process of manually configuring Docker containers, Linux file permissions, environment variables, and database connections.

By acting as an intelligent bridge between your Git repository and a local Docker infrastructure, Autovelql allows developers to go from "zero" to a fully functional, database-seeded application in minutes.

---

### [LANGUAGES] Select Language / Selecciona Idioma

[[ENGLISH] **English (Reference Manual)**](#-english-reference-manual) | [[ESPAÑOL] **Español**](#-guía-en-español) | [[DEUTSCH] **Deutsch**](#-anleitung-auf-deutsch) | [[KOREAN] **한국어**](#-한국어-가이드) | [[ITALIANO] **Italiano**](#-guida-in-italiano) | [[VALENCIÀ] **Valencià**](#-guia-en-valencià)

---

<br>

## [ENGLISH] English Reference Manual

### [PREREQUISITES] System Prerequisites

Before running Autovelql, ensure your system meets the following requirements. The software relies on these core components to virtualize the environment.

1.  **Docker Desktop**: The engine that powers the containers.
    - _Requirement:_ Must be installed and **currently running** (look for the whale icon in your taskbar).
    - _Download:_ [Docker Desktop Official Site](https://www.docker.com/products/docker-desktop/)
2.  **Git SCMS**: Required to clone your repositories from GitHub/GitLab.
    - _Download:_ [Git Official Site](https://git-scm.com/downloads)
3.  **Internet Connection**: Necessary for:
    - Downloading the Docker Images (MySQL 8.0, PHP 8.2, Apache, PhpMyAdmin).
    - Cloning your source code.
    - Running `composer install` inside the container.

> **Note on Python:** You do **not** need to manually install Python. Autovelql includes a self-contained environment management script.

---

### [INFO] Technical Architecture

When you build a project, Autovelql orchestrates a complete stack known as **LAMP** (Linux, Apache, MySQL, PHP) on Docker:

- **App Container:** Runs PHP 8.2 and Apache. Mounts your source code at `/app`.
- **Database Container:** Runs MySQL 8.0.
- **Management Container:** Runs PhpMyAdmin (PMA) for GUI database management.
- **Networking:** An internal Docker network connects these services automatically.
- **Volumes:** Data persistence is handled via Docker Volumes (mounted in `proyecto/docker_volumes`).

---

### [INSTALL] Installation & Startup Methods

#### Method A: Native Launchers (Recommended)

This is the standard way to run the application on your host machine.

1.  **Step 1:** Download the latest Source Code zip from the Releases page.
2.  **Step 2:** Extract the folder to a location of your choice (e.g., `Documents/Autovelql`).
3.  **Step 3:** Run the launcher:
    - **[WINDOWS] Windows:** Double-click `start_windows.bat`.
      - _Note:_ If prompted by Windows SmartScreen, click "More info" -> "Run anyway". Also accept Admin permissions if the script needs to install dependencies.
    - **[LINUX / MAC] Linux & macOS:** Open a terminal in the folder and run:
      ```bash
      . ./start_linux.sh
      ```
      _(Ensure you include the leading dot and space for proper shell sourcing)._

#### Method B: GitHub Package (Isolated Docker Container)

If you prefer not to use Python on your host or want a completely isolated toolchain, you can run the builder itself inside Docker.

```bash
docker run -it --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(pwd)/proyecto:/app/proyecto \
  ghcr.io/your-username/autovelql:latest
```

_Note: This requires mounting the Docker socket so the container can spawn sibling containers._

---

### [GUIDE] Detailed Usage Guide

Once the graphical interface loads, follow these steps to deploy your application.

#### 1. Repository Configuration

This tells Autovelql where to get your source code.

- **Repository URL:** Enter the full HTTPS clone URL of your repository.
  - _Example:_ `https://github.com/laravel/laravel.git`
  - _Important:_ Ensure you have access to the repo. If it is private, you may need to authorize Git credentials in your terminal or use SSH (if configured).
- **Branch:** The specific branch you want to checkout.
  - _Default:_ `main` (or `master` for older legacy projects).

#### 2. Database Definition

Autovelql generates a custom `docker-compose.yml` and updates your Laravel `.env` file based on these values.

- **DB Name:** The logical name of the database (e.g., `my_app`).
- **DB User:** The proprietary user account for the database application.
- **DB Password:** The secret key for the database user.

#### 3. Execution (Build Project)

Clicking **"BUILD PROJECT"** triggers an automated pipeline:

1.  **Preparation:** Checks if the `proyecto` folder exists and cleans it if necessary.
2.  **Cloning:** Executes `git clone` to fetch your source code.
3.  **Infrastructure:** Generates `docker-compose.yml` and runs `docker compose up -d`.
4.  **Health Check:** Waits for MySQL to accept connections (prevents connection errors during migration).
5.  **Permission Fix:** Runs `chmod -R 777` on `storage/` and `bootstrap/cache/`. This is critical for Windows users to prevent "Permission Denied" errors in logs.
6.  **Dependency Injection:** Runs `composer install` inside the container to download PHP libraries.
7.  **Environment Config:** Generates `APP_KEY` and populates `.env` with the DB credentials you provided.
8.  **Database Seeding:** Runs `php artisan migrate --seed` to populate tables.

#### 4. Accessing the Application

Upon success, the tool will open your default browser:

- **Application URL:** `http://localhost:80` (Standard HTTP port).
- **Database Manager:** `http://localhost:8080` (PhpMyAdmin).

---

### [UPDATES] Project Lifecycle Management

Autovelql is smart enough to detect if you have worked on a project before.

- **[UPDATE] Update Mode (Safe):**
  - _Behavior:_ This mode performs a `git pull` (or re-clone) of the code but **preserves** the `docker_volumes` folder.
  - _Use Case:_ Use this when a teammate pushes new code, but you do not want to lose your local database data (users, test entries, etc.).
- **[CLEAN] Clean Install Mode (Destructive):**
  - _Behavior:_ Using advanced cleaning scripts, this mode force-stops containers, removes orphans, and deletes the entire `proyecto` directory including the database volumes.
  - _Use Case:_ Use this when the environment is corrupted or you want to start fresh from a "Factory Reset" state.

---

### [FAQ] Troubleshooting & Common Issues

#### Docker Connectivity Issues

- **Issue:** Log shows _"Error: Docker is not running"_ or _"Daemon not reachable"_.
- **Solution:** Open Docker Desktop dashboard. Wait for the status bar to turn green. If on Linux, restart the service: `sudo systemctl restart docker`.

#### Port Conflicts (3306 / 80)

- **Issue:** Docker fails to bind port 0.0.0.0:3306 or 0.0.0.0:80.
- **Cause:** You likely have XAMPP, WAMP, Laragon, or a local MySQL server running on your machine.
- **Solution:** Stop all local web server services. Alternatively, you can edit the generated `docker-compose.yml` in the `proyecto` folder and change the ports mapping (e.g., `"8081:80"`), then run `docker compose up -d`.

#### Database Connection Refused

- **Issue:** Laravel logs say `SQLSTATE[HY000] [2002] Connection refused`.
- **Cause:** Your `.env` file might be pointing to `127.0.0.1` or `localhost`.
- **Solution:** Autovelql automatically handles this, but if you edit `.env` manually, remember: inside Docker, the database host is named `mysql` (the service name), not localhost. Ensure `DB_HOST=mysql`.

#### File Permission Errors (Windows)

- **Issue:** Laravel log file could not be opened or written.
- **Solution:** Detailed permission fixing is built-in. However, if you add new folders manually, you may need to enter the container and `chmod` them:
  ```bash
  docker compose exec app chmod -R 777 storage
  ```

---

### [LICENSE] License (Proprietary Freeware)

**Autovelql © 2025 - All Rights Reserved.**

This software is provided under a **Proprietary Freeware** license. It is free to use but restricted in modification.

1.  **Grant of License:** You are granted a non-exclusive license to use this software for personal, educational, or commercial purposes at no cost.
2.  **No Source Modification:** This is **not** Open Source software. The underlying source code, logic, and design methodologies remain the exclusive intellectual property of the author.
3.  **Prohibitions:**
    - You may NOT modify, adapt, translate, reverse engineer, decompile, or disassemble the Software.
    - You may NOT redistribute modified versions of the Software.
    - You may NOT sell, lease, rent, or sublicense the Software to third parties.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.**

---

<br>

## [ESPAÑOL] Guía en Español

**Autovelql** es una solución profesional para la automatización de entornos Laravel.

### [PREREQUISITES] Requisitos

- **Docker Desktop:** Debe estar instalado y corriendo.
- **Git:** Para descargar el código.

### [INSTALL] Instalación

- **Windows:** Ejecuta el script `start_windows.bat`.
- **Linux/Mac:** Ejecuta `. ./start_linux.sh` desde la terminal.

### [GUIDE] Uso Detallado

1.  **Repositorio:** Introduce la URL HTTPS de tu Git.
2.  **Base de Datos:** Configura nombre, usuario y contraseña. Autovelql sincronizará estos datos entre Docker y Laravel.
3.  **Construir:** Al pulsar "BUILD PROJECT", el sistema levantará un stack LAMP completo (Linux, Apache, MySQL, PHP), corregirá permisos (`chmod 777`), instalará dependencias (`composer`) y ejecutará migraciones.

### [LICENSE] Licencia

**Proprietary Freeware (2025).**
Uso gratuito permitido. Prohibida la modificación, ingeniería inversa o venta del código fuente.

---

<br>

## [DEUTSCH] Anleitung auf Deutsch

**Autovelql** ist ein professionelles Tool zur Automatisierung von Laravel-Umgebungen.

### [INSTALL] Installation

- **Windows:** Führen Sie `start_windows.bat` aus.
- **Linux/Mac:** Führen Sie `. ./start_linux.sh` im Terminal aus.

### [GUIDE] Nutzung

Geben Sie Ihre Git-Repository-URL und die gewünschten Datenbankdaten ein. Das System erstellt automatisch eine vollständige LAMP-Stack-Umgebung (Linux, Apache, MySQL, PHP) in Docker Containern.

### [LICENSE] Lizenz

**Proprietäre Freeware (2025).**
Kostenlose Nutzung erlaubt. Änderung, Reverse Engineering oder Verkauf des Quellcodes sind untersagt.

---

<br>

## [KOREAN] 한국어 가이드

**Autovelql**은 Laravel 개발 환경을 위한 전문가용 자동화 도구입니다.

### [INSTALL] 설치 방법

- **Windows:** `start_windows.bat` 파일을 실행하십시오.
- **Linux/Mac:** 터미널에서 `. ./start_linux.sh` 명령어를 실행하십시오.

### [GUIDE] 사용법

Git 레포지토리 URL과 데이터베이스 자격 증명을 입력하면, 도구가 자동으로 Docker 컨테이너(LAMP 스택)를 생성하고 환경을 구성합니다.

### [LICENSE] 라이선스

**독점 프리웨어 (2025).**
무료 사용이 가능하지만, 소스 코드의 수정, 역분석, 판매는 엄격히 금지됩니다.

---

<br>

## [ITALIANO] Guida in Italiano

**Autovelql** è una soluzione professionale per l'automazione degli ambienti Laravel.

### [INSTALL] Installazione

- **Windows:** Esegui lo script `start_windows.bat`.
- **Linux/Mac:** Esegui `. ./start_linux.sh` nel terminale.

### [GUIDE] Uso

Inserisci l'URL del repository Git e le credenziali del database. Il sistema creerà automaticamente un ambiente LAMP completo in Docker.

### [LICENSE] Licenza

**Freeware Proprietario (2025).**
Uso gratuito consentito. Vietata la modifica, il reverse engineering o la vendita del codice sorgente.

---

<br>

## [VALENCIÀ] Guia en Valencià

**Autovelql** és una eina professional per a l'automatització d'entorns Laravel.

### [INSTALL] Instal·lació

- **Windows:** Executa l'arxiu `start_windows.bat`.
- **Linux/Mac:** Executa `. ./start_linux.sh` al terminal.

### [GUIDE] Ús

Introdueix l'URL del repositori Git i les credencials de la base de dades. El sistema alçarà automàticament un entorn LAMP complet (Linux, Apache, MySQL, PHP) en contenidors Docker.

### [LICENSE] Llicència

**Freeware Propietari (2025).**
Ús gratuït permés. Prohibida la modificació, enginyeria inversa o venda del codi font.
