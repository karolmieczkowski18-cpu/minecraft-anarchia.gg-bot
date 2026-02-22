import pyautogui
import time
import random
from pynput import keyboard
import sys


pyautogui.FAILSAFE = True


pyautogui.PAUSE = 0.05

print("=== MINECRAFT AUTOCLICKER (WINDOWS VERSION) ===")
print("Instrukcja:")
print("1. Ustaw celownik w grze.")
print("2. Masz 5 sekund na aktywowanie okna Minecrafta.")
print("3. Aby WYŁĄCZYĆ: naciśnij klawisz ENTER w tym oknie.")
print("-----------------------------------------------")
time.sleep(5)

running = True
hit_count = 0
current_slot = 1

def on_press(key):
    global running
 
    if key == keyboard.Key.enter:
        print("\n[STOP] Wykryto ENTER. Zatrzymywanie...")
        running = False
        return False


listener = keyboard.Listener(on_press=on_press)
listener.start()

print("BOCENIE ROZPOCZĘTE! (Naciśnij ENTER, żeby przestać)")

try:
    while running:
     
        pyautogui.click()
        hit_count += 1
        
    
        if hit_count >= 6000:
            current_slot = (current_slot % 9) + 1
            pyautogui.press(str(current_slot))
            print(f"\n[INFO] Zmieniono slot na: {current_slot}")
            hit_count = 0
            
      
        wait_time = random.uniform(5.091, 6.111)
        

        sys.stdout.write(f"\rAtak nr: {hit_count} | Następny za: {wait_time:.2f}s  ")
        sys.stdout.flush()
     
       
        timeout = time.time() + wait_time
        while time.time() < timeout and running:
            time.sleep(0.1)

except Exception as e:
    print(f"\n[BŁĄD]: {e}")

finally:
    listener.stop()
    print("\n[KONIEC] Skrypt został pomyślnie wyłączony.")
    input("Naciśnij dowolny klawisz, aby zamknąć to okno...")
