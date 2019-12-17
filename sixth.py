class StarMap:
    graph = {}

    def add(self, stuff, orbiting):
        if orbiting not in self.graph:
            self.graph[orbiting] = []
        self.graph[orbiting].append(stuff)

    def get_direct_orbits(self):
        sum = 0
        for orbiting_bodies in self.graph.values():
            for orbiting_body in orbiting_bodies:
                if orbiting_body is not None:
                    sum += 1
        return sum

    def get_indirect_paths(self):
        sum = 0
        for key, orbiting_bodies in self.graph.items():
            sum

    def __str__(self):
        orbits = ""
        for key, orbiting_bodies in self.graph.items():
            for orbiting_body in orbiting_bodies:
                orbits += f'{key}){orbiting_body}\n'
        return orbits


if __name__ == '__main__':
    star_map = StarMap()
    star_map.add(None, "COM")
    star_map.add("B", "COM")
    star_map.add("C", "B")
    star_map.add("D", "C")
    star_map.add("E", "D")
    star_map.add("F", "E")
    star_map.add("G", "B")
    star_map.add("H", "G")
    star_map.add("I", "D")
    star_map.add("J", "E")
    star_map.add("K", "J")
    star_map.add("L", "K")
    print(star_map.get_direct_orbits())


