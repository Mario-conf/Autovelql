import customtkinter as ctk
import os
import subprocess
import shutil
import time
import webbrowser
import threading
from tkinter import messagebox
from urllib.parse import urlparse

# 1. Global Configuration
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 2. Main container folder
BASE_DIR = "proyecto"

class BuilderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Autovelql - Laravel & MySQL Environment Builder")
        self.geometry("800x780")
        self.resizable(True, True)
        
        # 3. Data variables
        self.repo_url = ctk.StringVar()
        self.branch = ctk.StringVar(value="main")
        
        # 4. Database variables (defaults)
        self.db_name = ctk.StringVar(value="laravel_db")
        self.db_user = ctk.StringVar(value="laravel_user")
        self.db_pass = ctk.StringVar(value="secret")

        self.is_running = False

        self.setup_ui()
        self.check_existing_project()

    def setup_ui(self):
        # 5. Title label
        self.label_title = ctk.CTkLabel(self, text="Autovelql", font=("Roboto", 28, "bold"))
        self.label_title.pack(pady=20)

        # 6. Git section
        frame_git = ctk.CTkFrame(self)
        frame_git.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(frame_git, text="Git Repository Configuration", font=("Roboto", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        
        ctk.CTkLabel(frame_git, text="Repository URL (.git):").pack(anchor="w", padx=10)
        self.entry_url = ctk.CTkEntry(frame_git, placeholder_text="https://github.com/user/project.git", textvariable=self.repo_url)
        self.entry_url.pack(fill="x", padx=10, pady=(0, 5))
        
        ctk.CTkLabel(frame_git, text="Branch:").pack(anchor="w", padx=10)
        self.entry_branch = ctk.CTkEntry(frame_git, textvariable=self.branch)
        self.entry_branch.pack(fill="x", padx=10, pady=(0, 10))

        # 7. Database section
        frame_db = ctk.CTkFrame(self)
        frame_db.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(frame_db, text="MySQL Configuration", font=("Roboto", 14, "bold")).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(frame_db, text="* These settings will create the DB and user with full permissions.", font=("Arial", 10), text_color="gray").pack(anchor="w", padx=10)

        grid_frame = ctk.CTkFrame(frame_db, fg_color="transparent")
        grid_frame.pack(fill="x", padx=5, pady=5)

        ctk.CTkLabel(grid_frame, text="DB Name:").grid(row=0, column=0, padx=5, sticky="w")
        ctk.CTkEntry(grid_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, sticky="ew")
        
        ctk.CTkLabel(grid_frame, text="DB User:").grid(row=0, column=2, padx=5, sticky="w")
        ctk.CTkEntry(grid_frame, textvariable=self.db_user).grid(row=0, column=3, padx=5, sticky="ew")

        ctk.CTkLabel(grid_frame, text="Password:").grid(row=1, column=0, padx=5, sticky="w", pady=10)
        ctk.CTkEntry(grid_frame, textvariable=self.db_pass).grid(row=1, column=1, padx=5, sticky="ew", pady=10)

        grid_frame.columnconfigure(1, weight=1)
        grid_frame.columnconfigure(3, weight=1)

        # 8. Action button
        self.btn_action = ctk.CTkButton(self, text="BUILD PROJECT", height=50, command=self.start_process, font=("Roboto", 16, "bold"), fg_color="#1f538d")
        self.btn_action.pack(pady=10, padx=20, fill="x")

        # 9. Log console
        ctk.CTkLabel(self, text="Activity Log:").pack(anchor="w", padx=20)
        self.textbox_log = ctk.CTkTextbox(self)
        self.textbox_log.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        self.textbox_log.configure(state="disabled")

    def log(self, message):
        self.textbox_log.configure(state="normal")
        self.textbox_log.insert("end", f"> {message}\n")
        self.textbox_log.see("end")
        self.textbox_log.configure(state="disabled")
        print(message)

    def get_app_folder_name(self):
        # 10. Extract repo name from URL
        url = self.repo_url.get().strip()
        if not url: return None
        parsed = urlparse(url)
        path = parsed.path
        if path.endswith('.git'):
            path = path[:-4]
        return path.split('/')[-1] or "laravel_app"

    def check_existing_project(self):
        # 11. Check if project folder exists
        if os.path.exists(BASE_DIR):
            self.btn_action.configure(text="EXISTING PROJECT DETECTED (Manage)", fg_color="#E59400", hover_color="#B87700")

    def start_process(self):
        if self.is_running: return
        
        url = self.repo_url.get().strip()
        app_name = self.get_app_folder_name()
        
        if not url:
            self.log("[ERROR] You must enter a GitHub URL.")
            return

        mode = "new"
        
        if os.path.exists(BASE_DIR) and os.listdir(BASE_DIR):
            dialog = ProjectExistsDialog(self)
            self.wait_window(dialog)
            if dialog.result is None: return
            mode = dialog.result

        self.is_running = True
        self.btn_action.configure(state="disabled", text="WORKING...")
        
        # 12. Start process in background thread
        threading.Thread(target=self.run_logic, args=(url, app_name, mode), daemon=True).start()

    def run_logic(self, url, app_name, mode):
        try:
            # Step 1: Prepare folder
            self.log("[1/10] Preparing project folder...")
            os.makedirs(BASE_DIR, exist_ok=True)
            app_path = os.path.join(BASE_DIR, app_name)
            
            # Step 2: Clean environment if needed
            if mode == 'clean':
                self.log("[2/10] [CLEAN] Wiping environment...")
                self.run_command("docker compose down -v --remove-orphans", cwd=BASE_DIR, ignore_error=True)
                self.log("[2/10] Waiting for Docker to release files...")
                time.sleep(3)
                
                if os.path.exists(BASE_DIR):
                    self.log(f"[2/10] Deleting folder {BASE_DIR}...")
                    try:
                        shutil.rmtree(BASE_DIR)
                    except Exception as e:
                        self.log(f"[2/10] shutil failed ({e}), using system command...")
                        if os.name == 'nt':
                            self.run_command(f'rmdir /s /q "{BASE_DIR}"', shell=True, ignore_error=True)
                        else:
                            self.run_command(f"rm -rf {BASE_DIR}", shell=True, ignore_error=True)
                
                os.makedirs(BASE_DIR, exist_ok=True)
            
            elif mode == 'update':
                self.log("[2/10] [UPDATE] Updating code only...")
                self.run_command("docker compose down", cwd=BASE_DIR, ignore_error=True)
                if os.path.exists(app_path):
                    shutil.rmtree(app_path, ignore_errors=True)
            else:
                self.log("[2/10] New installation mode.")

            # Step 3: Clone repository
            self.log(f"[3/10] Cloning repository into: {app_name}...")
            self.run_command(f"git clone -b {self.branch.get()} {url} {app_name}", cwd=BASE_DIR)

            # Step 4: Generate Docker Compose
            self.log("[4/10] Generating docker-compose.yml...")
            self.create_docker_compose(app_name)

            # Step 5: Start Docker containers
            self.log("[5/10] Starting containers (Apache + MySQL + PMA)...")
            self.run_command("docker compose up -d --build", cwd=BASE_DIR)

            # Step 6: Wait for database
            self.log("[6/10] Waiting for MySQL...")
            self.wait_for_db()

            # Step 7: Fix permissions
            self.log("[7/10] [FIX] Setting permissions on storage/ (chmod 777)...")
            folders_to_fix = ["storage", "bootstrap/cache"]
            for folder in folders_to_fix:
                full_path = os.path.join(app_path, folder)
                if not os.path.exists(full_path):
                     os.makedirs(full_path, exist_ok=True)
                self.run_command(f"docker compose exec -T -w /app app chmod -R 777 {folder}", cwd=BASE_DIR)

            # Step 8: Configure .env file
            self.log("[8/10] Configuring .env file...")
            self.setup_env_file(app_path)

            # Step 9: Install dependencies
            self.log("[9/10] Installing dependencies (Composer)...")
            self.run_command("docker compose exec -T -w /app app composer install", cwd=BASE_DIR)
            
            self.log("[9/10] Generating application key...")
            self.run_command("docker compose exec -T -w /app app php artisan key:generate", cwd=BASE_DIR)

            # Step 10: Run migrations
            self.log("[10/10] Running migrations (Creating tables)...")
            if mode == 'clean' or mode == 'new':
                self.run_command("docker compose exec -T -w /app app php artisan migrate --seed", cwd=BASE_DIR)
            else:
                self.run_command("docker compose exec -T -w /app app php artisan migrate --force", cwd=BASE_DIR)

            self.log("[SUCCESS] Process completed successfully.")
            
            time.sleep(2)
            webbrowser.open("http://localhost:8080")
            webbrowser.open("http://localhost")
            
            self.quit()

        except Exception as e:
            self.log(f"[ERROR] {str(e)}")
            import traceback
            traceback.print_exc()
        finally:
            self.is_running = False
            self.btn_action.configure(state="normal", text="RETRY")

    def create_docker_compose(self, app_folder_name):
        # 13. Docker Compose template
        content = f"""
services:
    app:
        image: webdevops/php-apache:8.2
        container_name: laravel_project_app
        volumes:
            - ./{app_folder_name}:/app
        ports:
            - "80:80"
        environment:
            WEB_DOCUMENT_ROOT: /app/public
            PHP_DATE_TIMEZONE: Europe/Madrid
            PHP_DISPLAY_ERRORS: 1
        depends_on:
            - mysql

    mysql:
        image: mysql:8.0
        container_name: laravel_project_db
        environment:
            MYSQL_ROOT_PASSWORD: root
            MYSQL_DATABASE: {self.db_name.get()}
            MYSQL_USER: {self.db_user.get()}
            MYSQL_PASSWORD: {self.db_pass.get()}
        ports:
            - "3306:3306"
        volumes:
            - ./docker_volumes/mysql:/var/lib/mysql

    phpmyadmin:
        image: phpmyadmin/phpmyadmin
        container_name: laravel_project_pma
        links:
            - mysql:db
        ports:
            - "8080:80"
        environment:
            PMA_HOST: mysql
            MYSQL_ROOT_PASSWORD: root
"""
        with open(os.path.join(BASE_DIR, "docker-compose.yml"), "w") as f:
            f.write(content.strip())

    def setup_env_file(self, app_path):
        # 14. Setup .env file
        env_example = os.path.join(app_path, ".env.example")
        env_dest = os.path.join(app_path, ".env")

        if os.path.exists(env_example):
            shutil.copy(env_example, env_dest)
        else:
            with open(env_dest, "w") as f: f.write("APP_NAME=Laravel\n")

        with open(env_dest, "r") as f: lines = f.readlines()
        
        overrides = {
            "DB_CONNECTION=": "DB_CONNECTION=mysql\n",
            "DB_HOST=": "DB_HOST=mysql\n",
            "DB_PORT=": "DB_PORT=3306\n",
            "DB_DATABASE=": f"DB_DATABASE={self.db_name.get()}\n",
            "DB_USERNAME=": f"DB_USERNAME={self.db_user.get()}\n",
            "DB_PASSWORD=": f"DB_PASSWORD={self.db_pass.get()}\n",
            "APP_URL=": "APP_URL=http://localhost\n"
        }

        new_lines = []
        found_keys = []
        
        for line in lines:
            replaced = False
            for key, val in overrides.items():
                if line.startswith(key):
                    new_lines.append(val)
                    found_keys.append(key)
                    replaced = True
                    break
            if not replaced:
                new_lines.append(line)

        for key, val in overrides.items():
            if key not in found_keys:
                new_lines.append(val)

        with open(env_dest, "w") as f: f.writelines(new_lines)

    def run_command(self, command, cwd=None, shell=True, ignore_error=False):
        # 15. Execute shell command
        self.log(f"Exec: {command}")
        try:
            executable = '/bin/bash' if os.name != 'nt' else None
            subprocess.check_call(command, shell=True, cwd=cwd, executable=executable)
        except subprocess.CalledProcessError as e:
            if not ignore_error:
                raise Exception(f"Command failed: {command}")

    def wait_for_db(self):
        # 16. Wait for MySQL to be ready
        time.sleep(5)
        for i in range(30):
            try:
                self.run_command(f"docker compose exec -T mysql mysqladmin ping -h localhost -u root -proot --silent", cwd=BASE_DIR)
                self.log("[OK] MySQL is ready.")
                return
            except:
                time.sleep(2)
        self.log("[WARNING] MySQL timeout, continuing anyway...")

# 17. Dialog for existing project conflict
class ProjectExistsDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Conflict")
        self.geometry("480x320")
        self.result = None
        self.attributes('-topmost', True)
        
        ctk.CTkLabel(self, text="Project Detected!", font=("Roboto", 18, "bold"), text_color="#E59400").pack(pady=20)
        
        btn_update = ctk.CTkButton(self, text="UPDATE (Keep Database)", fg_color="green", height=60, command=self.on_update)
        btn_update.pack(pady=10, padx=20, fill="x")

        btn_clean = ctk.CTkButton(self, text="CLEAN INSTALL (Wipe Everything)", fg_color="red", height=60, command=self.on_clean)
        btn_clean.pack(pady=5, padx=20, fill="x")

    def on_update(self):
        self.result = 'update'
        self.destroy()

    def on_clean(self):
        self.result = 'clean'
        self.destroy()

# 18. Entry point
if __name__ == "__main__":
    app = BuilderApp()
    app.mainloop()