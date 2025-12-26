# Autovelql v2.0 - Official Release

## [INFO] What is New?

This is the restart of the project with a new identity: **Autovelql**.

### [FEATURES] Key Features

- **Automated Environment:** Sets up Docker, MySQL, PHP 8.2, and PhpMyAdmin in one click.
- **MySQL Support:** Forced MySQL connection (replacing SQLite defaults).
- **PermisoFix:** Auto-correction of `chmod 777` permissions for Windows/Docker volumes.
- **Multi-Language Support:** English, Spanish, German, Korean, Italian, Valencian.
- **Robust Cleaning:** Improved "Clean Install" logic to handle locked files on Windows.

### [FIXES] Bug Fixes

- Fixed `permission denied` errors in `storage/` folder.
- Fixed `sqlite` connection errors by injecting `DB_CONNECTION=mysql` in `.env`.
- Fixed window resizing issues (Resizable=True).

### [INSTALL] Installation

1.  **Windows:** Download and run `INICIAR_WINDOWS.bat`.
2.  **Linux/Mac:** Run `./iniciar_linux_mac.sh`.

---

_Verified working on Windows 10/11 and Docker Desktop v4.x_
