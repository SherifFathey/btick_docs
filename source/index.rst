===========================================
BTick: Behavior Tree Visualizer & Debugger
===========================================

BTick is a real-time visualization, debugging, and authoring tool for
`BehaviorTree.CPP <https://github.com/BehaviorTree/BehaviorTree.CPP>`_ v4,
designed for robotics development and ROS 2 applications.

It provides a graphical interface for inspecting behavior tree execution,
understanding node states, debugging failures, and working with behavior tree
XML files. BTick can run as a Docker-based web application or as a native
Linux desktop application.


What is BTick?
==============

Behavior trees are widely used in autonomous robotics to coordinate tasks such
as mobile navigation, docking, manipulation, and recovery behaviors.

As behavior trees become more complex, understanding their runtime behavior
through terminal logs alone can be difficult. BTick provides a visual way to
inspect tree execution and investigate unexpected behavior.

.. raw:: html

   <video controls autoplay loop muted playsinline style="display: block; margin: 0 auto; max-width: 100%;">
      <source src="_static/gifs/input.mp4" type="video/mp4">
      BTick interface showing behavior tree execution and node states
   </video>


Key Features
==============

- **Automatic Tree Discovery & Multi-Tree Support**: Discover and monitor multiple Behavior Trees and nested subtrees in real time.
- **Real-Time Execution Monitoring**: Visualize node statuses and execution flow as they change.
- **Interactive Breakpoints & Step Execution**: Pause, resume, succeed, fail through execution, and inspect node states.
- **Fault Injection & Runtime Overrides**: Force node statuses(`SUCCESS`, `FAILURE`, `RUNNING`, `SKIPPED`) and inject delays to test failure scenarios.
- **Runtime Port Editing**: Modify supported node input ports during execution.
- **Live Blackboard Monitoring & Editing**: Inspect and modify blackboard variables at runtime.
- **Session Recording & Time-Travel Replay**: Record execution transitions and replay sessions using a timeline scrubber.
- **Standalone Session Logging & Export**: Save and load session logs for offline analysis and debugging.
- **Execution Timing & Performance Analysis**: Analyze execution timing to identify delays and potential bottlenecks.
- **Integrated Behavior Tree XML Editor**: Create, edit, and validate BehaviorTree.CPP v4 XML files visually.
- **Scalable Visualization & Navigation**: Navigate complex Behavior Trees with interactive panning and zooming.
- **Multi-Protocol Monitoring & Telemetry**: Support BTick, Groot2 Pro Features compatibility, and Nav2 logging.
- **Web & Desktop Applications**: Use BTick through web and desktop interfaces.

Getting Started
===============

Ready to use BTick? Start with :doc:`getting_started` to set up your
environment and connect to a behavior tree.

Documentation Contents
======================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started

.. toctree::
   :maxdepth: 2
   :caption: Concepts

   architecture
   protocol_comparison

.. toctree::
   :maxdepth: 2
   :caption: Application Guides

   monitor
   xml_editor

.. toctree::
   :maxdepth: 2
   :caption: Integrations

   btick_Integration