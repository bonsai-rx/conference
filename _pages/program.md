---
layout: page
title:  Program
permalink: /program/
---

|             | Monday                       | Tuesday           | Wednesday              |
|:-----------:|:----------------------------:|:-----------------:|:----------------------:|
| 09:00-10:45 | [Present and Future of Bonsai](#present-and-future-of-bonsai) | [Machine Learning and Quantifying Behavior](#machine-learning-and-quantifying-behavior) | [Hardware: Harp](#hardware-harp) |
| 11:00-12:45 | [Posters and Show-and-Tell](#posters-and-show-and-tell) | [Immersive Environments](#immersive-environments) | [Hardware: ONIX](#hardware-onix) |
| 12:45-14:00 | Lunch                        | Lunch             | Lunch                  |
| 14:00-16:00 | [Task Control and Reproducible Research Practices](#task-control-and-reproducible-research-practices) | [Developing Bonsai with AI](#developing-bonsai-with-ai) | [Hackathon](#hackathon) |

#### Present and Future of Bonsai

**Abstract**: Bonsai has become a powerful platform for real-time data acquisition and closed-loop experimentation, widely used in neuroscience and other scientific domains. We will open the Bonsai Developer Conference by presenting the most recent developments in the language, visual editor, and package ecosystem, including the redesigned editor navigation and package manager introduced in Bonsai 2.9, and share the roadmap toward Bonsai 3, from a modern .NET runtime to a cross-platform editor. We will also discuss how the project is governed: how changes to the language and ecosystem are proposed and decided, how packages are distributed and signed, and the role of the Bonsai Foundation in supporting a growing community of contributors.
<br>
<br>

#### Posters and Show-and-Tell

**Abstract**: One of the main goals of the Bonsai Developer Conference is to promote collaborations and sharing across the Bonsai community. This session opens the floor to everyone attending, with posters and live demonstrations of workflows, packages, devices, and experiments built with Bonsai. Placing it early in the program gives everyone a chance to meet and find common interests that can carry over into the discussions of the following days. We strongly encourage anyone participating in the conference to propose a poster or demonstration in the registration form.
<br>
<br>

#### Task Control and Reproducible Research Practices

**Abstract**: Bonsai is increasingly used not only to acquire data but to specify the logic of complex experiments. In this session we will survey workflow patterns for flexible and parameterizable task control, where task structures and rig configurations are specified in external configuration files and schemas instead of being fixed inside workflows. We will show how code generation tools such as Bonsai.Sgen turn these schemas into typed configuration and metadata for both Bonsai workflows and Python analysis, and how experimental metadata, provenance, and standard data formats can be recorded alongside acquisition so that data can be accessed and explored as soon as it is collected. We will finish with a discussion of current limitations and best practices for reproducible research with Bonsai.
<br>
<br>

#### Machine Learning and Quantifying Behavior

**Abstract**: The potential for closed-loop experiments in neuroscience is most limited by our ability to measure the behavior of interest in real time. In this session we will bring together the growing options for online machine learning and computer vision in Bonsai, from pose estimation with SLEAP, DeepLabCut, and MediaPipe, to emerging work on synchronized multi-camera rigs and real-time 3D pose tracking. We will also present new developments in the Bonsai.ML package, including the integration of deep learning models through TorchSharp and online methods such as linear dynamical systems and neural decoding, and discuss how models trained offline can be deployed and adapted in live experiments.
<br>
<br>

#### Immersive Environments

**Abstract**: Real-time closed-loop immersive environments are fundamental for next-generation understanding of brain function and behavior, and also one of the most fun ways to learn reactive programming. In this session we will discuss how to create immersive environments in Bonsai, from interactive visual stimuli and virtual reality displays with BonVision, to multichannel spatial audio with the new Bonsai.Mixer package and interactive control panels with Bonsai.ImGui. We will also discuss how to couple rendering to real-time tracking and experimental hardware, and how to measure and minimize end-to-end latency in closed-loop stimulus presentation.
<br>
<br>

#### Developing Bonsai with AI

**Abstract**: AI coding assistants have made it easier than ever to write new Bonsai operators, packages, and workflows, but code that is quick to produce is not necessarily easy to review, maintain, or trust. In this session we will discuss how to use these tools productively in Bonsai development, and how project templates, continuous integration, documentation, and shared repository standards can keep the results consistent and maintainable. We will also look at how a headless editor and command-line tools open Bonsai to automation, and at the role of AI tools in teaching and learning Bonsai. The discussion leads directly into the hackathon on the following day.
<br>
<br>

#### Hardware: Harp

**Abstract**: Harp is an open standard for hardware-timestamped data acquisition and experimental control, designed from the outset to interface with Bonsai. In this session we will present the current state of the Harp ecosystem: the first tagged release of the specification and progress toward Harp 2.0, firmware cores for both ATxmega and RP2040 microcontrollers, and a growing family of devices developed across institutions. We will demonstrate the new command-line toolkit for checking a device against the specification, updating firmware, and generating firmware, Bonsai, and Python interfaces from a single device description, together with the Harp Python packages for reading recorded data. We will finish with a discussion of how the standard is evolving and how new devices and contributors can join.
<br>
<br>

#### Hardware: ONIX

**Abstract**: ONIX is an open-source acquisition platform from Open Ephys for electrophysiology and other neural recordings in freely moving animals, integrated with Bonsai through the OpenEphys.Onix1 package. In this session we will present recent developments, including support for Neuropixels 2.0 probes, probe configuration through standard ProbeInterface files, efficient logging of acquisition data to Apache Arrow, and new tools for visualizing probe data in real time. We will also cover related hardware such as Miniscopes and commutators, and how ONIX and Harp devices can be combined and synchronized in the same experiment.
<br>
<br>

#### Hackathon

**Abstract**: We will close the conference with a hackathon in the Teaching Lab. Bring a problem, a workflow, a device, or an idea for a new package, and work on it together with other participants and the Bonsai developers. There will be no talks. The afternoon is entirely for building, fixing, and learning from each other.
