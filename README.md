# Lazuri
control program for Lazuri

## Setting Up Ethernet for VNC Viewer
### Getting Devices Ready
1. Turn on **both** the laptop and Raspberry Pi. **MAKE SURE THAT THEY BOTH WORK.**
2. Connect the laptop and the raspberry pi with ethernet cable

### Configuring IP on the Raspberry Pi
1. Click on the Internet icon.
2. Hover over **Advanced Options** and click **Edit Connections**.
3. Check if there is a wired connection. If not, check if the ethernet cable is working or not.
4. Select the wired connection and then click on the gear icon near the bottom left of the window.
5. Go to **IPv4 Settings**.
6. In "Methods", change **Automatic (DCHP)** to **Manual**.
7. Note down the IP Address and netmask. This will be useful for later.
8. Save the configuration by clicking **Save**.

### Configuring IP on the Laptop (Windows 10)
1. Press Win+R to open the **Run** command.
2. Type in **ncpa.cpl**
3. Click on the ethernet connection, which should be called "Ethernet".
4. Click **Properties**.
5. Double Click on **“Internet Protocol Version 4 (TCP/IPv4)”**.
6. Set a static IP (192.168.137.123) and subnet mask (255.255.255.0) for the connection.
7. Press "OK" to save and close the window.

### Checking if it works
Type in `ping <ip>` in the terminal (Raspberry Pi) / cmd (Laptop) to check if the ethernedt is connected between the devices.
  
