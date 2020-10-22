class DB_Shotgun:
    def __init__(self):
        self.capacity = 2
        self.damage = 120
        self.reload_time = 'moderate'
        self.base_accuracy = 45
        self.shell_count = 2
        def fire():
            if self.shell_count == 2:
                fire_both = input('fire both barrels?\n')
                if fire_both == 'y':
                    # combat double shot
                    self.shell_count -= 2
                elif fire_both == 'n':
                    # combat single shot
                    self.shell_count -= 1
                else:
                    # your gun blows up
                    placlass DB_Shotgun:
    def __init__(self):
        self.capacity = 2
        self.damage = 120
        self.reload_time = 'moderate'
        self.base_accuracy = 45
        self.shell_count = 2
        def fire():
            if self.shell_count == 2:
                fire_both = input('fire both barrels?\n')
                if fire_both == 'y':
                    # combat double shot
                    self.shell_count -= 2
                elif fire_both == 'n':
                    # combat single shot
                    self.shell_count -= 1
                else:
                    # your gun blows up
            if self.shell_count == 1:
                    # combat ingle shot
                    self.shell_count -= 1
        def reload():
            if 'shotgun shell' in player.inventory:
                self.shell_count += 1
                print('who wants some?')
            else:
                    self.shell_count -= 1
        def reload():
            if 'shotgun shell' in player.inventory:
                self.shell_count += 1
                print('who wants some?')
            else:
                print('you have no ammo dude')
                
