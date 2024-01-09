
# Contents
- [Contents](#contents)
- [Tips](#tips)
- [LLMs for Audiovisual Generation](#llms-for-audiovisual-generation)
  - [Image Generation](#image-generation)
    - [Multimodal Language Model-based](#multimodal-language-model-based)
    - [Datasets](#datasets)
  - [Video Generation](#video-generation)
    - [Multimodal Language Model-based](#multimodal-language-model-based-1)
    - [Datasets](#datasets-1)
  - [Audio Generation](#audio-generation)
    - [Multimodal Language Model-based](#multimodal-language-model-based-2)
    - [Datasets](#datasets-2)
  - [3D Generation](#3d-generation)
    - [Multimodal Language Model-based](#multimodal-language-model-based-3)
      - [General Object](#general-object)
      - [Avatar](#avatar)
    - [Datasets](#datasets-3)
- [LLMs for Audiovisual Editing](#llms-for-audiovisual-editing)
  - [Image Editing](#image-editing)
    - [Multimodal Language Model-based](#multimodal-language-model-based-4)
  - [Video Editing](#video-editing)
    - [Multimodal Language Model-based](#multimodal-language-model-based-5)
  - [Audio Editing](#audio-editing)
    - [Multimodal Language Model-based](#multimodal-language-model-based-6)
  - [3D Editing](#3d-editing)
    - [Multimodal Language Model-based](#multimodal-language-model-based-7)
      - [Avatar](#avatar-1)
      - [General Object](#general-object-1)
- [Multi-Modal Agents](#multi-modal-agents)
- [LLMs for Audiovisual Understanding](#llms-for-audiovisual-understanding)
  - [Image Understanding](#image-understanding)
  - [Video Understanding](#video-understanding)
  - [Audio Understanding](#audio-understanding)
  - [3D Understanding](#3d-understanding)
# Tips
- Free feel to search papers of a specific author via `ctrl + F` and then type the author name. The dropdown list of authors will automatically expand when searching.
- Besides directly clicking the above categorization, you can also search the related papers via the following tags: `customization`, `iteractive`, `human motion generation`.


# LLMs for Audiovisual Generation

## Image Generation

+ **Customization Assistant for Text-to-image Generation** (5 Dec 2023)<details><summary>Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, et al.</summary> Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, Tong Sun</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.03045)\
Tags: `customization`
<!-- [![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F689c358c5f9b5b1693a8bcc7e6e0460012f5cf9e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Sequential-Modeling-Enables-Scalable-Learning-for-Bai-Geng/689c358c5f9b5b1693a8bcc7e6e0460012f5cf9e)
[![Code](https://img.shields.io/github/stars/ytongbai/LVM.svg?style=social&label=Star)](https://github.com/ytongbai/LVM)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://yutongbai.com/lvm.html) -->

<!-- + **Sequential Modeling Enables Scalable Learning for Large Vision Models** (1 Dec 2023)<details><summary>Yutong Bai, Xinyang Geng, Karttikeya Mangalam, et al.</summary> Yutong Bai, Xinyang Geng, Karttikeya Mangalam, Amir Bar, Alan Yuille, Trevor Darrell, Jitendra Malik, Alexei A Efros</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.00785)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F689c358c5f9b5b1693a8bcc7e6e0460012f5cf9e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Sequential-Modeling-Enables-Scalable-Learning-for-Bai-Geng/689c358c5f9b5b1693a8bcc7e6e0460012f5cf9e)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://yutongbai.com/lvm.html)
[![Code](https://img.shields.io/github/stars/ytongbai/LVM.svg?style=social&label=Star)](https://github.com/ytongbai/LVM) -->

+ **CoDi-2: In-Context, Interleaved, and Interactive Any-to-Any Generation** (30 Nov 2023) <details><summary>Zineng Tang, Ziyi Yang, Mahmoud Khademi, et al.</summary>Zineng Tang, Ziyi Yang, Mahmoud Khademi, Yang Liu, Chenguang Zhu, Mohit Bansal</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.18775)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F78582ad19779a69d97b797a3c6eb2397f99398b6%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CoDi-2%3A-In-Context%2C-Interleaved%2C-and-Interactive-Tang-Yang/78582ad19779a69d97b797a3c6eb2397f99398b6)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://codi-2.github.io/)
[![Code](https://img.shields.io/github/stars/microsoft/i-Code.svg?style=social&label=Star)](https://github.com/microsoft/i-Code/tree/main/CoDi-2)

+ **ChatIllusion: Efficient-Aligning Interleaved Generation ability with Visual Instruction Model** (29 Nov 2023) <details><summary>Xiaowei Chi, Yijiang Liu, Zhengkai Jiang, et al.</summary> Xiaowei Chi, Yijiang Liu, Zhengkai Jiang, Rongyu Zhang, Ziyi Lin, Renrui Zhang, Peng Gao, Chaoyou Fu, Shanghang Zhang, Qifeng Liu, Yike Guo</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17963)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F22d55c52f43f59634586ab95fefbb7dba8c8b190%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ChatIllusion%3A-Efficient-Aligning-Interleaved-with-Chi-Liu/22d55c52f43f59634586ab95fefbb7dba8c8b190)
[![Code](https://img.shields.io/github/stars/litwellchi/ChatIllusion.svg?style=social&label=Star)](https://github.com/litwellchi/ChatIllusion)

+ **TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering** (28 Nov 2023) <details><summary>Jingye Chen, Yupan Huang, Tengchao Lv, et al.</summary>Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16465)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1c6e2a4da1ead685a95c079751bf4d7a727d8180%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/TextDiffuser-2%3A-Unleashing-the-Power-of-Language-Chen-Huang/1c6e2a4da1ead685a95c079751bf4d7a727d8180)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jingyechen.github.io/textdiffuser2/)
[![Code](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social&label=Star)](https://github.com/microsoft/unilm/tree/master/textdiffuser-2)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/JingyeChen22/TextDiffuser-2)

+ **Self-correcting LLM-controlled Diffusion Models** (27 Nov 2023)<details><summary>Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, et al.</summary> Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, Boyi Li, Trevor Darrell</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16090)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Self-correcting-LLM-controlled-Diffusion-Models-Wu-Lian/42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e)

+ **Tokenize and Embed ALL for Multi-modal Large Language Models** (8 Nov 2023)<details><summary>Zhen Yang, Yingxue Zhang, Fandong Meng, et al.</summary> Zhen Yang, Yingxue Zhang, Fandong Meng, Jie Zhou</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.04589)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F59d716b442ab760a78f58de6748c0fa1d507bfc1%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/TEAL%3A-Tokenize-and-Embed-ALL-for-Multi-modal-Large-Yang-Zhang/59d716b442ab760a78f58de6748c0fa1d507bfc1)

+ **LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts** (16 Oct 2023)<details><summary>Hanan Gani, Shariq Farooq Bhat, Muzammal Naseer, et al.</summary>Hanan Gani, Shariq Farooq Bhat, Muzammal Naseer, Salman Khan, Peter Wonka</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.10640)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4cb2c262ce34f41974f1b1623fc5a6e32956ded3%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLM-Blueprint%3A-Enabling-Text-to-Image-Generation-Gani-Bhat/4cb2c262ce34f41974f1b1623fc5a6e32956ded3)

+ **Making Multimodal Generation Easier: When Diffusion Models Meet LLMs** (13 Oct 2023)<details><summary>Xiangyu Zhao, Bo Liu, Qijiong Liu, et al.</summary>Xiangyu Zhao, Bo Liu, Qijiong Liu, Guangyuan Shi, Xiao-Ming Wu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08949v1)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F833cdd713c27ab5899bb912a1d511c10af61cefb%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Making-Multimodal-Generation-Easier%3A-When-Diffusion-Zhao-Liu/833cdd713c27ab5899bb912a1d511c10af61cefb)
[![Code](https://img.shields.io/github/stars/zxy556677/EasyGen.svg?style=social&label=Star)](https://github.com/zxy556677/EasyGen)

+ **Idea2Img: Iterative Self-Refinement with GPT-4V(ision) for Automatic Image Design and Generation** (12 Oct 2023)<details><summary>Zhengyuan Yang, Jianfeng Wang, Linjie Li, et al.</summary>Zhengyuan Yang, Jianfeng Wang, Linjie Li, Kevin Lin, Chung-Ching Lin, Zicheng Liu, Lijuan Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.08541)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1d14a708622917da4b9820ada6d32af24fc1651a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Idea2Img%3A-Iterative-Self-Refinement-with-for-Image-Yang-Wang/1d14a708622917da4b9820ada6d32af24fc1651a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://idea2img.github.io/)

+ **OpenLEAF: Open-Domain Interleaved Image-Text Generation and Evaluation** (11 Oct 2023)<details><summary>Jie An, Zhengyuan Yang, Linjie Li, et al.</summary>Jie An, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu, Lijuan Wang, Jiebo Luo</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.07749)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F7f1ba5630c3baa09b11cc665b3f71cdb117e5ffb%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/OpenLEAF%3A-Open-Domain-Interleaved-Image-Text-and-An-Yang/7f1ba5630c3baa09b11cc665b3f71cdb117e5ffb)

+ **Mini-DALLE3: Interactive Text to Image by Prompting Large Language Models** (11 Oct 2023)<details><summary>Zeqiang Lai, Xizhou Zhu, Jifeng Dai, et al.</summary>Zeqiang Lai, Xizhou Zhu, Jifeng Dai, Yu Qiao, Wenhai Wang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.07653)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ff669d7a6fab0147253178a6fc854e05e3d92fb3f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Mini-DALLE3%3A-Interactive-Text-to-Image-by-Prompting-Lai-Zhu/f669d7a6fab0147253178a6fc854e05e3d92fb3f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://minidalle3.github.io/)
[![Code](https://img.shields.io/github/stars/Zeqiang-Lai/Mini-DALLE3.svg?style=social&label=Star)](https://github.com/Zeqiang-Lai/Mini-DALLE3)

+ **MiniGPT-5: Interleaved Vision-and-Language Generation via Generative Vokens** (3 Oct 2023)\
Kaizhi Zheng, Xuehai He, Xin Eric Wang.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.02239)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fe7d09b6f2bc878cf2c993acf675f409d0b55f35a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MiniGPT-5%3A-Interleaved-Vision-and-Language-via-Zheng-He/e7d09b6f2bc878cf2c993acf675f409d0b55f35a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://eric-ai-lab.github.io/minigpt-5.github.io/)
[![Code](https://img.shields.io/github/stars/eric-ai-lab/MiniGPT-5.svg?style=social&label=Star)](https://github.com/eric-ai-lab/MiniGPT-5)

+ **Making LLaMA SEE and Draw with SEED Tokenizer** (2 Oct 2023)<details><summary>Yuying Ge, Sijie Zhao, Ziyun Zeng, et al.</summary>Yuying Ge, Sijie Zhao, Ziyun Zeng, Yixiao Ge, Chen Li, Xintao Wang, Ying Shan</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.01218)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5ba1525dc6d382ee0a4a1ca3c64fc5907ca64c67%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Making-LLaMA-SEE-and-Draw-with-SEED-Tokenizer-Ge-Zhao/5ba1525dc6d382ee0a4a1ca3c64fc5907ca64c67)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/seed/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/SEED.svg?style=social&label=Star)](https://github.com/AILab-CVC/SEED)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://dad1ed9a9fb76fe83b.gradio.live/)

+ **InstructCV: Instruction-Tuned Text-to-Image Diffusion Models as Vision Generalists** (30 Sep 2023)<details><summary>Yulu Gan, Sungwoo Park, Alexander Schubert, et al.</summary>Yulu Gan, Sungwoo Park, Alexander Schubert, Anthony Philippakis, Ahmed M. Alaa</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.00390)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F819f477065088220a6f706cd9ef76dbcb4b4c134%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InstructCV%3A-Instruction-Tuned-Text-to-Image-Models-Gan-Park/819f477065088220a6f706cd9ef76dbcb4b4c134)
[![Code](https://img.shields.io/github/stars/AlaaLab/InstructCV.svg?style=social&label=Star)](https://github.com/AlaaLab/InstructCV)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/alaa-lab/InstructCV)

+ **Text-to-Image Generation for Abstract Concepts** (26 Sep 2023) <details><summary>Jiayi Liao, Xu Chen, Qiang Fu, et al.</summary>Jiayi Liao, Xu Chen, Qiang Fu, Lun Du, Xiangnan He, Xiang Wang, Shi Han, Dongmei Zhang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.14623)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F0d38f1edac66b4645cf5fa05abaf9d92cba5d5d3%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Text-to-Image-Generation-for-Abstract-Concepts-Liao-Chen/0d38f1edac66b4645cf5fa05abaf9d92cba5d5d3)

+ **DreamLLM: Synergistic Multimodal Comprehension and Creation** (20 Sep 2023)<details><summary>Runpei Dong, Chunrui Han, Yuang Peng, et al.</summary>Runpei Dong, Chunrui Han, Yuang Peng, Zekun Qi, Zheng Ge, Jinrong Yang, Liang Zhao, Jianjian Sun, Hongyu Zhou, Haoran Wei, Xiangwen Kong, Xiangyu Zhang, Kaisheng Ma, Li Yi</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.11499)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F7b689adb8c156d6158660f90d1c86888ee281f63%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/DreamLLM%3A-Synergistic-Multimodal-Comprehension-and-Dong-Han/7b689adb8c156d6158660f90d1c86888ee281f63)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreamllm.github.io/)
[![Code](https://img.shields.io/github/stars/RunpeiDong/DreamLLM.svg?style=social&label=Star)](https://github.com/RunpeiDong/DreamLLM)

+ **SwitchGPT: Adapting Large Language Models for Non-Text Outputs** (14 Sep 2023)\
Wang, Xinyu, Bohan Zhuang, and Qi Wu.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.07623)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F366564d210768814bc880e391b909cfbd95f8964%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/SwitchGPT%3A-Adapting-Large-Language-Models-for-Wang-Zhuang/366564d210768814bc880e391b909cfbd95f8964)
[![Code](https://img.shields.io/github/stars/xinke-wang/SwitchGPT.svg?style=social&label=Star)](https://github.com/xinke-wang/SwitchGPT)

+ **NExT-GPT: Any-to-Any Multimodal LLM** (11 Sep 2023)<details><summary>Shengqiong Wu, Hao Fei, Leigang Qu, et al.</summary>Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, Tat-Seng Chua</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.05519)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ffa75a55760e6ea49b39b83cb85c99a22e1088254%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/NExT-GPT%3A-Any-to-Any-Multimodal-LLM-Wu-Fei/fa75a55760e6ea49b39b83cb85c99a22e1088254)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://next-gpt.github.io/)
[![Code](https://img.shields.io/github/stars/NExT-GPT/NExT-GPT.svg?style=social&label=Star)](https://github.com/NExT-GPT/NExT-GPT)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://9704af1b453125102e.gradio.live/)

+ **LayoutLLM-T2I: Eliciting Layout Guidance from LLM for Text-to-Image Generation** (9 Aug 2023)\
Qu, Leigang, et al. ACM MM 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.05095)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F7d78238a9bad60433d616abdd93c735087d99670%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LayoutLLM-T2I%3A-Eliciting-Layout-Guidance-from-LLM-Qu-Wu/7d78238a9bad60433d616abdd93c735087d99670)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://layoutllm-t2i.github.io/)
[![Code](https://img.shields.io/github/stars/LayoutLLM-T2I/LayoutLLM-T2I.svg?style=social&label=Star)](https://github.com/LayoutLLM-T2I/LayoutLLM-T2I)

+ **Planting a SEED of Vision in Large Language Model** (16 Jul 2023)\
Yuying, Ge, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.08041)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F40298b8d50109c52fc10763eddc64a07cf8acb31%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Planting-a-SEED-of-Vision-in-Large-Language-Model-Ge-Ge/40298b8d50109c52fc10763eddc64a07cf8acb31)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/seed/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/SEED.svg?style=social&label=Star)](https://github.com/AILab-CVC/SEED)

+ **Generative Pretraining in Multimodality** (11 Jul 2023)\
Quan, Sun, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.05222)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F94053805cd59f2e9a47fe3f080c7e7afefb337cc%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Generative-Pretraining-in-Multimodality-Sun-Yu/94053805cd59f2e9a47fe3f080c7e7afefb337cc)
[![Code](https://img.shields.io/github/stars/baaivision/Emu.svg?style=social&label=Star)](https://github.com/baaivision/Emu)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](http://218.91.113.230:9002)

+ **SPAE: Semantic Pyramid AutoEncoder for Multimodal Generation with Frozen LLMs** (30 Jun 2023)\
Yu, Lijun, et al. NeurIPS 2023 spotlight.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.17842)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F376f494126d1ea4f571ea0263c43ac2b6331800a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/SPAE%3A-Semantic-Pyramid-AutoEncoder-for-Multimodal-Yu-Cheng/376f494126d1ea4f571ea0263c43ac2b6331800a)

+ **Controllable Text-to-Image Generation with GPT-4** (29 May 2023)\
Zhang, Tianjun, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.18583)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F3a79545719fb193a6b4042ef7d1d87cfd267be06%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Controllable-Text-to-Image-Generation-with-GPT-4-Zhang-Zhang/3a79545719fb193a6b4042ef7d1d87cfd267be06)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://github.com/tianjunz/Control-GPT) 

+ **Generating Images with Multimodal Language Models** (26 May 2023)\
Koh, Jing Yu, Daniel Fried, and Ruslan Salakhutdinov. NeurIPS 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.17216)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F6fb5c0eff3696ef252aca9638e10176ecce7cecb%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Generating-Images-with-Multimodal-Language-Models-Koh-Fried/6fb5c0eff3696ef252aca9638e10176ecce7cecb)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jykoh.com/gill)
[![Code](https://img.shields.io/github/stars/kohjingyu/gill.svg?style=social&label=Star)](https://github.com/kohjingyu/gill)

+ **LayoutGPT: Compositional Visual Planning and Generation with Large Language Models** (24 May 2023)\
Feng, Weixi, et al. NeurIPS 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.15393)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F66d755730f5d08a6f4fcc5e81f24982ba389dca9%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LayoutGPT%3A-Compositional-Visual-Planning-and-with-Feng-Zhu/66d755730f5d08a6f4fcc5e81f24982ba389dca9)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://layoutgpt.github.io/)
[![Code](https://img.shields.io/github/stars/weixi-feng/LayoutGPT.svg?style=social&label=Star)](https://github.com/weixi-feng/LayoutGPT)

+ **Visual Programming for Text-to-Image Generation and Evaluation** (24 May 2023)\
Jaemin Cho, Abhay Zala, Mohit Bansal. NeurIPS 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.15328)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F9837349417e36ef5be06da0fd6c74042148bdaa2%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Visual-Programming-for-Text-to-Image-Generation-and-Cho-Zala/9837349417e36ef5be06da0fd6c74042148bdaa2)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://vp-t2i.github.io/)
[![Code](https://img.shields.io/github/stars/j-min/VPGen.svg?style=social&label=Star)](https://github.com/j-min/VPGen)

+ **LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models** (23 May 2023)\
Lian, Long, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.13655)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fe9ae0c76a71b8f302eb17b1c4462b9cc97d87cd0%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLM-grounded-Diffusion%3A-Enhancing-Prompt-of-Models-Lian-Li/e9ae0c76a71b8f302eb17b1c4462b9cc97d87cd0)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llm-grounded-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedDiffusion)

+ **Interactive Data Synthesis for Systematic Vision Adaptation via LLMs-AIGCs Collaboration** (22 May 2023)\
Yu, Qifan, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.12799)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F43a55dbd95c9d5cd82de8db276f41adeec4a937d%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Interactive-Data-Synthesis-for-Systematic-Vision-Yu-Li/43a55dbd95c9d5cd82de8db276f41adeec4a937d)
[![Code](https://img.shields.io/github/stars/Yuqifan1117/Labal-Anything-Pipeline.svg?style=social&label=Star)](https://github.com/Yuqifan1117/Labal-Anything-Pipeline)

+ **CoDi: Any-to-Any Generation via Composable Diffusion** (19 May 2023)<details><summary>Zineng Tang, Ziyi Yang, Chenguang Zhu, et al. NeurIPS 2023.</summary>Zineng Tang, Ziyi Yang, Chenguang Zhu, Michael Zeng, Mohit Bansal</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.11846)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F9f411fda2ad5b141a3115f707bcf5ee865b3fb94%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Any-to-Any-Generation-via-Composable-Diffusion-Tang-Yang/9f411fda2ad5b141a3115f707bcf5ee865b3fb94)
[![Code](https://img.shields.io/github/stars/microsoft/i-Code.svg?style=social&label=Star)](https://github.com/microsoft/i-Code/tree/main/i-Code-V3)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://codi-gen.github.io/)

+ **Grounding Language Models to Images for Multimodal Inputs and Outputs** (31 Jan 2023)\
Koh, Jing Yu, Ruslan Salakhutdinov, and Daniel Fried. ICML 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.13823)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F6173520a1eb2814d067e8c5fd16212b7cbf6ee78%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Grounding-Language-Models-to-Images-for-Multimodal-Koh-Salakhutdinov/6173520a1eb2814d067e8c5fd16212b7cbf6ee78)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jykoh.com/fromage)
[![Code](https://img.shields.io/github/stars/kohjingyu/fromage.svg?style=social&label=Star)](https://github.com/kohjingyu/fromage)

### Multimodal Language Model-based

+ **PIXART-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis** (30 Sep 2023)<details><summary>Nupur Kumari, Bingliang Zhang, Richard Zhang, et al. CVPR 2023.</summary>Junsong Chen, Jincheng Yu, Chongjian Ge, Lewei Yao, Enze Xie, Yue Wu, Zhongdao Wang, James Kwok, Ping Luo, Huchuan Lu, Zhenguo Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.00426)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F144eca44e250cc462f6fc3a172abb865978f66f5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/PixArt-%CE%B1%3A-Fast-Training-of-Diffusion-Transformer-Chen-Yu/7dfe1c9f1d7120102499c7e561efc2326e7a0358)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://pixart-alpha.github.io/)
[![Code](https://img.shields.io/github/stars/PixArt-alpha/PixArt-alpha.svg?style=social&label=Star)](https://github.com/PixArt-alpha/PixArt-alpha)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/PixArt-alpha/PixArt-alpha)

+ **TextDiffuser: Diffusion Models as Text Painters** (18 May 2023) <details><summary>Jingye Chen, Yupan Huang, Tengchao Lv, et al. NeurIPS 2023.</summary>Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, Furu Wei</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.10855)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fe779781f1bea273573fc9d3f1a5e874bcff2cd2b%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/TextDiffuser%3A-Diffusion-Models-as-Text-Painters-Chen-Huang/e779781f1bea273573fc9d3f1a5e874bcff2cd2b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://jingyechen.github.io/textdiffuser/)
[![Code](https://img.shields.io/github/stars/microsoft/unilm.svg?style=social&label=Star)](https://github.com/microsoft/unilm/tree/master/textdiffuser)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/JingyeChen22/TextDiffuser)

+ **TiGAN: Text-Based Interactive Image Generation and Manipulation** (Dec 2022)<details><summary>Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, et al. AAAI 2022.</summary>Yufan Zhou, Ruiyi Zhang, Jiuxiang Gu, Chris Tensmeyer, Tong Yu,Changyou Chen, Jinhui Xu, Tong Sun</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/20270)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F839dc73c1adae268144d9cfb9d70985b2001304f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/TiGAN%3A-Text-Based-Interactive-Image-Generation-and-Zhou-Zhang/839dc73c1adae268144d9cfb9d70985b2001304f)\
Tags: `iteractive`

+ **Multi-Concept Customization of Text-to-Image Diffusion** (8 Dec 2022)<details><summary>Nupur Kumari, Bingliang Zhang, Richard Zhang, et al. CVPR 2023.</summary>Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, Jun-Yan Zhu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.04488)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F144eca44e250cc462f6fc3a172abb865978f66f5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Multi-Concept-Customization-of-Text-to-Image-Kumari-Zhang/144eca44e250cc462f6fc3a172abb865978f66f5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.cs.cmu.edu/~custom-diffusion/)
[![Code](https://img.shields.io/github/stars/adobe-research/custom-diffusion.svg?style=social&label=Star)](https://github.com/adobe-research/custom-diffusion)\
Tags: `customization`

+ **DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation** (25 Aug 2022)<details><summary>Nataniel Ruiz, Yuanzhen Li, Varun Jampani, et al. CVPR 2023.</summary>Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, Kfir Aberman</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.12242)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5b19bf6c3f4b25cac96362c98b930cf4b37f6744%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/DreamBooth%3A-Fine-Tuning-Text-to-Image-Diffusion-for-Ruiz-Li/5b19bf6c3f4b25cac96362c98b930cf4b37f6744)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreambooth.github.io/)\
Tags: `customization`

+ **An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion** (2 Aug 2022)<details><summary>Rinon Gal, Yuval Alaluf, Yuval Atzmon, et al. </summary>Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.01618)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5b19bf6c3f4b25cac96362c98b930cf4b37f6744%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/DreamBooth%3A-Fine-Tuning-Text-to-Image-Diffusion-for-Ruiz-Li/5b19bf6c3f4b25cac96362c98b930cf4b37f6744)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dreambooth.github.io/)
[![Code](https://img.shields.io/github/stars/rinongal/textual_inversion.svg?style=social&label=Star)](https://github.com/rinongal/textual_inversion)\
Tags: `customization`

+ **Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding** (23 May 2022)\
Saharia, Chitwan, et al. NeurIPS 2022.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2205.11487)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F9695824d7a01fad57ba9c01d7d76a519d78d65e7%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Photorealistic-Text-to-Image-Diffusion-Models-with-Saharia-Chan/9695824d7a01fad57ba9c01d7d76a519d78d65e7)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://imagen.research.google/) 

+ **High-Resolution Image Synthesis with Latent Diffusion Models** (20 Dec 2021)\
Rombach, Robin, et al. CVPR 2022 (Oral).\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2112.10752)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fc10075b3746a9f3dd5811970e93c8ca3ad39b39d%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/High-Resolution-Image-Synthesis-with-Latent-Models-Rombach-Blattmann/c10075b3746a9f3dd5811970e93c8ca3ad39b39d)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ommer-lab.com/research/latent-diffusion-models/)
[![Code](https://img.shields.io/github/stars/CompVis/stable-diffusion.svg?style=social&label=Star)](https://github.com/CompVis/stable-diffusion)

### Datasets

## Video Generation

+ **InterControl: Generate Human Motion Interactions by Controlling Every Joint** (27 Nov 2023)<details><summary>Zhenzhi Wang, Jingbo Wang, Dahua Lin, et al.</summary>Zhenzhi Wang, Jingbo Wang, Dahua Lin, Bo Dai</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.15864)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F9cdb7e415a96795dc6705e66f3b798238b4dec2c%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InterControl%3A-Generate-Human-Motion-Interactions-by-Wang-Wang/9cdb7e415a96795dc6705e66f3b798238b4dec2c)
[![Code](https://img.shields.io/github/stars/zhenzhiwang/intercontrol.svg?style=social&label=Star)](https://github.com/zhenzhiwang/intercontrol)\
Tags: `human motion generation`

+ **GPT4Motion: Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning** (21 Nov 2023)<details><summary>Jiaxi Lv, Yi Huang, Mingfu Yan, et al.</summary>Jiaxi Lv, Yi Huang, Mingfu Yan, Jiancheng Huang, Jianzhuang Liu, Yifan Liu, Yafei Wen, Xiaoxin Chen, Shifeng Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.12631)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F9cdb7e415a96795dc6705e66f3b798238b4dec2c%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InterControl%3A-Generate-Human-Motion-Interactions-by-Wang-Wang/9cdb7e415a96795dc6705e66f3b798238b4dec2c)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://gpt4motion.github.io/)

+ **Language Model Beats Diffusion -- Tokenizer is Key to Visual Generation** (9 Oct 2023)<details><summary>Lijun Yu, José Lezama, Nitesh B. Gundavarapu, et al.</summary>Lijun Yu, José Lezama, Nitesh B. Gundavarapu, Luca Versari, Kihyuk Sohn, David Minnen, Yong Cheng, Agrim Gupta, Xiuye Gu, Alexander G. Hauptmann, Boqing Gong, Ming-Hsuan Yang, Irfan Essa, David A. Ross, Lu Jiang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.05737)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F985f0c89c5a607742ec43c1fdc2cbfe54541cbad%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Language-Model-Beats-Diffusion-Tokenizer-is-Key-to-Yu-Lezama/985f0c89c5a607742ec43c1fdc2cbfe54541cbad)

+ **LLM-grounded Video Diffusion Models** (29 Sep 2023)<details><summary>Long Lian, Baifeng Shi, Adam Yala, et al.</summary>Long Lian, Baifeng Shi, Adam Yala, Trevor Darrell, Boyi Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.17444)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F87bf66eb6d22df17f70170a0e575b4f12c4813ef%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLM-grounded-Video-Diffusion-Models-Lian-Shi/87bf66eb6d22df17f70170a0e575b4f12c4813ef)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llm-grounded-video-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedVideoDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedVideoDiffusion)

+ **VideoDirectorGPT: Consistent Multi-scene Video Generation via LLM-Guided Planning** (26 Sep 2023)<details><summary>Han Lin, Abhay Zala, Jaemin Cho, et al.</summary>Han Lin, Abhay Zala, Jaemin Cho, Mohit Bansal</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.15091)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F16753e0317730e8c1b297338300a8c6163dd06f2%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VideoDirectorGPT%3A-Consistent-Multi-scene-Video-via-Lin-Zala/16753e0317730e8c1b297338300a8c6163dd06f2)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://videodirectorgpt.github.io/)
[![Code](https://img.shields.io/github/stars/HL-hanlin/VideoDirectorGPT.svg?style=social&label=Star)](https://github.com/HL-hanlin/VideoDirectorGPT)

+ **Free-Bloom: Zero-Shot Text-to-Video Generator with LLM Director and LDM Animator** (25 Sep 2023)<details><summary>Hanzhuo Huang, Yufan Feng, Cheng Shi, et al. NIPS 2023.</summary>Hanzhuo Huang, Yufan Feng, Cheng Shi, Lan Xu, Jingyi Yu, Sibei Yang</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.14494)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F120aca3e415b6641a0b0cd20695ab85ed7789612%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Free-Bloom%3A-Zero-Shot-Text-to-Video-Generator-with-Huang-Feng/120aca3e415b6641a0b0cd20695ab85ed7789612)
[![Code](https://img.shields.io/github/stars/SooLab/Free-Bloom.svg?style=social&label=Star)](https://github.com/SooLab/Free-Bloom)

+ **Empowering Dynamics-aware Text-to-Video Diffusion with Large Language Models** (26 Aug 2023)<details><summary>Hao Fei, Shengqiong Wu, Wei Ji, et al.</summary>Hao Fei, Shengqiong Wu, Wei Ji, Hanwang Zhang, Tat-Seng Chua</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.13812)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd0a7f7fe31e0e0c42b471b4c47a313bd8c8e5206%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Empowering-Dynamics-aware-Text-to-Video-Diffusion-Fei-Wu/d0a7f7fe31e0e0c42b471b4c47a313bd8c8e5206)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](http://haofei.vip/Dysen-VDM/)
[![Code](https://img.shields.io/github/stars/scofield7419/Dysen.svg?style=social&label=Star)](https://github.com/scofield7419/Dysen)

+ **Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation** (23 May 2023)<details><summary>Susung Hong, Junyoung Seo, Sunghwan Hong, et al.</summary>Susung Hong, Junyoung Seo, Sunghwan Hong, Heeseong Shin, Seungryong Kim</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.14330)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fb1750d2a6e3480e690999916a86c8b3876577b39%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Large-Language-Models-are-Frame-level-Directors-for-Hong-Seo/b1750d2a6e3480e690999916a86c8b3876577b39)
[![Code](https://img.shields.io/github/stars/KU-CVLAB/DirecT2V.svg?style=social&label=Star)](https://github.com/KU-CVLAB/DirecT2V)

+ **Text2Motion: From Natural Language Instructions to Feasible Plans** (21 Mar 2023)<details><summary>Kevin Lin, Christopher Agia, Toki Migimatsu, et al.</summary>Kevin Lin, Christopher Agia, Toki Migimatsu, Marco Pavone, Jeannette Bohg</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.12153)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F8f2d4758e6d525509ae36bb30224dc9259027e6b%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Text2Motion%3A-from-natural-language-instructions-to-Lin-Agia/8f2d4758e6d525509ae36bb30224dc9259027e6b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://sites.google.com/stanford.edu/text2motion)
[![Code](https://img.shields.io/github/stars/KU-CVLAB/DirecT2V.svg?style=social&label=Star)](https://github.com/KU-CVLAB/DirecT2V)

### Multimodal Language Model-based
+ **VBench: Comprehensive Benchmark Suite for Video Generative Models** (29 Nov 2023)\
Huang, Ziqi, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17982)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4e9a8141da2a8c603722b07d096109207f8e0b66%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VBench%3A-Comprehensive-Benchmark-Suite-for-Video-Huang-He/4e9a8141da2a8c603722b07d096109207f8e0b66)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://vchitect.github.io/VBench-project/)
[![Code](https://img.shields.io/github/stars/Vchitect/VBench.svg?style=social&label=Star)](https://github.com/Vchitect/VBench)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/Vchitect/VBench_Leaderboard)

+ **Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets** (25 Nov 2023)\
Blattmann, Andreas, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.15127)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1206b05eae5a06ba662ae79fb291b50e359c4f42%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Stable-Video-Diffusion%3A-Scaling-Latent-Video-Models-Blattmann-Dockhorn/1206b05eae5a06ba662ae79fb291b50e359c4f42)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://stability.ai/research/stable-video-diffusion-scaling-latent-video-diffusion-models-to-large-datasets)
[![Code](https://img.shields.io/github/stars/Stability-AI/generative-models.svg?style=social&label=Star)](https://github.com/Stability-AI/generative-models)

+ **VideoCrafter1: Open Diffusion Models for High-Quality Video Generation** (30 Oct 2023)\
Chen, Haoxin, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.19512)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1891c3756f870d902a0b793a1dcd5cc34c778612%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VideoCrafter1%3A-Open-Diffusion-Models-for-Video-Chen-Xia/1891c3756f870d902a0b793a1dcd5cc34c778612)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/videocrafter/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/VideoCrafter.svg?style=social&label=Star)](https://github.com/AILab-CVC/VideoCrafter)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/VideoCrafter/VideoCrafter)

+ **FreeNoise: Tuning-Free Longer Video Diffusion via Noise Rescheduling** (23 Oct 2023)<details><summary>Haonan Qiu, Menghan Xia, Yong Zhang, et al.</summary>Haonan Qiu, Menghan Xia, Yong Zhang, Yingqing He, Xintao Wang, Ying Shan, Ziwei Liu</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.15169)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd831988859f0c077b38094446d8585a8340af223%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/FreeNoise%3A-Tuning-Free-Longer-Video-Diffusion-via-Qiu-Xia/d831988859f0c077b38094446d8585a8340af223)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](http://haonanqiu.com/projects/FreeNoise.html)
[![Code](https://img.shields.io/github/stars/arthur-qiu/LongerCrafter.svg?style=social&label=Star)](https://github.com/arthur-qiu/LongerCrafter)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/MoonQiu/LongerCrafter)

+ **Animate-A-Story: Storytelling with Retrieval-Augmented Video Generation** (13 Jul 2023)\
He, Yingqing, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.06940)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F77040969110fab39a55699cb06f9edf68789445a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Animate-A-Story%3A-Storytelling-with-Video-Generation-He-Xia/77040969110fab39a55699cb06f9edf68789445a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ailab-cvc.github.io/Animate-A-Story/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/Animate-A-Story.svg?style=social&label=Star)](https://github.com/AILab-CVC/Animate-A-Story)

+ **Make-Your-Video: Customized Video Generation Using Textual and Structural Guidance** (1 Jun 2023)\
Xing, Jinbo, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.00943)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F52b10ae66d025e99fbb602935e155f97f4f0696f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Make-Your-Video%3A-Customized-Video-Generation-Using-Xing-Xia/52b10ae66d025e99fbb602935e155f97f4f0696f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://doubiiu.github.io/projects/Make-Your-Video/)
[![Code](https://img.shields.io/github/stars/AILab-CVC/Make-Your-Video.svg?style=social&label=Star)](https://github.com/AILab-CVC/Make-Your-Video)

+ **Follow Your Pose: Pose-Guided Text-to-Video Generation using Pose-Free Videos** (3 Apr 2023)\
Ma, Yue, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.01186)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fee73edebd42626d9c2d91e35fd2ed3cdb0fb26d0%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Follow-Your-Pose%3A-Pose-Guided-Text-to-Video-using-Ma-He/ee73edebd42626d9c2d91e35fd2ed3cdb0fb26d0)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://follow-your-pose.github.io/)
[![Code](https://img.shields.io/github/stars/mayuelala/FollowYourPose.svg?style=social&label=Star)](https://github.com/mayuelala/FollowYourPose)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/YueMafighting/FollowYourPose)

+ **VideoFusion: Decomposed Diffusion Models for High-Quality Video Generation** (15 Mar 2023)\
Luo, Zhengxiong, et al. CVPR 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.08320)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F26c6090b7e7ba4513f82aa28d41360c60770c618%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VideoFusion%3A-Decomposed-Diffusion-Models-for-Video-Luo-Chen/26c6090b7e7ba4513f82aa28d41360c60770c618)

### Datasets

+ **InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation** (13 Jul 2023)\
Wang, Yi, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.06942)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F369b449415d50387fba048bbd4d26ee890df84b5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InternVid%3A-A-Large-scale-Video-Text-Dataset-for-and-Wang-He/369b449415d50387fba048bbd4d26ee890df84b5)
[![Code](https://img.shields.io/github/stars/OpenGVLab/InternVideo.svg?style=social&label=Star)](https://github.com/OpenGVLab/InternVideo)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/datasets/OpenGVLab/InternVid)

## Audio Generation
+ **Diffsound: Discrete Diffusion Model for Text-to-sound Generation** (Wed, 20 Jul 2022)<details><summary>Dongchao Yang, Jianwei Yu, Helin Wang, et al. (TASLP2022)</summary>Dongchao Yang, Jianwei Yu, Helin Wang, Wen Wang, Chao Weng, Yuexian Zou, Dong Yu</details>\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2207.09983)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fc036f75da24ba64a583e0b6d41c5b792347bffa6%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Diffsound%3A-Discrete-Diffusion-Model-for-Generation-Yang-Yu/c036f75da24ba64a583e0b6d41c5b792347bffa6)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://dongchaoyang.top/text-to-sound-synthesis-demo/)
[![Code](https://img.shields.io/github/stars/Text-to-sound-Synthesis.svg?style=social&label=Star)](https://github.com/yangdongchao/Text-to-sound-Synthesis)


+ **LLM-grounded Video Diffusion Models** (29 Sep 2023)<details><summary>Long Lian, Baifeng Shi, Adam Yala, et al.</summary>Long Lian, Baifeng Shi, Adam Yala, Trevor Darrell, Boyi Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.17444)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F87bf66eb6d22df17f70170a0e575b4f12c4813ef%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLM-grounded-Video-Diffusion-Models-Lian-Shi/87bf66eb6d22df17f70170a0e575b4f12c4813ef)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llm-grounded-video-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/TonyLianLong/LLM-groundedVideoDiffusion.svg?style=social&label=Star)](https://github.com/TonyLianLong/LLM-groundedVideoDiffusion)


+ **Mustango: Toward Controllable Text-to-Music Generation** (14 Nov 2023)\
Jan Melechovsky, Zixun Guo, Deepanway Ghosal, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.08355)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F26d51f1353353fc4e87d8cb2db0caf255e9ee434%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Mustango%3A-Toward-Controllable-Text-to-Music-Melechovsk%C3%BD-Guo/26d51f1353353fc4e87d8cb2db0caf255e9ee434)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://amaai-lab.github.io/mustango/)
[![Code](https://img.shields.io/github/stars/amaai-lab/mustango.svg?style=social&label=Star)](https://github.com/amaai-lab/mustango)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/declare-lab/mustango)

+ **Music ControlNet: Multiple Time-varying Controls for Music Generation** (13 Nov 2023)\
Shih-Lun Wu, Chris Donahue, Shinji Watanabe, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.07069)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F42239e71a712d70cd24e06ffc0cf0d22fc628a36%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Music-ControlNet%3A-Multiple-Time-varying-Controls-Wu-Donahue/42239e71a712d70cd24e06ffc0cf0d22fc628a36)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://musiccontrolnet.github.io/web/)

+ **Controllable Music Production with Diffusion Models and Guidance Gradients** (1 Nov 2023)\
Mark Levy, Bruno Di Giorgi, Floris Weers, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.00613)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F87e36f66b0c28ca7a327257ccb00282bdf7fe7d5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Controllable-Music-Production-with-Diffusion-Models-Levy-Giorgi/87e36f66b0c28ca7a327257ccb00282bdf7fe7d5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://machinelearning.apple.com/research/controllable-music)

+ **JEN-1 Composer: A Unified Framework for High-Fidelity Multi-Track Music Generation** (29 Oct 2023)\
Yao Yao, Peike Li, Boyu Chen, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.19180)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/JEN-1-Composer%3A-A-Unified-Framework-for-Multi-Track-Yao-Li/53612c6896c680c9113f967d4c2dae908dd10bfe)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.jenmusic.ai/audio-demos)

+ **MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models** (18 Oct 2023)\
Dingyao Yu, Kaitao Song, Peiling Lu, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.11954)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MusicAgent%3A-An-AI-Agent-for-Music-Understanding-and-Yu-Song/beaf64df85f8204b8cd89a7f46827608e6d16922)
[![Code](https://img.shields.io/github/stars/microsoft/muzic.svg?style=social&label=Star)](https://github.com/microsoft/muzic/tree/main/musicagent)

+ **Audiogen: Textually guided audio generation** (30 Sep 2022)\
Felix Kreuk, Gabriel Synnaeve, Adam Polyak, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2209.15352)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Febb85974e06c4879b451fdfcb4f472a09471935b%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/AudioGen%3A-Textually-Guided-Audio-Generation-Kreuk-Synnaeve/ebb85974e06c4879b451fdfcb4f472a09471935b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://felixkreuk.github.io/audiogen/)

+ **Music understanding LLaMA: Advancing text-to-music generation with question answering and captioning** (22 Aug 2023)\
Shansong Liu, Atin Sakkeer Hussain, Chenshuo Sun, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.11276)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Music-Understanding-LLaMA%3A-Advancing-Text-to-Music-Liu-Hussain/a33b437618be733fea7176bd98e18b6362af0838)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://crypto-code.github.io/MU-LLaMA-Demo/)
[![Code](https://img.shields.io/github/stars/crypto-code/MU-LLaMA.svg?style=social&label=Star)](https://github.com/crypto-code/MU-LLaMA)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/datasets/mu-llama/MusicQA)

+ **AudioLDM 2: Learning holistic audio generation with self-supervised pretraining** (10 Aug 2023)\
Haohe Liu, Qiao Tian, Yi Yuan, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.05734)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F33de773be1733347a01cb07a5bb1b6cdfa956a47%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/AudioLDM-2%3A-Learning-Holistic-Audio-Generation-with-Liu-Tian/33de773be1733347a01cb07a5bb1b6cdfa956a47)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://audioldm.github.io/audioldm2/)
[![Code](https://img.shields.io/github/stars/haoheliu/audioldm2.svg?style=social&label=Star)](https://github.com/haoheliu/audioldm2)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/haoheliu/audioldm2-text2audio-text2music)

+ **JEN-1: TEXT-GUIDED UNIVERSAL MUSIC GENERATION WITH OMNIDIRECTIONAL DIFFUSION MODELS** (9 Aug 2023)\
Peike Li, Boyu Chen, Yao Yao, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.04729)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/JEN-1%3A-Text-Guided-Universal-Music-Generation-with-Li-Chen/880bf72f9e2c6a99a759d3be702046e57ce2b423)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.futureverse.com/research/jen/demos/jen1)

+ **MusicLDM: Enhancing Novelty in Text-to-Music Generation Using Beat-Synchronous Mixup Strategies** (3 Aug 2023)\
Ke Chen, Yusong Wu, Haohe Liu, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.01546)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MusicLDM%3A-Enhancing-Novelty-in-Text-to-Music-Using-Chen-Wu/464edfd902f652d3ab6a25dbb6d9fa47cc3246a9)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://musicldm.github.io/)
[![Code](https://img.shields.io/github/stars/RetroCirce/MusicLDM.svg?style=social&label=Star)](https://github.com/RetroCirce/MusicLDM/)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/ucsd-reach/musicldm)

+ **Wavjourney: Compositional audio creation with large language models** (26 Jul 2023)\
Xubo Liu, Zhongkai Zhu, Haohe Liu, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.14335)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/WavJourney%3A-Compositional-Audio-Creation-with-Large-Liu-Zhu/aa7bcd1f9453c9096ec78900a7b94e816ed0e1c5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://audio-agi.github.io/WavJourney_demopage/)
[![Code](https://img.shields.io/github/stars/Audio-AGI/WavJourney.svg?style=social&label=Star)](https://github.com/Audio-AGI/WavJourney)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/Audio-AGI/WavJourney)

+ **Simple and Controllable Music Generation** (8 Jun 2023)\
Jade Copet, Felix Kreuk, Itai Gat, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.05284)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Simple-and-Controllable-Music-Generation-Copet-Kreuk/4cc8e18f5eece0b0d8e1abcb8ee10fb33680fbb2)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ai.honu.io/papers/musicgen/)
[![Code](https://img.shields.io/github/stars/facebookresearch/audiocraft.svg?style=social&label=Star)](https://github.com/facebookresearch/audiocraft)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/facebook/MusicGen)

+ **MuseCoco: Generating Symbolic Music from Text** (31 May 2023)\
Peiling Lu, Xin Xu, Chenfei Kang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.00110)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MuseCoco%3A-Generating-Symbolic-Music-from-Text-Lu-Xu/a559acac0e84319d62cefd564a5eecbf9d566ec4)
[![Code](https://img.shields.io/github/stars/microsoft/muzic.svg?style=social&label=Star)](https://github.com/microsoft/muzic/tree/main/musecoco)

+ **Make-An-Audio 2: Temporal-Enhanced Text-to-Audio Generation** (29 May 2023)\
Jiawei Huang, Yi Ren, Rongjie Huang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.18474)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Make-An-Audio-2%3A-Temporal-Enhanced-Text-to-Audio-Huang-Ren/83d4b22d803ae856cf6b308482bd504fa151d39e)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://make-an-audio-2.github.io/)

+ **Efficient neural music generation** (25 May 2023)\
Max W. Y. Lam, Qiao Tian, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.15719)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Efficient-Neural-Music-Generation-Lam-Tian/38b93d01e08ab19ada89a40051a1ed4309fbe834)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://efficient-melody.github.io/)

+ **Listen, Think, and Understand** (18 May 2023)\
Yuan Gong, Hongyin Luo, Alexander H. Liu, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.10790)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Listen%2C-Think%2C-and-Understand-Gong-Luo/4bb0b12803791764d641a4cef1e0ce39cf049542)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/yuangongfdu/LTU)

+ **Audiogpt: Understanding and generating speech, music, sound, and talking head** (25 Apr 2023)\
Rongjie Huang, Mingze Li, Dongchao Yang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.12995)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/AudioGPT%3A-Understanding-and-Generating-Speech%2C-and-Huang-Li/8bc617c9139648d7a92991d70c671230bac7b2e2)
[![Code](https://img.shields.io/github/stars/AIGC-Audio/AudioGPT.svg?style=social&label=Star)](https://github.com/AIGC-Audio/AudioGPT)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/AIGC-Audio/AudioGPT)

+ **Text-to-Audio Generation using Instruction-Tuned LLM and Latent Diffusion Model** (24 Apr 2023)\
Deepanway Ghosal, Navonil Majumder, Ambuj Mehrish, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.13731)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Text-to-Audio-Generation-using-Instruction-Tuned-Ghosal-Majumder/f51bc74814a3452009ea5ca262d9768d08149ee6)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://tango-web.github.io/)
[![Code](https://img.shields.io/github/stars/declare-lab/tango.svg?style=social&label=Star)](https://github.com/declare-lab/tango)

+ **Noise2music: Text-conditioned music generation with diffusion models** (8 Feb 2023)\
Qingqing Huang, Daniel S. Park, Tao Wang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.03917)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Noise2Music%3A-Text-conditioned-Music-Generation-with-Huang-Park/02540ae926814f4b7972d3fa4dd33932fdc4b58b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://google-research.github.io/noise2music/)

+ **Make-an-audio: Text-to-audio generation with prompt-enhanced diffusion models** (30 Jan 2023)\
Rongjie Huang, Jiawei Huang, Dongchao Yang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.12661)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Make-An-Audio%3A-Text-To-Audio-Generation-with-Models-Huang-Huang/6d1433f3342fbee85ad1e2809e62734aec5c3853)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://text-to-audio.github.io/)
[![Code](https://img.shields.io/github/stars/Text-to-Audio/Make-An-Audio.svg?style=social&label=Star)](https://github.com/Text-to-Audio/Make-An-Audio)

+ **Audioldm: Text-to-audio generation with latent diffusion models** (29 Jan 2023)\
Haohe Liu, Zehua Chen, Yi Yuan, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.12503)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/AudioLDM%3A-Text-to-Audio-Generation-with-Latent-Liu-Chen/fa0f3d8aa20e8987dbc7a516d5399cfa3dc97b1b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://audioldm.github.io)
[![Code](https://img.shields.io/github/stars/haoheliu/audioldm2.svg?style=social&label=Star)](https://github.com/haoheliu/audioldm2)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/haoheliu/audioldm-text-to-audio-generation)

+ **Moûsai: Text-to-Music Generation with Long-Context Latent Diffusion** (27 Jan 2023)\
Flavio Schneider, Ojasv Kamal, Zhijing Jin, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.11757)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Mo%5C%5Eusai%3A-Text-to-Music-Generation-with-Latent-Schneider-Kamal/c5eb040156adf687d7b9a97b3b16f6f243a1a514)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://diligent-pansy-4cb.notion.site/Music-Generation-with-Diffusion-ebe6e9e528984fa1b226d408f6002d87)
[![Code](https://img.shields.io/github/stars/archinetai/audio-diffusion-pytorch.svg?style=social&label=Star)](https://github.com/archinetai/audio-diffusion-pytorch)

+ **MusicLM: Generating Music From Text** (26 Jan 2023)\
Andrea Agostinelli, Timo I. Denk, Zalán Borsos, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2301.11325)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F428854d9e75f94f0e61f37c6887c77800437d516%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MusicLM%3A-Generating-Music-From-Text-Agostinelli-Denk/428854d9e75f94f0e61f37c6887c77800437d516)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://google-research.github.io/seanet/musiclm/examples/)

### Multimodal Language Model-based

### Datasets

## 3D Generation
+ **MotionScript: Natural Language Descriptions for Expressive 3D Human Motions** (19 Dec 2023)\
Payam Jome Yazdian, Eric Liu, Li Cheng, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.12634)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F816792e66f463be2aa1888e4ecb51f8fb2b4dd79%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MotionScript%3A-Natural-Language-Descriptions-for-3D-Yazdian-Liu/816792e66f463be2aa1888e4ecb51f8fb2b4dd79)

+ **HOLODECK: Language Guided Generation of 3D Embodied AI Environments** (14 Dec 2023)\
Yue Yang, Fan-Yun Sun, Luca Weihs, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.09067)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1dbc2cdcae3e17c3d721d12a5a2d98ced727681a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Holodeck%3A-Language-Guided-Generation-of-3D-Embodied-Yang-Sun/1dbc2cdcae3e17c3d721d12a5a2d98ced727681a)
[![Code](https://img.shields.io/github/stars/allenai/Holodeck.svg?style=social&label=Star)](https://github.com/allenai/Holodeck)

+ **PoseGPT: Chatting about 3D Human Pose** (30 Nov 2023)\
Yao Feng, Jing Lin, Sai Kumar Dwivedi, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.18836)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4673c2ac4abb4b055da87171231acb60801ffe74%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/PoseGPT%3A-Chatting-about-3D-Human-Pose-Feng-Lin/4673c2ac4abb4b055da87171231acb60801ffe74)
[![Code](https://img.shields.io/github/stars/yfeng95/PoseGPT.svg?style=social&label=Star)](https://github.com/yfeng95/PoseGPT)

+ **ShapeGPT: 3D Shape Generation with A Unified Multi-modal Language Model** (29 Nov 2023)\ 
Fukun Yin, Xin Chen, Chi Zhang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17618)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5a185965ad1e87367d044b47043706d00b85b007%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ShapeGPT%3A-3D-Shape-Generation-with-A-Unified-Model-Yin-Chen/09157a8c0e7d7263ac035690118ddcbe295cee5c)
[![Code](https://img.shields.io/github/stars/OpenShapeLab/ShapeGPT.svg?style=social&label=Star)](https://github.com/OpenShapeLab/ShapeGPT)

+ **MotionGPT: Human Motion as a Foreign Language** (2023)\
Biao Jiang*, Xin Chen*, Wen Liu, et al.(NeurIPS 2023)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2306.14795.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd212fa27f5868f0fd106e1a7bba908fd47da0816%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MotionGPT%3A-Human-Motion-as-a-Foreign-Language-Jiang-Chen/d212fa27f5868f0fd106e1a7bba908fd47da0816)
[![Code](https://img.shields.io/github/stars/OpenMotionLab/MotionGPT.svg?style=social&label=Star)](https://github.com/OpenMotionLab/MotionGPT)

+ **3D-GPT: Procedural 3D MODELING WITH LARGE LANGUAGE MODELS** (2023)\
Chunyi Sun*, Junlin Han*, Weijian Deng, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.12945)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F588930cdd801f335b5e524d13f99aa94136a20a0%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/3D-GPT%3A-Procedural-3D-Modeling-with-Large-Language-Sun-Han/588930cdd801f335b5e524d13f99aa94136a20a0)
[![Code](https://img.shields.io/github/stars/Chuny1/3DGPT.svg?style=social&label=Star)](https://github.com/Chuny1/3DGPT)




### Multimodal Language Model-based
#### General Object

+ **DreamFusion: Text-to-3D using 2D Diffusion** (2023)\
Ben Poole, Ajay Jain, Jonathan T. Barron, et al. (ICLR2023 Oral)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2209.14988.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4c94d04afa4309ec2f06bdd0fe3781f91461b362%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/DreamFusion%3A-Text-to-3D-using-2D-Diffusion-Poole-Jain/4c94d04afa4309ec2f06bdd0fe3781f91461b362)
 
+ **Magic3D: High-Resolution Text-to-3D Content Creation** (2022)\
Chen-Hsuan Lin, Jun Gao, Luming Tang, et al. (CVPR2023 HighLight)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2023/papers/Lin_Magic3D_High-Resolution_Text-to-3D_Content_Creation_CVPR_2023_paper.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fbdf4af8311637c681904e71cf50f96fd0026f578%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Magic3D%3A-High-Resolution-Text-to-3D-Content-Lin-Gao/bdf4af8311637c681904e71cf50f96fd0026f578)

+ **Clip-forge: Towards zero-shot text-to-shape generation** (2022)\
Sanghi, Aditya, et al. (CVPR 2022)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2110.02624.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F738e3e0623054da29dc57fc6aee5e6711867c4e8%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CLIP-Forge%3A-Towards-Zero-Shot-Text-to-Shape-Sanghi-Chu/738e3e0623054da29dc57fc6aee5e6711867c4e8)
[![Code](https://img.shields.io/github/stars/AutodeskAILab/Clip-Forge.svg?style=social&label=Star)](https://github.com/AutodeskAILab/Clip-Forge)

+ **Zero-Shot Text-Guided Object Generation with Dream Fields** (2 Dec 2021) <details><summary>Ajay Jain, Ben Mildenhall, Jonathan T. Barron, et al. (CVPR2022)</summary>Ajay Jain, Ben Mildenhall, Jonathan T. Barron, Pieter Abbeel, Ben Poole</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2112.01455.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F03e1c3b5fdad9b21bbed3d13af7e8d6c73cbcfa6%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Zero-Shot-Text-Guided-Object-Generation-with-Dream-Jain-Mildenhall/03e1c3b5fdad9b21bbed3d13af7e8d6c73cbcfa6)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ajayj.com/dreamfields)
[![Code](https://img.shields.io/github/stars/google-research/google-research.svg?style=social&label=Star)](https://github.com/google-research/google-research/)

+ **Text2Mesh: Text-Driven Neural Stylization for Meshes** (2022)\
Oscar Michel, Roi Bar-On, Richard Liu, et al. (CVPR 2022)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2110.02624.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd15b27edf3630728cdb40f49946365d9011641cf%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Text2Mesh%3A-Text-Driven-Neural-Stylization-for-Michel-Bar-On/d15b27edf3630728cdb40f49946365d9011641cf)
[![Code](https://img.shields.io/github/stars/threedle/text2mesh.svg?style=social&label=Star)](https://github.com/threedle/text2mesh)

#### Avatar
+ **CLIP-Head: Text-Guided Generation of Textured Neural Parametric 3D Head Models** (25 Nov 2023)<details><summary>Pranav Manu, Astitva Srivastava, Avinash Sharma. SIGGRAPH Asia 2023.</summary>Pranav Manu, Astitva Srivastava, Avinash Sharma</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://raipranav384.github.io/clip_head/static/videos/Clip_Head.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F3c99ad4cf2fdd4417bcb591686bd23500b1b4a46%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CLIP-Head%3A-Text-Guided-Generation-of-Textured-3D-Manu-Srivastava/3c99ad4cf2fdd4417bcb591686bd23500b1b4a46)
[![Code](https://img.shields.io/github/stars/raipranav384/CLIP-Head.svg?style=social&label=Star)](https://github.com/raipranav384/CLIP-Head)

### Datasets

# LLMs for Audiovisual Editing

## Image Editing

+ **CHATEDIT: Towards Multi-turn Interactive Facial Image Editing via Dialogue** (20 Mar 2023)\
Cui, Xing, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.11108)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5a185965ad1e87367d044b47043706d00b85b007%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CHATEDIT%3A-Towards-Multi-turn-Interactive-Facial-via-Cui-Li/5a185965ad1e87367d044b47043706d00b85b007)
[![Code](https://img.shields.io/github/stars/cuixing100876/ChatEdit.svg?style=social&label=Star)](https://github.com/cuixing100876/ChatEdit)

+ **Guiding Instruction-based Image Editing via Multimodal Large Language Models** (29 Sep 2023)\
Fu, Tsu-Jui, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.17102v1)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F092245d86b77181c36f972b1b7a17a59cd989c4a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Guiding-Instruction-based-Image-Editing-via-Large-Fu-Hu/092245d86b77181c36f972b1b7a17a59cd989c4a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://mllm-ie.github.io/)
[![Code](https://img.shields.io/github/stars/tsujuifu/pytorch_mgie.svg?style=social&label=Star)](https://github.com/tsujuifu/pytorch_mgie)

+ **Interactive Image Manipulation with Complex Text Instructions** (25 Nov 2022)\
Ryugo Morita, Zhiqiang Zhang, Man M. Ho, Jinjia Zhou. WACV 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2211.15352)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F387144d293567408c363313aac971294e7ec8547%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Interactive-Image-Manipulation-with-Complex-Text-Morita-Zhang/387144d293567408c363313aac971294e7ec8547)

+ **InstructPix2Pix: Learning to Follow Image Editing Instructions** (17 Nov 2022)\
Brooks, Tim, Aleksander Holynski, and Alexei A. Efros. CVPR 2023 (Highlight).\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2211.09800)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fa2d2bbe4c542173662a444b33b76c66992697830%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InstructPix2Pix%3A-Learning-to-Follow-Image-Editing-Brooks-Holynski/a2d2bbe4c542173662a444b33b76c66992697830)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.timothybrooks.com/instruct-pix2pix)
[![Code](https://img.shields.io/github/stars/timothybrooks/instruct-pix2pix.svg?style=social&label=Star)](https://github.com/timothybrooks/instruct-pix2pix)


+ **Emu Edit: Precise Image Editing via Recognition and Generation Tasks** (16 Nov 2023)\
Shelly Sheynin, Adam Polyak, Uriel Singer, Yuval Kirstain, Amit Zohar, Oron Ashual, Devi Parikh, Yaniv Taigman. ArXiv 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.10089)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5bcb0153dd0840113eb27d4d6f753414ef656a03%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Emu-Edit%3A-Precise-Image-Editing-via-Recognition-and-Sheynin-Polyak/5bcb0153dd0840113eb27d4d6f753414ef656a03)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://emu-edit.metademolab.com/)


+ **Self-correcting LLM-controlled Diffusion Models** (27 Nov 2023)\
Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, Boyi Li, Trevor Darrell. ArXiv 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16090)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Self-correcting-LLM-controlled-Diffusion-Models-Wu-Lian/42c4315b5d2e33d7d9a0afdf84e6a47ccd7a700e)



### Multimodal Language Model-based


+ **SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations** (2 Aug 2021)\
Chenlin Meng, Yutong He, Yang Song, Jiaming Song, Jiajun Wu, Jun-Yan Zhu, Stefano Ermon. ICLR 2022. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2108.01073)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ff671a09e3e5922e6d38cb77dda8d76d5ceac2a27%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/SDEdit%3A-Guided-Image-Synthesis-and-Editing-with-Meng-He/f671a09e3e5922e6d38cb77dda8d76d5ceac2a27)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://sde-image-editing.github.io/)
[![Code](https://img.shields.io/github/stars/ermongroup/SDEdit.svg?style=social&label=Star)](https://github.com/ermongroup/SDEdit)



+ **DiffEdit: Diffusion-based semantic image editing with mask guidance** (20 Oct 2022) \
Guillaume Couairon, Jakob Verbeek, Holger Schwenk, Matthieu Cord. ICLR 2023 (notable top 25%). \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.11427)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F064ccebc03d3afabaae30fe29a457c1cfcdff7e3%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/DiffEdit%3A-Diffusion-based-semantic-image-editing-Couairon-Verbeek/064ccebc03d3afabaae30fe29a457c1cfcdff7e3)
<!-- [![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ashmrz.github.io/WatchYourSteps/) -->
<!-- [![Code](https://img.shields.io/github/stars/Xiang-cd/DiffEdit-stable-diffusion.svg?style=social&label=Star)](https://github.com/Xiang-cd/DiffEdit-stable-diffusion) -->


+ **Prompt-to-Prompt Image Editing with Cross Attention Control**
Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, Daniel Cohen-Or. ICLR 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2208.01626)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F04e541391e8dce14d099d00fb2c21dbbd8afe87f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Prompt-to-Prompt-Image-Editing-with-Cross-Attention-Hertz-Mokady/04e541391e8dce14d099d00fb2c21dbbd8afe87f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://prompt-to-prompt.github.io/)
[![Code](https://img.shields.io/github/stars/google/prompt-to-prompt.svg?style=social&label=Star)](https://github.com/google/prompt-to-prompt)

+ **Null-text Inversion for Editing Real Images using Guided Diffusion Models** \
Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, Daniel Cohen-Or. ICLR 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2211.09794)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4de94949daf9bc8dd0e5161d20dfe83198d20ec1%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Null-text-Inversion-for-Editing-Real-Images-using-Mokady-Hertz/4de94949daf9bc8dd0e5161d20dfe83198d20ec1)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://null-text-inversion.github.io/)
[![Code](https://img.shields.io/github/stars/google/prompt-to-prompt.svg?style=social&label=Star)](https://github.com/google/prompt-to-prompt/#null-text-inversion-for-editing-real-images)

+ **Imagic: Text-Based Real Image Editing with Diffusion Models** (17 Oct 2022)\
Bahjat Kawar, Shiran Zada, Oran Lang, Omer Tov, Huiwen Chang, Tali Dekel, Inbar Mosseri, Michal Irani. CVPR 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2210.09276)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F23e261a20a315059b4de5492ed071c97a20c12e7%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Imagic%3A-Text-Based-Real-Image-Editing-with-Models-Kawar-Zada/23e261a20a315059b4de5492ed071c97a20c12e7)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://imagic-editing.github.io/)
<!-- [![Code](https://img.shields.io/github/stars/pix2pixzero/pix2pix-zero.svg?style=social&label=Star)](https://github.com/pix2pixzero/pix2pix-zero) -->


+ **Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation** (22 Nov 2022) \
Narek Tumanyan, Michal Geyer, Shai Bagon, Tali Dekel. CVPR 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2211.12572)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fb000d6865db824af1563708fb7a545ddd65c6b3a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Plug-and-Play-Diffusion-Features-for-Text-Driven-Tumanyan-Geyer/b000d6865db824af1563708fb7a545ddd65c6b3a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://pnp-diffusion.github.io/)
[![Code](https://img.shields.io/github/stars/MichalGeyer/plug-and-play.svg?style=social&label=Star)](https://github.com/MichalGeyer/plug-and-play)


+ **SINE: SINgle Image Editing with Text-to-Image Diffusion Models** (8 Dec 2022) \
Zhixing Zhang, Ligong Han, Arnab Ghosh, Dimitris Metaxas, Jian Ren. CVPR 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.04489)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fa6ad30123bef4b19ee40c3d63cfabf00d211f0ef%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/SINE%3A-SINgle-Image-Editing-with-Text-to-Image-Zhang-Han/a6ad30123bef4b19ee40c3d63cfabf00d211f0ef)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://zhang-zx.github.io/SINE/)
[![Code](https://img.shields.io/github/stars/zhang-zx/SINE.svg?style=social&label=Star)](https://github.com/zhang-zx/SINE)


+ **Zero-shot Image-to-Image Translation** (6 Feb 2023) \
Gaurav Parmar, Krishna Kumar Singh, Richard Zhang, Yijun Li, Jingwan Lu, Jun-Yan Zhu
. SIGGRAPH 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2302.03027)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fdaf61010eee0fbf6f9bab7db71c395ffca6f3ff3%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Zero-shot-Image-to-Image-Translation-Parmar-Singh/daf61010eee0fbf6f9bab7db71c395ffca6f3ff3)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://pix2pixzero.github.io/)
[![Code](https://img.shields.io/github/stars/pix2pixzero/pix2pix-zero.svg?style=social&label=Star)](https://github.com/pix2pixzero/pix2pix-zero)

+ **MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing** (17 Apr 2023)\
Mingdeng Cao, Xintao Wang, Zhongang Qi, Ying Shan, Xiaohu Qie, Yinqiang Zheng. ICCV 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.08947)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F85963807c11abe38e9a2797d9860e012238607ef%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MasaCtrl%3A-Tuning-Free-Mutual-Self-Attention-Control-Cao-Wang/85963807c11abe38e9a2797d9860e012238607ef)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ljzycmd.github.io/projects/MasaCtrl/)
[![Code](https://img.shields.io/github/stars/TencentARC/MasaCtrl.svg?style=social&label=Star)](https://github.com/TencentARC/MasaCtrl)


+ **Watch Your Steps: Local Image and Scene Editing by Text Instructions** (17 Nov 2023)\
Tsung-Han Wu, Long Lian, Joseph E. Gonzalez, Boyi Li, Trevor Darrell. ArXiv 2023. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.08947)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F737ad8905228cd410e3342b5cceefd4feb57d166%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Watch-Your-Steps%3A-Local-Image-and-Scene-Editing-by-Mirzaei-Aumentado-Armstrong/737ad8905228cd410e3342b5cceefd4feb57d166)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ashmrz.github.io/WatchYourSteps/)


## Video Editing

+ **InstructVid2Vid: Controllable Video Editing with Natural Language Instructions** (21 May 2023)\
Bosheng Qin, Juncheng Li, Siliang Tang, Tat-Seng Chua, Yueting Zhuang. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.12328)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F205d2ed0906440f07a0275d7d6a63bced60951fc%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InstructVid2Vid%3A-Controllable-Video-Editing-with-Qin-Li/205d2ed0906440f07a0275d7d6a63bced60951fc)
<!-- [![Code](https://img.shields.io/github/stars/duyguceylan/pix2video.svg?style=social&label=Star)](https://github.com/duyguceylan/pix2video) -->

+ **CONSISTENT VIDEO-TO-VIDEO TRANSFER USING SYNTHETIC DATASET** (1 Nov 2023)\
Jiaxin Cheng, Tianjun Xiao, Tong He. ArXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.00213)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fe8bbffb8413cb1f88e99a7ecbabd21a6eac82271%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Consistent-Video-to-Video-Transfer-Using-Synthetic-Cheng-Xiao/e8bbffb8413cb1f88e99a7ecbabd21a6eac82271)
[![Code](https://img.shields.io/github/stars/amazon-science/instruct-video-to-video.svg?style=social&label=Star)](https://github.com/amazon-science/instruct-video-to-video)





### Multimodal Language Model-based

+ **M3L: Language-based Video Editing via Multi-Modal Multi-Level Transformers** (2 Apr 2021)\
Tsu-Jui Fu, Xin Eric Wang, Scott T. Grafton, Miguel P. Eckstein, William Yang Wang. CVPR 2022.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2104.01122)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F81349524489f8ba0812ac2529eac92ec45959782%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Language-based-Video-Editing-via-Multi-Modal-Fu-Wang/81349524489f8ba0812ac2529eac92ec45959782)

+ **Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation** (22 Dec 2022)\
Jay Zhangjie Wu, Yixiao Ge, Xintao Wang, Weixian Lei, Yuchao Gu, Yufei Shi, Wynne Hsu, Ying Shan, Xiaohu Qie, Mike Zheng Shou. ICCV 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2212.11565)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1367dcff4ccb927a5e95c452041288b3f0dd0eff%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Tune-A-Video%3A-One-Shot-Tuning-of-Image-Diffusion-Wu-Ge/1367dcff4ccb927a5e95c452041288b3f0dd0eff)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://fate-zero-edit.github.io/)
[![Code](https://img.shields.io/github/stars/showlab/Tune-A-Video.svg?style=social&label=Star)](https://tuneavideo.github.io/)

+ **Video-P2P: Video Editing with Cross-attention Control** (8 Mar 2023)\
Shaoteng Liu, Yuechen Zhang, Wenbo Li, Zhe Lin, Jiaya Jia. arXiv 2022.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.04761)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F6283502d6900a0b403e2454b1cb1cf16ddefd5a7%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Video-P2P%3A-Video-Editing-with-Cross-attention-Liu-Zhang/6283502d6900a0b403e2454b1cb1cf16ddefd5a7)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://video-p2p.github.io/)
[![Code](https://img.shields.io/github/stars/ShaoTengLiu/Video-P2P.svg?style=social&label=Star)](https://github.com/ShaoTengLiu/Video-P2P)

+ **FateZero: Fusing Attentions for Zero-shot Text-based Video Editing** (16 Mar 2023)\
Chenyang Qi, Xiaodong Cun, Yong Zhang, Chenyang Lei, Xintao Wang, Ying Shan, Qifeng Chen. ICCV 2023 (Oral).\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.09535)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F14ccb8bcceb6de10eda6ad08bec242a4f2946497%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/FateZero%3A-Fusing-Attentions-for-Zero-shot-Video-Qi-Cun/14ccb8bcceb6de10eda6ad08bec242a4f2946497)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://fate-zero-edit.github.io/)
[![Code](https://img.shields.io/github/stars/ChenyangQiQi/FateZero.svg?style=social&label=Star)](https://github.com/ChenyangQiQi/FateZero)


+ **Pix2Video: Video Editing using Image Diffusion** (22 Mar 2023)\
Ceylan, Duygu, Chun-Hao P. Huang, and Niloy J. Mitra. ICCV 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.12688)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F32a3c2fbd3e733bd0eea938517fec2ff8dc7c701%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Pix2Video%3A-Video-Editing-using-Image-Diffusion-Ceylan-Huang/32a3c2fbd3e733bd0eea938517fec2ff8dc7c701)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://duyguceylan.github.io/pix2video.github.io/)
[![Code](https://img.shields.io/github/stars/duyguceylan/pix2video.svg?style=social&label=Star)](https://github.com/duyguceylan/pix2video)

+ **Make-A-Protagonist: Generic Video Editing with An Ensemble of Experts** (15 May 2023)
Michal Geyer, Omer Bar-Tal, Shai Bagon, Tali Dekel. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.08850)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5f51eda9f7abddca027941d50fb0b6bf6f508eff%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Make-A-Protagonist%3A-Generic-Video-Editing-with-An-Zhao-Xie/5f51eda9f7abddca027941d50fb0b6bf6f508eff)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://make-a-protagonist.github.io/)
[![Code](https://img.shields.io/github/stars/HeliosZhao/Make-A-Protagonist.svg?style=social&label=Star)](https://github.com/HeliosZhao/Make-A-Protagonist)

+ **ControlVideo: Adding Conditional Control for One Shot Text-to-Video Editing** (26 May 2023)
Min Zhao, Rongzhen Wang, Fan Bao, Chongxuan Li, Jun Zhu. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.17098)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F14acc36d8c87f31f8dcbbf8433b91af70a2a516a%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ControlVideo%3A-Conditional-Control-for-One-shot-and-Zhao-Wang/14acc36d8c87f31f8dcbbf8433b91af70a2a516a)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://ml.cs.tsinghua.edu.cn/controlvideo/)
[![Code](https://img.shields.io/github/stars/thu-ml/controlvideo.svg?style=social&label=Star)](https://github.com/thu-ml/controlvideo)

+ **Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation** (13 Jun 2023)\
Shuai Yang, Yifan Zhou, Ziwei Liu, Chen Change Loy. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.07954)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1e09b83fe064826a9a1ac61a7bdc00f26be41aee%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Rerender-A-Video%3A-Zero-Shot-Text-Guided-Translation-Yang-Zhou/1e09b83fe064826a9a1ac61a7bdc00f26be41aee)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://www.mmlab-ntu.com/project/rerender/)
[![Code](https://img.shields.io/github/stars/williamyang1991/Rerender_A_Video.svg?style=social&label=Star)](https://github.com/williamyang1991/Rerender_A_Video)


+ **TokenFlow: Consistent Diffusion Features for Consistent Video Editing** (19 Jul 2023) \
Michal Geyer, Omer Bar-Tal, Shai Bagon, Tali Dekel. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.10373)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4761f173965195798cd3046ef4af608a83504e4d%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/TokenFlow%3A-Consistent-Diffusion-Features-for-Video-Geyer-Bar-Tal/4761f173965195798cd3046ef4af608a83504e4d)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://diffusion-tokenflow.github.io/)
[![Code](https://img.shields.io/github/stars/omerbt/TokenFlow.svg?style=social&label=Star)](https://github.com/omerbt/TokenFlow)


+ **CoDeF: Content Deformation Fields for Temporally Consistent Video Processing** (15 Aug 2023) \
Hao Ouyang, Qiuyu Wang, Yuxi Xiao, Qingyan Bai, Juntao Zhang, Kecheng Zheng, Xiaowei Zhou, Qifeng Chen, Yujun Shen. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.07926)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fc2d65fc3a7fde3f7662c6ef9448e5737d7e5551f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CoDeF%3A-Content-Deformation-Fields-for-Temporally-Hao-Wang/c2d65fc3a7fde3f7662c6ef9448e5737d7e5551f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://qiuyu96.github.io/CoDeF/)
[![Code](https://img.shields.io/github/stars/qiuyu96/CoDeF.svg?style=social&label=Star)](https://github.com/qiuyu96/CoDeF)


+ **StableVideo: Text-driven Consistency-aware Diffusion Video Editing** (18 Aug 2023)\
Wenhao Chai, Xun Guo, Gaoang Wang, Yan Lu. ICCV 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.09592)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F05cbac9a5101f47a6fabad72398616506572c9fa%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/StableVideo%3A-Text-driven-Consistency-aware-Video-Chai-Guo/05cbac9a5101f47a6fabad72398616506572c9fa)
[![Code](https://img.shields.io/github/stars/rese1f/StableVideo.svg?style=social&label=Star)](https://github.com/rese1f/StableVideo)


+ **MagicEdit: High-Fidelity Temporally Coherent Video Editing** (28 Aug 2023) \
Jun Hao Liew, Hanshu Yan, Jianfeng Zhang, Zhongcong Xu, Jiashi Feng. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.14749)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F8819777e104f8c4197c262e11a01b070b50007aa%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MagicEdit%3A-High-Fidelity-and-Temporally-Coherent-Liew-Yan/8819777e104f8c4197c262e11a01b070b50007aa)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://magic-edit.github.io/)
[![Code](https://img.shields.io/github/stars/magic-research/magic-edit.svg?style=social&label=Star)](https://github.com/magic-research/magic-edit)

+ **MagicStick: Controllable Video Editing via Control Handle Transformations** (1 Nov 2023)<details><summary>Yue Ma, Xiaodong Cun, Yingqing He, et al.</summary>Yue Ma, Xiaodong Cun, Yingqing He, Chenyang Qi, Xintao Wang, Ying Shan, Xiu Li, Qifeng Chen</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.03047)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fxxx%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Consistent-Video-to-Video-Transfer-Using-Synthetic-Cheng-Xiao/xxx)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://magic-stick-edit.github.io/)
[![Code](https://img.shields.io/github/stars/mayuelala/MagicStick.svg?style=social&label=Star)](https://github.com/mayuelala/MagicStick)


+ **LATENTWARP: CONSISTENT DIFFUSION LATENTS FOR ZERO-SHOT VIDEO-TO-VIDEO TRANSLATION** (1 Nov 2023)\
Yuxiang Bao, Di Qiu, Guoliang Kang, Baochang Zhang, Bo Jin, Kaiye Wang, Pengfei Yan. arXiv 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.00353)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1b4323a5324ee20fe9b2ff2a65ec26550a51ec2c%3Ffields%3DcitationCount)](https://semanticscholar.org/paper/LatentWarp%3A-Consistent-Diffusion-Latents-for-Bao-Qiu/1b4323a5324ee20fe9b2ff2a65ec26550a51ec2c)
<!-- [![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://diffusion-tokenflow.github.io/) -->
<!-- [![Code](https://img.shields.io/github/stars/omerbt/TokenFlow.svg?style=social&label=Star)](https://github.com/omerbt/TokenFlow) -->



## Audio Editing
### Multimodal Language Model-based


## 3D Editing

### Multimodal Language Model-based
#### Avatar
+ **ClipFace: Text-guided Editing of Textured 3D Morphable Models** (July 2023)\
SHIVANGI ANEJA, JUSTUS THIES, et al. SIGGRAPH 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2212.01406.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ff21e8eddf42580d1f38a11ec5acd8891c0454a1f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ClipFace%3A-Text-guided-Editing-of-Textured-3D-Models-Aneja-Thies/f21e8eddf42580d1f38a11ec5acd8891c0454a1f)
[![Code](https://img.shields.io/github/stars/cassiePython/CLIPNeRF.svg?style=social&label=Star)](https://github.com/cassiePython/CLIPNeRF)
#### General Object
+ **CLIP-NeRF: Text-and-Image Driven Manipulation of Neural Radiance Fields** (2022)\
Can Wang, et al. CVPR 2022.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2112.05139.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F0483be6c3ec6cd41ffe248f86effc7468d3ac7be%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CLIP-NeRF%3A-Text-and-Image-Driven-Manipulation-of-Wang-Chai/0483be6c3ec6cd41ffe248f86effc7468d3ac7be)
[![Code](https://img.shields.io/github/stars/shivangi-aneja/ClipFace.svg?style=social&label=Star)](https://github.com/shivangi-aneja/ClipFace)

+ **Blending-NeRF: Text-Driven Localized Editing in Neural Radiance Fields** (2023)\
Hyeonseop Song, Seokhun Choi, Hoseok Do, et al. ICCV 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.11974)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fbf7f31e07d9b128a0f555c275bc3fdb851f725b8%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Blending-NeRF%3A-Text-Driven-Localized-Editing-in-Song-Choi/bf7f31e07d9b128a0f555c275bc3fdb851f725b8)

# Multi-Modal Agents

+ **LLaVA-Interactive: An All-in-One Demo for Image Chat, Segmentation, Generation and Editing** (1 Nov 2023) <details><summary>Wei-Ge Chen, Irina Spiridonova, Jianwei Yang, et al.</summary> Wei-Ge Chen, Irina Spiridonova, Jianwei Yang, Jianfeng Gao, Chunyuan Li</details>
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.00571)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fc020f15be1dee20f9e2e0c5a6f05f272b5508325%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLaVA-Interactive%3A-An-All-in-One-Demo-for-Image-and-Chen-Spiridonova/c020f15be1dee20f9e2e0c5a6f05f272b5508325)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llava-vl.github.io/llava-interactive)
[![Code](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-Interactive-Demo.svg?style=social&label=Star)](https://github.com/LLaVA-VL/LLaVA-Interactive-Demo)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://llavainteractive.ngrok.app/)\
**Tags:** `Image Chat` `Image Segmentation`, `Image Generation` `Image Editing`

+ **ControlLLM: Augment Language Models with Tools by Searching on Graphs** (26 Oct 2023)\
Liu, Zhaoyang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.17796)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F288e7224d53d68669eb67f2496e068dc965c639e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ControlLLM%3A-Augment-Language-Models-with-Tools-by-Liu-Lai/288e7224d53d68669eb67f2496e068dc965c639e)
[![Code](https://img.shields.io/github/stars/OpenGVLab/ControlLLM.svg?style=social&label=Star)](https://github.com/OpenGVLab/ControlLLM)\
**Tags:** `Image Understanding` `Image Generation` `Image Editing` `Video Understanding` `Video Generation` `Video Editing` `Audio Understanding` `Audio Generation`

+ **ImageBind-LLM: Multi-modality Instruction Tuning** (7 Sep 2023)\
Han, Jiaming, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.03905)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F54c68b8623505dc6bf7a0b08aaa77ca9165f2d7f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/ImageBind-LLM%3A-Multi-modality-Instruction-Tuning-Han-Zhang/54c68b8623505dc6bf7a0b08aaa77ca9165f2d7f)
[![Code](https://img.shields.io/github/stars/OpenGVLab/LLaMA-Adapter.svg?style=social&label=Star)](https://github.com/OpenGVLab/LLaMA-Adapter)\
**Condition Modality:** `text` `image` `video` `audio` `point cloud`

+ **InternGPT: Solving Vision-Centric Tasks by Interacting with ChatGPT Beyond Language** (9 May 2023)\
Liu, Zhaoyang, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.05662)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F54a8b153ed04a872da878d695239bdc413dc782c%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InternGPT%3A-Solving-Vision-Centric-Tasks-by-with-Liu-He/54a8b153ed04a872da878d695239bdc413dc782c)
[![Code](https://img.shields.io/github/stars/OpenGVLab/InternGPT.svg?style=social&label=Star)](https://github.com/OpenGVLab/InternGPT)

+ **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face** (30 Mar 2023)\
Shen, Yongliang, et al. NeurIPS 2023 \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.17580)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd1120d67b700e4dfe8b39eb1e48fbdea4e1a0c43%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/HuggingGPT%3A-Solving-AI-Tasks-with-ChatGPT-and-its-Shen-Song/d1120d67b700e4dfe8b39eb1e48fbdea4e1a0c43)
[![Code](https://img.shields.io/github/stars/microsoft/JARVIS.svg?style=social&label=Star)](https://github.com/microsoft/JARVIS)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/microsoft/HuggingGPT)

+ **Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models** (8 Mar 2023)\
Wu, Chenfei, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.04671)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Faf997821231898a5f8d0fd78dad4eec526acabe5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Visual-ChatGPT%3A-Talking%2C-Drawing-and-Editing-with-Wu-Yin/af997821231898a5f8d0fd78dad4eec526acabe5)
[![Code](https://img.shields.io/github/stars/microsoft/JARVIS.svg?style=social&label=Star)](https://github.com/moymix/TaskMatrix)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/microsoft/visual_chatgpt)

+ **AutoGPT: build & use AI agents**\
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://news.agpt.co/)
[![Code](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT.svg?style=social&label=Star)](https://github.com/Significant-Gravitas/AutoGPT)


# LLMs for Audiovisual Understanding
## Image Understanding
+ **LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models** (28 Nov 2023)\
Li, Yanwei, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.17043)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F486c2df78cbb770a90a55f7fa3fe19102fba2c24%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LLaMA-VID%3A-An-Image-is-Worth-2-Tokens-in-Large-Li-Wang/486c2df78cbb770a90a55f7fa3fe19102fba2c24)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llama-vid.github.io/)
[![Code](https://img.shields.io/github/stars/dvlab-research/LLaMA-VID.svg?style=social&label=Star)](https://github.com/dvlab-research/LLaMA-VID)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](http://103.170.5.190:7864/)

+ **CogVLM: Visual Expert for Pretrained Language Models** (6 Nov 2023)\
Li, Yanwei, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.03079)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F3bf842dec99016da2d309ea8cbd7e25343032317%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/CogVLM%3A-Visual-Expert-for-Pretrained-Language-Wang-Lv/3bf842dec99016da2d309ea8cbd7e25343032317)
[![Code](https://img.shields.io/github/stars/THUDM/CogVLM.svg?style=social&label=Star)](https://github.com/THUDM/CogVLM)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](http://36.103.203.44:7861/)

+ **MiniGPT-v2: large language model as a unified interface for vision-language multi-task learning** (14 Oct 2023)\
Chen, Jun, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2310.09478)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1ddbd08ad8cf22a5c66c4242194c4286328533bf%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MiniGPT-v2%3A-large-language-model-as-a-unified-for-Chen-Zhu/1ddbd08ad8cf22a5c66c4242194c4286328533bf)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://minigpt-v2.github.io/)
[![Code](https://img.shields.io/github/stars/Vision-CAIR/MiniGPT-4.svg?style=social&label=Star)](https://github.com/Vision-CAIR/MiniGPT-4)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/Vision-CAIR/MiniGPT-v2)

+ **OphGLM: Training an Ophthalmology Large Language-and-Vision Assistant based on Instructions and Dialogue** (21 Jun 2023)\
Gao, Weihao, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.12174)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F0f8d12775a4685575f1489796b5dee9e11fbdfb5%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/OphGLM%3A-Training-an-Ophthalmology-Large-Assistant-Gao-Deng/0f8d12775a4685575f1489796b5dee9e11fbdfb5)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://minigpt-v2.github.io/)
[![Code](https://img.shields.io/github/stars/ML-AILab/OphGLM.svg?style=social&label=Star)](https://github.com/ML-AILab/OphGLM)

+ **Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization** (9 Sep 2023)\
Jin, Yang, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.04669)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fbcac614f9774488447221ebb4f16f05e3975ec1e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Unified-Language-Vision-Pretraining-in-LLM-with-Jin-Xu/bcac614f9774488447221ebb4f16f05e3975ec1e)
[![Code](https://img.shields.io/github/stars/jy0205/LaVIT.svg?style=social&label=Star)](https://github.com/jy0205/LaVIT)

+ **NExT-GPT: Any-to-Any Multimodal LLM** (11 Sep 2023)\
Wu, Shengqiong, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.05519)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ffa75a55760e6ea49b39b83cb85c99a22e1088254%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/NExT-GPT%3A-Any-to-Any-Multimodal-LLM-Wu-Fei/fa75a55760e6ea49b39b83cb85c99a22e1088254)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://next-gpt.github.io/)
[![Code](https://img.shields.io/github/stars/NExT-GPT/NExT-GPT.svg?style=social&label=Star)](https://github.com/NExT-GPT/NExT-GPT)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://1ca8b1601858a12830.gradio.live/)

+ **Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond** (24 Aug 2023)\
Bai, Jinze, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2308.12966)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ffc6a2f7478f68adefd69e2071f27e38aa1647f2f%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Qwen-VL%3A-A-Versatile-Vision-Language-Model-for-Text-Bai-Bai/fc6a2f7478f68adefd69e2071f27e38aa1647f2f)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://github.com/QwenLM/Qwen-VL/blob/master/TUTORIAL.md)
[![Code](https://img.shields.io/github/stars/QwenLM/Qwen-VL.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen-VL)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://modelscope.cn/studios/qwen/Qwen-VL-Chat-Demo/summary)

+ **VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks** (18 May 2023)\
Wang, Wenhai, et al. NeurIPS 2023.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.11175)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F42a30dc5470f54ec249f25d3c31e05d7c376c8e3%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VisionLLM%3A-Large-Language-Model-is-also-an-Decoder-Wang-Chen/42a30dc5470f54ec249f25d3c31e05d7c376c8e3)
[![Code](https://img.shields.io/github/stars/OpenGVLab/VisionLLM.svg?style=social&label=Star)](https://github.com/OpenGVLab/VisionLLM)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://github.com/OpenGVLab/InternGPT)

+ **InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning** (11 May 2023)\
Dai, Wenliang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.06500)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F8bd6a2a89503be083176f2cc26fabedb79238cbd%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/InstructBLIP%3A-Towards-General-purpose-Models-with-Dai-Li/8bd6a2a89503be083176f2cc26fabedb79238cbd)
[![Code](https://img.shields.io/github/stars/QwenLM/Qwen-VL.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen-VL)

+ **MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models** (20 Apr 2023)\
Zhu, Deyao, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.10592)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fca6a2bc279be5a3349a22bfd6866ed633d18734b%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/MiniGPT-4%3A-Enhancing-Vision-Language-Understanding-Zhu-Chen/ca6a2bc279be5a3349a22bfd6866ed633d18734b)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://minigpt-4.github.io/)
[![Code](https://img.shields.io/github/stars/Vision-CAIR/MiniGPT-4.svg?style=social&label=Star)](https://github.com/Vision-CAIR/MiniGPT-4)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/Vision-CAIR/MiniGPT-v2)

+ **Visual Instruction Tuning** (17 Apr 2023)\
Liu, Haotian, et al. NeurIPS 2023 (oral).\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.08485)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F1a8eb2cae1833df3bf12fe3b41b03d60b4a4a98d%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Visual-Instruction-Tuning-Liu-Li/1a8eb2cae1833df3bf12fe3b41b03d60b4a4a98d)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://llava-vl.github.io/)
[![Code](https://img.shields.io/github/stars/haotian-liu/LLaVA.svg?style=social&label=Star)](https://github.com/haotian-liu/LLaVA)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://llava.hliu.cc/)


## Video Understanding
+ **Video-Bench: A Comprehensive Benchmark and Toolkit for Evaluating Video-based Large Language Models** (27 Nov 2023)\
Ning, Munan, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.16103)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fb037bb09aa162d8a543e64ec777ca0edc732d2af%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Video-Bench%3A-A-Comprehensive-Benchmark-and-Toolkit-Ning-Zhu/b037bb09aa162d8a543e64ec777ca0edc732d2af)
[![Code](https://img.shields.io/github/stars/PKU-YuanGroup/Video-Bench.svg?style=social&label=Star)](https://github.com/PKU-YuanGroup/Video-Bench)

+ **PG-Video-LLaVA: Pixel Grounding Large Video-Language Models** (22 Nov 2023)\
Munasinghe, Shehan, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.13435)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4edbb942c2d20a6f5a4e3caa763a9761be953231%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/PG-Video-LLaVA%3A-Pixel-Grounding-Large-Models-Munasinghe-Thushara/4edbb942c2d20a6f5a4e3caa763a9761be953231)
[![Code](https://img.shields.io/github/stars/mbzuai-oryx/Video-LLaVA.svg?style=social&label=Star)](https://github.com/mbzuai-oryx/Video-LLaVA)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://mbzuai-oryx.github.io/Video-LLaVA/)

+ **Video-LLaVA: Learning United Visual Representation by Alignment Before Projection** (16 Nov 2023)\
Lin, Bin, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.10122)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F107fb6eec2febbae12db29bf3e311aaf5680027c%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Video-LLaVA%3A-Learning-United-Visual-Representation-Lin-Zhu/107fb6eec2febbae12db29bf3e311aaf5680027c)
[![Code](https://img.shields.io/github/stars/PKU-YuanGroup/Video-LLaVA.svg?style=social&label=Star)](https://github.com/PKU-YuanGroup/Video-LLaVA)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/LanguageBind/Video-LLaVA)

+ **Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding** (14 Nov 2023)\
Jin, Peng, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.08046)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Faad3d2e690f6c73f04a14622ceff51464bbc560e%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Chat-UniVi%3A-Unified-Visual-Representation-Empowers-Jin-Takanobu/aad3d2e690f6c73f04a14622ceff51464bbc560e)
[![Code](https://img.shields.io/github/stars/PKU-YuanGroup/Chat-UniVi.svg?style=social&label=Star)](https://github.com/PKU-YuanGroup/Chat-UniVi)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/Chat-UniVi/Chat-UniVi)


+ **Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding** (5 Jun 2023)\
Zhang, Hang, Xin Li, and Lidong Bing. EMNLP 2023's demo track. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.02858)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5d321194696f1f75cf9da045e6022b2f20ba5b9c%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Video-LLaMA%3A-An-Instruction-tuned-Audio-Visual-for-Zhang-Li/5d321194696f1f75cf9da045e6022b2f20ba5b9c)
[![Code](https://img.shields.io/github/stars/DAMO-NLP-SG/Video-LLaMA.svg?style=social&label=Star)](https://github.com/DAMO-NLP-SG/Video-LLaMA)
[![Demo](https://img.shields.io/badge/Demo-EEAD0E)](https://huggingface.co/spaces/DAMO-NLP-SG/Video-LLaMA)

+ **AntGPT: Can Large Language Models Help Long-term Action Anticipation from Videos?** (31 Jul 2023)\
Zhao, Qi, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.16368)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F6024f320e0a5b9b8fc29b86903aa9a96956b26dd%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/AntGPT%3A-Can-Large-Language-Models-Help-Long-term-Zhao-Zhang/6024f320e0a5b9b8fc29b86903aa9a96956b26dd)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://brown-palm.github.io/AntGPT/)

+ **Valley: Video Assistant with Large Language model Enhanced ability** (12 Jun 2023)\
Luo, Ruipu, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.07207)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4c4d176c6e28f48041f215d563f6ee8633534cff%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Valley%3A-Video-Assistant-with-Large-Language-model-Luo-Zhao/4c4d176c6e28f48041f215d563f6ee8633534cff)
[![Project_Page](https://img.shields.io/badge/Project_Page-00CED1)](https://valley-vl.github.io/)
[![Code](https://img.shields.io/github/stars/RupertLuo/Valley.svg?style=social&label=Star)](https://github.com/RupertLuo/Valley)

+ **Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models** (8 Jun 2023)\
Muhammad Maaz, Hanoona Rasheed, Salman Khan, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2306.05424)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fbf7025a2e5dbb3c09deae02a1aa98a256ca559e2%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Video-ChatGPT%3A-Towards-Detailed-Video-Understanding-Maaz-Rasheed/bf7025a2e5dbb3c09deae02a1aa98a256ca559e2)
[![Code](https://img.shields.io/github/stars/mbzuai-oryx/Video-ChatGPT.svg?style=social&label=Star)](https://github.com/mbzuai-oryx/Video-ChatGPT)

+ **VideoChat: Chat-Centric Video Understanding** (10 May 2023)\
Li, KunChang, et al. \
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.06355)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Fd48cb91b9e555194f7494c4d4bb9815021d3ee45%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VideoChat%3A-Chat-Centric-Video-Understanding-Li-He/d48cb91b9e555194f7494c4d4bb9815021d3ee45)
[![Code](https://img.shields.io/github/stars/OpenGVLab/Ask-Anything.svg?style=social&label=Star)](https://github.com/OpenGVLab/Ask-Anything)

+ **VideoLLM: Modeling Video Sequence with Large Language Models** (22 May 2023)\
Chen, Guo, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2305.13292)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ff9bfc6d9ba1665b73af3323d46c7642b852759ef%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/VideoLLM%3A-Modeling-Video-Sequence-with-Large-Models-Chen-Zheng/f9bfc6d9ba1665b73af3323d46c7642b852759ef)
[![Code](https://img.shields.io/github/stars/cg1177/VideoLLM.svg?style=social&label=Star)](https://github.com/cg1177/VideoLLM)

+ **Learning video embedding space with Natural Language Supervision** (25 Mar 2023)\
Uppala, Phani Krishna, Shriti Priya, and Vaidehi Joshi.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2303.14584)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F4e54a45d2118b61ae1baec07308af3fdd2c48759%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/Learning-video-embedding-space-with-Natural-Uppala-Bamotra/4e54a45d2118b61ae1baec07308af3fdd2c48759)


## Audio Understanding

## 3D Understanding

+ **LiDAR-LLM: Exploring the Potential of Large Language Models for 3D LiDAR Understanding** (21 Dec 2023)\
Senqiao Yang*, Jiaming Liu*, Ray Zhang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.14074)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F5edf706467dc76cd09319592d18db0ad4e1fb64d%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/LiDAR-LLM%3A-Exploring-the-Potential-of-Large-Models-Yang-Liu/5edf706467dc76cd09319592d18db0ad4e1fb64d)


+ **3D-LLM: Injecting the 3D World into Large Language Models** (2023)\
Yining Hong, Haoyu Zhen, Peihao Chen, et al. NeurIPS 2023 Spotlight\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2307.12981)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F7637ed79d30d0139901175ae4abedd822c217ab4%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/3D-LLM%3A-Injecting-the-3D-World-into-Large-Language-Hong-Zhen/7637ed79d30d0139901175ae4abedd822c217ab4)
[![Code](https://img.shields.io/github/stars/UMass-Foundation-Model/3D-LLM.svg?style=social&label=Star)](https://github.com/UMass-Foundation-Model/3D-LLM)

+ **PointLLM: Empowering Large Language Models to Understand Point Clouds** (2023)\
Runsen Xu, Xiaolong Wang, Tai Wang, et al.\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2308.16911.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2F6bcc6ab9c28805d4067e99b2cdc7524550fe80e1%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/PointLLM%3A-Empowering-Large-Language-Models-to-Point-Xu-Wang/6bcc6ab9c28805d4067e99b2cdc7524550fe80e1)
[![Code](https://img.shields.io/github/stars/OpenRobotLab/PointLLM.svg?style=social&label=Star)](https://github.com/OpenRobotLab/PointLLM)

 + **PointCLIP: Point Cloud Understanding by CLIP** (2022)\
Zhang, Renrui and Guo, Ziyu, Zhang, Wei, et al.(CVPR2022)\
[![Paper](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/pdf/2112.02413.pdf)
[![citation](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https%3A%2F%2Fapi.semanticscholar.org%2Fgraph%2Fv1%2Fpaper%2Ff3ce9ba3fcec362b70263a7ed63d9404975496a0%3Ffields%3DcitationCount)](https://www.semanticscholar.org/paper/PointCLIP%3A-Point-Cloud-Understanding-by-CLIP-Zhang-Guo/f3ce9ba3fcec362b70263a7ed63d9404975496a0)
[![Code](https://img.shields.io/github/stars/ZrrSkywalker/PointCLIP.svg?style=social&label=Star)](https://github.com/ZrrSkywalker/PointCLIP)
