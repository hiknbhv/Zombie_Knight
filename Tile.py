import pygame

class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=""):
        super().__init__()
        #Load in the correct image and add it to the correct sub group
        #Dirt tiles
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (1).png"), (32, 32))
        #Platform tiles
        elif image_int == 2:
            self.image = self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (2).png"), (32, 32))
            sub_group.add(self)
            # TODO: just like image_int == 1.  store the transformed image in self.image.  This will use Tile (2).png
            # TODO: 1 thing new.  add self to sub_group.  Just like you added self to main group down below.
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (3).png"), (32, 32))
            sub_group.add(self)
            # TODO: just like image_int == 1.  store the transformed image in self.image.  This will use Tile (3).png
            # TODO: 1 thing new.  add self to sub_group.  Just like you added self to main group down below.
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (4).png"), (32, 32))
            sub_group.add(self)
            # TODO: just like image_int == 1.  store the transformed image in self.image.  This will use Tile (4).png
            # TODO: 1 thing new.  add self to sub_group.  Just like you added self to main group down below.
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (5).png"), (32, 32))
            sub_group.add(self)
            # TODO: just like image_int == 1.  store the transformed image in self.image.  This will use Tile (5).png
            # TODO: 1 thing new.  add self to sub_group.  Just like you added self to main group down below.

        #Add every tile to the main group
        main_group.add(self)

        #Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #Create a mask for better player collisions
        self.mask = pygame.mask.from_surface(self.image)
