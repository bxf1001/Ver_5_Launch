from pywinauto import Application

#startapp = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
try:
    app = Application(backend='uia').connect(title_re="WhatsApp", timeout=5)
except TimeoutError:
    print(f" Try restarting whatsapp")