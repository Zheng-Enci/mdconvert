"""
PDF 导出器模块

用于将 Markdown 转换为 PDF 格式
"""

import os
from typing import Dict, Any
import markdown2


def _markdown_to_html(markdown_content: str) -> str:
    """
    将 Markdown 内容转换为 HTML

    使用 markdown2 库进行转换，启用多种扩展功能

    Args:
        markdown_content (str): Markdown 格式的内容字符串

    Returns:
        str: 转换后的 HTML 内容

    Note:
        启用的扩展功能包括：
        - fenced-code-blocks: 围栏代码块
        - tables: 表格支持
        - toc: 目录生成
        - code-friendly: 代码友好模式
        - footnotes: 脚注
        - strike: 删除线
        - task_list: 任务列表
    """
    extras = [
        'fenced-code-blocks',
        'tables',
        'toc',
        'code-friendly',
        'footnotes',
        'strike',
        'task_list'
    ]
    return markdown2.markdown(markdown_content, extras=extras)


class PDFExporter:
    """
    PDF 导出器类
    
    将解析后的 Markdown 数据转换为 PDF 文件
    
    Attributes:
        css_file (str): 自定义 CSS 样式文件路径，默认为 None
    """
    
    def __init__(self, css_file: str = None):
        """
        初始化 PDF 导出器
        
        Args:
            css_file (str): 自定义 CSS 样式文件路径，可选
        """
        self.css_file = css_file

    def export(self, parsed_data: Dict[str, Any], output_path: str) -> None:
        """
        将解析后的 Markdown 数据导出为 PDF 文件
        
        该方法执行以下步骤：
        1. 将 Markdown 内容转换为 HTML
        2. 将 HTML 包装在完整的 HTML 文档结构中
        3. 将 HTML 转换为 PDF
        
        Args:
            parsed_data (Dict[str, Any]): 包含 Markdown 解析结果的字典
                - content: Markdown 内容
                - title: 文档标题（可选）
            output_path (str): 输出 PDF 文件的路径
        """
        html_content = _markdown_to_html(parsed_data['content'])
        html_content = self._wrap_html(html_content, parsed_data.get('title', 'Document'))
        
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        self._html_to_pdf(html_content, output_path)

    def _wrap_html(self, body_content: str, title: str) -> str:
        """
        将 HTML 内容包装在完整的 HTML 文档结构中
        
        添加 HTML 头部、元数据和样式，创建完整的 HTML 文档
        
        Args:
            body_content (str): HTML 主体内容
            title (str): 文档标题
            
        Returns:
            str: 完整的 HTML 文档字符串
            
        Note:
            内置样式包括：
            - 中文字体支持（微软雅黑、黑体）
            - 标题样式
            - 代码块样式
            - 表格样式
            - 引用块样式
            - 链接和图片样式
        """
        custom_css = self._get_custom_css()
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <style>
                body {{
                    font-family: 'SimHei', 'SimKai', 'SimFang', 'SimSun', Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                    color: #333;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: #2c3e50;
                    margin-top: 20px;
                    margin-bottom: 10px;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Consolas', 'Monaco', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
                .codehilite {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                    margin: 15px 0;
                    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                }}
                .codehilite pre {{
                    background-color: transparent;
                    padding: 0;
                    margin: 0;
                    white-space: pre;
                }}
                .codehilite code {{
                    color: #333;
                }}
                .codehilite .k {{ color: #900; font-weight: bold; }}
                .codehilite .nf {{ color: #069; font-weight: bold; }}
                .codehilite .nb {{ color: #008080; }}
                .codehilite .s2 {{ color: #d14; }}
                .codehilite .kc {{ color: #008080; font-weight: bold; }}
                .codehilite .p {{ color: #333; }}
                .codehilite .w {{ color: #333; }}
                .codehilite .c {{ color: #60a0b0; font-style: italic; }}
                .codehilite .err {{ border: 1px solid #FF0000; }}
                .codehilite .o {{ color: #666; }}
                .codehilite .cm {{ color: #60a0b0; font-style: italic; }}
                .codehilite .cp {{ color: #009999; }}
                .codehilite .c1 {{ color: #60a0b0; font-style: italic; }}
                .codehilite .cs {{ color: #60a0b0; font-style: italic; }}
                .codehilite .gd {{ color: #A00000; }}
                .codehilite .ge {{ font-style: italic; }}
                .codehilite .gr {{ color: #FF0000; }}
                .codehilite .gh {{ color: #000080; font-weight: bold; }}
                .codehilite .gi {{ color: #00A000; }}
                .codehilite .go {{ color: #808080; }}
                .codehilite .gp {{ color: #c65d09; font-weight: bold; }}
                .codehilite .gs {{ font-weight: bold; }}
                .codehilite .gu {{ color: #800080; font-weight: bold; }}
                .codehilite .gt {{ color: #0040D0; }}
                .codehilite .kt {{ color: #900; font-weight: bold; }}
                .codehilite .m {{ color: #099; }}
                .codehilite .s {{ color: #d14; }}
                .codehilite .na {{ color: #008080; }}
                .codehilite .nb {{ color: #008080; }}
                .codehilite .nc {{ color: #458; font-weight: bold; }}
                .codehilite .no {{ color: #008080; }}
                .codehilite .nd {{ color: #3c5d5d; font-weight: bold; }}
                .codehilite .ni {{ color: #800080; }}
                .codehilite .ne {{ color: #900; font-weight: bold; }}
                .codehilite .nf {{ color: #069; font-weight: bold; }}
                .codehilite .nl {{ color: #900; font-weight: bold; }}
                .codehilite .nn {{ color: #555; }}
                .codehilite .nt {{ color: #000080; }}
                .codehilite .nv {{ color: #008080; }}
                .codehilite .ow {{ color: #000; font-weight: bold; }}
                .codehilite .w {{ color: #bbb; }}
                .codehilite .mf {{ color: #099; }}
                .codehilite .mh {{ color: #099; }}
                .codehilite .mi {{ color: #099; }}
                .codehilite .mo {{ color: #099; }}
                .codehilite .sb {{ color: #d14; }}
                .codehilite .sc {{ color: #d14; }}
                .codehilite .sd {{ color: #d14; }}
                .codehilite .s2 {{ color: #d14; }}
                .codehilite .se {{ color: #d14; }}
                .codehilite .sh {{ color: #d14; }}
                .codehilite .si {{ color: #d14; }}
                .codehilite .sx {{ color: #d14; }}
                .codehilite .sr {{ color: #009926; }}
                .codehilite .s1 {{ color: #d14; }}
                .codehilite .ss {{ color: #990073; }}
                .codehilite .bp {{ color: #999; }}
                .codehilite .vc {{ color: #008080; }}
                .codehilite .vg {{ color: #008080; }}
                .codehilite .vi {{ color: #008080; }}
                .codehilite .il {{ color: #099; }}
                blockquote {{
                    border-left: 4px solid #ddd;
                    margin: 0;
                    padding-left: 20px;
                    color: #666;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                a {{
                    color: #3498db;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                }}
                hr {{
                    border: none;
                    border-top: 1px solid #ddd;
                    margin: 20px 0;
                }}
                {custom_css}
            </style>
        </head>
        <body>
            {body_content}
        </body>
        </html>
        """

    def _get_custom_css(self) -> str:
        """
        获取自定义 CSS 样式
        
        如果设置了自定义 CSS 文件，则读取并返回其内容
        
        Returns:
            str: CSS 样式字符串，如果没有设置或文件不存在则返回空字符串
        """
        if self.css_file and os.path.exists(self.css_file):
            with open(self.css_file, 'r', encoding='utf-8') as f:
                return f.read()
        return ""

    def _html_to_pdf(self, html_content: str, output_path: str) -> None:
        """
        将 HTML 内容转换为 PDF 文件
        
        使用 pdfkit 进行转换
        
        Args:
            html_content (str): HTML 内容字符串
            output_path (str): 输出 PDF 文件的路径
        """
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        import pdfkit
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        pdfkit.from_string(html_content, output_path, configuration=config)
