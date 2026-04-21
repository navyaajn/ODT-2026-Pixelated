# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
Perfect Match 


## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Navyaa Jain | Fabrication/ Debugging | Technical Support| Hands-on building, soldering, assembly, troubleshooting hardware issues, identifying faults during integration, system integration, Snacks provider, emotional support, hypnosis code, Visruta and Navyaa code, video maker |
| Visruta Varma | Electronics / Coding / Circuit Design / Fabrication / Mechanics | Aesthetics | Circuit design, ESP32 programming, visual design decisions, translating concept into interactive output, crashout randomly |

## 1.3 Project Title
600 Pixels

## 1.4 One-Line Pitch
A dynamic LED wall that detects movement and lights up in real time, turning simple gestures into an engaging visual experience.

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This project is an interactive LED wall made using NeoPixel strips, an ultrasonic sensor, and a servo motor. The sensor scans horizontally by rotating on a servo and detects the position of a person or object in front of the wall. Based on this detection, corresponding sections of the LED strips light up, creating a direct visual response to movement. The installation is designed to be quick to engage with—people can simply walk by or wave their hand and immediately see the wall react.

The experience is playful and intriguing because it invites curiosity without demanding time or instructions. The moving sensor creates a sense of anticipation, and the real-time lighting response feels almost like the wall is “watching” or “tracking” you. Variations in lighting based on distance add a dynamic, almost disco-like effect, making it visually satisfying. The project combines hardware and software elements including an ESP32 microcontroller, NeoPixel LED strips, ultrasonic sensing, servo control, and power regulation using a buck converter.

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
- The experience is an interactive wall that responds to movement in real time. As a person walks past or waves their hand, a scanning sensor detects their position and lights up corresponding sections of LED strips, creating a dynamic visual trail that follows them.
- Curiosity first—because the wall appears to “notice” them. Then surprise and delight when their movement directly affects the lights. It should feel playful, slightly mysterious, and satisfying to control without needing instructions.'
- Because the output changes based on how they move. Users can experiment—move faster, slower, closer, farther—and see different lighting patterns. This variability, combined with the instant feedback, makes it engaging and replayable.

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
We are designing this project as if we are a small creative studio making a interactive experience for a mixed audience of classmates and exhibition visitors.

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Video / Interactive Installation | https://pin.it/6xYyJaCZk | The idea of a responsive light wall that reacts to human presence and creates an immediate visual connection |
| Video / Interactive Installation | (https://pin.it/6xYyJaCZk) | The scanning or tracking behaviour and how simple movement can be translated into engaging light patterns |

## 3.2 Original Twist
What makes your project original?

**Response:**  
Unlike typical LED walls that use cameras or fixed sensors, this project uses a single ultrasonic sensor mounted on a moving servo to scan space horizontally. This creates a more visible and mechanical interaction where users can actually see how the system is “searching” for them. The simplicity of using one moving sensor instead of multiple static inputs makes the interaction feel more intentional and slightly unexpected.

Additionally, the project focuses on quick engagement. It does not require instructions, controllers, or long interaction time. People can just walk by and instantly become part of the experience. The variation in lighting based on distance and position adds a dynamic, almost rhythmic visual effect, making it both interactive and visually appealing.

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
move in front of wall → sensor scans and detects position → corresponding LEDs light up → user changes movement → lights respond → press button → animated pixel art appears → interaction continues → repeat 

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? |Classmates, exhibition visitors, and anyone passing by the installation|
| Age range | 5+  |
| Solo or multiplayer | Both, one or multiple people can interact at the same time  |
| Expected duration of one round | 10–30 seconds, short and repeatable interactions |
| What should the player feel? | Curious, engaged, and entertained by the instant visual response |
| Is explanation required before use? | No, interaction is intuitive and can be understood by just observing |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** The player notices a wall with moving lights and a scanning sensor, which draws their attention.
2. **Start:** There is no formal start, the interaction begins as soon as they come near the wall.
3. **First Action:** The player moves their hand or body in front of the wall or presses one of the buttons.
4. **Main Interaction:** The player keeps moving to see how the lights follow them, or presses buttons to trigger different animated pixel visuals.
5. **System Response:** The sensor detects position and lights up corresponding LED sections, while button presses trigger animated pixel art on the wall.
6. **Win / Lose / End Condition:** There is no win or lose, the interaction naturally ends when the player walks away.
7. **Reset:** The system automatically resets when no movement is detected, ready for the next user.

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Rule 1]`NA

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [✅ ] Ultrasonic sensor correctly detects movement and position across the scanning range
- [✅ ] Servo motor smoothly scans left to right without failure
- [✅ ] LED strips light up accurately based on detected position
- [✅ ] System runs continuously without random flickering or power issues
- [✅ ] Interaction is immediate and responsive without noticeable delay

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
A small setup with 2–3 NeoPixel strips, one ultrasonic sensor mounted on a servo, and an ESP32 where movement is detected and corresponding LEDs light up. This version proves the core idea of motion-based light response.

## 5.3 Stretch Features
What features are nice to have but not essential?

- button-triggered animated pixel art modes
- Increasing number of LED strips for a larger and more detailed wall
- More complex lighting patterns based on speed and distance of movement

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [✅ ] Electronics-based
- [✅] Mechanical
- [✅] Sensor-based
- [ ] App-connected
- [✅ ] Motorized
- [ ] Sound-based
- [✅ ] Light-based
- [ ] Screen/UI-based
- [✅ ] Fabricated structure
- [ ] Game logic based
- [✅ ] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
The system takes input through an ultrasonic sensor that detects the distance and position of a person or object. This sensor is mounted on a servo motor, which continuously scans left to right to cover the full width of the wall.

The ESP32 processes this data by mapping the detected position to specific sections of the NeoPixel LED strips. Based on this, it decides which LEDs should light up and how they should behave.

The output is a visual response where the LED strips light up in real time, following the user’s movement and creating dynamic patterns.

Physically, the system consists of horizonatally arranged NeoPixel strips forming a wall, with the sensor and servo mounted at the top. Power is managed using a 12V adapter and a buck converter to safely supply the required voltage to the components.

There is no app interaction; the system works as a standalone installation.

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
- |Ultrasonic Sensor | Input | Detects distance and position of objects as it scans across the wall |
- |Push Buttons | Input | Triggers different animated pixel art patterns when pressed |'
- |Voltage Divider (Resistors) |Input Conditioning |Reduces echo pin voltage from the ultrasonic sensor to a safe level for the ESP32
- |ESP32 | Processing |Reads sensor and button inputs, maps position, and controls LED output and servo movement |
- |NeoPixel LED Strips | Output | Lights up corresponding sections and displays animations based on input |
- |Servo Motor | Output | Rotates the ultrasonic sensor left to right for continuous scanning |'
- |LM2596 Buck Regulator | Power Management | Steps down voltage from the power adapter to safely supply required voltage to LEDs     and components

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
<img width="750" height="1280" alt="image" src="https://github.com/user-attachments/assets/d6fc76b1-9955-4ccf-b8fc-ec2c70f358b9" />


Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
<img width="718" height="1280" alt="image" src="https://github.com/user-attachments/assets/a7e2f53f-be3a-426b-8e95-7ce8cb4622e8" />

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | NA |
| Width | 1meter |
| Height | 1/2 meter |
| Estimated weight |1-1.5kg |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [✅] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Write here]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
The ultrasonic sensor mounted on the servo motor moves horizontally from left to right.
The servo motor is controlled by the ESP32, which sends signals to rotate it continuously within a set angle range.
It sweeps approximately 0 to 180 degrees, covering the full width of the LED wall.'
It moves at a moderate, controlled speed so the sensor can accurately detect positions without skipping data
Servo jitter due to unstable power, incorrect angle calibration, loose mounting affecting accuracy, or delayed sensor readings causing mismatch between position and LED output.

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |
NA

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
NA
---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| ESP32 | 2 | Main controller for processing inputs and controlling outputs |
| NeoPixel LED Strips` | 10 | Visual output to display movement-based lighting  |
| Servo Motor | 1 |Rotates the ultrasonic sensor for scanning |
| Push Buttons | 2–3 | Triggers different animated pixel art modes |
| LM2596 Buck Regulator` | 1| Steps down voltage from power supply to safe levels` |
| Resistors (Voltage Divider) | 2 | Reduces echo pin voltage for ESP32 safety |
| 12V Power Adapter | 1 | Provides power to the system |
|Breadboard and Jumper Wires| Multiple| Circuit connections and prototyping

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
**Response:**
The ESP32 acts as the central controller, with all components connected to it and sharing a common ground. A 12V adapter supplies power, which is stepped down to 5V using an LM2596 buck regulator. This 5V line powers the servo motor, ultrasonic sensor, and all NeoPixel LED strips.

The servo motor is connected to GPIO 13 for signal control, allowing it to rotate and scan left to right. The ultrasonic sensor has its trigger pin connected to GPIO 5 and its echo pin connected to GPIO 18 through a voltage divider to reduce the signal to a safe level for the ESP32.

Five NeoPixel LED strips are connected to different GPIO pins: GPIO 23 for the top strip, GPIO 22 for the second strip, GPIO 21 for the middle strip, GPIO 19 for the fourth strip, and GPIO 25 for the bottom strip. All strips receive 5V power from the buck regulator and share a common ground.

Five push buttons are connected to GPIO pins 32, 33, 26, 27, and 14. Each button is connected between the GPIO pin and ground, using the ESP32’s internal pull-up resistors. These buttons are used to trigger different animation modes such as wave, heart, rings, text, and to return to the default radar mode.


## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
(https://app.cirkitdesigner.com/project/3e5981b6-d7fe-40d7-a713-8aec581a3cb6)
<img width="3000" height="2730" alt="circuit_image" src="https://github.com/user-attachments/assets/5afd9705-92ab-43c4-a8c1-e9bf3197bbd1" />


## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | 12V AC-DC adapter|
| Voltage required | 5V (stepped down using LM2596 buck regulator)|
| Current concerns |High current draw from multiple NeoPixel strips, required proper distribution and limiting number of strips to avoid instability |
| Safety concerns | Risk of overheating, voltage mismatch, or damaging ESP32 if voltage is not stepped down properly, ensured common ground and correct voltage regulation |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| MicroPython Thonny IDE	 | Programming the ESP32 to control sensor input, servo movement, and LED output Writing, uploading, and debugging MicroPython code on the ESP32 |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
Startup behavior:
On startup, the ESP32 initializes the servo, ultrasonic sensor, NeoPixel strips, and buttons. The servo begins scanning left to right.

Input handling:
The system takes input from the ultrasonic sensor for movement and from buttons for triggering animations.

Sensor reading:
The ultrasonic sensor continuously measures distance as it scans across the wall.

Decision logic:
The code maps the detected position to specific LED sections. If a button is pressed, it overrides the sensor mode and switches to animation mode.

Output behavior:
In default mode, LEDs light up based on position. In button mode, predefined pixel art or patterns are displayed for exactly 10 seconds.

Communication logic:
All components are directly controlled by the ESP32 using GPIO pins. No external communication or app is used.

Reset behavior:
After 10 seconds or a button press, the system returns to the default sensor-based interaction mode automatically.


## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1440" height="2840" alt="image" src="https://github.com/user-attachments/assets/f7e7f6bb-928d-4310-a25d-8514463e6a2b" />


## 10.4 Pseudocode

```START

INITIALIZE:
    set animation durations (10s, 15s for text)
    configure buttons as input with pull-up
    configure servo on GPIO 13
    configure ultrasonic sensor (TRIG = GPIO 5, ECHO = GPIO 18)
    configure 5 NeoPixel strips on GPIO 23, 22, 21, 19, 25
    set initial mode = radar
    set servo angle range and direction
    set frame counters and timers

LOOP FOREVER:

    READ button states

    IF wave button pressed:
        set mode = wave
        set mode end time = current time + 10s

    IF heart button pressed:
        set mode = heart
        set mode end time = current time + 10s

    IF rings button pressed:
        set mode = rings
        set mode end time = current time + 10s

    IF text button pressed:
        set mode = text
        set mode end time = current time + 15s

    IF stop button pressed:
        set mode = radar

    UPDATE previous button states

    IF mode is not radar AND current time > mode end:
        set mode = radar

    --------------------------------------------------

    IF mode == radar:
        move servo to current angle
        measure distance using ultrasonic sensor

        DETERMINE active LED strips based on distance:
            far → middle strip
            medium → 3 middle strips
            near → all strips

        UPDATE LED intensity smoothly

        CALCULATE LED position based on servo angle

        DRAW radar effect:
            front trail (bright)
            back trail (dim)
            color gradient along strip

        WRITE LED data

        UPDATE servo angle:
            move forward until max angle
            reverse direction at limits

        WAIT small delay

    --------------------------------------------------

    ELSE IF mode == wave:
        FOR each LED in each strip:
            calculate sine wave brightness
            assign blue color intensity
        display LEDs
        increment frame
        WAIT small delay

    --------------------------------------------------

    ELSE IF mode == heart:
        calculate color shift over time
        map heart pattern onto LED grid
        apply center brightness fade
        display LEDs
        increment time variable
        WAIT small delay

    --------------------------------------------------

    ELSE IF mode == rings:
        fade previous LED values
        calculate distance from center for each LED
        generate circular wave pattern
        accumulate brightness
        display LEDs
        increment frame
        WAIT small delay

    --------------------------------------------------

    ELSE IF mode == text:
        clear LEDs
        render scrolling text across strips
        move text position left
        reset when off screen
        display LEDs
        WAIT small delay

END LOOP
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [✅] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup NA
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| ESP32 | 2 | Yes (1) | Yes (1) | 400 | WiFi + Bluetooth microcontroller | One for use, one as backup in case of damage |
| NeoPixel LED Strip | 15 meters | No | Yes | 1650 | WS2812B addressable LEDs | Main visual output, individually controllable LEDs` |
| LM2596 Buck Regulator | 2 | No | Yes | 100 | DC-DC step down converter | To convert 12V to stable 5V, one extra for backup |
| Servo Motor |3 | Yes (1) | Yes (2) | 100 | `Standard 180° servo | One for use, extras in case of failure |
| Ultrasonic Sensor | 2 | yes | bo | 0 | HC-SR04` |For distance and position detection |
| Push Buttons | 2–3 | Yes | No | 0 |Standard tactile switches | To trigger animation modes |
| Jumper Wires | 100 | yes | yes | 400 | Male-to-male / male-to-female | For prototyping and connections |
| Red & Black Wires | 2 meters | yes | yes | 200 | Copper wires` | For stable power distribution |
| 12V Power Adapter | 1 | Yes | No | NA | AC-DC adapter | Main power supply |
| Resistors | 2 | Yes` | No | 0 | For voltage divider | To step down echo pin voltage safely |
| Foam Board | 1meter in lengh and 10mm x 15 | No | YES | 0 | Lightweight board | Structure support for LED wall |
| Black Paper | ebiugh to cover the board | No | YES | 250-300 | Matte sheet |Improves visual depth and contrast |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
NeoPixel LED strips were chosen because they are individually addressable, making it easy to control specific sections and create dynamic patterns. An ESP32 was used as it has enough GPIO pins and processing capability to handle multiple components together.

A servo motor was selected instead of a DC motor because it allows controlled angular movement, which is needed for accurate left-to-right scanning of the sensor. The ultrasonic sensor was used as a simple and cost-effective way to detect distance without needing complex camera systems.

The LM2596 buck regulator was necessary to safely step down 12V to 5V, since the LED strips require stable voltage and higher current. A voltage divider was used to protect the ESP32 from higher voltage signals coming from the sensor.

Foam board was chosen for the structure because it is lightweight, easy to cut, and stable enough to hold the LED strips. Black paper was added to improve the visual effect by increasing contrast and making the lights stand out more.

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| ESP32 | Main controller and backup unit | NA | 15TH APR |Received |
| LM2596 Buck Regulator | Step down voltage from 12V to 5V | Not applicable | Received |
| Wires (Jumper + Red/Black) | Connections and power distribution | NA | Already procured |
| NeoPixel LED Strips | Main visual output for the wall | NA |Already procured | 
| Servo Motors | To rotate ultrasonic sensor | NA |Already procured | 

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics (ESP32, NeoPixel strips, LM2596 buck regulator, ultrasonic sensor)| 2325 |
| Mechanical parts (servo motors) | 150 |
| Fabrication materials (foam board, black paper) | 200 |
| Purchased extras (wires, jumper wires, resistors) | 200 |
| Contingency (extra components / replacements)| 200 |
| **Total** | 3075 |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
Costs can be reduced by borrowing components like the ultrasonic sensor, buttons, servo motors, and wires instead of purchasing them. The number of NeoPixel strips can also be reduced to make a smaller version of the installation while still maintaining the core interaction.

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
Tasks are divided based on strengths. Visruta handles coding and circuit design, while Navyaa supports with debugging, coding help, and managing logistics like components and setup.

Decisions are usually mutual. If there is a disagreement, both approaches are tested and the one that works better, looks better, or fits the system more efficiently is chosen.

Progress is tracked using a basic timetable based on daily goals. Tasks are planned according to what needs to be completed by a certain time and this is generally followed.

If a task is delayed, it is usually completed the same day even if it requires working late. If progress stops due to confusion or technical issues, external help is taken before continuing.

Documentation is maintained alongside the build. While Visruta works on final coding and adjustments, Navyaa updates the repository and later handles documentation visuals like photos and videos.

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | Finalize concept | Navyaa & Visruta | 2–3 | 7 April |None |Completed |
| T2 | Complete BOM | Navyaa & Visruta  | 5-6 | 15 April | T1 |Completed |
| T3 | Test electronics | Navyaa & Visruta | 2-3 | 13–14 April | `T1| Completed|
| T4 | Build structure | Navyaa | 1 | 14 April | T1 |Completed |
| T5 | Write control code | Visruta | 4 |14 April| T3 | Completed |
| T6 | Integrate system | `Navyaa & Visruta | 5-6 | 16–17 April | T4, T5 | Completed|
| T7 | Playtest` | Navyaa & Visruta | 2 | 19–20 April | T6 | Completed |
| T8 |Refine and document | Navyaa & Visruta | 3 | 20 April | T7 |Completed |



## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | Navyaa |Visruta |
| Electronics | Visruta | Navyaa |
| Coding | Visruta | Navyaa |
| App NA
| Mechanical build NA
| Testing | Visruta |Navyaa |
| Documentation | Navyaa | Visruta |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [✅ ] Idea finalized
- [ ✅] Core interaction decided
- [✅ ] Sketches made
- [✅ ] BOM completed
- [✅ ] Purchase needs identified
- ✅[ ] Key uncertainty identified
- [ ✅] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [✅ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ✅] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ✅] Physical body built
- [ ✅] Electronics integrated
- [✅ ] Code connected to hardware
- [ ] App connected if required
- [✅ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- ✅[ ] Technical bugs reduced
- [ ✅] Playtesting completed
- [ ✅] Improvements made
- [✅ ] Documentation completed
- [ ✅] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 |Finalize concept and basic idea |Concept was finalized quickly and direction was clear | `Decided to go with interactive LED wall instead of a game |Start gathering components and plan electronics |
| Week 2 | Complete BOM and test basic electronics | BOM completed, servo and ultrasonic sensor tested after multiple issues | Faced problems with power and sensor understanding, added voltage divider | Build small prototype with LED strips |
| Week 3 |Build structure and develop code` | Structure built and initial code written, small prototype worked |Faced mapping issues with LED strips and coding errors, fixed through iteration| Scale up to full installation |
| Week 4 | Integrate full system and test | Full system built, major issues with power and LED behavior, reduced to 10 strips |Changed approach to fewer strips for stability | Final testing, refinement, and documentation |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| Servo malfunction or jitter | Technical | High | High | Use stable power supply, keep backup servo, test before integration` | Navyaa |
| LED strips flickering or not working properly | Technical | High | High | Proper power distribution using buck regulator, limit number of strips, test in smaller batches | Visruta |
| ESP32 getting damaged due to voltage issues | Technical` | `Medium | High | Use voltage divider, correct wiring, keep backup ESP32 | Navyaa |
| Loose wiring or connection failures | Material | High | Medium | Secure connections, use proper wires instead of only jumper wires | Visruta |


## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
The biggest uncertainty is power stability. There is a risk that components may get damaged or the system may not run consistently because the power supply may not be sufficient for all the LED strips and components together.

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
|Servo movement |Run servo sweep repeatedly and observe motion` | Smooth left to right movement without jitter or stopping |
| Sensor behavior | Place objects at different positions and distances | Correct detection and mapping to LED sections |
|LED strip behavior | Test strips in small groups and then combined setup | LEDs light correctly without flickering or random colors` |
| Power stability | Run full system for extended time | No overheating, no component failure, stable lighting output |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? |Observe first-time users and see if they start interacting without instructions |
| Is the interaction satisfying? | Ask users for quick feedback and watch their reactions while using it |
| Do players want another turn? |See if users repeat the interaction or call others to try it |
| Is the challenge balanced? | NA |
| Is the response clear and immediate? | Observe if users notice instant LED response to their movement without confusion |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
|13TH APRIL | Servo motors were not working properly due to frayed parts |Technical | Replaced with new servo motors | Worked | Continue testing with new components |
| 13 April | Ultrasonic sensor not giving readings when powered from breadboard | Technical | Tried different power sources, then used ESP32 Vin with voltage divider after guidance| Worked |Verify stable readings before integration |
| 14 apr` | Initial LED strip mapping was incorrect (wrong orientation) | Technical | Corrected code and recalculated LED positions| Worked| Test with small prototype again|
| 14th apr | LED strips behaving as one continuous strip instead of separate sections | Technical | Modified code logic to handle strips correctly | Partly | Further refine mapping logic |
| 17th apr | LEDs flickering and showing random colors when all strips connected | Technical | Checked wiring, power distribution, and consulted for explanation| Failed | Simplify setup and test in smaller batches |
| 18th apr | System unstable with full number of LED strips | Technical |Tried different ESP32, rechecked connections | Failed | Reduce number of strips |
| 18th apr| New ESP32 not working properly | Technical | Tested with peers and confirmed it was faulty | Worked (diagnosis) | Switch back to original ESP32 |
| 18th apr |Power issues when connecting more than 10 strips | Technical | Gradually added strips (2, 4, 6, 10) and tested | Partly | Limit system to 10 strips |
| 18th apr | General instability due to wiring and power distribution | Technical | Rebuilt connections multiple times and improved wiring approach | Worked | Final testing with stable setup |
| 19th apr | Buttons not working properly on same ESP32 setup | Technical | Added second ESP32 and connected both together | Failed (second ESP32 got damaged) | Return to single ESP32 with safer wiring |


## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| Ashitha | Moved in front of the wall and tried interacting with lights | Could not understand where the sensor was and how tracking works` | `[Action]` |
| Anish |Observed the installation and explored the interaction | Was unsure what the buttons do | `Felt the project had potential and said more could be done with it | Make button functions clearer and expand the interaction possibilities` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
The structure was made using foam board as the base because it is lightweight and easy to work with. The foam board was cut to the required size to form the wall. Black sheets were then added on top to improve the visual depth and make the LED lights stand out more clearly.

The NeoPixel strips were measured, cut, and arranged vertically on the board. They were fixed in place and then wired together carefully using jumper wires and additional red and black wires for power distribution.

The ultrasonic sensor was mounted on a servo at the top of the structure, ensuring it could scan across the full width. All components were connected to the ESP32, and wiring was adjusted multiple times during testing to fix issues with power and signal stability.

Several revisions were made during the build, especially in wiring and number of LED strips, to achieve a stable and working system.


## 17.2 Build Photos
Add photos throughout the project.
https://github.com/navyaajn/ODT2026-ProjectManagementTemplate/tree/23a3ffe67f0e991c4241778473b0247e3c42e48d/images


Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:



## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | 13–14 April | Initial working prototype with servo, ultrasonic sensor, and small number of LED strips | To test core idea and basic interaction` |
| `v2` | 17–18 April | Attempted full-scale setup with all LED strips, multiple wiring changes, and power adjustments |To scale up installation and achieve full wall effect |
| `v3` | 18–19 April | Reduced to 10 LED strips, fixed wiring, added voltage divider, stabilized system, attempted button integration | To ensure stable performance after failures with full setup |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
The final project is an interactive LED wall made using 10 NeoPixel strips arranged vertically on a foam board structure. An ultrasonic sensor mounted on a servo scans left to right and detects movement in front of the wall. Based on this, corresponding sections of the LED strips light up in real time, creating a responsive visual effect.

The system also includes buttons that trigger animated pixel art patterns for exactly 10 seconds, after which the system returns to the default motion-based interaction. The setup runs using an ESP32 with proper power management through a buck regulator and stable wiring.

## 18.2 What Works Well
Real-time motion tracking and LED response feels immediate and engaging
Stable performance with 10 LED strips after resolving power issues
Button-triggered animations add variation to the interaction

## 18.3 What Still Needs Improvement
Power system can be improved to support more LED strips
Sensor tracking can be more precise and smoother
Better finishing and cleaner wiring for a more polished look

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
The final project is an interactive LED wall made using 10 NeoPixel strips arranged vertically on a foam board structure. An ultrasonic sensor mounted on a servo scans left to right and detects movement in front of the wall. Based on this, corresponding sections of the LED strips light up in real time, creating a responsive visual effect. The system also includes buttons that trigger animated pixel art patterns for exactly 10 seconds, after which it returns to the default motion-based interaction. The setup runs using an ESP32 with power managed through a buck regulator and stable wiring.

What works well is that the motion tracking and LED response feel immediate and engaging. The system is stable with 10 LED strips after resolving earlier power issues. The button-triggered animations also add variation and make the interaction more interesting.

What still needs improvement is the power system, which currently limits the number of LED strips. The sensor tracking can be smoother and more accurate, and the overall finishing, especially wiring, can be cleaner for a more polished output.

Compared to the original plan, the project was scaled down from 15 LED strips to 10 due to power and stability issues. There were multiple changes in wiring, power distribution, and components to make the system work reliably. The button-based interaction was also added later to enhance the experience, which was not part of the initial idea.


## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
We learned that electronics requires a clear understanding of basics like voltage, current, and power, and we often had to apply 12th grade physics concepts while working on this project. It is important to always double check voltage and current before connecting components, as small mistakes can damage parts.

In coding, we learned how to map sensor input to outputs and handle multiple components together, along with debugging logic when things do not work as expected.

For mechanisms, we understood how to control precise movement using a servo and how physical positioning affects sensor accuracy.

In fabrication, we learned how to build a stable structure using simple materials and how proper placement of components affects the final result.

In integration, the biggest learning was that combining everything is the hardest part. Power distribution, wiring, and coordination between components need careful planning. We also learned to always keep spare components and handle everything carefully to avoid failures.


## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
This project helped us understand that designing for play is more about creating something that invites interaction naturally rather than forcing it. The wall works because people can just walk by and it responds, which makes it easy to approach without instructions. That simplicity is what creates curiosity and pulls people in.

We also learned that delight comes from immediate feedback. When the lights react instantly to movement, it feels satisfying and keeps people engaged. Small additions like changing patterns or animations make a big difference in keeping the experience interesting.

Clarity is important, especially in interactive systems. If users do not understand what is happening, they lose interest. We saw this when people were confused about where the sensor was or what the buttons did, which showed us that making interactions more visible or intuitive is important.

Physical interaction plays a big role because the experience depends on how people move. Different movements create different outputs, which makes it feel more personal and interactive.

Player understanding comes from observation more than explanation. If someone else uses it and understands it quickly, the design works. If not, something needs to be improved.

Iteration was the biggest part of the process. Almost nothing worked perfectly the first time. We had to keep testing, failing, and changing both the technical setup and the interaction design until it started working properly.

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
With more time, we would improve the power system to support more LED strips and scale the installation closer to the original plan. We would also explore adding simple games and interactive modes, since people suggested ideas like turning it into something similar to slither.io or Mario Kart style visuals.

Additionally, we would experiment with using the wall for different simulations, like a fireplace effect or other ambient visuals, to expand how it can be used beyond just interaction.

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [✅ ] Team details are complete
- [ ✅] Project description is complete
- [ ✅] Inspiration sources are included
- [✅ ] Player journey is written
- [✅ ] Sketches are added
- [✅ ] BOM is complete
- [✅ ] Purchase list is complete
- [✅ ] Budget summary is complete
- [ ✅] Mechanical planning is documented if applicable
- [ ✅] App planning is documented if applicable
- [✅ ] Code flowchart is added
- [✅ ] Task breakdown is complete
- [✅ ] Weekly logs are updated
- [✅ ] Risk register is complete
- [✅ ] Testing log is updated
- [✅ ] Playtesting notes are included
- [✅ ] Build photos are included
- [✅ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
