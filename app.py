import time
import edgeiq


def main():

    fps = edgeiq.FPS()

    try:

        capture_date = time.strftime('%Y-%m-%d')
        capture_time = time.strftime('%H:%M:%S')
        filename = "capture-{}-{}.avi".format(capture_date, capture_time)

        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.VideoWriter(output_path=filename) as video_writer, \
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
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
