import math

from manim import *


def get_direction_array(x, y):
    if x == 0 and y > 0:
        return UP
    elif x < 0:
        return LEFT
    elif x > 0:
        return RIGHT
    elif x == 0 and y < 0:
        return DOWN


class CreateCircle(Scene):
    def construct(self):
        vertices = [n + 1 for n in range(4)]
        edges = [(n + 1, n + 2) for n in range(4 - 1)]
        g = Graph(vertices, edges, layout='circular')
        tex_labels = []
        face1 = MathTex(r"F_{1}").scale(.75)
        for v in g.vertices:
            label = MathTex(fr"V_{v}").scale(0.5).next_to(g.vertices[v], DOWN)
            tex_labels.append(label)
        for e in g.edges:
            label2 = MathTex(fr"E{e}").scale(0.5).next_to(g.edges[e], np.array((0.0, 0.0, 0.0))).shift(
                np.array((0.0, 0.5, 0.0)))
            tex_labels.append(label2)
        label_group = VGroup(*tex_labels)
        equation = VGroup(MathTex(fr"V-E+F=2"), MathTex(f"{g.vertices.__len__()}-{g.edges.__len__()}+1=2")).arrange(
            DOWN).to_edge(DOWN)
        explanation = Text(" Edges = v \nso v−(v−1)+1=2").to_edge(LEFT).scale(.5)
        self.play(Create(g), Create(label_group), Write(face1), Write(equation), Write(explanation))
        self.wait(2)
        g.add_edges((4, 1))
        g.update_edges(g)
        label_group.add(MathTex(fr"E{(4, 1)}").scale(0.5).next_to(g.edges[(4, 1)], np.array((0.0, 0.0, 0.0))).shift(
            np.array((0.0, 0.5, 0.0))))
        face2 = MathTex(r"F_{2}").scale(.75).to_corner(UP + LEFT).shift(np.array((1.0, -1.0, 0.0)))
        explanation2 = Text(" Adding an edge \nwithout adding a \nvertex creates \na new face").to_edge(LEFT).shift(
            LEFT).scale(.5)
        equation2 = VGroup(MathTex(fr"V-E+F=2"), MathTex(f"{g.vertices.__len__()}-{g.edges.__len__()}+2=2")).arrange(
            DOWN).to_edge(DOWN)
        self.play(Transform(equation, equation2), Write(face2), Transform(explanation, explanation2))
        self.wait(2)
        self.play(FadeOut(g, label_group, explanation))
        vertices2 = [n + 1 for n in range(8)]
        edges2 = [(n + 1, n + 2) for n in range(8 - 1)] + [(n + 1, n + 3) for n in range(8 - 2) if n % 2 == 0] + [
            (1, 8), (7, 1)]
        print(vertices2)
        print(edges2)
        g2 = Graph(vertices2, edges2, layout='circular')
        tex_labels2 = []
        for v in g2.vertices:
            label = MathTex(fr"V_{v}").scale(0.5).next_to(g2.vertices[v], DOWN)
            tex_labels2.append(label)
        for e in g2.edges:
            print(e)
            print(g2.edges[e])
            if not e == (7, 1) and not e == (5, 7):
                label2 = MathTex(fr"E{e}").scale(0.5).next_to(g2.edges[e], np.array((0.0, 0.0, 0.0))).shift(
                    np.array((0.0, -0.25, 0.0)))
            else:
                label2 = MathTex(fr"E{e}").scale(0.5).next_to(g2.edges[e], np.array((0.0, 0.0, 0.0))).shift(
                    np.array((0.0, 0.25, 0.0)))
            tex_labels2.append(label2)

        faces = []
        for n in range(4):
            faces.append(
                MathTex(fr"F_{n + 3}").scale(.75).shift(
                    np.array((1.75 * math.cos(math.radians((n * 90) + 45)), 1.75 * math.sin(
                        math.radians((n * 90) + 45)), 0))))
        facelabels = VGroup(*faces)
        label_group2 = VGroup(*tex_labels2)
        self.play(Create(g2), Write(label_group2), Write(facelabels), Transform(equation, VGroup(MathTex(fr"V-E+F=2"),
                                                                                                 MathTex(
                                                                                                     f"{g2.vertices.__len__()}-"
                                                                                                     f"{g2.edges.__len__()}+{2 + faces.__len__()}=2")).arrange(
            DOWN).to_edge(DOWN)))
        self.wait(2)
