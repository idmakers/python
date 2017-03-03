import multiprocessing
import cv2

queue_from_cam = multiprocessing.Queue()

def cam_loop(queue_from_cam):

    cap = cv2.VideoCapture(0)

    hello, img = cap.read()

    queue_from_cam.put(img)


cam_process = multiprocessing.Process(target=cam_loop,args=(queue_from_cam,))
cam_process.start()

while queue_from_cam.empty():
    pass


from_queue = queue_from_cam.get()

cv2.imwrite('temp.png', from_queue)
