#!/usr/bin/env python

# This monitors the flight status of a suite of the FCU.

import sys
import rospy
from mavros_msgs.msg import State
from std_msgs.msg import String

class FCU_state_monitor:

  def __init__(self):

    # Instantiate instance of subscriber
    rospy.init_node('FCU_state_monitor')
    self.FCU_sub = rospy.Subscriber('/mavros/state', State, self.FCU_callback)    

    # Initialise variables used to track status etc.
    # These are available to all functions in the class
    self.FCU_status = "Initialising"

  def FCU_callback(self, msg):
    self.FCU_status = msg.mode
    print 'Status of FCU is: ', self.FCU_status

def main(args):
  sm = FCU_state_monitor()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)
