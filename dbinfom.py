import pyautogui
import time

pyautogui.FAILSAFE = False

print("Mantendo o sistema ativo via tecla Shift. Pressione Ctrl+C para parar.")

try:
    while True:
        pyautogui.press('shift')
        time.sleep(30)  # a cada 30 segundos
except KeyboardInterrupt:
    print("Encerrado pelo usuário.")