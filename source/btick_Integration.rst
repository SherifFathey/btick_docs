========================
BTick Integration
========================


The BTick integration uses ROS 2 communication to provide real-time Behavior Tree monitoring and interactive debugging for BehaviorTree.CPP v4 applications.

Overview & Capabilities
=======================

The integration connects BTick to the BehaviorTree.CPP execution and monitoring interfaces to expose tree structure, runtime state transitions, and supported debugging controls.

* **Automatic Tree Discovery**: Publishes tree structure, node hierarchy, and available port metadata.
* **Runtime State Monitoring**: Streams node status transitions, including ``IDLE``, ``RUNNING``, ``SUCCESS``, ``FAILURE``, and ``SKIPPED``.
* **Interactive Debugging**: Supports execution control through breakpoints and step-by-step ticking.
* **Fault and Delay Injection**: Supports testing selected execution scenarios using runtime debugging commands.
* **Live Blackboard Access**: Allows supported Blackboard variables to be inspected and modified during execution.

Prerequisites & Dependencies
============================

Ensure ROS 2 and the required BehaviorTree.CPP dependencies are installed.

Building the ``btick`` Package
------------------------------

Clone the repository into a ROS 2 workspace and build the package:

.. code-block:: bash

   mkdir -p ~/robot_ws/src
   cd ~/robot_ws/src
   git clone https://github.com/SherifFathey/btick.git


.. code-block:: bash

   cd ~/robot_ws
   rosdep install --from-paths src --ignore-src -r -y
   colcon build --packages-select btick --symlink-install
   source install/setup.bash

Package Configuration
=====================

CMakeLists.txt
--------------
Add ``btick`` to your project's dependencies:

.. code-block:: cmake

   cmake_minimum_required(VERSION 3.8)
   project(my_robot_behavior)

   find_package(ament_cmake REQUIRED)
   find_package(rclcpp REQUIRED)
   find_package(behaviortree_cpp REQUIRED)
   find_package(btick REQUIRED)

   add_executable(my_bt_runner src/my_bt_runner.cpp)
   ament_target_dependencies(my_bt_runner
     rclcpp
     behaviortree_cpp
     btick
   )

   install(TARGETS my_bt_runner
     DESTINATION lib/${PROJECT_NAME}
   )

package.xml
-----------
Declare dependencies in ``package.xml``:

.. code-block:: xml

   <depend>rclcpp</depend>
   <depend>behaviortree_cpp</depend>
   <depend>btick</depend>


C++ Integration Example: Adding BTick to ``main()``
===================================================

The following steps demonstrate how to integrate BTick into an existing BehaviorTree.CPP application.

Step 1: Include the BTick Header
--------------------------------

Include the BTick header in your C++ source file:

.. code-block:: cpp

   #include <btick/btick.hpp>

Step 2: Attach the BTick Monitor
--------------------------------

After creating your behavior tree, instantiate ``btick::Monitor`` to enable monitoring and supported debugging features in BTick.

.. code-block:: cpp

   btick::Monitor monitor(node, tree, "MainRobotTree", xml_path);

The constructor arguments are:

* ``node``: The ROS 2 node used for communication.
* ``tree``: The ``BT::Tree`` instance to monitor.
* ``"MainRobotTree"``: The tree name displayed in the BTick interface.
* ``xml_path``: The XML file path, used to retrieve tree definition details such as port metadata.

Step 3: Enable Optional Logging
-------------------------------

To record execution data to a JSON file, optionally create a ``btick::Logs`` instance:

.. code-block:: cpp

   btick::Logs logs(monitor, "/tmp/mission_log.json", true);

**Constructor Arguments:**


* ``monitor``: BTick monitor instance associated with the behavior tree.
* ``"/tmp/mission_log.json"``: Base path for the JSON log file.
* ``true``: Enables timestamp-based filenames, creating a new log file for each recording session.
* ``false``: Uses the same filename for each session instead of generating a timestamp-based filename.

Step 4: Complete BTick Integration
----------------------------------

The following example demonstrates how to integrate BTick into an existing ROS 2 application. It assumes that the required BehaviorTree.CPP node types have been registered and the XML file is available.

.. code-block:: cpp

   #include <string>
   #include <rclcpp/rclcpp.hpp>
   #include <behaviortree_cpp/bt_factory.h>
   #include <btick/btick.hpp>

   int main(int argc, char** argv)
   {
     rclcpp::init(argc, argv);
     auto node = rclcpp::Node::make_shared("my_robot_bt_runner");

     {
       // Register the required BehaviorTree.CPP node types.
       BT::BehaviorTreeFactory factory;
       // factory.registerNodeType<MyActionNode>("MyAction");

       // Create the behavior tree from its XML definition.
       const std::string xml_path = "/path/to/my_behavior_tree.xml";
       auto tree = factory.createTreeFromFile(xml_path);

       // Attach BTick monitoring and debugging.
       btick::Monitor monitor(node, tree, "MainRobotTree", xml_path);

       // Optional: Record execution data to a JSON file.
       btick::Logs logs(monitor, "/tmp/mission_log.json", true);

       // Execute the tree and process incoming ROS 2 commands.
       rclcpp::WallRate loop_rate(10);
       while (rclcpp::ok()) {
         tree.tickExactlyOnce();
         rclcpp::spin_some(node);
         loop_rate.sleep();
       }
     }  // Destroy logs and monitor before shutting down ROS 2.

     rclcpp::shutdown();
     return 0;
   }

The ROS 2 node must be spun so BTick can process incoming debugging commands. The ``btick::Logs`` instance is optional and can be omitted when execution recording is not required.


Working Example: Turtlesim BT
------------------------------

For a complete working example of BTick integrated with ROS 2 and BehaviorTree.CPP, see the `Turtlesim_BT repository <https://github.com/SherifFathey/Turtlesim_BT/tree/btick>`_, which includes a working integration of BTick for monitoring and debugging Behavior Trees.

Use this project as a practical reference for integrating BTick into your own ROS 2 applications.