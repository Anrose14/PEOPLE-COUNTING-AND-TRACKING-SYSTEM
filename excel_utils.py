import sys
import pygame
from datetime import datetime

def save_counts_to_text(count_entered, count_exited):
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create the content string
    content = f"Timestamp: {timestamp}\nEntered: {count_entered}\nExited: {count_exited}\n\n"
    
    # Save the content to a text file
    output_path = 'counts.txt'
    with open(output_path, 'a') as file:
        file.write(content)
    
    count=count_entered-count_exited;
    if count_entered == 3:
        # Perform alert actions
        print("Alert: Count reached 3!")
        pygame.mixer.init()
        pygame.mixer.music.load('emergency-alarm-with-reverb-29431.mp3')  # Replace 'alert.mp3' with the path to your MP3 file
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
             continue
        # Stop the program
        sys.exit()
                
    


