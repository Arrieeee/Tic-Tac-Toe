from GameFiles import GameLogic
import os
import neat


'''def eval_genomes(genomes, config):
    width, height = 700, 500

def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('')

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)'''

if __name__ == '__main__':
    '''local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    run_neat(config)'''

    game = GameLogic()
    game.run()