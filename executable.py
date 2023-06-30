from module import Canvas, Square, Rectangle, Canvas_Info, Square_Info, Rectangle_Info


"""First Image"""
canvas_info = Canvas_Info()
square_info = Square_Info()
rectangle_info = Rectangle_Info()

# Define canvas
canvas = Canvas(width=canvas_info.width, height=canvas_info.height,
                color=[canvas_info.R, canvas_info.G, canvas_info.B])
# Define square
square = Square(x=square_info.x, y=square_info.y, side=square_info.side,
                color=[square_info.R, square_info.G, square_info.B])
# Define rectangle
rectangle = Rectangle(x=rectangle_info.x, y=rectangle_info.y, width=rectangle_info.width,
                      height=rectangle_info.height,
                      color=[rectangle_info.R, rectangle_info.G, rectangle_info.B])
# Draw square and rectangle
square.draw(canvas)
rectangle.draw(canvas)
# Create canvas (can create multiple)
canvas.make(f"shape_images/canvas{Canvas.images_made}.png")


"""More Images"""
one_more = input('Do you want to create another image? {Y/N}: ')

while one_more == "Y":
    canvas_info = Canvas_Info()
    square_info = Square_Info()
    rectangle_info = Rectangle_Info()

    # Define canvas
    canvas = Canvas(width=canvas_info.width, height=canvas_info.height,
                    color=[canvas_info.R, canvas_info.G, canvas_info.B])
    # Define square
    square = Square(x=square_info.x, y=square_info.y, side=square_info.side,
                    color=[square_info.R, square_info.G, square_info.B])
    # Define rectangle
    rectangle = Rectangle(x=rectangle_info.x, y=rectangle_info.y, width=rectangle_info.width,
                          height=rectangle_info.height,
                          color=[rectangle_info.R, rectangle_info.G, rectangle_info.B])
    # Draw square and rectangle
    square.draw(canvas)
    rectangle.draw(canvas)
    # Create canvas (can create multiple)
    canvas.make(f"shape_images/canvas{Canvas.images_made}.png")

    # Asking again to come out of loop if needed.
    one_more = input('Do you want to create another image? {Y/N}: ')








