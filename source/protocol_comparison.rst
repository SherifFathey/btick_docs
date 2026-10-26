===================
Protocol Comparison
===================

BTick supports three integration methods for connecting to behavior trees: **BTick**, **Nav2**, and **Groot2**.

This page provides a centralized comparison of their supported capabilities, limitations, and runtime behavior.

Capability Comparison Matrix
============================

The three integration methods differ in how they discover behavior trees, receive execution updates, and interact with the running system.

.. list-table::
   :widths: 22 26 26 26
   :header-rows: 1

   * - Capability
     - BTick
     - Groot2
     - Nav2
   * - **Interaction Mode**
     - Interactive monitoring and control
     - Monitoring and breakpoint-based control
     - Passive, read-only monitoring
   * - **Tree Structure**
     - Automatically discovered through ROS 2 topics
     - Retrieved from the running tree through ZMQ
     - XML loaded manually and matched against Nav2 logs
   * - **Execution Updates**
     - Event-driven node transitions
     - Status polling and asynchronous ZMQ notifications
     - Node transitions published by Nav2
   * - **Breakpoints**
     - Supported
     - Supported
     - Not supported
   * - **Fault Injection**
     - Force ``SUCCESS``, ``FAILURE``, ``RUNNING`` (block tick), or ``SKIPPED``; supports delay injection.
     - Force ``SUCCESS`` or ``FAILURE`` through hook replacement.
     - Not supported.
   * - **Node Port Editing**
     - Live port updates supported
     - Not supported
     - Not supported
   * - **Status Reset Modes**
     - Configurable (**Current Tick** / **Parent Re-tick**)
     - Native Groot2 event stream
     - Native Nav2 event stream
   * - **Multiple Trees**
     - Multiple monitored trees, routed by ``tree_id``
     - One active tree per publisher connection; XML may contain multiple subtrees
     - Multiple loaded XML trees
   * - **Timing Data**
     - Transition durations reported by the bridge
     - Timing derived from recorded transitions
     - Duration unavailable in Nav2 logs
   * - **Session Recording**
     - UI session recording
     - UI session recording
     - UI session recording

The available controls depend on the integration method. Nav2 provides read-only telemetry, while BTick and Groot2 expose different sets of runtime debugging features.

Which One Should I Use?
=======================

- **Use BTick when:**

  * You are developing or maintaining a custom ROS 2 BehaviorTree.CPP application.
  * You need interactive debugging, including breakpoints, stepping, Blackboard variable updates, forced-status injection, or execution delays.
  * You want automatic tree discovery without manually loading XML files.

  Integration Guide: :doc:`btick_Integration`

- **Use Groot2 when:**

  * Your application already uses ``BT::Groot2Publisher``.
  * You need tree visualization, execution monitoring, breakpoint-based control, or forced-status injection through Groot2's debugging interface.
  * You want to monitor a BehaviorTree.CPP application through ZMQ.

- **Use Nav2 when:**

  * You are running Navigation2 (Nav2) on a mobile robot.
  * Passive monitoring of navigation states, recovery behaviors, and replanning activity meets your needs.

