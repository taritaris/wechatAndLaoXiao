import cv2
import mediapipe as mp
# 用来在图片中画出关键点
mp_drawing = mp.solutions.drawing_utils
# 关键点图样式
mp_drawing_styles = mp.solutions.drawing_styles
mpPose = mp.solutions.pose
pose = mpPose.Pose()

if __name__ == '__main__':

    file = '1.png'
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape

    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # mediapipe姿态检测只能检测一个人
    if results.pose_landmarks:
        for lm in results.pose_landmarks.landmark:
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)

    # 画关键点
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mpPose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imwrite('0.png', annotated_image)
