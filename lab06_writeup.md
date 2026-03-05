4.1:

git clone git@github.com:my-name/my-imaginary-repo.git
cd my-imaginary-repo
touch my_second_file.py
nano my_second_file.py

*inside file, add: print("Hello World")

then:

git add my_second_file.py
git commit -m "Added my_second_file.py"
git push origin main

4.2:

I developed code with my partner on my native OS using an IDE. I tracked nearly every change I made since there wasn't too much code. I then pushed to git, cloned the repo on my VM, and using 'scp' copied it to my RPi to update the code. This wasn't too efficient, but I was running into many bugs with git on the RPi. In the future, I will try to troubleshoot the error with git on my RPi so I elimate the need to use the VM.

I tried to use vim on the RPi, but it initially wasn't working. I feel comfortable with vim on my VM, but felt a lot more comfortable working on my native IDE. In the future, I'll practive even more with vim.

4.3: 
Even after removing sleep(), there's still a delay in the readings because the delay is built into ultrasonicRead() itself. It requires time to send a pulse and wait for an echo to return before calculating distance.

When the RPi reads the value, it doesn't communicate with the sensor. Instead, it communicated with the microcontroller on the GrovePi board using I2C. The microcontroller sends the distance measurement back to the RPi.

4.4: The rotary angle sensor outputs an analog voltage between 0 V and 5 V depending on the position of the knob. Using ADC, its converted into a value in between 0 and 1023 (1024 discrete levels). The value is proportional to the input voltage.

The RPi cannot perform this conversion because it doesn't have analog pins built in or an ADC. So the microcontroller on the GrovePi performs the conversion and sends the value to the RPi.

4.5:

If the LCD does not display text even though code runs, I would first verify that the GrovePi board and firmware are functioning correctly (python grove_firmware_version_check.py). I would also check if the I2C interface is enabled and that the device is detected (sudo raspi-config; sudo i2cdetect -y 1).

If the LCD does not appear, I would check cable connections, ensure the ports are corect, and try running an example grove LCD program.

