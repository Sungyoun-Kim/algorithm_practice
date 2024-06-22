def solution(brown, yellow):
    must_height_width_sum = (brown+4)//2
    avg_length = must_height_width_sum//2
    height =3
    width =must_height_width_sum-3

    #width greater than equal height!
    while True:
        yellow_area = (height-2) * (width -2)
        if yellow_area == yellow:
            return [width, height]
        else:
            height+=1
            width -=1
                