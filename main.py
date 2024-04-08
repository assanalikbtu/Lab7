import datetime
import pygame
import sys


class TimepieceApp:
    def __init__(self):
        pygame.init()
        self.display_width = 1000
        self.display_height = 800
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Timepiece")
        self.timepiece_image = pygame.image.load('mainclock.png')
        self.timepiece_rect = self.timepiece_image.get_rect(center=(self.display_width // 2, self.display_height // 2 - 10))
        self.hour_hand_image = pygame.image.load('rightarm.png')
        self.minute_hand_image = pygame.image.load('leftarm.png')
        self.hour_angle, self.minute_angle = self.obtain_current_time()
        self.minute_angle = self.minute_angle * 6
        self.hour_angle = self.hour_angle * 30

    def update_time(self):
        hour, minute = self.obtain_current_time()
        self.hour_angle = hour * 30
        self.minute_angle = minute * 6

    def obtain_current_time(self):
        time = datetime.datetime.now().time().strftime("%H:%M:%S")
        hours, minutes, seconds = [int(i) for i in time.split(':')]
        hours %= 12
        hours += 1.8
        hour_proportion = hours + minutes / 60 + seconds / 3600
        minutes_proportion = minutes + seconds / 60
        return hour_proportion, minutes_proportion

    def display_timepiece(self):
        self.display.fill((255, 255, 255))
        self.display.blit(self.timepiece_image, self.timepiece_rect)

    def display_hands(self):
        rotated_hour_hand = pygame.transform.rotate(self.hour_hand_image, -self.hour_angle)
        rotated_minute_hand = pygame.transform.rotate(self.minute_hand_image, -self.minute_angle)
        rotated_hour_hand_rect = rotated_hour_hand.get_rect(center=self.timepiece_rect.center)
        rotated_minute_hand_rect = rotated_minute_hand.get_rect(center=self.timepiece_rect.center)
        self.display.blit(rotated_hour_hand, rotated_hour_hand_rect)
        self.display.blit(rotated_minute_hand, rotated_minute_hand_rect)

    def initiate(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_time()
            self.display_timepiece()
            self.display_hands()
            pygame.display.flip()
            pygame.time.Clock().tick(10)


app = TimepieceApp()
app.initiate()