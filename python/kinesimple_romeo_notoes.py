from dynamic_graph import plug
from dynamic_graph.sot.core import *
from dynamic_graph.sot.core.math_small_entities import Derivator_of_Matrix
from dynamic_graph.sot.dynamics import *
from dynamic_graph.sot.dyninv import *
import dynamic_graph.script_shortcuts
from dynamic_graph.script_shortcuts import optionalparentheses
from dynamic_graph.matlab import matlab
from dynamic_graph.sot.core.meta_task_6d import MetaTask6d,toFlags
from attime import attime

from robotSpecific_romeo_notoes import pkgDataRootDir,modelName,robotDimension,initialConfig,gearRatio,inertiaRotor
from robotSpecific_romeo_notoes import specificitiesName,jointRankName
robotName = 'romeo_notoes'

from numpy import *
def totuple( a ):
    al=a.tolist()
    res=[]
    for i in range(a.shape[0]):
        res.append( tuple(al[i]) )
    return tuple(res)


# --- ROBOT SIMU ---------------------------------------------------------------
# --- ROBOT SIMU ---------------------------------------------------------------
# --- ROBOT SIMU ---------------------------------------------------------------

robotDim=robotDimension[robotName]
robot = RobotSimu("robot")
robot.resize(robotDim)

robot.set( initialConfig[robotName] )
dt=5e-3

# --- VIEWER -------------------------------------------------------------------
# --- VIEWER -------------------------------------------------------------------
# --- VIEWER -------------------------------------------------------------------
try:
    import robotviewer

    def stateFullSize(robot):
        return [float(val) for val in robot.state.value]
    RobotSimu.stateFullSize = stateFullSize

    robot.viewer = robotviewer.client('XML-RPC')
#    robot.viewer.updateElementConfig('hrp',robot.stateFullSize())

    def refreshView( robot ):
        robot.viewer.updateElementConfig('hrp',robot.stateFullSize())
    RobotSimu.refresh = refreshView
    def incrementView( robot,dt ):
        robot.incrementNoView(dt)
        robot.refresh()
    RobotSimu.incrementNoView = RobotSimu.increment
    RobotSimu.increment = incrementView
    def setView( robot,*args ):
        robot.setNoView(*args)
        robot.refresh()
    RobotSimu.setNoView = RobotSimu.set
    RobotSimu.set = setView

    robot.refresh()
except:
    print "No robot viewer, sorry."
    robot.viewer = None


# --- MAIN LOOP ------------------------------------------

qs=[]
def inc():
    attime.run(robot.control.time+1)
    robot.increment(dt)
    tr.triger.recompute( robot.control.time )
    qs.append(robot.state.value)

from ThreadInterruptibleLoop import *
@loopInThread
def loop():
    inc()

runner=loop()

@optionalparentheses
def go(): runner.play()
@optionalparentheses
def stop(): runner.pause()
@optionalparentheses
def next(): runner.once()

# --- DYN ----------------------------------------------------------------------
# --- DYN ----------------------------------------------------------------------
# --- DYN ----------------------------------------------------------------------

modelDir = pkgDataRootDir[robotName]
xmlDir = pkgDataRootDir[robotName]
specificitiesPath = xmlDir + '/' + specificitiesName[robotName]
jointRankPath = xmlDir + '/' + jointRankName[robotName]

dyn = Dynamic("dyn")
dyn.setFiles(modelDir, modelName[robotName],specificitiesPath,jointRankPath)
dyn.parse()

dyn.inertiaRotor.value = inertiaRotor[robotName]
dyn.gearRatio.value = gearRatio[robotName]

plug(robot.state,dyn.position)
dyn.velocity.value = robotDim*(0.,)
dyn.acceleration.value = robotDim*(0.,)

dyn.ffposition.unplug()
dyn.ffvelocity.unplug()
dyn.ffacceleration.unplug()

#dyn.setProperty('ComputeBackwardDynamics','true')
#dyn.setProperty('ComputeAccelerationCoM','true')

robot.control.unplug()

# --- Task Dyn -----------------------------------------
class MetaTaskKine6d( MetaTask6d ):
    def createTask(self):
        self.task = Task('task'+self.name)

    def createGain(self):
        self.gain = GainAdaptive('gain'+self.name)
        self.gain.set(0.1,0.1,125e3)
    def plugEverything(self):
        self.feature.setReference(self.featureDes.name)
        plug(self.dyn.signal(self.opPoint),self.feature.signal('position'))
        plug(self.dyn.signal('J'+self.opPoint),self.feature.signal('Jq'))
        self.task.add(self.feature.name)
        plug(self.task.error,self.gain.error)
        plug(self.gain.gain,self.task.controlGain)
    def keep(self):
        self.feature.position.recompute(self.dyn.position.time)
        self.feature.keep()

# Task right hand
taskRH=MetaTaskKine6d('rh',dyn,'rh','right-wrist')
taskRH.ref = ((0,0,-1,0.22),(0,1,0,-0.37),(1,0,0,.74),(0,0,0,1))
taskLH=MetaTaskKine6d('lh',dyn,'lh','left-wrist')
#TODO taskLH.ref = ((0,0,-1,0.22),(0,1,0,0.37),(1,0,0,.74),(0,0,0,1))

# Task LFoot: Move the right foot up.
taskRF=MetaTaskKine6d('rf',dyn,'rf','right-ankle')
taskLF=MetaTaskKine6d('lf',dyn,'lf','left-ankle')

# --- TASK COM ------------------------------------------------------
dyn.setProperty('ComputeCoM','true')

featureCom    = FeatureGeneric('featureCom')
featureComDes = FeatureGeneric('featureComDes')
plug(dyn.com,featureCom.errorIN)
plug(dyn.Jcom,featureCom.jacobianIN)
featureCom.setReference('featureComDes')
featureComDes.errorIN.value =  (0.05,  0,   0.675);

taskCom = Task('taskCom')
taskCom.add('featureCom')

gCom = GainAdaptive('gCom')
plug(taskCom.error,gCom.error)
plug(gCom.gain,taskCom.controlGain)
gCom.set(1,1,1)

# --- TASK SUPPORT --------------------------------------------------
featureSupport    = FeatureGeneric('featureSupport')
plug(dyn.com,featureSupport.errorIN)
plug(dyn.Jcom,featureSupport.jacobianIN)

taskSupport=TaskInequality('taskSupport')
taskSupport.add(featureSupport.name)
taskSupport.selec.value = '011'
taskSupport.referenceInf.value = (-0.08,-0.045,0)    # Xmin, Ymin
taskSupport.referenceSup.value = (0.11,0.335,0)  # Xmax, Ymax
taskSupport.dt.value=dt

# --- TASK POSTURE --------------------------------------------------
featurePosture    = FeatureGeneric('featurePosture')
featurePostureDes = FeatureGeneric('featurePostureDes')
plug(dyn.position,featurePosture.errorIN)
featurePosture.setReference('featurePostureDes')
featurePosture.jacobianIN.value = totuple( identity(robotDim) )
featurePostureDes.errorIN.value = dyn.position.value

taskPosture = Task('taskPosture')
taskPosture.add('featurePosture')

gPosture = GainAdaptive('gPosture')
plug(taskPosture.error,gPosture.error)
plug(gPosture.gain,taskPosture.controlGain)
gPosture.set(1,1,1)

postureSelec = range(0,3)      # right leg
postureSelec += range(6,9)     # left leg
postureSelec += range(12,16)   # chest+head
#postureSelec += range(16,19)   # right arm
#postureSelec += range(23,26)   # left arm
featurePosture.selec.value = toFlags(postureSelec)

# --- TASK JL ------------------------------------------------------
taskJL = TaskJointLimits('taskJL')
plug(dyn.position,taskJL.position)
plug(dyn.lowerJl,taskJL.referenceInf)
plug(dyn.upperJl,taskJL.referenceSup)
taskJL.dt.value = dt
taskJL.selec.value = toFlags(range(6,robotDim))

# --- SOT Dyn OpSpaceH --------------------------------------
# SOT controller.
sot = SolverKine('sot')
sot.setSize(robotDim)
#sot.damping.value = 2e-2

plug(sot.control,robot.control)

def sot_addContact( sot,metaTask ):
    metaTask.keep()
    sot.push(metaTask.task.name)
import new
sot.addContact = new.instancemethod(sot_addContact, sot, sot.__class__)


# --- TRACE ----------------------------------------------

from dynamic_graph.tracer import *
from dynamic_graph.tracer_real_time import *
tr = TracerRealTime('tr')
tr.setBufferSize(10485760)
tr.open('/tmp/','dyn_','.dat')
tr.start()

#robot.periodicCall addSignal tr.triger

#tr.add('p6.error','position')
tr.add('featureCom.error','comerror')
tr.add('dyn.com','com')
tr.add('dyn.position','state')
# tr.add('gCom.gain','')
# tr.add('gCom.error','gerror')

tr.add('sot.control','')

# --- shortcuts -------------------------------------------------
qn=taskJL.normalizedPosition
q=taskJL.position
comref=featureComDes.errorIN

@optionalparentheses
def iter():         print 'iter = ',robot.state.time
@optionalparentheses
def dump():         tr.dump()
@optionalparentheses
def status():       print runner.isPlay
@optionalparentheses
def iter():         print 'iter = ',robot.state.time

# --- RUN ------------------------------------------------

#sot.damping.value=.1
sot.addContact(taskLF)
sot.addContact(taskRF)
sot.push(taskCom.name)
#sot.push(taskJL.name)
#sot.push(taskSupport.name)
sot.push(taskRH.task.name)
sot.push(taskLH.task.name)

rhUT=PoseUThetaToMatrixHomo('rhUT')
rhUT.sin.value =(0.3,-0.2,0.84,  0.0,0.5,0.5)
rhUT.sout.recompute(1)
plug(rhUT.sout,taskRH.featureDes.position)
taskRH.gain.setConstant(1)

lhUT=PoseUThetaToMatrixHomo('lhUT')
lhUT.sin.value =(0.3, 0.2,0.84,  0.0,0.5,-0.5)
lhUT.sout.recompute(1)
plug(lhUT.sout,taskLH.featureDes.position)

# comref.value=( 0.05,  0.1,  0.75 )

tr.add('taskJL.normalizedPosition','qn')

@attime(100)
def m1():
    "Timer 1... done"

attime(1000,stop,'pause')
attime(1000,dump,'dump')

#matlab.prec=4
#matlab.fullPrec=0
