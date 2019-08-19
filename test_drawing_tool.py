import unittest
from drawing_tool import Canvas


class TestDrawingTool(unittest.TestCase):
    """Tests for DrawingTool class"""

    def setUp(self):
        self.c = Canvas((20, 4))
        self.params = {'L': (10, 2, 10, 4), 'R': (16, 1, 20, 3), 'B': (10, 3, 'o')}

    def test_input_create_command(self):
        with open('input.txt', 'r') as f:
            self.assertIn('C', f.readline())

    def test_create_line(self):
        """line creation check"""
        self.c.create_line(self.params['L'])
        if self.params['L'][0] == self.params['L'][2]:
            for line in range(self.params['L'][1]-1, self.params['L'][3]-self.params['L'][1]):
                self.assertIn('x', self.c.canvas[self.params['L'][line] - 1][self.params['L'][0]-1])
        elif self.params['L'][1] == self.params['L'][3]:
            self.assertIn('x', self.c.canvas[self.params['L'][1]-1])

    def test_create_rectangle(self):
        """rectangle creation check"""
        count = 0
        self.c.create_rectangle(self.params['R'])
        for line in range((self.params['R'][1] - 1), self.params['R'][3]):
            for col in range((self.params['R'][0] - 1), self.params['R'][2]):
                if self.c.canvas[line][col] == ' ':
                    self.c.canvas[line][col] = '_'
                count = count + 1 if self.c.canvas[line][col] == 'x' else count
        self.assertEqual(count, (self.params['R'][3]-self.params['R'][1]+self.params['R'][2]-self.params['R'][0])*2)

    def test_fill(self):
        """fill check"""
        self.c.bucket_fill(self.params['B'][0], self.params['B'][1], self.params['B'][2])
        fill, not_fill = 0, 0
        for line in self.c.canvas:
            fill += line.count(self.params['B'][2])
            not_fill += (line.count('x') + line.count('_'))
        self.assertEqual(fill, (self.c.w * self.c.h) - not_fill)


if __name__ == '__main__':
    unittest.main()