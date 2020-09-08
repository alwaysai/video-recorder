import time
import edgeiq
import argparse


def main(cam, record_fps, gstreamer):

    fps = edgeiq.FPS()

    try:

        capture_date = time.strftime('%Y-%m-%d')
        capture_time = time.strftime('%H:%M:%S')
        filename = "capture-{}-{}.avi".format(capture_date, capture_time)

        video_stream = None
        if gstreamer:
            video_stream = edgeiq.GStreamerVideoStream(cam=cam).start()
        else:
            video_stream = edgeiq.WebcamVideoStream(cam=cam).start()

        with edgeiq.VideoWriter(
                        output_path=filename, fps=record_fps) as video_writer, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()

            # loop detection
            while True:
                frame = video_stream.read()

                # Write frame to video
                video_writer.write_frame(frame)

                streamer.send_data(frame)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        if video_stream is not None:
            video_stream.stop()
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Video Recorder')
    parser.add_argument(
            '--camera', type=int, default=0,
            help='Set the camera index. (default: 0)')
    parser.add_argument(
            '--record-fps', type=int, default=30,
            help='Set the recording FPS. (default: 30)')
    parser.add_argument(
            '--gstreamer', action='store_true',
            help='Use GStreamer for ribbon cameras')

    args = parser.parse_args()

    if args.gstreamer:
        gstreamer = True
    else:
        gstreamer = False

    main(args.camera, args.record_fps, gstreamer)
