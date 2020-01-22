import math

def publishMotors(turn, move):
    yaw = 0
    travel = 0
    
    if (turn > 0):
        yaw = 2
    elif (turn < 0):
        yaw = -2

    if (move != 0):
        travel = 1

    return [yaw, travel]

def publishArrived():
    return None

def move(boat, dest, yaw):

    deltx = boat[0] - dest[0]
    delty = boat[1] - dest[1]

    #calculating where the boat should go
    angleToMoveRad = math.tan(math.abs(deltx)/math.abs(delty)) #calculating delta from y axis
    angleDest = angleDest * (180/math.pi)

    
    if deltx > 0:
        if delty < 0:
            #4th quad
            angleDest += 270
    
    else:
        if delty > 0:
            #2nd quad
            angleDest += 90

        else:
            #3rd quad
            angleDest += 180


    # num of degrees remaining
    deltYaw = math.abs(angleDest - yaw)
    oppositeDir = False 
    if deltYaw >180:
        oppositeDir = True
        deltYaw = 360 - deltYaw

    clockwise = False
    if yaw >= 0 and yaw < angleDest:
        clockwise = True

    if oppositeDir:
        clockwise = !clockwise
    

    travel = math.sqrt(delty**2 + deltx**2)
    destArrivalOff = 15 
    destAngleOff = 2

    if((travel >= 0) and (travel < destArrivalOff) and (angleDest - destAngleOff < yaw) and (angleDest + 2 > yaw )): #check if dest reached

        return publishArrived()
    else:
        x = 0 #turn
        y = 0 #move

        if (clockwise):
            x = 1
        else:
            x= -1

        if (x == 0):
            y = 1

        return publishMotors(x, y)

def main():
    count = 0
     
    boat = [0,0]
    dest = [15, 20]
    yaw = 250

    results = move(boat, dest, yaw)

    while (results != None):
        yaw += results[0]
        boat....

        print(count, boat, dest, yaw)

        results = move(boat, dest, yaw)

    print("ARRIVED")

def updateYaw (x,y,yaw):
    if x = 0:
        return yaw
    else:
        return travel * YAW.DIFF
