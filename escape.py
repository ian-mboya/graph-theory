class Spaceship:
    def __init__(self):
        self.sections = {
            'bridge': ['engines', 'oxygen'],
            'engines': ['bridge', 'oxygen', 'navigation'],
            'navigation': ['engines', 'escape_module'],
            'communication': ['oxygen', 'navigation'],
            'oxygen': ['bridge', 'engines', 'communication'],
            'escape_module': []
        }
        self.visited = []

    def find_path(self, current_section, target_section, path=[]):
        path = path + [current_section]
        if current_section == target_section:
            return path
        if current_section not in self.sections:
            return None
        for section in self.sections[current_section]:
            if section not in path:
                new_path = self.find_path(section, target_section, path)
                if new_path:
                    return new_path
        return None

    def escape(self):
        start_section = 'bridge'
        target_section = 'escape_module'
        path = self.find_path(start_section, target_section)
        if path:
            for i in range(len(path) - 1):
                print(f'{path[i]} -> {path[i + 1]}')
        else:
            print('No path found.')

if __name__ == "__main__":
    spaceship = Spaceship()
    spaceship.escape()
