#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#imports



class Camera:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

class Window:
    def __init__(self,width=480,height=480,x=0,y=0,title="Wumpos3D"):
        self.width = width
        self.height = height
        self.X = x
        self.y = y
        self.title = title
        self.windowObj = None

class GUI:
    def __init__(self, window=Window(),fullscreen=False,camera=Camera()):
        self.window = window
        self.fullscreen = fullscreen
        self.camera = camera
        self.engine = OpenWumpus()

    def renderScreen(self):
        __initializeGlut()

    def __initializeGlut(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.window.width,self.window.height)
        glutInitWindowPosition(self.window.x,self.window.y)
        self.window.windowObj = glutCreateWindow(self.window.title)
        glutDisplayFunc(self.engine.DrawGLScene)
        glutIdleFunc(self.engine.DrawGLScene)
        if self.fullscreen: glutFullScreen()
        glutReshapeFunc(self.engine.resizeGLScene)
        glutKeyboardFunc(self.engine.keyPressed)
        self.engine.initializeGL(self.window.width,self.window.height)
        glutMainLoop()

class OpenWumpus:
    def __init__(self):
        pass
    
    def initializeGL(self, width, height):
        glClearColor(0,0,0,0)
        glClearDepth(1)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45,float(width)/float(height),0.1,100)
        glMatrixMode(GL_MODELVIEW)
    
    def drawGLScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef()
        glRotatef()
        #TODO create the object
        glutSwapBuffers()
    
    def resizeGLScene(self, width, height):
        if height == 0: height = 1
        glViewport(0,0,width,height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45,float(width)/float(height),0.1,100)
        glMatrixMode(GL_MODELVIEW)
        
    
    def keyPressed(self,*args):
        print(args[0])
