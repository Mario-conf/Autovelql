# Autovelql – Laravel & MySQL Environment Builder

![Autovelql Logo](docs/img/beg.png)

![Version](https://img.shields.io/badge/version-3.0-blue.svg)
![License](https://img.shields.io/badge/license-Proprietary_Freeware-red.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Autovelql** is a professional-grade automation tool designed to streamline the initialization of Laravel development environments using Docker. 

It eliminates the complex and error-prone process of manually configuring containers, permissions, environment variables, and database connections.

---

## Languages / Idiomas

- [English](#-english-reference-manual)
- [Español](#-guía-en-español)
- [Deutsch](#-anleitung-auf-deutsch)
- [한국어](#-한국어-가이드)
- [Italiano](#-guida-in-italiano)




---

# [English] English Reference Manual

## Prerequisites

- Docker Desktop (running)
- Git
- Internet connection
  > Python installation is NOT required.

## Architecture

Autovelql deploys a full **LAMP stack** using Docker:

- PHP 8.2 + Apache container
- MySQL 8.0 container
- PhpMyAdmin container
- Internal Docker network
- Persistent volumes (`proyecto/docker_volumes`)

## Installation

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

## Usage

1. Enter Git repository URL
2. Select branch
3. Configure database credentials
4. Click **BUILD PROJECT**

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

## Access

- Laravel App: [http://localhost](http://localhost)
- PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

## Update Modes

### Update Mode (Safe)

- Preserves database volumes
- Updates source code

### Clean Install (Destructive)

- Deletes containers and volumes
- Fresh rebuild

## Troubleshooting & FAQ

**Port Conflicts**

- **Cause:** Port 80 or 8080 is already in use by another application.
- **Solution:** Ensure no other services (like XAMPP, Laragon, or other Docker containers) are running on these ports before starting.

**Docker permission denied**

- **Cause:** The user running the app inside the container usually maps to `www-data`.
- **Solution:** The structure ensures correct permissions. If you face issues on Linux/macOS, ensure your user is in the `docker` group.

**Styles or Assets not loading**

- **Cause:** Asset compilation (Vite/Mix) might have failed or cache is stale.
- **Solution:** Try forcing a rebuild of the containers to ensure all assets are compiled correctly.

---

# [Spanish] Guía en Español

## Requisitos

- Docker Desktop en ejecución
- Git
- Conexión a Internet

## Arquitectura

- PHP 8.2 + Apache
- MySQL 8.0
- PhpMyAdmin
- Red Docker interna
- Volúmenes persistentes

## Instalación

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

## Uso

1. Introduce la URL del repositorio Git
2. Selecciona la rama
3. Configura la base de datos
4. Pulsa **BUILD PROJECT**

## Proceso Automático

- Clonado del código
- Creación de contenedores
- Instalación de dependencias
- Generación de APP_KEY
- Migraciones y seeders
- Corrección de permisos

## Acceso

- Aplicación: [http://localhost](http://localhost)
- PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

## Solución de Problemas y FAQ

**Conflictos de Puertos**

- **Causa:** El puerto 80 u 8080 está en uso por otra aplicación.
- **Solución:** Asegúrate de que no haya otros servicios (como XAMPP, Laragon u otros contenedores Docker) ejecutándose en estos puertos antes de iniciar.

**Permiso denegado en Docker**

- **Causa:** El usuario que ejecuta la aplicación dentro del contenedor suele mapearse a `www-data`.
- **Solución:** La estructura asegura los permisos correctos. Si tienes problemas en Linux/macOS, asegúrate de que tu usuario esté en el grupo `docker`.

**Estilos o Assets no cargan**

- **Causa:** La compilación de assets (Vite/Mix) puede haber fallado o la caché está obsoleta.
- **Solución:** Intenta forzar una reconstrucción de los contenedores para asegurar que todos los assets se compilen correctamente (`docker compose build --no-cache`).

---

# [Deutsch] Anleitung auf Deutsch

## Voraussetzungen

- Docker Desktop
- Git
- Internetverbindung

## Architektur

- PHP 8.2 + Apache
- MySQL 8.0
- PhpMyAdmin
- Persistente Docker-Volumes

## Installation

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

## Nutzung

1. Git-Repository-URL eingeben
2. Branch auswählen
3. Datenbank konfigurieren
4. **BUILD PROJECT** starten

## Automatisierte Schritte

- Repository klonen
- Container starten
- Composer installieren
- APP_KEY erzeugen
- Migrationen ausführen

## Zugriff

- Anwendung: [http://localhost](http://localhost)
- PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

## Fehlerbehebung & FAQ

**Port-Konflikte**

- **Ursache:** Port 80 oder 8080 wird bereits von einer anderen Anwendung verwendet.
- **Lösung:** Stellen Sie sicher, dass keine anderen Dienste (wie XAMPP, Laragon oder andere Docker-Container) auf diesen Ports laufen.

**Docker Zugriff verweigert**

- **Ursache:** Der Benutzer im Container wird oft als `www-data` abgebildet.
- **Lösung:** Die Struktur gewährleistet korrekte Berechtigungen. Bei Problemen unter Linux/macOS prüfen Sie, ob Ihr Benutzer in der `docker`-Gruppe ist.

**Styles oder Assets laden nicht**

- **Ursache:** Asset-Kompilierung (Vite/Mix) fehlgeschlagen oder Cache veraltet.
- **Lösung:** Versuchen Sie, die Container neu zu bauen (`docker compose build --no-cache`), um eine korrekte Kompilierung sicherzustellen.

---

# [Korean] 한국어 가이드

## 필수 조건

- Docker Desktop 실행 중
- Git 설치
- 인터넷 연결

## 아키텍처

- PHP 8.2 + Apache
- MySQL 8.0
- PhpMyAdmin
- Docker 네트워크 및 볼륨

## 설치

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

## 사용 방법

1. Git 저장소 URL 입력
2. 브랜치 선택
3. 데이터베이스 설정
4. **BUILD PROJECT** 클릭

## 자동 처리 작업

- 코드 클론
- 컨테이너 실행
- Composer 설치
- APP_KEY 생성
- 마이그레이션 실행

## 접속

- Laravel 앱: [http://localhost](http://localhost)
- PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

## 문제 해결 및 FAQ

**포트 충돌**

- **원인:** 포트 80 또는 8080이 다른 애플리케이션에서 사용 중입니다.
- **해결:** 시작하기 전에 다른 서비스(XAMPP, Laragon 등)가 해당 포트에서 실행되고 있지 않은지 확인하십시오.

**Docker 권한 거부**

- **원인:** 컨테이너 내부 사용자가 보통 `www-data`로 매핑됩니다.
- **해결:** 이 구조는 올바른 권한을 보장합니다. Linux/macOS에서 문제가 발생하면 사용자가 `docker` 그룹에 속해 있는지 확인하십시오.

**스타일 또는 자산 로드 실패**

- **원인:** 자산 컴파일(Vite/Mix) 실패 또는 캐시가 오래되었습니다.
- **해결:** 모든 자산이 올바르게 컴파일되도록 컨테이너를 다시 빌드해 보십시오 (`docker compose build --no-cache`).

---

# [Italian] Guida in Italiano

## Requisiti

- Docker Desktop
- Git
- Connessione Internet

## Architettura

- PHP 8.2 + Apache
- MySQL 8.0
- PhpMyAdmin
- Volumi persistenti

## Installazione

### Windows

```bat
start_windows.bat
```

### Linux / macOS

```bash
. ./start_linux.sh
```

## Utilizzo

1. Inserire URL Git
2. Selezionare branch
3. Configurare database
4. Avviare **BUILD PROJECT**

## Accesso

- Applicazione: [http://localhost](http://localhost)
- PhpMyAdmin: [http://localhost:8080](http://localhost:8080)

## Risoluzione Problemi e FAQ

**Conflitti di Porta**

- **Causa:** La porta 80 o 8080 è già in uso da un'altra applicazione.
- **Soluzione:** Assicurarsi che nessun altro servizio (come XAMPP, Laragon o altri container Docker) sia in esecuzione su queste porte.

**Permesso Docker negato**

- **Causa:** L'immagine utente nel container è solitamente mappata su `www-data`.
- **Soluzione:** La struttura garantisce i permessi corretti. Se riscontri problemi su Linux/macOS, verifica che il tuo utente sia nel gruppo `docker`.

**Stili o Asset non caricati**

- **Causa:** Compilazione asset (Vite/Mix) fallita o cache obsoleta.
- **Soluzione:** Prova a forzare una ricostruzione dei container per garantire la corretta compilazione (`docker compose build --no-cache`).

---

## Developer Contact / Contacto del Desarrollador

**Mario Conf**

- SysAdmin & Full Stack Developer
- 📍 Granada, Andalucía, España
- © 2025 Autovelql. All rights reserved.

---

## License / Licencia

**Autovelql © 2025 – Proprietary Freeware**
Free to use. Modification, redistribution, reverse engineering or resale is prohibited.
Uso gratuito permitido. Prohibida la modificación, redistribución, ingeniería inversa o venta.
