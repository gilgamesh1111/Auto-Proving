# 自动证明（Automated Theorem Prover）

### 项目简介

本项目是一款旨在自动证明数学问题的智能工具。它通过结合大型语言模型与精密的证明策略，实现了从问题分析到最终证明的全流程自动化。

### 系统架构

本工具采用三模型协同工作的架构，以确保证明过程的严谨与高效：

1.  **初始化模型 (Init Model):**
    * 接收用户输入的数学问题。
    * 分析问题，并自动搜索相关的背景知识与核心定理。
    * 将问题的自然语言表述与形式化的 Lean 语言表述进行存储，为下一步证明做好准备。

2.  **证明模型 (Prover Model):**
    * 接收初始化模型处理后的数据。
    * 基于提供的定理与问题表述，执行核心的推理与证明任务，生成证明步骤。

3.  **代理模型 (Agent Model):**
    * 对证明模型生成的证明过程进行审查与总结。
    * 构建并动态更新“证明树”（Proof Tree），在必要时进行剪枝优化，剔除无效的证明路径。
    * 最终筛选并保存最满意、最可靠的证明结果。

---

### Windows 环境安装指南

#### 1. 克隆代码仓库

```bash
git clone <the_repository_url>
cd LEL
````

#### 2\. 安装环境与依赖

我们推荐使用 [Pixi](https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi) 进行环境管理，其体验与 `conda` 类似。

进入项目目录后，使用 Pixi 激活环境并安装所有依赖项：

```bash
pixi shell
```

#### 3\. 配置 API Keys

您需要提供必要的 API 密钥以启用模型的全部功能。

首先，复制模板文件：

```bash
copy .env_template .env
```

然后，编辑新建的 `.env` 文件，填入您的 API 密钥。

#### 4\. 运行项目

配置完成后，打开并运行 `main.ipynb` 即可开始使用。

-----

### 重要配置与注意事项

1.  **网络环境:** 本工具的许多功能（如模型调用、在线搜索）需要连接国际互联网，请确保您的网络环境符合要求。

2.  **Lean 环境:**

      * 请务必确认您的电脑已正确安装 Lean 环境。您可以通过以下命令快速安装：
        ```bash
        pixi shell
        leanup install
        ```
      * **首次启动** Lean 交互式服务时，初始化过程可能需要 **180 到 200 分钟**。
      * 运行 Lean 服务时，请确保您的设备**至少有 10GB 可用内存**。

3.  **必需的 API Keys:**

      * **[Gemini](https://aistudio.google.com/app/apikey):** 提供基础的免费额度。
      * **[Open Router](https://openrouter.ai/settings/keys):** 按需付费，支持微信支付。
      * **[DashScope (灵积)](https://dashscope.console.aliyun.com/apiKey):** 阿里云出品，提供免费额度。
      * **[Lean Explore](https://www.leanexplore.com/login?redirect=/api-keys):** 免费。

4.  **可选的 API Keys:**

      * **[Mineru](https://mineru.net/apiManage):** 如果您需要将 PDF 文档转换为 Markdown 并同步到向量知识库，请配置此 API 密钥。此服务免费，但需要国内网络环境。配置后可调用 `vec_store.sync_md(r".\src\src_pdf")` 函数。

-----

### 功能亮点

1.  **自动化知识库管理:**
    每次运行时，工具会自动扫描知识库目录，将新增的 `.md` 文件内容解析并同步到向量数据库中，实现知识的持续积累。

2.  **并行化模型调用:**
    在调用证明模型时，您可以指定一个模型列表，实现多个模型的并行推理，从而提升证明效率和成功率。例如：

    ```python
    modelName = ["deepseek/deepseek-prover-v2" for i in range(2)]
    ```

3.  **灵活的模型切换:**
    当 Gemini 的免费额度用尽时，您可以轻松切换到其他备用模型，例如通义千问（Qwen）：

    ```python
    llm = ChatTongyi(model="qwen-max", temperature=0.0)
    ```

### 常见问题与解决方案

1.  **问题: 导入 `duckduckgo_search` 失败。**
      * **原因:** `duckduckgo_search` 库的包名已从 `duckduckgo_search` 更改为 `ddgs`，但 `langchain` 框架可能未及时更新。
      * **解决方案:** 手动修改 `langchain` 的依赖文件。文件路径通常为：`.pixi\envs\default\Lib\site-packages\langchain_community\utilities\duckduckgo_search.py`，在文件中将旧的包名替换为 `ddgs` 即可。

-----

### 如何贡献

我们欢迎任何形式的贡献，让这个项目变得更好！

1.  **Fork** 本仓库。
2.  创建新的功能分支 (例如 `Feat_xxx`)。
3.  提交您的代码。
4.  新建一个 **Pull Request**。

<!-- end list -->