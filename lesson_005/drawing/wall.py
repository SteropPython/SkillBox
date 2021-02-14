import simple_draw as sd


def draw_wall(startPointX=200,
              startPointY=0,
              finishPointX=800,
              finishPointY=500,
              brickWidth=100,
              brickHight=50):

    brickStep = 0

    start_x = startPointX

    finish_y = startPointY

    while finish_y < finishPointY:
        if brickStep % 2 == 0:
            startPointX += brickWidth / 2
            finish_x = finishPointX - brickWidth / 2
        else:
            finish_x = finishPointX
        while startPointX < finish_x:
            startPoint = sd.get_point(startPointX, finish_y)
            endPoint = sd.get_point(startPointX + brickWidth, finish_y + brickHight)
            sd.rectangle(startPoint, endPoint, width=2)
            startPointX += brickWidth
        finish_y += brickHight
        startPointX = start_x
        brickStep += 1

    line_left = sd.Vector(sd.get_point(startPointX, 0), 90, finishPointY, 2)

    line_right = sd.Vector(sd.get_point(finishPointX, 0), 90, finishPointY, 2)

    line_down = sd.Vector(sd.get_point(startPointX, startPointY + 2), 0, finishPointX - startPointX, 2)

    line_left.draw()

    line_right.draw()

    line_down.draw()
