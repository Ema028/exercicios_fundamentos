from turtle import Turtle

north = 90
south = 270
west = 180
east = 0

class Snake:

      def __init__(self):
        self.all_turtles = []
        # Guarda a localização da cauda da serpente em all_turtles[index]
        self.index = 2
        self.create_snake()
        self.head = self.all_turtles[0]

      def create_snake(self):
        for i in range(self.index + 1):
            new_turtle = Turtle("square")
            new_turtle.penup()
            self.all_turtles.append(new_turtle)
            # Enfileirar as partes iniciais da cobra
            if i > 0:
                new_turtle.goto(x = self.all_turtles[i - 1].xcor() - 20, y = self.all_turtles[i - 1].ycor())

      def move(self):
        # Calculando index do último pedaço da cobra
        n = len(self.all_turtles) - 1

        # start = n, stop = 0, step = -1
        for i in range(n, 0, -1):
            self.all_turtles[i].goto(x = self.all_turtles[i - 1].xcor(), y = self.all_turtles[i - 1].ycor())

        self.head.forward(20)

      def left(self):
          if self.head.heading() != east:
            self.head.setheading(west)
      def right(self):
          if self.head.heading() != west:
            self.head.setheading(east)
      def up(self):
          if self.head.heading() != south:
            self.head.setheading(north)
      def down(self):
          if self.head.heading() != north:
            self.head.setheading(south)

      def grow(self):
          self.index += 1
          new_turtle = Turtle("square")
          new_turtle.penup()
          self.all_turtles.append(new_turtle)
          new_turtle.goto(self.all_turtles[self.index - 1].pos())

      def reset(self):
          for turtle in self.all_turtles:
              turtle.goto(1000, 1000)
          self.all_turtles.clear()
          self.index = 2
          self.create_snake()
          self.head = self.all_turtles[0]
            
