# 导入模块,应该将所有模块和常量放在此处统一导入，避免出现导入问题和命名问题
init -1 python:
    import time
    
    # 自定义着色器
    renpy.register_shader("example.gradient", variables="""
        uniform vec4 u_gradient_left;
        uniform vec4 u_gradient_right;
        uniform vec2 u_model_size;
        varying float v_gradient_done;
        attribute vec4 a_position;
        """, vertex_300="""
        v_gradient_done = a_position.x / u_model_size.x;
    """, fragment_300="""
        gl_FragColor *= mix(u_gradient_left, u_gradient_right, v_gradient_done);
    """)