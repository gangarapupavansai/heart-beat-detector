import serial
import time
from collections import deque

# Configure serial port
ser = serial.Serial('COM3', 9600)  # Change COM port as needed

threshold = 550  # Adjust based on your sensor readings
last_beat_time = 0
bpm_values = deque(maxlen=10)

while True:
    try:
        line = ser.readline().decode().strip()

        if not line.isdigit():
            continue

        signal = int(line)

        current_time = time.time()

        # Simple peak detection
        if signal > threshold and (current_time - last_beat_time) > 0.3:
            interval = current_time - last_beat_time

            if last_beat_time > 0:
                bpm = 60 / interval
                bpm_values.append(bpm)

                avg_bpm = sum(bpm_values) / len(bpm_values)

                print(f"Heartbeat detected! BPM: {avg_bpm:.1f}")

            last_beat_time = current_time

    except KeyboardInterrupt:
        print("Stopped.")
        break
Arduino example (sending pulse values)
const int pulsePin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int signal = analogRead(pulsePin);
  Serial.println(signal);
  delay(10);
}
