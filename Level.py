class Level:
    def __init__(self, enemy_setup):
        self.enemy_setup = enemy_setup

    def get_enemy_setup(self):
        return self.enemy_setup

    def is_completed(self):
        for enemy_line in self.enemy_setup:
            for enemy in enemy_line:
                if enemy.alive is True:
                    return False
        return True
