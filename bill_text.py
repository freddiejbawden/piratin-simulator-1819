class Bill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load(path.join(img_dir,'piratebill.gif'))
        self.imageMaster = self.imageMaster.convert()
        self.original_image = self.imageMaster
        self.image = pygame.transform.scale(self.imageMaster, (600, 280))
        self.position = (1.5*WIDTH/4,3*HEIGHT/4)
        self.rect = self.image.get_rect(center=self.position)

def draw_text_on_bill(text,screen,WIDTH,HEIGHT,font=pygame.font.SysFont('Comic Sans MS',25),charchop=37):
    words = text.split(" ")
    cur_line = ""
    height_offset=0
    for word in words:
        if len(cur_line) + len(word) + 1 < 37:
            cur_line = cur_line + word + ' '
        else:
            screen.blit(font.render(cur_line,False,(0,0,0)),(WIDTH-50,HEIGHT-120+height_offset))
            height_offset += 25
            cur_line = word + ' '
    screen.blit(font.render(cur_line,False,(0,0,0)),(WIDTH-50,HEIGHT-120+height_offset))
