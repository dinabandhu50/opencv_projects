# OpenCV Tutorials

This repo contains opencv python tutorials

# Lessons

1. Read and write image

    1. Do not use `cv2.imshow()` function for displaying images, It has lot of issues with it, it is frustrating.
    2. Use `matplotlib` for image displaying, but remember `cv2` has `BGR` image where as `plt` has `RGB` image:

        ```python
        img = cv2.imread('image_1.jpg',1)
        plt.figure()
        plt.imshow(cv2.cvtColor(
            img,
            cv2.COLOR_BGR2RGB))
        plt.show()
        ```

    3. This problem is mainly occuring because : I was using vscode for coding and I was using the right upper `RUN` button for running the python script. Do not use the green button at the right upper corner of vscode, use `python script.py` instead

2. Video read and write
    1. Use `cv2.imshow()` for video displaying purpose
