import pygame
import random

pygame.init()

# Fenêtre
LARGEUR = 500
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu d'Esquive")

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
NOIR = (0, 0, 0)

# Police
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def afficher_texte(texte, taille, couleur, x, y):
    font_local = pygame.font.SysFont(None, taille)
    rendu = font_local.render(texte, True, couleur)
    fenetre.blit(rendu, (x, y))

def boucle_jeu():
    joueur_largeur = 50
    joueur_hauteur = 50
    joueur_x = LARGEUR // 2 - joueur_largeur // 2
    joueur_y = HAUTEUR - joueur_hauteur - 10
    vitesse_joueur = 5

    obstacle_largeur = 50
    obstacle_hauteur = 50
    obstacle_x = random.randint(0, LARGEUR - obstacle_largeur)
    obstacle_y = -obstacle_hauteur
    vitesse_obstacle = 5

    score = 0
    en_jeu = True

    while en_jeu:
        clock.tick(60)
        fenetre.fill(BLANC)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and joueur_x > 0:
            joueur_x -= vitesse_joueur
        if touches[pygame.K_RIGHT] and joueur_x < LARGEUR - joueur_largeur:
            joueur_x += vitesse_joueur

        obstacle_y += vitesse_obstacle
        if obstacle_y > HAUTEUR:
            obstacle_y = -obstacle_hauteur
            obstacle_x = random.randint(0, LARGEUR - obstacle_largeur)
            score += 1
            vitesse_obstacle += 0.2

        joueur_rect = pygame.Rect(joueur_x, joueur_y, joueur_largeur, joueur_hauteur)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_largeur, obstacle_hauteur)
        if joueur_rect.colliderect(obstacle_rect):
            return score  # Fin du jeu

        pygame.draw.rect(fenetre, BLEU, joueur_rect)
        pygame.draw.rect(fenetre, ROUGE, obstacle_rect)

        texte_score = font.render("Score: " + str(score), True, NOIR)
        fenetre.blit(texte_score, (10, 10))

        pygame.display.flip()

def ecran_game_over(score):
    en_pause = True
    while en_pause:
        fenetre.fill(BLANC)
        afficher_texte("GAME OVER", 60, ROUGE, 130, 200)
        afficher_texte(f"Score: {score}", 40, NOIR, 190, 270)
        afficher_texte("Appuie sur R pour rejouer ou Q pour quitter", 30, NOIR, 50, 330)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return  # Rejouer
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Boucle principale
while True:
    score_final = boucle_jeu()
    ecran_game_over(score_final)
