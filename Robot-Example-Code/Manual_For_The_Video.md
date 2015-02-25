
# Manual to go with the Video at vimeo: (https://vimeo.com/120392503)
1) Intro
2) Tools
3) Parts List
4) Assembly
###1) Intro
Hello Everyone! In this video, I will be showing you how to assemble your very own low cost robot. Just so you know, the DFRobot Mobile Platform Kit that this robot uses does have a general assembly manual which you can use as reference, but keep in mind that we will be making some modifications in assembly.
Note: There will be soldering involved but we will not cover how to solder. If you are new to soldering, there is a good amount of tutorials on how to properly solder on the internet.
###2) Tools
The following are the tools you will need:
1) A Philips screwdriver
2) Soldering iron with solder
3) Small flat-head screwdriver
4) Needle-nose pliers
5) Wire strippers
###3) Parts List
The following are the parts you will need:
1) DFRobot Romeo All-in-One Microcontroller
2) Fuselage Lower Plate
3) Fuselage Upper Plate
4) 2 Motors
5) 2 Wheels
6) Caster
7) Battery Holder
8) 2 Wheel Encoders
9) 2 Encoder Sensors
10) 4 Philips Truss Screws
11) 4 red M2.5 Washers
12) 4 Clear Spacers
13) 8 M3 Nut
14) 4 M2.5 Nut
15) 2 Philips Truss Screws
16) 2 M4 Nut
17) 2 Philips Countersunk Screws
18) 4 Philips Flange Screws
19) 2 Yellow Extensions
20) 2 Pointed Screws
21) 2 shielded cables containing two wires and ground
###4) Assembly
Now we are ready to put together our robot!
1) The first thing we will do would be to attach the black wheel encoders to the motors. Take a pointed screw and screw it into the center of the encoder.
2) Now take this and attach it into the inner plastic rod next to the motor
a. The encoders will move along with the rotation of the wheel. Do the same assembly on the other motor.
3) We will now attach the motor to the lower plate along with the encoder sensors.
a. Place the motor inside the lower plate . Ensure the two holes line up with the two holes on the plate.
b. Starting with the lower hole, put a Philips truss screw through it. On the screw, put the following things in order:
b.i. M3Nut, spacer, red M2.5 washer, encoder sensor ( make sure the wheel sits in the middle of the sensor), and finally add a M2.5 Nut to secure everything in place.
b.ii. This part is a bit tricky so it might take a while to get right. As you can see, it’s quite a struggle.
c. Got it all together? Wonderful. Now do the same for the top hole. It not as bad as before though so don’t worry.
d. Now we have both the top and bottom connection done. We are almost done, just do the same thing on the other side.
e. just to see how our motor system works, lets pop in a wheel
4) With both encoder sensors attached, we are now half way done with our assembly! The next thing we will do is pop on the wheels. You will notice that there are notches where the wheel connects. Just line them up with the motor and apply a little pressure to attach.
a. When you rotate your wheel, you’ll see the encoder move along with it. The encoder sensor senses the movement of the wheel and , if programmed correctly, communicates with the microcontroller how fast and far the robot has moved.
###5) Now let’s attach the caster to the lower plate. With the ball of the caster facing down, place the caster on top of the lower plate as shown. Now get the Philips Truss Screws and put them through the two holes. Now get two M4 nuts and secure the caster in place.
a. The caster acts as a third wheel for the robot.
###6) It’s time to attach the battery holder. Place the battery holder on top of the caster and line it up with the two holes shown. Take two Philips countersunk screws and attach them to the battery holder and secure them in with two M3 Nuts.
###7) It’s time to solder on the wires to the motor. While your soldering iron is heating up, Take your shielded cable and unravel it a bit on both ends. You will notice that your cable contains two covered wires and a bare strand of wire. The covered wires are what we will be attaching to the motor. The naked wire will be attached to ground.
a. On the back of your motor, you will notice two copper pieces with a hole in them. This is where you will be soldering your wire to.
b. Prep the wires by stripping both ends and twisting the threads of each wire.
c. Now get your soldering iron and solder the wires on.
d. while you are soldering the colored wire to the motor, tuck in the ground wire into the shielding. The other end of the ground wire will be attached to ground
###8) Ok so we are now finish with the setup for the lower plate. We will now attach the microcontroller to the upper plate.
a. You will notice that the top plate has a multitude of holes. On the micro controller, you will see that it has four holes, each near the corners. Try to find at least 2 holes opposite each other so that the board is stable
b. Take the yellow extensions and place them on the upper plate.
c. Now take the Philips Flange Screw and screw the microcontroller onto the yellow extension
d. Now take the M3 Nut and secure the yellow extension onto the upper plate.
e. It is important to make sure that the board is suspended above the plate as screwing the board directly on the upper plate can lead to a malfunctioning board. You need to protect the connections on the bottom of the board.
###9) Now it is time to attach the lower plate to the upper plate. There are many holes in the upper plate but if you look closely, you can see that 4 of them match up with the 4 holes on the lower plate.
a. Locate the corresponding screw holes on the upper plate to the lower one. Attach 4 philips flange screw to the plates.
b. Grab the motor wire and attach them to the corresponding M1 and M2 screw terminals on the board
c. Grab the battery wire and place them in the power clamp thing next to the M1 screw terminal
d. Grab the two encoder sensor wires and attach them to the digital pins area. Be sure to line them up according to the color. Keep note of which digital pin you put this on.
###10) We are finally done! You should now have a fully assembled robot. The next step is to do some testing using example code to ensure that the robot’s connections are all working. Happy tinkering!
Link to microcontroller manual : http://www.dfrobot.com/wiki/index.php?title=DFRduino_Romeo-All_in_one_Controller_V1.1%28SKU:DFR0004%29
assembly manual for the robot frame is here:
http://www.dfrobot.com/image/data/ROB0005/3PA%20InstructionManual%20V1.1.pdf
* When programming, be sure to set the board as an Arduino Uno
