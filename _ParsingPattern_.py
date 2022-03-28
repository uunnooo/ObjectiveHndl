"""
Parsing pattern to get the data in the rawdata of vehicle objective



"""

# Vehicle Information
class Pattern_Infor_Vehicle :
    def __init__(self) :
        self.VEHICLE_WEIGHT_FL = r'.*?vehicle.*?weight.*?f.*?l.*?'
        self.VEHICLE_WEIGHT_FR = r'.*?vehicle.*?weight.*?f.*?r.*?'
        self.VEHICLE_WEIGHT_RL = r'.*?vehicle.*?weight.*?r.*?l.*?'
        self.VEHICLE_WEIGHT_RR = r'.*?vehicle.*?weight.*?r.*?r.*?'
        self.VEHICLE_HEIGHT_OVERALL = r'.*?vehicle.*?overall.*?height.*?'
        self.VEHICLE_HEIGHT_CG = r'.*?vehicle.*?cg.*?height.*?'
        self.VEHICLE_WHELLBASE = r'.*?vehicle.*?wheel.*?base.*?'
        self.VEHICLE_GEAR_RATIO = r'.*?vehicle.*?gear.*?ratio.*?'
        self.VEHICLE_INERTIA_ZZ = r'.*?vehicle.*?izz.*?'

class Pattern_Infor_Sensor :
    def __init__(self) :
        self.SENSOR_POSITION_X = r'.*?imu.*?position.*?x.*?|.*?sensor.*?position.*?x.*?'
        self.SENSOR_POSITION_Y = r'.*?imu.*?position.*?y.*?|.*?sensor.*?position.*?y.*?'
        self.SENSOR_POSITION_Z = r'.*?imu.*?position.*?z.*?|.*?sensor.*?position.*?z.*?'

class Pattern_ChannelName :
    def __init__(self) :
        self.TIME = r'time'
        self.SWA = r'.*?swa.*?|.*?steering.*?angle.*?'
        self.SWT = r'.*?swt.*?|.*?steering.*?torque.*?'
        self.LATITUDE = r'.*?latitude.*?|.*?pos.*?lat.*?'
        self.LONGITUDE = r'.*?longitude.*?|.*?pos.*?long.*?'
        self.ALTITUDE = r'.*?altitude.*?|.*?pos.*?alt.*?'
        self.POSITION_X = r'.*?pos.*?local.*?x.*?|.*?pos.*?x.*?'
        self.POSITION_Y = r'.*?pos.*?local.*?y.*?|.*?pos.*?y.*?'
        self.DISTANCE = r'.*?distance.*?'
        self.VELOCITY_FOR = r'.*?vel.*?for.*?'
        self.VELOCITY_LAT = r'.*?vel.*?lat.*?'
        self.VELOCITY_HOR = r'.*?vel.*?hor.*?|.*?speed.*?'
        self.GROUND_ACC_FOR = r'.*?acc.*?for.*?'
        self.GROUND_ACC_LAT = r'.*?acc.*?lat.*?'
        self.GROUND_ACC_DOW = r'.*?acc.*?dow.*?'
        self.HEADING_ANGLE = r'.*?head.*?ang.*?|.*?ang.*?head.*?'
        self.ROLL_ANGLE = r'.*?roll.*?ang.*?|.*?ang.*?roll.*?'
        self.PITCH_ANGLE = r'.*?pitch.*?ang.*?|.*?ang.*?pitch.*?'
        self.SIDESLIP = r'.*?slip.*?ang|.*?ang.*?slip'
        self.SIDESLIP_FA = r'.*?slip.*?ang.*?1|.*?ang.*?slip.*?1'
        self.SIDESLIP_RA = r'.*?slip.*?ang.*?2|.*?ang.*?slip.*?2'
        self.GROUND_ANGRATE_FOR = r'.*?for.*?ang.*?rate.*?|.*?ang.*?rate.*?for.*?'
        self.GROUND_ANGRATE_LAT = r'.*?lat.*?ang.*?rate.*?|.*?ang.*?rate.*?lat.*?'
        self.GROUND_ANGRATE_VER = r'.*?ver.*?ang.*?rate.*?|.*?ang.*?rate.*?ver.*?'
        self.HEIGHT_FL = r'.*?height.*?fl.*?|.*?fl.*?height.*?'
        self.HEIGHT_FR = r'.*?height.*?fr.*?|.*?fr.*?height.*?'
        self.HEIGHT_RL = r'.*?height.*?rl.*?|.*?rl.*?height.*?'
        self.HEIGHT_RR = r'.*?height.*?rr.*?|.*?rr.*?height.*?'
        self.ROAD_TEMP = r'.*?road.*?temp.*?|.*?temp.*?road.*?'

class InformationTest(Pattern_Infor_Vehicle, Pattern_Infor_Sensor, Pattern_ChannelName) :
    def __init__(self):
        Pattern_Infor_Vehicle.__init__(self)
        Pattern_Infor_Sensor.__init__(self)
        Pattern_ChannelName.__init__(self)
