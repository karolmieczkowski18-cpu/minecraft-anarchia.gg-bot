import pydirectinput
import pyautogui
import time
import random
from pynput import keyboard
import sys

# Safety Settings
pyautogui.FAILSAFE = True

print("=== MINECRAFT ULTIMATE AFK BOT (WINDOWS) ===")
print("1. Place food in slot 9.")
print("2. You have 5 seconds to switch to Minecraft.")
print("3. STOP: Press ENTER key in this window.")
print("-----------------------------------------------")
time.sleep(5)

running = True
hit_count = 0
current_slot = 1

# Time trackers
last_jump_time = time.time()
last_eat_time = time.time()

def on_press(key):
    global running
    if key == keyboard.Key.enter:
        print("\n[STOP] Shutting down bot...")
        running = False
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("BOT STARTED! (Press ENTER to stop)")

try:
    while running:
        now = time.time()

        # --- 1. EATING (Every 60 minutes) ---
        if now - last_eat_time > 3600:
            print("\n[ACTION] Time to eat. Switching to slot 9...")
            pydirectinput.press('9')
            time.sleep(0.5)
            print("[ACTION] Eating (holding Right Click)...")
            pydirectinput.mouseDown(button='right')
            time.sleep(5)  # Holds right click for 5 seconds
            pydirectinput.mouseUp(button='right')
            
            # Switch back to the combat slot
            pydirectinput.press(str(current_slot))
            last_eat_time = now
            print(f"[INFO] Back to combat on slot {current_slot}.")

        # --- 2. ANTI-AFK JUMP (Every 2 minutes) ---
        if now - last_jump_time > 120:
            print("\n[ACTION] Anti-AFK Jump!")
            pydirectinput.press('space')
            last_jump_time = now

        # --- 3. ATTACK (Left Click) ---
        pydirectinput.click()
        hit_count += 1
        
        # Switch combat slots every 6000 hits (Cycles slots 1-8)
        if hit_count >= 6000:
            current_slot = (current_slot % 8) + 1 
            pydirectinput.press(str(current_slot))
            print(f"\n[INFO] Switched weapon to slot: {current_slot}")
            hit_count = 0
            
        # --- 4. RANDOM DELAY ---
        wait_time = random.uniform(5.091, 6.111)
        
        # Status line
        next_eat = int((3600 - (time.time() - last_eat_time))/60)
        sys.stdout.write(f"\rHits: {hit_count} | Next in: {wait_time:.2f}s | Next meal in: {next_eat} min. ")
        sys.stdout.flush()
        
        # Breakable sleep
        timeout = time.time() + wait_time
        while time.time() < timeout and running:
            time.sleep(0.1)

except Exception as e:
    print(f"\n[ERROR]: {e}")

finally:
    listener.stop()
    print("\n[FINISHED] Bot is now OFF.")
    input("Press any key to close this window...")
