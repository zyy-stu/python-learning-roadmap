# Python Learning Roadmap

## 项目介绍

Python Learning Roadmap 是一套长期维护的中文开源教程。主仓库整理 Python 知识之间的先后关系、分阶段学习路线和统一编写规范。六个专题仓库分别承载教程、代码示例、练习与项目实践。学习者可以顺序完成基础路线，也可以根据前置知识进入适合自己的专题。

## 项目特点

- 用知识树组织语言基础、高级机制、应用生态和工程化。
- 提供初级、中级、高级三条循序渐进的学习路线。
- 教程与配套说明统一使用中文，保留代码和技术名称的原始拼写。
- 专题内容按统一规范配备可运行代码、练习题和综合实战项目。
- 通过 Issue、Pull Request 和变更记录持续维护内容。

## 项目知识体系

[完整知识树](knowledge-tree/README.md)覆盖 Python 基础、高级机制、Web 开发、数据分析、人工智能、工程化与实战项目。六个专题从基本语法与对象模型延伸到服务开发、数据处理、模型应用和综合交付。工程化贯穿代码组织、测试和部署。

## 七个仓库导航

- [学习导航 · python-learning-roadmap](https://github.com/zyy-stu/python-learning-roadmap)
- [Python 基础教程 · python-basic](https://github.com/zyy-stu/python-basic)
- [Python 高级教程 · python-advanced](https://github.com/zyy-stu/python-advanced)
- [Python Web 开发 · python-web](https://github.com/zyy-stu/python-web)
- [Python 数据分析 · python-data-science](https://github.com/zyy-stu/python-data-science)
- [Python AI 开发 · python-ai](https://github.com/zyy-stu/python-ai)
- [Python 实战项目 · python-projects](https://github.com/zyy-stu/python-projects)

各仓库的前置知识、目标读者和建设状态见[仓库清单](repositories/repository-list.md)。

## 学习路线

| 阶段 | 建议起点 | 完成目标 |
| --- | --- | --- |
| [初学者](roadmap/beginner.md) | 安装 Python，练习基础语法 | 独立完成能读写文件的命令行程序 |
| [中级学习者](roadmap/intermediate.md) | 梳理类型、对象和模块设计 | 完成带数据库、类型注解和测试的小应用 |
| [高级学习者](roadmap/advanced.md) | 研究语言机制与系统边界 | 在一个应用方向交付可测试、可部署的项目 |

## 技术环境

- **Python 3.11+** 用于运行教程代码。以各篇教程标注的版本和依赖为准。
- **Git** 用于获取示例、管理修改和提交贡献。
- **VS Code** 或 **PyCharm** 均可编辑 Python，打开项目后选择对应的虚拟环境作为解释器。
- 运行 `python --version` 和 `git --version` 确认命令可用。Windows 也可使用 `py -3.11 --version` 检查解释器。

## 教程规范

教程按目标、前置知识、概念、示例、练习和学习导航组织。每个示例说明运行命令、所需依赖和预期结果。编写时使用[教程规范](standards/tutorial-standard.md)与[模板入口](templates/README.md)。

## 贡献方式

欢迎补充实例、修正文档、提交练习或报告复现问题。先阅读[贡献指南](CONTRIBUTING.md)，再提交 Issue 或 Pull Request。代码变更请附运行命令和验证结果。

## 项目发展规划

先在 GitHub 建设 Markdown 教程和可运行示例，再用文档网站验证在线阅读体验，逐步推进独立学习平台。详见[网站规划](website/README.md)。

## 开源协议

本项目采用 [MIT 许可证](LICENSE)。版权声明保留待确认字段。
