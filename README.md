# Autovelql – Laravel & MySQL Environment Builder

![Version](https://img.shields.io/badge/version-3.0-blue.svg)
![License](https://img.shields.io/badge/license-Proprietary_Freeware-red.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Autovelql** is a professional-grade automation tool designed to streamline the initialization of Laravel development environments using Docker.

It eliminates the complex and error-prone process of manually configuring containers, permissions, environment variables, and database connections.

---

## [Global] Languages / Idiomas

- [English](#-english-reference-manual)
- [Español](#-guía-en-español)
- [Deutsch](#-anleitung-auf-deutsch)
- [한국어](#-한국어-가이드)
- [Italiano](#-guida-in-italiano)
- [Valencià](#-guia-en-valencià)

<br>

---

# [English] English Reference Manual

## Prerequisites

- Docker Desktop (running)
- Git
- Internet connection

> Python installation is NOT required.

---

## Architecture

Autovelql deploys a full **LAMP stack** using Docker:

- PHP 8.2 + Apache container
- MySQL 8.0 container
- PhpMyAdmin container
- Internal Docker network
- Persistent volumes (`proyecto/docker_volumes`)

---

## Installation

### Windows
```bat
start_windows.bat
````

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## Usage

1. Enter Git repository URL
2. Select branch
3. Configure database credentials
4. Click **BUILD PROJECT**

---

## Automated Build Pipeline

1. Project cleanup
2. Git clone
3. Docker Compose generation
4. Container startup
5. MySQL health check
6. Permission fix (`chmod -R 777`)
7. Composer install
8. Laravel APP_KEY generation
9. Database migrations & seeders

---

## Access

* Laravel App: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## Update Modes

### Update Mode (Safe)

* Preserves database volumes
* Updates source code

### Clean Install (Destructive)

* Deletes containers and volumes
* Fresh rebuild

---

## License

**Autovelql © 2025 – Proprietary Freeware**

Free to use.
Modification, redistribution, reverse engineering or resale is prohibited.

---

# [Spanish] Guía en Español

## Requisitos

* Docker Desktop en ejecución
* Git
* Conexión a Internet

---

## Arquitectura

* PHP 8.2 + Apache
* MySQL 8.0
* PhpMyAdmin
* Red Docker interna
* Volúmenes persistentes

---

## Instalación

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## Uso

1. Introduce la URL del repositorio Git
2. Selecciona la rama
3. Configura la base de datos
4. Pulsa **BUILD PROJECT**

---

## Proceso Automático

* Clonado del código
* Creación de contenedores
* Instalación de dependencias
* Generación de APP_KEY
* Migraciones y seeders
* Corrección de permisos

---

## Acceso

* Aplicación: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## Licencia

**Freeware Propietario (2025)**
Uso gratuito permitido. Prohibida la modificación o redistribución.

---

# [Deutsch] Anleitung auf Deutsch

## Voraussetzungen

* Docker Desktop
* Git
* Internetverbindung

---

## Architektur

* PHP 8.2 + Apache
* MySQL 8.0
* PhpMyAdmin
* Persistente Docker-Volumes

---

## Installation

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## Nutzung

1. Git-Repository-URL eingeben
2. Branch auswählen
3. Datenbank konfigurieren
4. **BUILD PROJECT** starten

---

## Automatisierte Schritte

* Repository klonen
* Container starten
* Composer installieren
* APP_KEY erzeugen
* Migrationen ausführen

---

## Zugriff

* Anwendung: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## Lizenz

**Proprietäre Freeware (2025)**
Änderung oder Weiterverteilung verboten.

---

# [Korean] 한국어 가이드

## 필수 조건

* Docker Desktop 실행 중
* Git 설치
* 인터넷 연결

---

## 아키텍처

* PHP 8.2 + Apache
* MySQL 8.0
* PhpMyAdmin
* Docker 네트워크 및 볼륨

---

## 설치

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## 사용 방법

1. Git 저장소 URL 입력
2. 브랜치 선택
3. 데이터베이스 설정
4. **BUILD PROJECT** 클릭

---

## 자동 처리 작업

* 코드 클론
* 컨테이너 실행
* Composer 설치
* APP_KEY 생성
* 마이그레이션 실행

---

## 접속

* Laravel 앱: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## 라이선스

**독점 프리웨어 (2025)**
수정, 재배포, 판매 금지

---

# [Italian] Guida in Italiano

## Requisiti

* Docker Desktop
* Git
* Connessione Internet

---

## Architettura

* PHP 8.2 + Apache
* MySQL 8.0
* PhpMyAdmin
* Volumi persistenti

---

## Installazione

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## Utilizzo

1. Inserire URL Git
2. Selezionare branch
3. Configurare database
4. Avviare **BUILD PROJECT**

---

## Accesso

* Applicazione: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## Licenza

**Freeware Proprietario (2025)**
Vietata modifica o rivendita.

---

# [Valencià] Guia en Valencià

## Requisits

* Docker Desktop actiu
* Git instal·lat
* Connexió a Internet

---

## Arquitectura

* PHP 8.2 + Apache
* MySQL 8.0
* PhpMyAdmin
* Volums persistents

---

## Instal·lació

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

---

## Ús

1. Introduir URL Git
2. Seleccionar branca
3. Configurar base de dades
4. Polsar **BUILD PROJECT**

---

## Accés

* Aplicació: [http://localhost](http://localhost)
* PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

---

## Llicència

**Freeware Propietari (2025)**
Prohibida la modificació o venda del programari.

