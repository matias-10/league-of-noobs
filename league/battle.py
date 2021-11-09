from typing import List

import pygame
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d


class View:
    """A pseudo-interface for views that can be used in the game class."""

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        """View-specific event loop for key-bindings"""
        raise NotImplementedError("You need to override the 'event_loop' method in every class inheriting from the View class.")

    def update(self) -> None:
        """Update the view's state"""
        raise NotImplementedError("You need to override the 'update' method in every class inheriting from the View class.")
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the view's contents."""
        raise NotImplementedError("You need to override the 'draw' method in every class inheriting from the View class.")



class Battle(View):
    def __init__(self):
        self.circle_x = 50
        self.circle_y = 50

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == KEYDOWN:
                print(event)

    def update(self) -> None:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_d]:
            self.circle_x += 5
        
        if keys_pressed[K_a]:
            self.circle_x -= 5

        if keys_pressed[K_s]:
            self.circle_y += 5
        
        if keys_pressed[K_w]:
            self.circle_y -= 5
        
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 128), (self.circle_x, self.circle_y), 20)