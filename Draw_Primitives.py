import tkinter as tk

class CustomPrimitiveDrawer:
    def __init__(self, master):
        self.master = master
        master.title("Custom Geometric Primitive Drawer")
        self.initialize_gui()
        self.point_list = []
        self.primitive_type = "polygon"

    def initialize_gui(self):
        self.canvas = tk.Canvas(self.master, width=500, height=500, background="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Button-1>", self.on_left_click)

        self.create_menus()

    def create_menus(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        primitive_menu = tk.Menu(menu)
        menu.add_cascade(label="Primitive", menu=primitive_menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        primitive_menu.add_command(label="Polygon", command=self.set_primitive_polygon)
        primitive_menu.add_command(label="Line", command=self.set_primitive_line)
        primitive_menu.add_command(label="Circle", command=self.set_primitive_circle)
        primitive_menu.add_command(label="Ellipse", command=self.set_primitive_ellipse)

        file_menu.add_command(label="Clear Points", command=self.clear_all_points)
        file_menu.add_command(label="Change Primitive", command=self.change_current_primitive)
        file_menu.add_separator()
        file_menu.add_command(label="Add Row", command=self.add_row)
        file_menu.add_command(label="Remove Row", command=self.remove_row)
        file_menu.add_command(label="Add Column", command=self.add_column)
        file_menu.add_command(label="Remove Column", command=self.remove_column)

    def on_right_click(self, event):
        x, y = event.x, event.y
        self.point_list.append((x, y))
        self.redraw()

    def on_left_click(self, event):
        x, y = event.x, event.y
        self.point_list.append((x, y))
        self.redraw()

    def change_current_primitive(self):
        primitive_types = ["polygon", "line", "circle", "ellipse"]
        current_index = primitive_types.index(self.primitive_type)
        self.primitive_type = primitive_types[(current_index + 1) % len(primitive_types)]
        self.redraw()

    def clear_all_points(self):
        self.point_list = []
        self.redraw()

    def set_primitive_polygon(self):
        self.primitive_type = "polygon"
        self.redraw()

    def set_primitive_line(self):
        self.primitive_type = "line"
        self.redraw()

    def set_primitive_circle(self):
        self.primitive_type = "circle"
        self.redraw()

    def set_primitive_ellipse(self):
        self.primitive_type = "ellipse"
        self.redraw()

    def add_row(self):
        grid_size = 20
        y_increment = 500 / grid_size
        new_points = []

        for x, y in self.point_list:
            new_points.append((x, y + y_increment))

        self.point_list.extend(new_points)
        self.redraw()

    def remove_row(self):
        if self.point_list:
            grid_size = 20
            y_increment = 500 / grid_size
            self.point_list = [point for x, y in self.point_list if y < 500 - y_increment]
            self.redraw()

    def add_column(self):
        grid_size = 20
        x_increment = 500 / grid_size
        new_points = []

        for x, y in self.point_list:
            new_points.append((x + x_increment, y))

        self.point_list.extend(new_points)
        self.redraw()

    def remove_column(self):
        if self.point_list:
            grid_size = 20
            x_increment = 500 / grid_size
            self.point_list = [point for x, y in self.point_list if x < 500 - x_increment]
            self.redraw()

    def redraw(self):
        self.clear_canvas()
        self.draw_grid()
        self.draw_primitives()

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw_grid(self):
        grid_size = 20
        for i in range(0, 500, grid_size):
            self.canvas.create_line(i, 0, i, 500, fill="gray")
            self.canvas.create_line(0, i, 500, i, fill="gray")

    def draw_primitives(self):
        if self.primitive_type == "polygon" and len(self.point_list) >= 3:
            self.draw_polygon()

        elif self.primitive_type == "line" and len(self.point_list) >= 2:
            self.draw_lines()

        elif self.primitive_type == "circle" and len(self.point_list) >= 2:
            self.draw_circle()

        elif self.primitive_type == "ellipse" and len(self.point_list) >= 2:
            self.draw_ellipse()

        self.draw_points()

    def draw_polygon(self):
        points = [point for pair in self.point_list for point in pair]
        self.canvas.create_polygon(points, outline="white")

    def draw_circle(self):
        x1, y1 = self.point_list[0]
        x2, y2 = self.point_list[1]
        radius = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, outline="white")

    def draw_ellipse(self):
        x1, y1 = the.point_list[0]
        x2, y2 = self.point_list[1]
        self.canvas.create_oval(x1, y1, x2, y2, outline="white")

    def draw_lines(self):
        for i in range(1, len(self.point_list)):
            x1, y1 = self.point_list[i - 1]
            x2, y2 = self.point_list[i]
            self.canvas.create_line(x1, y1, x2, y2, fill="white")

    def draw_points(self):
        for x, y in self.point_list:
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomPrimitiveDrawer(root)
    root.mainloop()
