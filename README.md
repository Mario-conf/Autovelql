# Autovelql - Laravel & MySQL Environment Builder

![Version](https://img.shields.io/badge/version-2.0-blue.svg) ![License](https://img.shields.io/badge/license-Proprietary_Freeware-red.svg) ![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Autovelql** is the ultimate tool to automate the creation of Laravel development environments. Forget about manually configuring Docker, Linux permissions, environment variables, or databases.

With a single click, **Autovelql** downloads your repository, spins up servers, configures the database, and hands you a project ready to work.

---

### [LANGUAGES] Select Language / Selecciona Idioma

[[ENGLISH] **English (Main Guide)**](#-english-guide) | [[ESPAÑOL] **Español**](#-guía-en-español) | [[DEUTSCH] **Deutsch**](#-anleitung-auf-deutsch) | [[KOREAN] **한국어**](#-한국어-가이드) | [[ITALIANO] **Italiano**](#-guida-in-italiano) | [[VALENCIÀ] **Valencià**](#-guia-en-valencià)

---

<br>

## [ENGLISH] English Guide

### [PREREQUISITES] Prerequisites

To work its magic, you only need:

1.  **Docker Desktop** (Must be installed and running).
2.  **Git** (Recommended for cloning repositories).
3.  **Internet Connection**.

> **Note:** You do **not** need to install Python manually; the software uses its own embedded environment.

### [INSTALL] Installation & Start

#### Option A: Portable Scripts (Recommended)

This is the easiest way. Just download the source and run:

- **[WINDOWS] Windows:** Double-click on `start_windows.bat`.
- **[LINUX / MAC] Linux & macOS:** Open terminal and run: `. ./start_linux.sh`

#### Option B: GitHub Package (Docker Image)

If you prefer to run the app in an isolated container without installing Python locally:

```bash
docker run -it --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(pwd)/proyecto:/app/proyecto \
  ghcr.io/tu-usuario/autovelql:latest
```

### [GUIDE] Usage Guide

Once the **Autovelql** window opens:

1.  **Repository Setup:**

    - **Repo URL:** Paste your GitHub project link (e.g., `https://github.com/user/my-repo.git`).
    - **Branch:** Default is `main`, change if needed.

2.  **Database Configuration:**

    - Define **DB Name**, **User**, and **Password**. Autovelql syncs this automatically in MySQL and your Laravel `.env`.

3.  **Build Project:**

    - Click the blue **"BUILD PROJECT"** button.
    - Sit back! The system will clone code, start containers, fix permissions (`chmod 777`), install composer dependencies, and run migrations.

4.  **Ready!**
    - **App:** `http://localhost`
    - **Database (PMA):** `http://localhost:8080`

### [UPDATES] Updates vs. Clean Install

If a project already exists, Autovelql detects it:

- [UPDATE] **UPDATE (Keep DB):** Updates code from Git but keeps your database data intact.
- [CLEAN] **CLEAN INSTALL (Wipe):** Deletes **everything** (Code & DB) and starts from scratch.

### [LICENSE] License (Proprietary Freeware)

**Autovelql © 2025 - All Rights Reserved.**

1.  **Free Use:** You may use this software for free for personal, educational, or commercial purposes.
2.  **Closed Source:** This is **not** Open Source. Source code, design, and logic belong exclusively to the author.
3.  **Restrictions:** Modification, reverse engineering, decompilation, and redistribution of modified copies are **strictly prohibited**.

---

<br>

## [ESPAÑOL] Guía en Español

**Autovelql** automatiza tu entorno Laravel + Docker + MySQL en un clic.

### [INSTALL] Cómo Iniciar

- **Windows:** Doble click en `start_windows.bat`.
- **Linux/Mac:** Ejecuta `. ./start_linux.sh` en la terminal.

### [GUIDE] Instrucciones

1.  **Pega la URL** de tu repositorio GitHub.
2.  Configura el **Nombre de BD** y Usuario (se crearán automáticamente).
3.  Pulsa **CONSTRUIR PROYECTO**.
4.  El sistema configurará Docker, Permisos, Composer y Migraciones por ti.

### [LICENSE] Licencia (Freeware Propietario)

**Uso gratuito permitido.** Código cerrado. **Prohibido** modificar, desensamblar, vender o redistribuir el código fuente sin permiso explícito del autor.

---

<br>

## [DEUTSCH] Anleitung auf Deutsch

**Autovelql** ist das ultimative Tool zur Automatisierung von Laravel-Entwicklungsumgebungen.

### [INSTALL] Starten

- **Windows:** Doppelklick auf `start_windows.bat`.
- **Linux/Mac:** Führen Sie `. ./start_linux.sh` im Terminal aus.

### [GUIDE] Anleitung

1.  **GitHub-URL** einfügen.
2.  **Datenbanknamen** und Benutzer konfigurieren.
3.  Klicken Sie auf **CONSTRUIR PROYECTO**.
4.  Das System konfiguriert Docker, Berechtigungen, Composer und Migrationen automatisch.

### [LICENSE] Lizenz (Proprietäre Freeware)

**Kostenlose Nutzung erlaubt.** Closed Source. Änderungen, Reverse Engineering, Verkauf oder Weitergabe des Quellcodes sind **strengstens untersagt**.

---

<br>

## [KOREAN] 한국어 가이드

**Autovelql**은 Laravel 및 MySQL 개발 환경을 자동으로 구축해주는 도구입니다.

### [INSTALL] 시작하기

- **Windows:** `start_windows.bat` 파일을 더블 클릭하세요.
- **Linux/Mac:** 터미널에서 `. ./start_linux.sh` 를 실행하세요.

### [GUIDE] 사용법

1.  GitHub **레포지토리 URL**을 입력하세요.
2.  **데이터베이스 이름**과 사용자를 설정하세요 (자동으로 생성됩니다).
3.  **CONSTRUIR PROYECTO** 버튼을 클릭하세요.
4.  시스템이 Docker, 권한, Composer, 마이그레이션을 자동으로 설정합니다.

### [LICENSE] 라이선스 (독점 프리웨어)

**무료 사용 가능.** 비공개 소스. 작성자의 명시적인 허가 없이 소스 코드를 **수정, 역분석, 판매 또는 재배포하는 것은 엄격히 금지됩니다.**

---

<br>

## [ITALIANO] Guida in Italiano

**Autovelql** è lo strumento definitivo per automatizzare la creazione di ambienti di sviluppo Laravel.

### [INSTALL] Come Iniziare

- **Windows:** Doppia clic su `start_windows.bat`.
- **Linux/Mac:** Esegui `. ./start_linux.sh` nel terminale.

### [GUIDE] Istruzioni

1.  **Incolla l'URL** del tuo repository GitHub.
2.  Configura il **Nome DB** e l'Utente (verranno creati automaticamente).
3.  Clicca su **CONSTRUIR PROYECTO** (Costruisci Progetto).
4.  Il sistema configurerà Docker, Permessi, Composer e Migrazioni per te.

### [LICENSE] Licenza (Freeware Proprietario)

**Uso gratuito consentito.** Codice chiuso. È **vietato** modificare, disassemblare, vendere o ridistribuire il codice sorgente senza esplicito permesso dell'autore.

---

<br>

## [VALENCIÀ] Guia en Valencià

**Autovelql** automatitza el teu entorn Laravel + Docker + MySQL en un sol clic.

### [INSTALL] Com Iniciar

- **Windows:** Doble clic en `start_windows.bat`.
- **Linux/Mac:** Executa `. ./start_linux.sh` en la terminal.

### [GUIDE] Instruccions

1.  **Pega l'URL** del teu repositori GitHub.
2.  Configura el **Nom de BD** i Usuari (es crearan automàticament).
3.  Prem **CONSTRUIR PROYECTO**.
4.  El sistema configurarà Docker, Permisos, Composer i Migracions per tu.

### [LICENSE] Llicència (Freeware Propietari)

**Ús gratuït permés.** Codi tancat. Està **prohibit** modificar, desassemblar, vendre o redistribuir el codi font sense permís explícit de l'autor.
