init:
    transform leftcenter:
        anchor (0.5,0.5)
        pos (0.25,0.5)

    transform rightcenter:
        anchor (0.5,0.5)
        pos (0.75,0.5)

    transform ppm_left:
        anchor (0.5,0.5)
        pos (0.5,0.6)
        zoom 1.5

    transform bzoomout:
        linear 1.0 zoom 1.0

    transform movetop_zoomout:
        parallel:
            linear 2.0 ypos 0.75
            linear 2.0 zoom 1.5

    transform xshake:
        ease 0.1 xoffset 20
        ease 0.2 xoffset -20
        ease 0.1 xoffset 0
        repeat 2

    transform yshake:
        ease 0.1 yoffset 20
        ease 0.2 yoffset -20
        ease 0.1 yoffset 0
        repeat 2



    transform half:
        zoom 0.5
    transform two:
        yalign 0.4
        zoom 2.0

    transform alpha_down:
        linear 1.0 alpha 0.75

    transform alpha_up:
        linear 1.0 alpha 1.0

    transform alpha_shake:
        linear 0.2 alpha 0.8
        linear 0.2 alpha 1.0
        repeat 2

    transform in_out_half:
        xanchor 1.0
        easein 3.0 xpos 0.0
        pause 1.0
        easeout 1.0 xpos 125

    transform ball_h:
        pos (0.75,0.4)
        zoom 0.25
    transform ball_move:
        linear 1.0 xpos 0.47
    transform hug:
        linear 1.0 zoom 2.0
    transform leave:
        linear 1.0 zoom 1.0

    transform h_move:
        parallel:
            linear 1.0 pos (0.5,0.5)
            easein 1.0 zoom 1.25

    transform scroll:
        yalign 0.0
        linear 10.0 yalign 1.0
    
    transform to_left (delay_time):
        time delay_time
        linear 1.0 xalign 0.2

    # 下列几种变换只是实验用途
    # 色彩渐变
    transform gradient:
        shader "example.gradient"
        u_gradient_left (1.0, 0.0, 0.0, 1.0)
        u_gradient_right (0.0, 0.0, 1.0, 1.0)
    # 改变亮度
    transform brightness(bright = -0.7):
        matrixcolor BrightnessMatrix(bright)
    # 亮度闪烁r次
    transform twinkle(speed=0.2, r=3):
        matrixcolor BrightnessMatrix(-0.2)
        linear speed matrixcolor BrightnessMatrix(0.2)
        repeat r