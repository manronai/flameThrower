import pyaudio
import pygame
pygame.init()
p = pyaudio.PyAudio()
sps = 44100
chunk = 1024
INPUT = True
OUTPUT = True
channel = 1
run = 1
frs = []
size = pyaudio.paInt16
stream = p.open(format=size, channels=channel, rate=sps, input=INPUT, output=OUTPUT, frames_per_buffer=chunk)
for i in range(0, int((sps*10)/chunk)):
    print(i)
    u = stream.read(chunk)
    frs.append(u)

win = pygame.display.set_mode((393, 399))
while run:
    pygame.time.delay(3999)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
    pygame.display.update()
pygame.quit()
for ii in frs:
    stream.write(ii)
stream.stop_stream()
stream.close()
p.terminate()
