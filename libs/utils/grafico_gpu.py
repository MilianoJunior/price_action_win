# import math
# from vispy import app, gloo


# class Canvas(app.Canvas):

#     def __init__(self, *args, **kwargs):
#         app.Canvas.__init__(self, *args, **kwargs)
#         self._timer = app.Timer('auto', connect=self.on_timer, start=True)
#         self.tick = 0

#     def on_draw(self, event):
#         gloo.clear(color=True)

#     def on_timer(self, event):
#         self.tick += 1 / 60.0
#         c = abs(math.sin(self.tick))
#         gloo.set_clear_color((c, c, c, 1))
#         self.update()

# if __name__ == '__main__':
#     canvas = Canvas(keys='interactive', always_on_top=True)
#     canvas.show()
#     app.run()
    # pacotes = ['Pyglet', 'Glfw', 'SDL2', 'wx', 'EGL', 'osmesa', 'tkinter']
    # texto = ''
    # for text in pacotes:
    #     texto += ' ' + text
        
    # print(f'pip install {texto}')










# -*- coding: utf-8 -*-
import numpy as np
from vispy import app, gloo
from vispy.gloo import Program, VertexBuffer, IndexBuffer
import vispy


print(vispy.sys_info())

vertex_shader = """
attribute vec2 a_position;
void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

fragment_shader = """
uniform vec4 u_color;
void main() {
    gl_FragColor = u_color;
}
"""

class RealTimeLinePlot(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive')
        self.program = Program(vertex_shader, fragment_shader)
        self.program['u_color'] = (1, 0, 0, 1)

        self.n_points = 1000
        self.data = np.zeros((self.n_points, 2), dtype=np.float32)

        self.program['a_position'] = VertexBuffer(self.data)

        gloo.set_state(clear_color='white', blend=True,
                        blend_func=('src_alpha', 'one_minus_src_alpha'))

        self._timer = app.Timer('auto', connect=self.update, start=True)

    def on_draw(self, event):
        gloo.clear()
        self.program.draw('line_strip')

    def update(self, event):
        self.data[:-1] = self.data[1:]
        self.data[-1] = (np.random.uniform(-1, 1), np.random.uniform(-1, 1))
        self.program['a_position'].set_data(self.data)
        self.update()

if __name__ == '__main__':
    plot = RealTimeLinePlot()
    plot.show()
    app.run()
