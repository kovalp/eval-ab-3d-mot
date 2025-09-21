"""
Utility class to load data.
"""


class TrackData:

    def __init__(
        self,
        frame=-1,
        obj_type='unset',
        truncation=-1,
        occlusion=-1,
        obs_angle=-10,
        x1=-1,
        y1=-1,
        x2=-1,
        y2=-1,
        w=-1,
        h=-1,
        l=-1,
        x=-1000,
        y=-1000,
        z=-1000,
        ry=-10,
        score=-1000,
        track_id=-1,
    ):
        """
        Constructor, initializes the object given the parameters.
        """
        self.frame = frame
        self.track_id = track_id
        self.obj_type = obj_type
        self.truncation = truncation
        self.occlusion = occlusion
        self.obs_angle = obs_angle
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = w
        self.h = h
        self.l = l
        self.x = x
        self.y = y
        self.z = z
        self.ry = ry
        self.score = score
        self.ignored = False
        self.valid = False
        self.tracker = -1

    def __str__(self):
        """
        Print read data.
        """
        attrs = vars(self)
        return '\n'.join('%s: %s' % item for item in attrs.items())
