import leap
import sys


class TradukiListener(leap.Listener):
    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()

        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
          frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

def main():
    listener = TradukiListener()
    controller = leap.Controller()

    controller.add_listener(listener)
    try:
        sys.stdin.readline()
    except:
        pass
    finally:
        controller.remove_listener(listener)

main()
