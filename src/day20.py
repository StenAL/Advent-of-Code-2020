from util import *
from collections import *
import copy

day = 20


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data.append("")
    tiles = dict()
    acc = []
    tile_id = -1
    for line in data:
        if line == "":
            tiles[tile_id] = acc
            acc = []
            continue
        if line.startswith("Tile"):
            tile_id = line.split(" ")[1][:-1]
            continue
        acc.append(line)
    # print(tiles)

    all_edges = dict()
    for tile_id, tile in tiles.items():
        tile_length = len(tile)
        edges = []
        e1 = tile[0]
        edges.append(e1)
        e2 = "".join([tile[i][tile_length - 1] for i in range(tile_length)])
        edges.append(e2)
        e3 = tile[tile_length - 1]
        edges.append(e3)
        e4 = "".join([tile[i][0] for i in range(tile_length)])
        edges.append(e4)
        all_edges[tile_id] = edges

    ans = 1
    for k1, v1 in all_edges.items():
        edges1 = v1
        matches = 0
        for k2, v2 in all_edges.items():
            edges2 = v2
            if v1 == v2:
                continue

            for edge1 in edges1:
                if edge1 in edges2 or edge1[::-1] in edges2:
                    matches += 1
        if matches == 2:  # corner
            print("c", k1)
            ans *= int(k1)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data.append("")
    tiles = dict()
    acc = []
    tile_id = -1
    for line in data:
        if line == "":
            tiles[tile_id] = Tile(tile_id, acc)
            acc = []
            continue
        if line.startswith("Tile"):
            tile_id = line.split(" ")[1][:-1]
            continue
        acc.append(line)

    all_edges = dict()
    for tile_id, tile in tiles.items():
        all_edges[tile_id] = tile.get_edges()

    ans = 1
    neighbors = defaultdict(list)
    for k1, edges1 in all_edges.items():
        for k2, edges2 in all_edges.items():
            if edges1 == edges2:
                continue
            for edge1 in edges1:
                if (edge1 in edges2 or edge1[::-1] in edges2):  # and k1 not in neighbors[k2]:
                    neighbors[k1].append(k2)

    processing_stack = []
    done = set()
    processing_stack.append(list(tiles.values())[0])
    # processing_stack.append(tiles["1481"])

    while len(processing_stack) > 0:
        # print(processing_stack)
        tile = processing_stack.pop(0)
        if tile.k in done:
            continue
        edges = tile.get_edges()
        n = neighbors[tile.k]
        for neighbor in n:
            if neighbor in done:
                continue
            neighbor_tile = tiles[neighbor]
            while True:
                neighbor_edges = neighbor_tile.get_edges()
                if edges[0] == neighbor_edges[2]:  # above
                    tile.up = neighbor_tile
                    neighbor_tile.down = tile
                    break
                elif edges[0] == neighbor_edges[2][::-1]:  # flipped above
                    tile.up = neighbor_tile
                    neighbor_tile.down = tile
                    for j in range(len(neighbor_tile.content)):
                        neighbor_tile.content[j] = neighbor_tile.content[j][::-1]
                    break
                elif edges[1] == neighbor_edges[3]:  # right
                    tile.right = neighbor_tile
                    neighbor_tile.left = tile
                    break
                elif edges[1] == neighbor_edges[3][::-1]:  # flipped right
                    tile.right = neighbor_tile
                    neighbor_tile.left = tile
                    neighbor_tile.content.reverse()
                    break
                elif edges[2] == neighbor_edges[0]:  # below
                    tile.down = neighbor_tile
                    neighbor_tile.up = tile
                    break
                elif edges[2] == neighbor_edges[0][::-1]:  # flipped below
                    tile.down = neighbor_tile
                    neighbor_tile.up = tile
                    for j in range(len(neighbor_tile.content)):
                        neighbor_tile.content[j] = neighbor_tile.content[j][::-1]
                    break
                elif edges[3] == neighbor_edges[1]:  # left
                    tile.left = neighbor_tile
                    neighbor_tile.right = tile
                    break
                elif edges[3] == neighbor_edges[1][::-1]:  # flipped left
                    tile.left = neighbor_tile
                    neighbor_tile.right = tile
                    neighbor_tile.content.reverse()
                    break
                neighbor_tile.content = rotate_right(neighbor_tile.content)
            processing_stack.append(neighbor_tile)

        done.add(tile.k)

    random_tile = list(tiles.values())[0]
    top_corner = traverse_top_left(random_tile, tiles)
    id_grid = []
    i = 0
    while top_corner:
        id_grid.append([])
        r = top_corner
        while r:
            id_grid[i].append(r)
            r = r.right
        top_corner = top_corner.down
        i += 1

    for row in id_grid:
        print(row)

    for tile in tiles.values():
        tile.content = tile.content[1:-1]
        for i in range(len(tile.content)):
            tile.content[i] = tile.content[i][1:-1]

    grid = []
    for row in id_grid:
        x = []
        for i in range(len(row[0].content)):
            y = []
            for j in range(len(row)):
                y += row[j].content[i]
            x.append("".join(y))
        grid.append("\n".join(x))
    grid = "\n".join(grid).split("\n")

    sea_monster_depth = 3
    sea_monster_width = len("#    ##    ##    ###")
    sea_monster_hashtags = 15
    # for el in grid:
    #     print(el)
    # print(grid)
    monsters = 0
    c = 0
    while True:
        print(grid)
        for i in range(len(grid) - sea_monster_depth):
            row_width = len(grid[i])
            for j in range(row_width - sea_monster_width):
                if grid[i + 1][j] == "#" and grid[i + 2][j + 1] == "#" and grid[i + 1][j + 5] == "#" \
                        and grid[i + 1][j + 6] == "#" and grid[i + 2][j + 7] == "#" and grid[i + 2][j + 10] == "#" \
                        and grid[i + 1][j + 11] == "#" and grid[i + 1][j + 12] == "#" and grid[i + 2][j + 13] == "#" \
                        and grid[i + 2][j + 16] == "#" and grid[i + 1][j + 17] == "#" and grid[i][j + 18] == "#" \
                        and grid[i + 1][j + 18] == "#" and grid[i + 1][j + 19] == "#":
                    monsters += 1
        if monsters > 0:
            break
        grid = rotate_right(grid)
        c += 1
        if c == 4:
            grid.reverse()

    total_hashtags = sum([line.count("#") for line in grid])
    monster_hashtags = monsters * sea_monster_hashtags
    ans = total_hashtags - monster_hashtags
    print(ans)
    return ans


def traverse_top_left(tile, tiles):
    if tile.up:
        return traverse_top_left(tile.up, tiles)
    if tile.left:
        return traverse_top_left(tile.left, tiles)
    return tile


def rotate_right(m):
    m = list(zip(*m[::-1]))
    m = [''.join(list(el)) for el in m]
    return m


class Tile:
    def __init__(self, k, content):
        self.up = None
        self.left = None
        self.down = None
        self.right = None
        self.k = k
        self.content = content

    def get_edges(self):
        tile = self.content
        tile_length = len(self.content)
        edges = []
        e1 = tile[0]  # top
        edges.append(e1)
        e2 = "".join([tile[i][tile_length - 1] for i in range(tile_length)])  # right
        edges.append(e2)
        e3 = tile[tile_length - 1]  # bottom
        edges.append(e3)
        e4 = "".join([tile[i][0] for i in range(tile_length)])  # left
        edges.append(e4)
        return edges

    def __str__(self):
        uk = "None"
        lk = "None"
        dk = "None"
        rk = "None"
        if self.up is not None:
            uk = self.up.k
        if self.right is not None:
            rk = self.right.k
        if self.down is not None:
            dk = self.down.k
        if self.left is not None:
            lk = self.left.k

        return f"{self.k}-({uk},{rk},{dk},{lk})"

    def __repr__(self):
        return self.k


# task1()
task2()
