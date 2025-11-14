import subprocess
import sys

# List of modules to install
modules_to_install = ['pyautogui', 'mediapipe', 'opencv-python']

def install_modules(modules):
    for module in modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

if __name__ == '__main__':
    install_modules(modules_to_install)
