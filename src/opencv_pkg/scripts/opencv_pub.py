#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import cv2 as cv 

def talker():
    pub = rospy.Publisher('coord_board', String, queue_size=10)
    rospy.init_node('open_cv_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    cap = cv.VideoCapture(0)

    while not rospy.is_shutdown():
        if cap.isOpened():
            ret, frame = cap.read()
            cv.imshow('frame', frame)
            if cv.waitKey(10) & 0xFF == 27:
                break
            size = frame.shape
            size = str(size[0]) + str(size[1]) + str(size[2])
            rospy.loginfo(size)
            pub.publish(size)
        rate.sleep()
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass