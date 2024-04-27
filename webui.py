# -*- encoding: utf-8 -*-
# 导入streamlit库，用于创建Web界面
import streamlit as st
# 从webui_pages包的utils模块导入工具函数
from webui_pages.utils import *
# 导入streamlit_option_menu，用于创建带图标的下拉菜单
from streamlit_option_menu import option_menu
# 从webui_pages.dialogue模块导入对话页面函数
from webui_pages.dialogue.dialogue import dialogue_page, chat_box
# 从webui_pages.knowledge_base模块导入知识库页面函数
from webui_pages.knowledge_base.knowledge_base import knowledge_base_page
# 导入os模块，用于操作文件和目录
import os
# 导入sys模块，用于访问与Python解释器相关的参数和函数
import sys
# 从configs模块导入版本信息
from configs import VERSION
# 从server.utils模块导入api_address函数，用于获取API地址
from server.utils import api_address
# 创建一个ApiRequest类的实例，用于发起API请求
api = ApiRequest(base_url=api_address())

# 检查是否以lite模式运行
if __name__ == "__main__":
    is_lite = "lite" in sys.argv

    # 设置页面配置，包括页面标题、图标、侧边栏初始状态和菜单项
    st.set_page_config(
        "Langchain-Chatchat WebUI",  # 页面标题
        os.path.join("img", "chatchat_icon_blue_square_v2.png"),  # 页面图标
        initial_sidebar_state="expanded",  # 侧边栏初始状态为展开
        menu_items={  # 菜单项配置
            'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',  # 获取帮助链接
            'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",  # 报告错误链接
            'About': f"欢迎使用 Langchain-Chatchat WebUI {VERSION}！"  # 关于信息，显示版本号
        }
    )

    # 定义页面字典，包含页面名称、图标和对应的页面函数
    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_page,
        },
        "知识库管理": {
            "icon": "hdd-stack",
            "func": knowledge_base_page,
        },
    }

    # 使用with语句进入侧边栏的上下文管理器
    with st.sidebar:
        # 在侧边栏显示logo图片
        st.image(
            os.path.join("img", "logo-long-chatchat-trans-v2.png"),
            use_column_width=True
        )
        # 在侧边栏显示版本信息
        st.caption(
            f"<p align=\"right\">当前版本：{VERSION}</p>",
            unsafe_allow_html=True,
        )
        # 获取页面名称列表和图标列表
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        # 设置默认选中的页面索引
        default_index = 0

        # 使用option_menu函数创建带图标的下拉菜单，选择页面
        selected_page = option_menu(
            "",  # 菜单标题
            options=options,  # 页面选项
            icons=icons,  # 页面图标
            default_index=default_index,  # 默认选中的页面索引
        )

    # 根据用户选择的页面，调用对应的页面函数
    if selected_page in pages:
        pages[selected_page]["func"](api=api, is_lite=is_lite)
        
