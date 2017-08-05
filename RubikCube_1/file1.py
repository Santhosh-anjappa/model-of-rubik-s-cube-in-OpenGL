from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
ver = [[-1,-1,-1],[-1,1,-1],[1,1,-1],[1,-1,-1],[-1,-1,1],[-1,1,1],[1,1,1],[1,-1,1]]
color = [[0,0,0],[0,1,0],[1,1,0],[1,0,0],[0,0,1],[0,1,1],[1,1,1],[1,0,1]]   # 0-Black 1-Green 2-Yellow 3-Red 4-Blue 5-LightBlue 6-White 7-Cyan
# cubespos = [[-2, -2, 2,0], [0, -2, 2,0], [2, -2, 2,0], [2, -2, 0,0], [2, -2, -2,0], [0, -2, -2,0], [-2, -2, -2,0], [-2, -2, 0,0],[0,-2,0,3],
#             [-2, 0, 2,0], [0, 0, 2,7], [2, 0, 2,0], [2, 0, 0,1], [2, 0, -2,0], [0, 0, -2,2], [-2, 0, -2,0], [-2, 0, 0,4],
#             [-2, 2, 2,0], [0, 2, 2,0], [2, 2, 2,0], [2, 2, 0,0], [2, 2, -2,0], [0, 2, -2,0], [-2, 2, -2,0], [-2, 2, 0,0],[0,2,0,5]]

cubespos = [[-2, -2, 2,[7,4,3]], [0, -2, 2,[7,0,3]], [2, -2, 2,[7,1,3]], [2, -2, 0,[0,1,3]], [2, -2, -2,[2,1,3]], [0, -2, -2,[2,0,3]], [-2, -2, -2,[2,4,3]], [-2, -2, 0,[0,4,3]],[0,-2,0,[0,0,3]],
             [-2, 0, 2,[7,4,0]], [0, 0, 2,[7,0,0]],  [2, 0, 2, [7,1,0]], [2, 0, 0,[0,1,0]], [2, 0, -2,[2,1,0]], [0, 0, -2,[2,0,0]], [-2, 0, -2,[2,4,0]], [-2, 0, 0,[0,4,0]],
             [-2, 2, 2,[7,4,5]], [0, 2, 2,[7,0,5]], [2, 2, 2,[7,1,5]], [2, 2, 0,[0,1,5]], [2, 2, -2,[2,1,5]], [0, 2, -2,[2,0,5]], [-2, 2, -2,[2,4,5]], [-2, 2, 0,[0,4,5]],[0,2,0,[0,0,5]]]

def drawcube(v):
    glPushMatrix()
    glTranslatef(v[0],v[1],v[2])
    cube(v[3])
    glPopMatrix()

def polygon(a, b, c, d,x):
    glColor3fv(color[x])
    glBegin(GL_POLYGON)
    glVertex3iv(ver[a])
    glVertex3iv(ver[b])
    glVertex3iv(ver[c])
    glVertex3iv(ver[d])
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP)
    glVertex3iv(ver[a])
    glVertex3iv(ver[b])
    glVertex3iv(ver[c])
    glVertex3iv(ver[d])
    glEnd()

def cube(c):

    polygon(0,1,2,3,c[0])
    polygon(4,5,6,7,c[0])
    polygon(0,1,5,4,c[1])
    polygon(7,6,2,3,c[1])
    polygon(1,2,6,5,c[2])
    polygon(0,3,7,4,c[2])

global l,m,n,thetax,thetay
x1=0
y1=0
l = 1
m = 1
n = 1
thetax = 0
thetay = 0
def display():
    global l,m,n
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0,0,500,500)
    gluPerspective(45,48/64,1,100)
    glLoadIdentity()
    gluLookAt(l,m,n,0,0,0,0,1,0)

    glPushMatrix()
    glRotatef(thetax,1,0,0)
    glRotatef(thetay, 0, 1, 0)
    for i in cubespos:
        drawcube(i)
    glPopMatrix()
    glutSwapBuffers()


def keyboard(ch,x,y):
    global thetax,thetay

    if(ch == b's'):
        if(thetax > 360):
            thetax = 0
        thetax += 10

    elif (ch == b'w'):
        if (thetax < 0):
            thetax = 360
        thetax -= 10

    elif (ch == b'd'):
        if (thetay > 360):
            thetay = 0
        thetay += 10

    elif (ch == b'a'):
        if (thetay < 0):
            thetay = 360
        thetay -= 10

    display()


def myinit():
    glClearColor(.20,.20,.20,1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-10,10,-10,10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glLineWidth(3.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(500,500)
    glutCreateWindow(b'cube')
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glEnable(GL_DEPTH_TEST)
    myinit()
    glutMainLoop()


main()