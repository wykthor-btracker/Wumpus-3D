#imports
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import pywavefront

#imports
 
## TODO snakeCaseIfy the functions name's (O)--(O)

class Camera:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

class Window:
    def __init__(self,width=480,height=480,x=0,y=0,title="Wumpos3D"):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.title = title
        self.windowObj = None

class GUI:
    def __init__(self, window=Window(),fullscreen=False,camera=Camera()):
        self.window = window
        self.fullscreen = fullscreen
        self.camera = camera
        self.engine = OpenWumpus()
        self.scene = None
        self.scene_scale = None
        self.scene_trans = None
        self.a = 0
        self.b = 0

    def renderScreen(self):
        self.__loadModels()
        self.__initializeGlut()

    def __initializeGlut(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.window.width,self.window.height)
        glutInitWindowPosition(self.window.x,self.window.y)
        self.window.windowObj = glutCreateWindow(self.window.title)
        glutDisplayFunc(self.drawGLScene)
        glutIdleFunc(self.drawGLScene)
        if self.fullscreen: glutFullScreen()
        glutReshapeFunc(self.engine.resizeGLScene)
        glutKeyboardFunc(self.keyPressed)
        self.engine.initializeGL(self.window.width,self.window.height)
        glutMainLoop()
    
    def __loadModels(self):
        self.scene = pywavefront.Wavefront('Models/door/Door.obj', create_materials=True,collect_faces=True)
        scene_box = (self.scene.vertices[0], self.scene.vertices[0])
        for vertex in self.scene.vertices:
            min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
            max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
            scene_box = (min_v, max_v)
        scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
        max_scene_size = max(scene_size)
        scaled_size    = 10
        self.scene_scale    = [scaled_size/max_scene_size for i in range(3)]
        self.scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

    def Model(self):
        try:
            glPushMatrix()
        except:
            print("oh kurwa")
        glScalef(*self.scene_scale)
        glTranslatef(*self.scene_trans)
        for mesh in self.scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                glColor3f(1,0.5,0.5)
                for vertex_i in face:
                    glVertex3f(*self.scene.vertices[vertex_i])
            glEnd()
        glPopMatrix()

    def drawGLScene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.b,0,-10)
        glRotatef(self.a,0,1,0)


        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        self.Model()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glutSwapBuffers()
    
    def keyPressed(self,*args):
        if args[0] == b'\x1b':
            print("Quiting...")
            sys.exit()
        elif args[0] == b'a':
            self.a += 2
        elif args[0] == b'd':
            self.a -= 2
        elif args[0] == b'w':
            self.b += 2
        elif args[0] == b's':
            self.b -= 2
 
class OpenWumpus:
    def __init__(self):
        self.buffer = []

    def initializeGL(self, width, height):
        glClearColor(0,0,0,0)
        glClearDepth(1)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45,(width/height),1,100)
        glMatrixMode(GL_MODELVIEW)
    
    def resizeGLScene(self, width, height):
        if height == 0: height = 1
        glViewport(0,0,width,height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45,(width/height),1,100)
        glMatrixMode(GL_MODELVIEW)

def main():
    gui = GUI()
    gui.renderScreen()
    
if __name__ == '__main__':
    main()
