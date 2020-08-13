# Simple Video Recorder
This alwaysAI app records and saves video from a USB webcam or CSI ribbon camera.

## Setup
This app requires an alwaysAI account. Head to the [Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account yet. Follow the instructions to install the alwaysAI toolchain on your development machine.

Next, create an empty project to be used with this app. When you clone this repo, you can run `aai app configure` within the repo directory and your new project will appear in the list.

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
