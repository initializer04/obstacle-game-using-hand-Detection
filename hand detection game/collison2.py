
def jump(paddle):
    if(paddle.y-25<350):
        paddle.block_vel=-paddle.block_vel
    if(paddle.y+25>600):
        paddle.block_vel=-paddle.block_vel

