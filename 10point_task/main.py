import cv2

inp_dir = 'python_split_image_by_ch'
output_dir = 'python_split_image_by_ch/outp_dir'


def merge_channels(input_dir, output_dir):
    with open(input_dir + '/image_counter.txt', newline='') as length:
        count = int(length.readline())
    for i in range(count):
        num = str(i + 1).zfill(5)
        image = cv2.imread(input_dir + '/data' + f'/{num}_b.jpg')
        image2 = cv2.imread(input_dir + '/data' + f'/{num}_g.jpg')
        image3 = cv2.imread(input_dir + '/data' + f'/{num}_r.jpg')
        (B, Gg, Rr) = cv2.split(image)
        (Bb, G, Rrr) = cv2.split(image2)
        (Bbb, Ggg, R) = cv2.split(image3)
        bgr = cv2.merge((B, G, R))
        cv2.imwrite(output_dir + f'/{num}.jpg', bgr)


merge_channels(inp_dir, output_dir)
