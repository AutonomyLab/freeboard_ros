# freeboard_ros

*freeboard_ros* is a proof-of-concept ROS wrapper for [freeboard](http://freeboard.io/) realtime dashboard using [roslibjs](http://wiki.ros.org/roslibjs). The long term goal of this project is to make it easier to create embeddable real-time dashboards for robots running ROS.

## Approach & Roadmap

- Create a `roslibjs` plugin for `freeboard`: [Our local fork](https://github.com/AutonomyLab/freeboard.git) of `freeboad` includes a proof-of-concept [plugin](https://github.com/AutonomyLab/freeboard/blob/ros-dev/plugins/ros/ros.js) for `freeboard` that enables `freeboard` to connect to a local [rosbridge server](http://wiki.ros.org/rosbridge_server) and expose any ROS topic as a *data source* in `freeboard`. Development is done in `ros-dev` branch. This fork is embedded in this git repository as a git submodule.

- Serve freeboard dashboard using a standalone ROS Node: `scripts/freeboard_ros.py` is a standalone ROS node that serves `freeboard` as a web application using [Bottle](http://bottlepy.org/docs/dev/index.html).

## Download and Compile Instructions

*Note:* `python-bottle` is not yet added to `rosdep` database, therefor you need to install it manually either using `apt-get` or `pip` (on Ubuntu the package is called `python-bottle`).

```bash
$ cd /path/to/catkin_ws
$ git clone --recursive https://github.com/AutonomyLab/freeboard_ros.git src/freeboard_ros
# -r is to ignore rosdep error for python-bottle
$ rosdep install --from-paths src -i -r
$ catkin_make # or catkin build
```

## Usage

```bash
$ roslaunch rosbridge_server rosbridge_websocket.launch
$ rosrun freeboard_ros freeboard_ros.py _host:=HOST/LOCALIP _port:=3274 _debug:=True
```

Sample launch file:

```xml
<launch>
    <include file="$(find rosbridge_server)/launch/rosbridge_websocket.launch"/>
    <node pkg="freeboard_ros" name="freeboard_ros" type="freeboard_ros.py" output="screen">
        <param name="~host" value="192.168.1.52"/>
        <param name="~port" value="3274"/>
        <param name="~debug" value="True"/>
    </node>
</launch>
```

- Open `http://[HOST or LOCALIP]:3274/freeboard/` in your browser.
- Add a data source of type **ROS Subscriber**, type in the topic name, refresh rate and a preferred name for this source.
- The source will be available to use (as a JSON data structure) in any of `freeboard`'s widgets.
 
