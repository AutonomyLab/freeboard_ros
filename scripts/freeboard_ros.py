#!/usr/bin/env python

from bottle import route, run, static_file
import os
import rospy

@route('/freeboard/<filename:path>')
def send_static(filename):
    script_dir = os.path.dirname(os.path.realpath(__file__)) + '/../freeboard/'
    # TODO
    print script_dir
    return static_file(filename, root=script_dir)


@route('/freeboard/')
def freeboard():
    return send_static('index.html')


def main():
    rospy.init_node("freeboard_ros_node")

    port = int(rospy.get_param("~port", 3274))
    debug = rospy.get_param("~debug", False)
    host = rospy.get_param("~host", "localhost")

    run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    main()
