# 从 markconv 包中导入 MDConverter 类
from markconv import MDConverter
from markconv.exporters import PDFExporter


def pdf_basic_example():
    """
    PDF 转换基本使用示例
    
    该函数演示了如何使用 PDFExporter 将 Markdown 文件转换为 PDF 文件
    包括：
    - 创建 PDF 导出器实例（支持自定义 CSS 样式）
    - 解析 Markdown 文件
    - 指定输出 PDF 文件路径
    - 执行转换操作
    - 使用自定义 CSS 文件美化输出
    """
    # 打印示例标题
    print("PDF 转换基本使用示例")
    # 打印分隔线
    print("=" * 50)
    
    # 创建 MDConverter 实例，传入自定义 CSS 文件路径
    # 参数说明：
    #   - css_file: 自定义 CSS 样式文件的路径
    #     程序会读取该文件内容并插入到生成的 HTML 的 <style> 标签中
    #     自定义样式会覆盖或补充内置的默认样式
    #   - encoding: 文件编码格式，默认为 'utf-8'
    converter = MDConverter(css_file="custom.css")
    
    # 定义输入的 Markdown 文件路径（使用原始字符串 r 避免转义问题）
    input_file = r'sample.md'
    
    # 解析 Markdown 文件
    parsed_data = converter.parser.parse_file(input_file)
    
    # 创建 PDF 导出器实例
    # 参数说明：
    #   - css_file: 自定义 CSS 样式文件的路径（可选）
    pdf_exporter = PDFExporter(css_file="custom.css")
    
    # 定义输出的 PDF 文件路径（相对路径）
    output_file = 'examples/sample.pdf'
    
    # 调用 export 方法执行转换
    # 参数说明：
    #   - parsed_data: 包含 Markdown 解析结果的字典
    #     - content: Markdown 内容
    #     - title: 文档标题（可选）
    #   - output_file: 输出的 PDF 文件路径（如果目录不存在会自动创建）
    pdf_exporter.export(parsed_data, output_file)
    
    print(f"PDF 文件已生成: {output_file}")


# 当脚本被直接运行时，执行示例函数
# 如果脚本被导入为模块，则不会执行
if __name__ == '__main__':
    pdf_basic_example()
