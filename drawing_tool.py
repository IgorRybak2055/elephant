class Canvas:
    def __init__(self, p):
        """create canvas"""
        self.w = p[0]
        self.h = p[1]
        self.canvas = [[' ' for _ in range(p[0])] for _ in range(p[1])]

    def create_line(self, coords):
        """create line on canvas"""

        if len(coords) != 4:
            exit('Wrong number of coordinates. Should be 4!')

        start_point, endpoint = coords[:2], coords[2:]
        if start_point[0] == endpoint[0]:
            for point in range(start_point[1] - 1, endpoint[1]):
                self.canvas[point][start_point[0] - 1] = 'x'
        elif start_point[1] == endpoint[1]:
            for point in range(start_point[0] - 1, endpoint[0]):
                self.canvas[start_point[1] - 1][point] = 'x'

    def create_rectangle(self, coords):
        """create rectangle on canvas"""

        if len(coords) != 4:
            exit('Wrong number of coordinates. Should be 4!')
        elif coords[0] > coords[2] or coords[1] > coords[3]:
            point1, point2 = coords[::2], coords[1::2]
            point1.sort()
            point2.sort()
            coords = []
            for i in range(len(point1)):
                coords.extend((point1[i], point2[i]))

        self.create_line([coords[0], coords[1], coords[2], coords[1]])
        self.create_line([coords[2], coords[1], coords[2], coords[3]])
        self.create_line([coords[0], coords[3], coords[2], coords[3]])
        self.create_line([coords[0], coords[1], coords[0], coords[3]])

    def bucket_fill(self, x, y, color):
        """fill area"""

        if 0 <= y < self.h and 0 <= x < self.w and self.canvas[y][x] == ' ':
            self.canvas[y][x] = color
            self.bucket_fill(x, y - 1, color)
            self.bucket_fill(x, y + 1, color)
            self.bucket_fill(x - 1, y, color)
            self.bucket_fill(x + 1, y, color)


def write_results():
    """write results to file"""

    output_file.write('-'*22 + '\n')
    for line in c.canvas:
        output_file.write('|' + ''.join(line) + '|' + '\n')
    output_file.write('-'*22 + '\n')


def check_coords(coords):
    """checking coordinates in the canvas"""

    for i in range(len(coords)):
        if i % 2:
            if coords[i] > c.h:
                coords[i] = c.h
            elif coords[i] < 0:
                coords[i] = 0
        else:
            if coords[i] > c.w:
                coords[i] = c.w
            elif coords[i] < 0:
                coords[i] = 0


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        task = input_file.read()

        for command in task.split('\n'):
            action = command[0]
            try:
                params = list(map(int, command[1:].split()))
            except ValueError:
                params = command[1:].split()

            if action == 'C':
                c = Canvas(params)

            try:
                if action == 'L':
                    check_coords(params)
                    c.create_line(params)
                elif action == 'R':
                    check_coords(params)
                    c.create_rectangle(params)
                elif action == 'B':
                    c.bucket_fill(int(params[0]), int(params[1]), params[2])

                write_results()

            except NameError:
                exit('Canvas for drawing is missing!')
                break