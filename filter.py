import os, sys, pygame, shutil
from glob import glob

class ImageFilter():
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Image Filterer')
        pygame.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.font = pygame.font.Font(None, 40)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.image_names = []
        self.image = None
        self.image_index = 0
        self.textSurface = None
        # ---
        self.load_image_names()
        self.load_image()
        self.update_text()

    def filter_image(self):
        head, tail = os.path.split(self.get_current_image_name())
        destination = "./filtered/" + tail
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy(self.get_current_image_name(), destination)
        print("Copied image:", self.get_current_image_name())

    def get_current_image_name(self):
        return self.image_names[self.image_index]

    def load_image_names(self):
        self.image_names = glob("./**/*.jpg", recursive=True)

    def load_image(self):
        tmp_image = pygame.image.load(self.get_current_image_name())
        self.current_image = pygame.transform.scale(tmp_image, (self.WIDTH, self.HEIGHT))
    
    def update_text(self):
        color = (0,255,0)
        index_text = '(' + str(self.image_index+1) + '/' + str(len(self.image_names)) + ')'
        filename_text = self.get_current_image_name()
        full_text = index_text + ' ' + filename_text
        print(full_text)
        self.textSurface = self.font.render(full_text, False, color)

    def change_index(self, mod):
        if self.image_index+mod < 0:
            return
        elif self.image_index+mod >= len(self.image_names):
            return
        self.image_index += mod
        self.load_image()
        self.update_text()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.filter_image()
                if event.key == pygame.K_LEFT:
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_ALT:
                        self.change_index(-1000)
                    elif mods & pygame.KMOD_CTRL:
                        self.change_index(-100)
                    elif mods & pygame.KMOD_SHIFT:
                        self.change_index(-10)
                    else:
                        self.change_index(-1)
                if event.key == pygame.K_RIGHT:
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_ALT:
                        self.change_index(1000)
                    elif mods & pygame.KMOD_CTRL:
                        self.change_index(100)
                    elif mods & pygame.KMOD_SHIFT:
                        self.change_index(10)
                    else:
                        self.change_index(1)
                                

    def display(self):
        self.screen.blit(self.current_image, (0,0))
        self.screen.blit(self.textSurface, (0,0))
        pygame.display.flip()

    def update(self):
        self.get_input()
        self.display()

    def run(self):
        while True:
            self.update()

def main():
    image_filter = ImageFilter(1200, 700)
    image_filter.run()

if __name__ == "__main__":
    main()