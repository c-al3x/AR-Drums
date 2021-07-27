# AR_Drums 

A newly started application for an augmented reality drum kit!

We are currently in the very beginning stages of development.

## Installation 

Assuming git and pip are already installed on your machine, installing the AR Drums application involves only one line! Simply copy and paste the following line in your terminal:
```
git clone https://github.com/jm00n/AR_Drums.git && cd AR_Drums && pip3 install -r requirements.txt 
```

## Usage

### Running Application

Assuming you are in this project's root directory, simply enter the following in your terminal each time you would like to run the program:

` python3 src/ar_drums.py `

### Current Tips

Currently, for the best experience with the application, connect an external camera to your computer and place the camera IN FRONT of yourself or simply use your computer's internal webcam and place the computer IN FRONT of yourself. You can monitor your movements and the placements of the drums on your computer's screen, which should display a live video feed once the application starts running. Currently, aim for a setting that is not dark and has controlled lighting. The program tracks anything blue, so make sure to attach/place something blue near or at the tip of your drumsticks. This will allow for your drumsticks to be tracked. You may substitute drumsticks with something else (such as pencils/pens) as long as it has a speicifically blue tip/end that allows it to be tracked. Aim to have nothing else in the background that is blue (and try not to wear blue yourself). In order to play the drumkit along with the kick, you can sit on a chair with one leg up on the seat in which your foot on the seat has blue on it or near it in order to trigger the kick. (For instance, placing a pen with a blue tip/end in between two toes.) Yes, it is silly and unnatural, but currently, that is the best that can be done in order to use the whole kit at once. Try not to play anything quickly and try to keep the contour boxes that appear on your drumsticks and what not to be ones that don't have multiple boxes directly around them or inside them or very near them. This may cause a single drum hit to trigger multiple. Moving further away from the camera can fix this problem of too many contour boxes on drumsticks. 

### Drum Parts

* The red box triggers a snare drum sample.
* The yellow box triggers a hi-hat sample.
* The orange box triggers a ride cymbal sample.
* The pink box triggers a kick drum sample.

### Quitting the Application

If you would like to quit the application, simply press "q" on your keyboard. If that does not work, try clicking the live video feed itself and then press "q" again.  
 
