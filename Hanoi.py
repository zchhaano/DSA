def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)
#what does it do?

def moveDisk(fromPole, toPole):
    print("moving disk from %d to %d\n" % (fromPole, toPole))

moveTower(3,1,3,2)           