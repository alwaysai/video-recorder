# Simple Video Recorder
This alwaysAI app records and saves video from a USB webcam or CSI ribbon camera.

## Setup
This app requires access to alwaysAI's Beta program. To sign up go to the [Sign up page](https://www.alwaysai.co/dashboard)

Once accepted to the program, follow the setup instructions located on the [Docs page](https://www.alwaysai.co/docs/getting_started/introduction.html) - Note this link is accessible only to beta users.

## Usage
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path

`aai app configure`

To build and deploy the docker image of the app to the target device

`aai app deploy`

The app has the following options:

```
$ aai app start -- --help
usage: app.py [-h] [--camera CAMERA] [--gstreamer]

Video Recorder

optional arguments:
  -h, --help       show this help message and exit
  --camera CAMERA  Set the camera index. (default: 0)
  --gstreamer      Use GStreamer for ribbon cameras
```

To start the app using the defaults:

`aai app start`

To capture video from camera index 1:

`aai app start -- --camera 1`

To capture video from a CSI ribbon camera:

`aai app start -- --gstreamer`

> Note that tha extra `--` in the above commands is used to indicate that the parameters that follow are to be passed through to the python app, rather than used by the CLI.

Once started, the app will begin recording a video.  The video will be saved when the app is shut down, either by the stop button on the Streamer or exiting with CTRL-C. The video feed will also be displayed on the Streamer.

The FPS is set to 30, but may need to be updated if the camera being used has a different FPS. Ideally, the recording FPS should match the camera FPS for videos to look natural.
