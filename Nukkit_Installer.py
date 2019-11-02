import subprocess
print ("Version: 1.3")
action = input ("What do you want me to do? Install Nukkit, Start Nukkit, or Upgrade Nukkit? Say 'install' to install, 'start' to start, and 'upgrade' to upgrade. ")
def installdep():
    subprocess.call ("sudo apt install python -y", shell=True)
    subprocess.call ("sudo apt install default-jdk -y", shell=True)
def serverinstall():
    subprocess.call ("cd", shell=True)
    subprocess.call ("wget -O nukkit.jar https://go.pimylifeup.com/3xsPQA/nukkit", shell=True)
if action == "install":
    subprocess.call ("cd", shell=True)
    installdep()
    serverinstall()
    bootanswer = input ("The install is completed. Do you want me to start up Nukkit for you? (y/n) ")
if action == "start":
    subprocess.call ("cd", shell=True)
    print("Ok. Starting up Nukkit...")
    subprocess.call ("sudo java -jar nukkit.jar", shell=True)
if action == "upgrade":
    subprocess.call ("cd", shell=True)
    subprocess.call ("wget -O nukkit.jar https://go.pimylifeup.com/3xsPQA/nukkit", shell=True)
    print ("Nukkit has been updated to the latest stable version.")
    raw_input ("Press ENTER to end process")
if bootanswer == "y":
    print("Booting up Nukkit...")
    subprocess.call ("sudo java -jar nukkit.jar", shell=True)
if bootanswer == "n":
    print ("Ok you will have to start up Nukkit by yourself by running 'java -jar nukkit.jar'.")
else:
    print ("Make sure you are typing a valid command!")
