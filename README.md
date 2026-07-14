<p align="left">
  <img src="https://i.ytimg.com/vi/YuOnfQd-aTw/sddefault.jpg" alt="Stalker" width="600">
</p>
# Сталкер — EuroPi Script - DustyMirror 2026

[English](#english) | [中文](#chinese)

---

<a name="english"></a>
## English

<p align="left">
  <img src="https://github.com/dustymirror/STALKER/blob/main/stalker.gif" alt="Stalker" width="300">
</p>

### Overview
**STALKER** is a script for the [EuroPi](https://github.com/Allen-Synthesis/EuroPi) eurorack module. It randomly displays phrases from the film *Сталкер* (directed by Andrei Tarkovsky 1979) on the built-in OLED screen, while generating 5 CV outputs and a trigger signal based on the linguistic characteristics of each phrase.

The script is designed to bring the atmosphere of the film into your modular synth system—each phrase carries its own "emotional weight," reflected in the voltage outputs.

---

### Features

- **79 phrases** from the film *Stalker* (English subtitles)
- **5 CV outputs** dynamically generated from each phrase:
  - **CV1**: Phrase length (0–10V)
  - **CV2**: Emotional weight (0–10V)
  - **CV3**: Punctuation intensity (0–10V)
  - **CV4**: Character hash (0–10V, random-like variation)
  - **CV5**: Fixed 3V reference
- **Trigger output** (CV6): 35ms pulse on every phrase change
- **OLED display**: Auto line-wrapping (up to 3 lines, 16 chars per line)
- **K1/K2 knobs**: Adjust text position (X/Y offset)
- **B1 button**: Pause/Resume playback
- **B2 button**: Skip to next random phrase
- **DIN input**: External trigger to skip to next phrase
- **AIN input**: Control display duration (0.5–10 seconds)

---

### CV Output Mapping

| CV Output | Dimension | Range | Description |
|-----------|-----------|-------|-------------|
| CV1 | Phrase length | 0–10V | Longer phrases → higher voltage |
| CV2 | Emotional weight | 0–10V | Weighted by keywords (death, fear, hope, love...) |
| CV3 | Punctuation | 0–10V | `?` or `!` → 8V, otherwise 1V |
| CV4 | Character hash | 0–10V | Pseudo-random variation based on text |
| CV5 | Reference | 3V fixed | Constant 3V output |
| CV6 | Trigger | 35ms pulse | 35ms gate on every phrase change |

---

### Controls

| Control | Function |
|---------|----------|
| **B1** (short press) | Pause / Resume |
| **B2** (short press) | Skip to next random phrase |
| **DIN** (external trigger) | Skip to next random phrase |
| **K1** (knob) | Adjust text X position (left/right) |
| **K2** (knob) | Adjust text Y position (up/down) |
| **AIN** (CV input) | Control display duration (0.5–10V → 0.5–10s; 0V → random 2–6s) |

---

### Installation

1. Copy `stalker.py` to the `/lib/contrib/` directory on your EuroPi.
2. Restart EuroPi.
3. Select **"Stalker"** from the main menu.

---

### File Structure

/lib/contrib/stalker.py


---

### Technical Details

- **Display**: 128×32 OLED, auto line-wrapping (max 3 lines)
- **Trigger pulse**: 35ms (configurable in `st()` method)
- **Phrase duration**: Random 2–6 seconds, or AIN-controlled 0.5–10 seconds
- **Debounce**: B1 = 200ms, B2 = 150ms, DIN = 150ms
- **Class inheritance**: `EuroPiScript` (required for menu loading)

---

### Requirements

- EuroPi firmware v0.21.2 or later
- MicroPython environment

---

### Credits

- Film: *Stalker* (1979) — Directed by Andrei Tarkovsky
- Subtitles: English translation from the film
- Hardware: [EuroPi](https://github.com/Allen-Synthesis/EuroPi) by Allen Synthesis

---

<a name="chinese"></a>
## 中文

### 概述

**STALKER** 是为 [EuroPi](https://github.com/Allen-Synthesis/EuroPi) 模块编写的脚本。它从塔可夫斯基导演的电影《潜行者》中随机抽取台词，显示在 OLED 屏幕上，并根据每句台词的文字特征生成 5 路 CV 输出和 1 路触发信号。

程序旨在将电影的氛围带入模块合成器系统——每句台词都带有自己的“情感重量”，并反映在电压输出中。

---

### 功能

- **79 句台词**，来自电影《潜行者》（英文字幕）
- **5 路 CV 输出**，动态生成：
  - **CV1**：台词长度（0–10V）
  - **CV2**：情绪权重（0–10V）
  - **CV3**：标点强度（0–10V）
  - **CV4**：字符哈希（0–10V，类随机变化）
  - **CV5**：固定 3V 参考电压
- **触发输出**（CV6）：每次切换台词时输出 35ms 脉冲
- **OLED 显示**：自动换行（最多 3 行，每行 16 字符）
- **K1/K2 旋钮**：调节文字位置（X/Y 偏移）
- **B1 按钮**：暂停/继续播放
- **B2 按钮**：跳转到下一句随机台词
- **DIN 输入**：外部触发跳转下一句
- **AIN 输入**：控制显示时长（0.5–10 秒）

---

### CV 输出对照表

| CV 通道 | 维度 | 范围 | 说明 |
|---------|------|------|------|
| CV1 | 台词长度 | 0–10V | 台词越长 → 电压越高 |
| CV2 | 情绪权重 | 0–10V | 根据关键词（死亡、恐惧、希望、爱……）加权 |
| CV3 | 标点强度 | 0–10V | 含 `?` 或 `!` → 8V，否则 1V |
| CV4 | 字符哈希 | 0–10V | 基于文本的伪随机变化 |
| CV5 | 参考电压 | 3V 固定 | 恒定 3V 输出 |
| CV6 | 触发脉冲 | 35ms | 每次切换台词输出 35ms 脉冲 |

---

### 操作说明

| 控制 | 功能 |
|------|------|
| **B1**（短按） | 暂停/继续 |
| **B2**（短按） | 跳转到下一句随机台词 |
| **DIN**（外部触发） | 跳转到下一句随机台词 |
| **K1**（旋钮） | 调节文字 X 轴位置（左右） |
| **K2**（旋钮） | 调节文字 Y 轴位置（上下） |
| **AIN**（CV 输入） | 控制显示时长（0.5–10V → 0.5–10 秒；0V → 随机 2–6 秒） |

---

### 安装方法

1. 将 `stalker.py` 复制到 EuroPi 的 `/lib/contrib/` 目录下
2. 重启 EuroPi
3. 在主菜单中选择 **"Stalker"**

---

### 文件结构

/lib/contrib/stalker.py

---

### 技术参数

- **显示屏**：128×32 OLED，自动换行（最多 3 行）
- **触发脉冲**：35ms（可在 `st()` 方法中调整）
- **台词时长**：随机 2–6 秒，或 AIN 控制 0.5–10 秒
- **防抖**：B1 = 200ms，B2 = 150ms，DIN = 150ms

---

### 系统要求

- EuroPi 固件 v0.21.2 或更高版本
- MicroPython 环境

---

### 致谢

- 电影：《潜行者》（1979）—— 导演：安德烈·塔可夫斯基
- 字幕：电影英文字幕
- 硬件：[EuroPi](https://github.com/Allen-Synthesis/EuroPi) by Allen Synthesis

---
